import cv2 as cv2
import numpy as np


class OpenCVExamples:
    def blend(src, toBlend):
        dst = cv2.addWeighted(src, 0.7, toBlend, 0.3, 0)
        return dst
        