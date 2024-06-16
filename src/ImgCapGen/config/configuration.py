import os
from pathlib import Path
from ImgCapGen.entity.config_entity import PrepareVGGConfig, PredictionConfig
from ImgCapGen.constants import CONFIG_FILE_PATH
from ImgCapGen.utils.common import *

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)

    def get_vgg16_config(self) -> PrepareVGGConfig:
        config = self.config.prepare_vgg_model

        prepare_config = PrepareVGGConfig(
            root_dir= config.root_dir,
            vgg_model_path= config.vgg_model_path
        )

        return prepare_config

    def get_prediction_config(self) -> PredictionConfig:
        config = self.config.prediction

        prediction_config = PredictionConfig(
            tokenizer= config.tokenizer,
            model= config.model
        )

        return prediction_config