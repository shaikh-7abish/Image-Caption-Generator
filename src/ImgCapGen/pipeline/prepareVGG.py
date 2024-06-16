from ImgCapGen.config.configuration import ConfigurationManager
from ImgCapGen.components.prepareVGG import PrepareVGG
from ImgCapGen import logger

STAGE_NAME = 'PREPARE VGG 16'

class PrepareVGG16Pipeline:
    def __init__(self) -> None:
        pass

    def main(self, img):
        config = ConfigurationManager()
        pred_config = config.get_vgg16_config()
        pred_config = PrepareVGG()
        pred_config.get_model()