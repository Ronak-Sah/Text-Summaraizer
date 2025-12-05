import os
from src.logger import logger
from src.entity import ModelTrainerConfig
import torch
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from transformers import DataCollatorForSeq2Seq
from transformers import  Trainer, TrainingArguments
from datasets import load_from_disk

class Model_Trainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config= config
        self.device= "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name).to(self.device)
        self.tokenizer=AutoTokenizer.from_pretrained(config.model_name)
        self.data_collator=DataCollatorForSeq2Seq(self.tokenizer,model=self.model)


    def train(self):
        training_args = TrainingArguments(
            fp16=True,
            output_dir=self.config.output_dir,          
            num_train_epochs=self.config.num_train_epochs,             
            per_device_train_batch_size=self.config.per_device_train_batch_size,  
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,  
            warmup_steps=self.config.warmup_steps,               
            gradient_accumulation_steps=self.config.gradient_accumulation_steps, 
            weight_decay=self.config.weight_decay           
    
        )
        dataset_samsum = load_from_disk(self.config.data_path)

        trainer = Trainer(
            model=self.model,                         
            args=training_args,                 
            train_dataset=dataset_samsum["train"].select(range(10)),         
            eval_dataset=dataset_samsum["test"].select(range(10)),           
            data_collator=self.data_collator
        )
        trainer.train()
        self.model.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        self.tokenizer.save_pretrained(os.path.join(self.config.root_dir,"Tokenizer"))
    