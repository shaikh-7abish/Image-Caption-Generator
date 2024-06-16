import numpy as np
from ImgCapGen.entity.config_entity import PredictionConfig
from ImgCapGen.utils.common import *

class Prediction:
    def __init__(self, config: PredictionConfig):
        self.config = config

    def generate_cap(self, imgfile, max_length = 34):
        features = extract_features(imgfile)
        start = '<start>'
        tokenizer = load_pickle(self.config.tokenizer)
        model = load_model(self.config.model)

        for i in range(max_length):
            sequence = tokenizer.texts_to_sequences([start])[0]
            sequence = padding([sequence], maxlen=max_length)

            yhat = model.predict([features,sequence], verbose= 1)
            predicted_index = np.argmax(yhat)

            words = get_word_from_index(index= predicted_index, tokenizer= tokenizer)
            if words == None or words == 'end':
                break
            start += " " + words

        return start
