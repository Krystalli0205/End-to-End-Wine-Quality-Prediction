from wine_quality_prediction_project.config.configuration import ConfigurationManager
from wine_quality_prediction_project.components.data_ingestion import DataIngestion
from wine_quality_prediction_project import logger


STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager() # import from config
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config) # import from components
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
