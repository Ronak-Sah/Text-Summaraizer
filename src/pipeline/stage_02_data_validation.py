from src.config.configuration import ConfigurationManager
from src.components.data_validation import Data_Validation
from src.logger import logger 



class Data_Validation_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation()

        data_validation=Data_Validation(data_validation_config)
        data_validation.validate_files()
        