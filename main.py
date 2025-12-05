from src.logger import logger 
from src.pipeline.stage_01_data_ingestion import Data_Ingestion_pipeline
from src.pipeline.stage_02_data_validation import Data_Validation_pipeline
from src.pipeline.stage_03_data_transformation import Data_Transformation_pipeline
from src.pipeline.stage_04_model_trainer import Model_trainer_pipeline
from src.pipeline.stage_05_model_evaluation import Model_evaluation_pipeline

logger.info("Code Starts")
logger.info("======================================================================")


Stage_Name="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} started<<<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion=Data_Ingestion_pipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} ended<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


logger.info("======================================================================")


Stage_Name="Data Validation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} started<<<<<<<<<<<<<<<<<<<<<<<")
    data_validation=Data_Validation_pipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} ended<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


logger.info("======================================================================")

Stage_Name="Data transformation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} started<<<<<<<<<<<<<<<<<<<<<<<")
    data_transformation=Data_Transformation_pipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} ended<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("======================================================================")


Stage_Name="Model training Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} started<<<<<<<<<<<<<<<<<<<<<<<")
    model_trainer=Model_trainer_pipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} ended<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("======================================================================")


Stage_Name="Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} started<<<<<<<<<<<<<<<<<<<<<<<")
    model_evaluation=Model_evaluation_pipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>>>>>>>>>{Stage_Name} ended<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

logger.info("======================================================================")