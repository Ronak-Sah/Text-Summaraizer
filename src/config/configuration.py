#Reading all YAML files (config.yaml, params.yaml),creating folders, and generating configuration objects for each ML pipeline stage.

from src.entity import DataValidationConfig
from src.entity import DataIngestionConfig
from src.entity import DataTransformationConfig
from src.entity import ModelEvaluationConfig
from src.entity import ModelTrainerConfig
from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils.common import read_yaml,create_directories


class ConfigurationManager:
    def __init__(self,config_filepath= CONFIG_FILE_PATH,params_filepath= PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    # Attribute for data ingestion
    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config.data_ingestion                 # Extracts only the data_ingestion part of config.yaml.

        create_directories([config.root_dir])               # Create data_ingestion.root directory

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    # Attribute for data validation
    def get_data_validation(self) -> DataValidationConfig:
        config = self.config.data_validation                 # Extracts only the data_ingestion part of config.yaml.

        create_directories([config.root_dir])               # Create data_ingestion.root directory

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_files=config.all_required_files,
        )

        return data_validation_config
    
    # Attribute for data transformation
    def get_data_transformation(self) -> DataTransformationConfig:
        config = self.config.data_transformation                 # Extracts only the data_ingestion part of config.yaml.

        create_directories([config.root_dir])               # Create data_ingestion.root directory

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name,
        )

        return data_transformation_config
    
    # Attribute for Model Training
    def get_model_trainer(self) -> ModelTrainerConfig:
        config = self.config.model_trainer                 # Extracts only the data_ingestion part of config.yaml.
        params = self.params.model_trainer
        create_directories([config.root_dir])               # Create data_ingestion.root directory

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_name=config.model_name,
            output_dir = params.output_dir,       
            num_train_epochs = params.num_train_epochs,                
            per_device_train_batch_size = params.per_device_train_batch_size,
            per_device_eval_batch_size = params.per_device_eval_batch_size,
            warmup_steps = params.warmup_steps     ,     
            gradient_accumulation_steps = params.gradient_accumulation_steps,
            weight_decay = params.weight_decay
        )

        return model_trainer_config
    

    # Attribute for Model Evaluation
    def get_model_evaluation(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation                 # Extracts only the data_ingestion part of config.yaml.
        # params = self.params.model_evaluation
        create_directories([config.root_dir])               # Create data_ingestion.root directory

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
        )

        return model_evaluation_config