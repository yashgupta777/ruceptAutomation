
import RuceptAutomationService as automation_service
import RuceptLogger as RuceptLogger

main_service = automation_service.RuceptMainService()

logger_instance = RuceptLogger.RuceptLogger()
operation_name = "phone_automation"

# init logger
logger = logger_instance.init_logger()
logger.debug(operation_name + " started")

base_folder = "/home/ubuntu/automation_v2/phone_automation/"
#base_folder1 = "/home/ubuntu/automation/uploader2/public/uploads/"
#base_folder = "/home/ubuntu/automation_v2/phone_automation/"
# base_folder = "/home/local/JASPERINDIA/verma.deepak/rucept_data/cloud_folder_str/phone_automation/"

main_service.perform_impostion(operation_name, base_folder, "phones")
