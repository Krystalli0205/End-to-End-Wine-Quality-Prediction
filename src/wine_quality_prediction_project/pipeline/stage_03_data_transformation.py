from wine_quality_prediction_project.config.configuration import ConfigurationManager
from wine_quality_prediction_project.components.data_transformation import DataTransformation
from wine_quality_prediction_project import logger
from pathlib import Path


STAGE_NAME = "Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Data validation failed.")
        
        except Exception as e:
            print(e)
        