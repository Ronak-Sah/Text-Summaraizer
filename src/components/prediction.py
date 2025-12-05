from src.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation

    
    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={"length_penalty":0.8,"num_beams":8,"max_length":128}


        pipe=pipeline("summaraization",model="pegasus-samsum-model",tokenizer=tokenizer)

        ans=pipe(text,**gen_kwargs)[0]["summay_text"]

        print("Input text :")
        print(text)

        print("\nModel summary : ")
        print(ans)