import Image
import os

import cv2
import numpy as np

from src.com.rucept.automation import RuceptLogger
from src.com.rucept.automation.Utilities import Utils

utils = Utils.Utils()
logger_instance = RuceptLogger.RuceptLogger()
operation_name = "FileImposition "


class FileImposer:
    def __init__(self):
        self.data = []
    
    @classmethod
    def impose_image(cls,
                     operation_name,
                     base_folder,
                     template_image_path,
                     design_image_path,
                     dst_folder,
                     dst_image_name):
        # init logger
        # logger = logger_instance.init_logger(operation_name)
        
        temp_folder = base_folder + "temp/"
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        
        img = cv2.imread(design_image_path, cv2.IMREAD_UNCHANGED)
        phn_image = cv2.imread(template_image_path, cv2.IMREAD_UNCHANGED)
        
        pix = np.asarray(phn_image)
        
        pix = pix[:, :, 0:3]  # Drop the alpha channel
        idx = np.where(pix - 255)[0:2]  # Drop the color when finding edges
        box = map(min, idx)[::-1] + map(max, idx)[::-1]
        
        trimmed_phn_image = phn_image[box[1]:box[3] - 1, box[0]:box[2] + 1]
        trimmed_phn_image_path = temp_folder + "phone.png"
        utils.save_image(trimmed_phn_image, trimmed_phn_image_path)
        
        height, width, depth = trimmed_phn_image.shape[:3]
        
        ih, iw = img.shape[:2]
        
        icx = iw / 2
        ich = ih / 2
        
        cropped = img[ich - (height / 2):ich + (height / 2) - 1, icx - width / 2:icx + width / 2 + 1]
        
        cropped_img_path = temp_folder + "cropped.png"
        utils.save_image(cropped, cropped_img_path)
        
        ##################################################################################################
        ############ Merging starts here #################################################################
        
        im = Image.open(cropped_img_path)
        im.save(cropped_img_path)
        # img_dest = im.copy().convert('RGBA')
        
        res = None
        
        merged_img_path = dst_folder + "/" + dst_image_name
        utils.save_image(res, merged_img_path)
        
        background = Image.open(cropped_img_path)
        foreground = Image.open(trimmed_phn_image_path)
        
        background.paste(foreground, (0, 0), foreground)
        # background.show()
        background.save(merged_img_path)
