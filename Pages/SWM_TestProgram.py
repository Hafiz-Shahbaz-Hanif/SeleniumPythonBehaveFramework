import time

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.Exceptions import MyException
from selenium.webdriver.support.ui import WebDriverWait

from utilities.customLogger import LogGen
from utilities.randomTextGen import RandomTextGen


class swmTestProgramClass:
    logger = LogGen.loggen()

    def __init__(self):
        pass

    tpLevel_dd = "Level"
    loader = "(//body[@class='loading'])[1]"
    mCombineHeader = "//div[@id='panel3_ChartContainer_subtitle']"
    generalTabXpath = "//*[@id='general-tab']"

    def selectTestProgramFromRulesInputSelection(self, context):
        try:
            level = context.driver.find_element(By.ID, self.tpLevel_dd)
            select = Select(level)
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            option_value_to_select = "Test Program"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Test Program Level is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickOnGeneralTab(self, context):
        try:
            generalTab = context.driver.find_element(By.XPATH, self.generalTabXpath)
            generalTab.click()
            self.logger.info("********** General Tab is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)
