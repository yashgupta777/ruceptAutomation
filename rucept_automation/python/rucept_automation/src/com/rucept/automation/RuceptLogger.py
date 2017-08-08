import logging
import os
import time


class RuceptLogger:
    
    def __init__(self):
        self.logger = None
    
    @classmethod
    def init_logger(cls):
        app_name = "Rucept"
        file_name = str(time.strftime("%Y_%m_%d_%H"))
        logger = logging.getLogger(app_name)
        
        log_dir = "/var/tmp/" + app_name + "/logs/"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_file_name = log_dir + "/" + file_name + ".log"
        
        hdlr = logging.FileHandler(log_file_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)
        cls.logger = logger
        return logger
    
    def set_logger(self, logger):
        self.logger = logger
        
    def get_logger(self):
        return self.logger
    
    @classmethod
    def dolog(cls, message):
        # if cls.logger is None:
        #     cls.init_logger
        #
        # cls.logger.debug(message)
        pass
