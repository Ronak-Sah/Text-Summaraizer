from src.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation()

    
    def predict(self,text,num_length,beam_length):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={"length_penalty":0.8,"num_beams":beam_length,"max_length":num_length}


        pipe=pipeline("summarization",model=self.config.model_path,tokenizer=tokenizer)

        ans=pipe(text,**gen_kwargs)[0]["summary_text"]

        print("Input text :")
        print(text)

        print("\nModel summary : ")
        print(ans)
        return ans 