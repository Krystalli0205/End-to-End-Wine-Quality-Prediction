from wine_quality_prediction_project import logger
from wine_quality_prediction_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality_prediction_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wine_quality_prediction_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wine_quality_prediction_project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from wine_quality_prediction_project.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage" 

try:
    logger.info(f"Running {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    data_validation_pipeline = DataTransformationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
    raise e



STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"Running {STAGE_NAME}")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
    raise e
