# It contains dataclasses that define the structure of configuration objects.

from dataclasses import dataclass
from pathlib import Path

# Configuration for data ingestion

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url :str
    local_data_file :Path
    unzip_dir :Path


# Configuration for data validation

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file : Path
    all_required_files : list

# Configuration for data transformation

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path : Path
    tokenizer_name : str


# Configuration for Model Trainer 

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path : Path
    model_name : str
    output_dir : str        
    num_train_epochs : int                
    per_device_train_batch_size : int
    per_device_eval_batch_size : int 
    warmup_steps : int            
    gradient_accumulation_steps : int
    weight_decay : float 


# Configuration for Model Evaluation

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir : Path
    data_path : Path
    model_path : Path
    tokenizer_path : Path
    metric_file_name : Path