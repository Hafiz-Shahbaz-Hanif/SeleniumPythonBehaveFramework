import time
import pyodbc
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utilities.Exceptions import MyException
from utilities.customLogger import LogGen


class SWMDashboard:

    logger = LogGen.loggen()

    loader = "(//body[@class='loading'])[1]"
    swmDashStatusDevice = "// *[ @ id = '1'] / *[ @ aria-describedby = 'SWMPolicies_SourceFacility']"
    swmDashboardDDBtn = "//*[@href='/swm/dashboard']"

    def __init__(self):
        pass

    def swmDashboard(self, context):
        try:
            swmDashboardDDSelection = context.driver.find_element(By.XPATH, self.swmDashboardDDBtn)
            swmDashboardDDSelection.click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("SWM Dashboard Selected From Dropdown")
        except Exception as e:
            MyException.handle_exception(context, e)

    def swmDashboardStatus(self, context):
        try:
            swmDashboardStatusFacility = context.driver.find_element(By.XPATH, self.swmDashStatusDevice)
            swmDashboardStatusFacility.click()
            WebDriverWait(context.driver, 60).until(EC.visibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("Clicked on Source Facility From SWM Status by Devices Module")
        except Exception as e:
            MyException.handle_exception(context, e)



