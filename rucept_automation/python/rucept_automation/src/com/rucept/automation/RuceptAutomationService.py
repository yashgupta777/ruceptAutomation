import os
import sys

import CsvGenerator
import FileImposer
import RuceptLogger
import Utils

# init logger
logger_instance = RuceptLogger.RuceptLogger()
logger = logger_instance.init_logger()

imposer = FileImposer.FileImposer()
csv_generator = CsvGenerator.CSVGenerator()
utils = Utils.Utils()


class RuceptMainService:
    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()
    
    @classmethod
    def perform_impostion(cls, operation_name, base_folder, template_folder_name):
        req_folder = "/home/ubuntu/automation/uploader2/public/uploads/"
        finished_req_folder = base_folder + "finished_req/"
        output_folder = base_folder + "output/"
        
        template_img_folder = base_folder + "/" + template_folder_name + "/"
        csv_out_folder = base_folder + "csv_output/"
        
        for req_id in os.listdir(req_folder):
            logger.debug(operation_name + " : design image : " + req_id)
            dsn_img_path = req_folder + req_id
            
            ## check for image files recursively
            if utils.is_image(dsn_img_path):
                path = utils.strip_image_extensions(dsn_img_path)
                req_output_folder = output_folder
                desired_output_folder = req_output_folder + utils.strip_image_extensions(req_id)
                
                if not path.endswith("_done") \
                        and not os.path.exists(desired_output_folder):
                    os.makedirs(desired_output_folder)
                    
                    for template_img in os.listdir(template_img_folder):
                        logger.debug(operation_name + " : template image : " + template_img)
                        desired_output_image_name = utils.strip_image_extensions(req_id) + "_" + template_img
                        template_img_path = template_img_folder + template_img
                        
                        imposer.impose_image(operation_name,
                                             base_folder,
                                             template_img_path,
                                             dsn_img_path,
                                             desired_output_folder,
                                             desired_output_image_name)
                        logger.debug(operation_name + " : imposition done")
                        
                        utils.con_aws_s3(desired_output_folder,
                                         desired_output_image_name,
                                         None,
                                         None)
                        logger.debug(
                            operation_name + " : S3 upload done : " + desired_output_folder + "/" + desired_output_image_name)
                        
                        try:
                            os.remove(desired_output_folder + "/" + desired_output_image_name)
                            logger.debug(
                                operation_name + " : Removed file after s3 upload : " + desired_output_folder + "/" + desired_output_image_name)
                        except OSError:
                            logger.error(operation_name +
                                         " : Could not remove file : " + desired_output_folder + "/" + desired_output_image_name)
                            pass
                        
                        csv_generator.generate_amazon_csv(operation_name,
                                                           csv_out_folder,
                                                           utils.strip_image_extensions(req_id) + ".csv",
                                                           utils.strip_image_extensions(template_img),
                                                           utils.strip_image_extensions(req_id),
                                                           desired_output_image_name)
                    
                    # once request is processed, mark this req folder as done
                    os.rename(req_folder + req_id, finished_req_folder + req_id)
                    
                    logger.debug(
                        operation_name + " : input request named as " + req_id + " moved to : " + finished_req_folder + req_id)
                    logger.debug("---------------------------------------")
                
                else:
                    os.rename(req_folder + req_id, finished_req_folder + req_id)
                    logger.debug(
                        operation_name + " : ALREADY PROCESSED : input request named as " + req_id + " moved to : " + finished_req_folder + req_id)
                    logger.debug("---------------------------------------")
                    
                    
