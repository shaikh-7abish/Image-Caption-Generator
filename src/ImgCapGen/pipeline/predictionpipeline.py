from ImgCapGen.config.configuration import ConfigurationManager
from ImgCapGen.components.prediction import Prediction
from ImgCapGen.utils.common import save_result
from ImgCapGen import logger

STAGE_NAME = 'PREDICTION'

class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def main(self, img):
        config = ConfigurationManager()
        pred_config = config.get_prediction_config()
        pred_config = Prediction(config= pred_config)
        caption = pred_config.generate_cap(img)
        # save_result("results.txt", caption)
        print(caption)