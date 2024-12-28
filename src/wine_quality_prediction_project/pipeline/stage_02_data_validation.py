from wine_quality_prediction_project.config.configuration import ConfigurationManager
from wine_quality_prediction_project.components.data_validation import DataValidation
from wine_quality_prediction_project import logger


STAGE_NAME = "Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
