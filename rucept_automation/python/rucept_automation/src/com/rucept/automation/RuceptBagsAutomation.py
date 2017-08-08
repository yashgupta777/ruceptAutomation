# from src.com.rucept.automation.logger import RuceptLogger
# from src.com.rucept.automation.services.RuceptAutomationService import RuceptMainService as main_service

import RuceptAutomationService as automation_service
import RuceptLogger as RuceptLogger

main_service = automation_service.RuceptMainService()
logger_instance = RuceptLogger.RuceptLogger()
operation_name = "bags_automation"

# init logger
logger = logger_instance.init_logger()
logger.debug(operation_name + " started")

base_folder = "/home/ubuntu/automation_v2/bag_automation/"
# base_folder = "/home/local/JASPERINDIA/verma.deepak/rucept_data/cloud_folder_str/bag_automation/"

main_service.perform_impostion(operation_name, base_folder, "bags")
