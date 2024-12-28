from wine_quality_prediction_project.config.configuration import ConfigurationManager
from wine_quality_prediction_project.components.model_evaluation import ModelEvaluation
from wine_quality_prediction_project import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_results()