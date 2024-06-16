from ImgCapGen.config.configuration import ConfigurationManager
from ImgCapGen.components.prepareVGG import PrepareVGG
from ImgCapGen import logger

STAGE_NAME = 'PREPARE VGG 16'

class PrepareVGG16Pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        pred_config = config.get_vgg16_config()
        pred_model = PrepareVGG(config= pred_config)
        pred_model.get_model()