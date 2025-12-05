import os
from src.logger import logger
from src.entity import DataTransformationConfig
from datasets import  load_dataset
from transformers import AutoTokenizer

class Data_Transformation:
    def __init__(self,config: DataTransformationConfig):
        self.config= config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def tokenize_function(self,example):
        # Tokenize dialogue (input)
        inputs = self.tokenizer(example["dialogue"], max_length=512, truncation=True)
        # Tokenize summary (target)
        targets = self.tokenizer(example["summary"], max_length=512, truncation=True)

        inputs["labels"] = targets["input_ids"]
        return {
            "input_ids":inputs["input_ids"],
            "attention_mask":inputs["attention_mask"],
            "labels":targets["input_ids"]
        }
    
    def convert(self):
        dataset_samsum = load_dataset("csv", data_files={
            "train": "artifacts/data_ingestion/samsum/train.csv",
            "test": "artifacts/data_ingestion/samsum/test.csv",
            "validation": "artifacts/data_ingestion/samsum/validation.csv",
            }
        )
        dataset_samsum_pt=dataset_samsum.map(self.tokenize_function,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))

