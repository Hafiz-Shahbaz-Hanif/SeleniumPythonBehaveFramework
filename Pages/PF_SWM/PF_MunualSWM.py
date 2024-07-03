import time
import allure
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities.customLogger import LogGen
from utilities.Exceptions import MyException


class ManualSWM:
    logger = LogGen.loggen()

    def __init__(self):
        pass

    swmManualSWM_lnk = "//span[normalize-space()='Manual SWM']"

    loader = "(//body[@class='loading'])[1]"

    sourceFacility_silicon = "//select[@id='SourceFacility']//option[@value='SILICON']"
    sourceWorkCenter_waferSort = "//select[@id='SourceWorkCenter']//option[@value='WAFER SORT']"
    sourceDevice_4670 = "//select[@id='SourceDevice']//option[@value='4670']"
    sourceTestProgram_PREBAKE_STDF_4670 = "//select[@id='SourceTestProgram']//option[@value='PREBAKE_-_STDF_4670']"
    sourceLotsTable = "//table[@id='SourceLotGrid']//td[@title='72100']/preceding-sibling::td/input"
    sourceWafers_silicon = "//table[@id='SourceWafersGrid']//td[@title='8']/preceding-sibling::td/input"

    targetFacility_silicon = "//select[@id='TargetFacility']//option[@value='SILICON']"
    targetWorkCenter_waferSort = "//select[@id='TargetWorkCenter']//option[@value='WAFER SORT']"
    targetDevice_4670 = "//select[@id='TargetDevice']//option[@value='4670']"
    targetTestProgram_POSTBAKE_STDF_4670 = "//select[@id='TargetTestProgram']//option[@value='POSTBAKE_-_STDF_4670']"
    targetLotsTable = "//table[@id='TargetLotsGrid']//td[@title='72100']/preceding-sibling::td/input"
    targetWafers_silicon = "//table[@id='TargetWafersGrid']//td[@title='8']/preceding-sibling::td/input"

    btn_generateManualSwm = "//input[@id='btn-calculate']"
    div_ManualSWM_CBWMap = "//div[@id='panel3_ChartContainer_subtitle']"
    btn_SaveToYieldwerx = "//button[@id='btn-save-to-yieldwerx']"
    msg_Success = "//div[@class='bootstrap-growl alert alert-success']"

    # *****************************                                 *****************************
    # *****************************     SWM Manual SWM Creation     *****************************
    # *****************************                                 *****************************

    def clickSwmManualSWM(self, context):
        try:
            context.driver.find_element(By.XPATH, self.swmManualSWM_lnk).click()
            self.logger.info("********** Clicked On The SWM Manual SWM **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

            # Verify if the URL matches the expected one
            current_url_ManualSWM = context.driver.current_url
            expected_url_ManualSWM = "http://localhost:9090/swm/ManualSWMSelection"
            assert current_url_ManualSWM == expected_url_ManualSWM, f"URL mismatch: Expected {expected_url_ManualSWM}, got {current_url_ManualSWM}"
            self.logger.info(f"********** URL Verified: {current_url_ManualSWM} **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceFacility_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceFacility_silicon).click()
            self.logger.info("********** Source Facility Is Selected  **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceWorkCenter_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceWorkCenter_waferSort).click()
            self.logger.info("********** Source Work Center Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceDevice_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceDevice_4670).click()
            self.logger.info("********** Source Device Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceTestProgram_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceTestProgram_PREBAKE_STDF_4670).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source Test program  Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceLots_Silicon(self, context):
        try:
            checkBox_SourceLotsTable = context.driver.find_element(By.XPATH, self.sourceLotsTable)

            if not checkBox_SourceLotsTable.is_selected():
                checkBox_SourceLotsTable.click()
                WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
                self.logger.info("********** Source Lots Is Selected  **********")
            else:
                self.logger.info("********** Source Lots Is Already Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceWafers_Silicon(self, context):
        try:
            checkBox_SourceWafersTable = context.driver.find_element(By.XPATH, self.sourceWafers_silicon)

            if not checkBox_SourceWafersTable.is_selected():
                checkBox_SourceWafersTable.click()
                self.logger.info("********** Source Wafers Is Selected  **********")
            else:
                self.logger.info("********** Source Wafers Is Already Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetFacility_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetFacility_silicon).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target facility Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetWorkCenter_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetWorkCenter_waferSort).click()
            self.logger.info("********** Target Work Center Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetDevice_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetDevice_4670).click()
            self.logger.info("********** Target device Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetTestProgram_Silicon(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetTestProgram_POSTBAKE_STDF_4670).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target Test program Is Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetLots_Silicon(self, context):
        try:
            checkBox_TargetLotsTable = context.driver.find_element(By.XPATH, self.targetLotsTable)
            if not checkBox_TargetLotsTable.is_selected():
                checkBox_TargetLotsTable.click()
                WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
                self.logger.info("********** Target Lots Is Selected  **********")
            else:
                self.logger.info("********** Target Lots Is Already Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetWafers_Silicon(self, context):
        try:
            checkBox_TargetWafersTable = context.driver.find_element(By.XPATH, self.targetWafers_silicon)
            if not checkBox_TargetWafersTable.is_selected():
                checkBox_TargetWafersTable.click()
                self.logger.info("********** Target Wafers Is Selected  **********")
            else:
                self.logger.info("********** Target Wafers Is Already Selected  **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickGenerateManualSWMButton(self, context):
        try:
            btn_GM_SWM = context.driver.find_element(By.XPATH, self.btn_generateManualSwm)
            btn_GM_SWM.click()
            self.logger.info("**********  Clicked On Generate Manual SWM Button  *********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

            # Verify if the URL matches the expected one
            current_url_ManualSWMView = context.driver.current_url
            expected_url_ManualSWMView = "http://localhost:9090/Swm/ManualSWMView"
            assert current_url_ManualSWMView == expected_url_ManualSWMView, f"URL mismatch: Expected {expected_url_ManualSWMView}, got {current_url_ManualSWMView}"
            self.logger.info(f"********** URL Verified: {current_url_ManualSWMView} **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def dataCombineBinWaferMap(self, context):
        try:
            div_MSwm_CombineBWM = context.driver.find_element(By.XPATH, self.div_ManualSWM_CBWMap)
            val_CombineBWM = div_MSwm_CombineBWM.text
            self.logger.info(f"**********  Get Data Of Combine Bin Wafer Map {val_CombineBWM}  *********")

            lot_id_match = re.search(r'Lot ID: (.+)', val_CombineBWM)
            wafer_id_match = re.search(r'Wafer ID: (.+)', val_CombineBWM)
            yield_match = re.search(r'Yield: ([\d.]+%)', val_CombineBWM)

            lot_id = lot_id_match.group(1) if lot_id_match else None
            wafer_id = wafer_id_match.group(1) if wafer_id_match else None
            yield_value = yield_match.group(1) if yield_match else None

            self.logger.info(f"********** Lot ID: {lot_id}, Wafer ID: {wafer_id}, Yield: {yield_value} *********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSaveToYieldwerx(self, context):
        try:
            button_SaveToYieldwerx = context.driver.find_element(By.XPATH, self.btn_SaveToYieldwerx)
            button_SaveToYieldwerx.click()
            self.logger.info("**********  Clicked On Save To Yieldwerx Button  *********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def verifySuccessMessage(self, context):
        try:
            cls_SuccessMessage = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.msg_Success)))
            success_message_text = cls_SuccessMessage.text
            self.logger.info(f"********** Success Message Verified: {success_message_text} *********")
            if "success" in success_message_text.lower():
                self.logger.info("********** Manual SWM Successfully Saved to Yieldwerx  *********")
        except Exception as e:
            MyException.handle_exception(context, e)
