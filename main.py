from ImgCapGen.pipeline.prepareVGG import PrepareVGG16Pipeline
from ImgCapGen.pipeline.predictionpipeline import Prediction
from ImgCapGen import logger

STAGE_NAME = 'PREPARE VGG16 MODEL STAGE'
try:
    logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
    obj = PrepareVGG16Pipeline()
    obj.main()
    logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = 'PREDICTION STAGE'
try:
    logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
    obj = Prediction()
    obj.main("traffic.jpg")
    logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e