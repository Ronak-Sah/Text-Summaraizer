import os
from src.logger import logger
from src.entity import ModelEvaluationConfig
import torch
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_from_disk
from tqdm import tqdm
from evaluate import load
import pandas as pd

class Model_Evaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def  generate_batch_sized_chunks(self,list_of_elements,batch_size):
        """split the batches into smaller batches that we can process simultaneosly
        Yield successive batched sized chunks from list_of_elements"""
        for i in range(0,len(list_of_elements),batch_size):
            yield list_of_elements[i:i+batch_size] 


    def calculate_metric(self,dataset,metric,model,tokenizer,batch_size=16,column_text="dialogue",column_summary="summary"):
        X_batches=list(self.generate_batch_sized_chunks(dataset[column_text],batch_size))
        y_batches=list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size))

        for X_batch,y_batch in tqdm(zip(X_batches,y_batches),total=len(X_batches)):
            inputs=tokenizer(X_batch,max_length=512,truncation=True,padding=True,
                return_tensors="pt")

            summaries=model.generate(input_ids=inputs["input_ids"].to(self.device),attention_mask=inputs["attention_mask"].to(self.device),
                                            length_penalty=0.8,num_beams=8,max_length=128)


            decode_summaries=[tokenizer.decode(s,skip_special_tokens=True,clean_up_tokenization_spaces=True) for s in summaries]

            decode_summaries = [d.strip() for d in decode_summaries]
            
            metric.add_batch(predictions=decode_summaries,references=y_batch)

        score=metric.compute()
        return score

    def evaluate(self):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(self.device)

        dataset=load_from_disk(self.config.data_path)

        rouge_names=["rouge1", "rouge2", "rougeL", "rougeLsum"]

        rouge_metric = load("rouge")

        score=self.calculate_metric(dataset["test"][0:10],rouge_metric,model,tokenizer,batch_size=2,
                       column_text="dialogue",column_summary="summary")

        rouge_dict = {rn: score[rn] for rn in rouge_names}

        df=pd.DataFrame(rouge_dict,index=["pegasus"])

        df.to_csv(self.config.metric_file_name,index=False)
        logger.info(f"Metric CSV creted at {self.config.metric_file_name}")