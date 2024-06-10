import os
import sys
import dill
import base64
from src.ClothingApparel.logger import logging
from src.ClothingApparel.exception import CustomException


def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str) -> object:
    try:
        logging.info("Entered the load_object method of utils")
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise CustomException(e, sys)

def image_to_base64(image):
    with open(image, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return my_string