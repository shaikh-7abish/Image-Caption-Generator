from ImgCapGen.entity.config_entity import PrepareVGGConfig
from ImgCapGen.utils.common import *
from tensorflow.keras.applications.vgg16 import VGG16

class PrepareVGG:
    def __init__(self, config: PrepareVGGConfig):
        self.config = config
        create_directories(
            path_to_directories= config.root_dir,
            verbose= True
        )

    def get_model(self):
        vgg = VGG16()
        vgg = Model(inputs = vgg.inputs, outputs = vgg.layers[-2].output)
        save_model(path= self.config.vgg_model_path, model= vgg)

    