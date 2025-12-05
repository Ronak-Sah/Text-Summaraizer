from src.config.configuration import ConfigurationManager
from src.components.data_trasnsformation import Data_Transformation
from src.logger import logger


class Data_Transformation_pipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation()

        data_transformation=Data_Transformation(data_transformation_config)
        data_transformation.convert()
        
        