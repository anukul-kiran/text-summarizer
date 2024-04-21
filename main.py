from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>stage {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f'>>>>>>stage {STAGE_NAME} started <<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data transformation Stage'

try:
    logger.info(f">>>>>>>>>>stage{STAGE_NAME} started<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f'>>>>>>>>>> stage{STAGE_NAME} started<<<<<<<<<')
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


