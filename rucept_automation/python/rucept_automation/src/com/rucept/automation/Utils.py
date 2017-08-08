import cv2
import boto
from boto.s3.key import Key
import boto.s3
import os

# this class needs a lot of re-factoring
# will do once will have some bandwidth

class Utils:
    def __init__(self):
        self.data = []
    
    @classmethod
    def show_image(cls, src, title, wait_seconds):
        if title is None:
            title = "Image"
        cv2.imshow(title, src)
        cv2.waitKey(wait_seconds * 1000)
        return
    
    @classmethod
    def save_image(cls, img, path):
        cv2.imwrite(path, img)
    
    @classmethod
    def strip_image_extensions(cls, path):
        path = path.replace(".jpg", "")
        path = path.replace(".JPG", "")
        path = path.replace(".png", "")
        path = path.replace(".PNG", "")
        path = path.replace(".jpeg", "")
        path = path.replace(".JPEG", "")
        return path

    @classmethod
    def con_aws_s3(cls, directory, filename, percent_callback, num_cb):
        #access key and secret are purposefully kept here, please dont re-factor for now
        conn = boto.connect_s3("AKIAJWNED2WVRQIONZ2A", "ianLiH4jSSmwavc9s+6EEaOLcIcwr4QELXw+6bXM")
        bucket = conn.get_bucket('rucept')
        file_to_upload = os.path.join(directory, filename)
        k = Key(bucket)
        k.key = filename
        k.set_contents_from_filename(file_to_upload,
                                     cb=percent_callback,
                                     num_cb=num_cb)  # uploading the image files into aws s3
        
    @classmethod
    def is_image(cls, dsn_img):
        if dsn_img.endswith(".png") \
                or dsn_img.endswith(".PNG") \
                or dsn_img.endswith(".jpg") \
                or dsn_img.endswith(".JPG") \
                or dsn_img.endswith(".jpeg") \
                or dsn_img.endswith(".JPEG"):
            return True

Utils().__init__()
