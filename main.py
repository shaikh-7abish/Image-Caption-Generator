import os
from ImgCapGen.pipeline.prepareVGG import PrepareVGG16Pipeline
from ImgCapGen.pipeline.predictionpipeline import PredictionPipeline
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

image_path = input("Please enter the path to the image file: ")
if os.path.exists(image_path):
  STAGE_NAME = 'PREDICTION STAGE'
  try:
    logger.info(f">>>>>-- {STAGE_NAME} started. --<<<<<")
    obj = PredictionPipeline()
    obj.main(image_path)
    logger.info(f">>>>>-- {STAGE_NAME} successfully completed --<<<<<\n\nx====================x")
  except Exception as e:
    logger.exception(e)
    raise e
else:
  print('No file found!')