from wine_quality_prediction_project.config.configuration import ConfigurationManager
from wine_quality_prediction_project.components.model_trainer import ModelTrainer
from wine_quality_prediction_project import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        