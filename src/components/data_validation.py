import os
from src.logger import logger
from src.entity import DataValidationConfig

class Data_Validation:
    def __init__(self,config: DataValidationConfig):
        self.config= config


    def validate_files(self):
        try:
            validation_status= True
            folder_path=os.path.join("artifacts","data_ingestion","samsum")
            all_files = os.listdir(folder_path)

            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    break

            with open(self.config.status_file, "w") as fobj:
                fobj.write(f"Validation status : {validation_status}")

            return validation_status


        except Exception as e:
            logger.error(e)
            raise e
