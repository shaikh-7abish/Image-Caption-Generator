import os
import yaml
from pathlib import Path
import pickle
import tensorflow as tf
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from ImgCapGen import logger
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: str, verbose=True):
    os.makedirs(path_to_directories, exist_ok=True)
    if verbose:
        logger.info(f"created directory at: {path_to_directories}")

@ensure_annotations
def load_pickle(path_to_pickle_file: Path) -> ConfigBox:
    pickle_file = pickle.load(open(path_to_pickle_file, 'rb'))
    logger.info(f"Successfully loaded Pickle file from: {path_to_pickle_file}")
    return ConfigBox(pickle_file)

@ensure_annotations
def load_model(path_to_model: Path) -> tf.keras.Model:
    model = tf.keras.Models.load_model(path_to_model)
    logger.info(f"Successfully loaded Model from: {path_to_model}")
    return model

def load_vgg():
    vgg = VGG16()
    vgg = Model(inputs = vgg.inputs, outputs = vgg.layers[-2].output)
    logger.info('VGG16 Loaded')
    return vgg

def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

def extract_features(imgfile):
    image_features = {}
    image = load_img(imgfile, target_size= (224,224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    logger.info('Image Preprocessed')

    vgg = load_model('artifacts/prepare_vgg_model/vgg16.h5')
    img_feature = vgg.predict(image, verbose = 1)
    image_id = imgfile.split('.')[0]
    image_features[image_id] = img_feature
    logger.info("Feature Extracted from Image using VGG16")

    return image_features

def padding(sequence, max_length: int):
    return pad_sequences([sequence], maxlen = max_length)

@ensure_annotations
def get_word_from_index(index: int, tokenizer) -> str:
    return next((word for word, idx in tokenizer.word_index.items() if idx == index), None)

@ensure_annotations
def save_result(result_file_path: Path, result: str):
    if result_file_path.exists():
        with result_file_path.open("a", encoding="utf-8") as file:
            file.write(result + "\n")
    else:
        with result_file_path.open("w", encoding="utf-8") as file:
            file.write(result + "\n")