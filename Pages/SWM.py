import re
import time
import pyodbc
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utilities.Exceptions import MyException
from utilities.customLogger import LogGen
from utilities.randomTextGen import RandomTextGen


class SWMClass:
    logger = LogGen.loggen()
    name = None

    def __init__(self):
        pass

    nameSWM = ""
    policyNameSWM = ""
    swm_dd = "//span[normalize-space()='SWM']"
    swmRule_lnk = "//a[@href='/swm/rules']"
    swmPolicy_lnk = "//span[normalize-space()='SWM Policies']"
    newSwmRule_btn = "//span[normalize-space()='New SWM Rule']"
    Name_txt = "//input[@id='Name']"
    description_txt = "//textarea[@id='Description']"
    inputData_tab = "//a[@id='input-data-selection-tab']"
    ruleDefinition_tab = "//a[@id='bin-rule-tab']"
    ruleDefinition = "bin-rule-tab"
    OutputDataSelection_tab = "//a[normalize-space()='Output Data Selection']"
    manageException_tab = "//a[@id='manage-exception-tab']"
    automateSwmPolices_lnk = "//span[normalize-space()='Automate SWM Policies']"
    manualSwmPolices_lnk = "//span[normalize-space()='Manual SWM']"
    automateSwmPolicy_btn = "//a[@title='New Automate SWM Policy']"
    level_dd = "Level"
    bin_dd = "BinTypeID"
    custom_rb = "//input[@value='Custom']"
    all_rb = "//input[@value='All']"
    loader = "(//body[@class='loading'])[1]"
    sourceFacility_sl = "//select[@id='SourceFacility']//option[@value='MPS'][normalize-space()='MPS']"
    sourceWorkCenter_sl = "//select[@id='SourceWorkCenter']//option[@value='WAFER SORT']"
    sourceDevice_sl = "//select[@id='SourceDevice']//option[@value='DEV1']"
    sourceProbe_sl = "//select[@id='SourceProbes']//option[@value='1|M']"
    sourceTestProgram_sl = "//option[@value='TP_A2']"
    targetTestProgram_sl = "//option[@value='TP_B1']"
    targetFacility_sl = "//select[@id='TargetFacility']//option[@value='MPS']"
    targetWorkCenter_sl = "//select[@id='TargetWorkCenter']//option[@value='WAFER SORT']"
    targetDevice_sl = "//select[@id='TargetDevice']//option[@value='DEV2']"
    targetProbe_sl = "//select[@id='TargetProbes']//option[@value='1|M']"
    ruleType_dd = "//select[@id='RuleTypeID']"
    binRuleDetail_sl = "RuleMissingDieID"
    sourceRuleBin_sl = "SourceRuleBinID"
    targetRuleBin_sl = "TargetRuleBinID"
    customBin_sl = "RuleBinTypeID"
    binNumber_txt = "custom-bin-number"
    email_tab = "//a[@id='email-notification-tab']"
    emailPolicy_tab = "//a[@id='email-tab']"
    binName_txt = "custom-bin-name"
    ownerName_txt = "//input[@id='OwnerName']"
    ownerEmail_txt = "//input[@id='OwnerEmailAddress']"
    save_btn = "//input[@value='Save']"
    newSwmPolicy_btn = "//span[normalize-space()='New SWM Policy']"
    inputDataRuleSelection_tab = "//a[@id='input-data-selection-tab']"
    rulesForPolicy_cb = "//tbody/tr[2]/td[1]/input[1]"
    metadataSelection_dd = "//select[@id='MetaDataID']"
    delete_btn = "//span[@class='ui-button-icon-primary ui-icon ui-icon-trash'][1]"
    deletePopup_btn = "//button[normalize-space()='Yes']"
    generateManualSwm_btn = "//input[@id='btn-calculate']"
    saveToYieldwerx_btn = "//button[@id='btn-save-to-yieldwerx']"

    sourceLegend_btn = "//a[@id='panel1_ChartContainer_legend']"
    targetLegend_btn = "//a[@id='panel2_ChartContainer_legend']"
    combineLegend_btn = "//a[@id='panel3_ChartContainer_legend']"

    sourceZoom_btn = "//button[@id='panel1_ChartContainer_zoom']"
    targetZoom_btn = "//button[@id='panel2_ChartContainer_zoom']"
    combineZoom_btn = "//button[@id='panel3_ChartContainer_zoom']"

    newTabChart_ttl = "//b[@id='chart-title-bold']"
    closeLegendSource_btn = "//div[@id='panel1_ChartContainer_legend_data']//button[@type='button']"
    closeLegendTarget_btn = "//div[@id='panel2_ChartContainer_legend_data']//button[@type='button']"
    closeLegendCombine_btn = "//div[@id='panel3_ChartContainer_legend_data']//button[@type='button']"

    sourceFacilityDiv = "//*[@id='SourceFacility']"
    targetFacilityDiv = "//*[@id='TargetFacility']"
    sourceFacilityOption = "//*[@id='SourceFacility']//*"
    targetFacilityOption = "//*[@id='TargetFacility']//*"

    manageTabForException = "//*[@id='manage-exception-tab']"

    def clickOnSWMDropDown(self, context):
        try:
            context.driver.find_element(By.XPATH, self.swm_dd).click()
            self.logger.info("********** Clicked On The SWM drop Down **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def test(self, context):
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.4,58840;DATABASE=yw_V4_Automation_4_2_25_0_AhsanMughal;UID=sa;PWD=subway3328'
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        # Use pyodbc to query SQL Server and retrieve data
        context.user_details_from_db = cursor.execute("SELECT * FROM WAFER WHERE Wafer_Sequence='1201'").fetchone()
        self.logger.info("i am here")

    def clickSWMRules(self, context):
        try:
            context.driver.find_element(By.XPATH, self.swmRule_lnk).click()
            self.logger.info("********** Clicked On The SWM rules **********")
            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def verifySwmRulePageOpen(self, context):
        try:
            status = context.driver.find_element(By.XPATH, self.newSwmRule_btn).is_displayed()
            assert status is True
            self.logger.info("********** verified Rule Page Opened **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickNewSwmRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.newSwmRule_btn).click()
            self.logger.info("********** Clicked On The New Rule Button **********")
            time.sleep(3)
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def enterNameForSWMRule(self, context):
        try:
            global nameSWM
            nameSWM = RandomTextGen.randomText()
            context.driver.find_element(By.XPATH, self.Name_txt).send_keys(nameSWM)
            self.logger.info("**********  Name is written **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def enterDescriptionForSWMRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.description_txt).send_keys("This is a SWM Rule")
            self.logger.info("**********  Description is written **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickInputDataSelection(self, context):
        try:
            context.driver.find_element(By.XPATH, self.inputData_tab).click()
            self.logger.info("**********  Input Data Selection Tab Is Selected *********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectLevelSwmRule(self, context):
        try:
            level = context.driver.find_element(By.ID, self.level_dd)
            select = Select(level)
            option_value_to_select = "Device"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Level is Selected **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectBin(self, context):
        try:
            bin = context.driver.find_element(By.ID, self.bin_dd)
            select = Select(bin)
            option_value_to_select = "49"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Level is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickRulesValidation(self, context):
        try:
            context.driver.find_element(By.XPATH, self.custom_rb).click()
            self.logger.info("**********  Custom radio button is checked **********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.all_rb).click()
            self.logger.info("**********  All radio button is checked **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceFacility(self, context):
        try:
            selectSourceFacilitySWM = context.driver.find_element(By.XPATH, self.sourceFacility_sl)
            selectSourceFacilitySWM.click()
            SWMClass.name = selectSourceFacilitySWM
            self.logger.info(f"*********** Name Stored: {SWMClass.name} ***********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source Facility Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceWorkCenter(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceWorkCenter_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source Work Center Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceDevice(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceDevice_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source Device Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceTestProgram(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceTestProgram_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source Test program  Is Selected  **********")

        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectSourceProbe(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceProbe_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Source probe Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetFacility(self, context):
        try:

            context.driver.find_element(By.XPATH, self.targetFacility_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target facility Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetWorkCenter(self, context):
        try:

            context.driver.find_element(By.XPATH, self.targetWorkCenter_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target Work Center Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetDevice(self, context):
        try:

            context.driver.find_element(By.XPATH, self.targetDevice_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target device Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetTestProgram(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetTestProgram_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target Test program  Is Selected  **********")

        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectTargetProbe(self, context):
        try:

            context.driver.find_element(By.XPATH, self.targetProbe_sl).click()
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Target facility Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickRuleDefinition(self, context):
        driver = context.driver
        driver.find_element(By.XPATH, self.ruleDefinition_tab)
        try:
            element = WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ruleDefinition_tab))
            )
            print("xpath is: ", element)
            element.click()

            self.logger.info("********** Clicked On Rule Definition Tab  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectRuleType(self, context):
        try:
            ruleType = context.driver.find_element(By.XPATH, self.ruleType_dd)
            select = Select(ruleType)
            option_value_to_select = "1"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Rule Tyoe  is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectBinRuleDetails(self, context):
        try:
            ruleType = context.driver.find_element(By.ID, self.binRuleDetail_sl)
            select = Select(ruleType)
            option_value_to_select = "2"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Rule Details  is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceBin(self, context):
        try:
            bin = context.driver.find_element(By.ID, self.sourceRuleBin_sl)
            select = Select(bin)
            option_value_to_select = "5"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Source Rule Bin is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetBin(self, context):
        try:
            bin = context.driver.find_element(By.ID, self.targetRuleBin_sl)
            select = Select(bin)
            option_value_to_select = "5"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Target Rule Bin is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectCustomBin(self, context):
        try:
            binType = context.driver.find_element(By.ID, self.customBin_sl)
            select = Select(binType)
            option_value_to_select = "3"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Custom Bin is Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectBinNumberBinName(self, context):
        try:
            findBinNum = context.driver.find_element(By.ID, self.binNumber_txt)
            findBinNum.send_keys("37")
            self.logger.info("********** Bin Number Entered **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

            findBinName = context.driver.find_element(By.ID, self.binName_txt)
            findBinName.send_keys("Swm Bin")
            self.logger.info("********** Bin Name Entered **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectEmailNotificationTab(self, context):
        try:
            context.driver.find_element(By.XPATH, self.email_tab).click()
            self.logger.info("**********  Email Notification Tab Is Selected *********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def enterNameEmail(self, context):
        try:
            context.driver.find_element(By.XPATH, self.ownerName_txt).send_keys("yieldwerx owner")
            self.logger.info("********** Name is entered **********")
            context.driver.find_element(By.XPATH, self.ownerEmail_txt).send_keys("alert@yieldwerx.com")
            self.logger.info("********** Email is entered **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def saveButton(self, context):
        try:
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.save_btn).click()
            self.logger.info("********** Clicked on Save button **********")
            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def verifySwmRule(self, context):
        try:
            time.sleep(4)
            latestRecord = context.driver.find_element(By.XPATH, "//tr[2]/td[4]")
            latestRecordText = latestRecord.text
            assert latestRecordText == nameSWM, f"Expected '{nameSWM}'  but got '{latestRecordText}'"
            self.logger.info("********** Record is Successfully Created **********")

        except Exception as e:
            MyException.handle_exception(context, e)

        # *****************************                             *****************************
        # *****************************     SWM Policy Creation     *****************************
        # *****************************                             *****************************

    def clickSwmPolicy(self, context):
        try:
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            context.driver.find_element(By.XPATH, self.swmPolicy_lnk).click()
            self.logger.info("********** Clicked On The SWM rules **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickNewSwmPolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.newSwmPolicy_btn).click()
            self.logger.info("********** Clicked On The New Policy Button **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            MyException.handle_exception(context, e)

    def enterNameForSWMPolicy(self, context):
        try:
            global nameSWM
            nameSWM = RandomTextGen.randomText()
            context.driver.find_element(By.XPATH, self.Name_txt).send_keys(nameSWM)
            self.logger.info("**********  Name is written **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def enterDescriptionForSWMPolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.description_txt).send_keys("This is a SWM Policy")
            self.logger.info("**********  Description is written **********")
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickTestProgramOptions(self, context):
        try:
            context.driver.find_element(By.XPATH, self.custom_rb).click()
            self.logger.info("**********  Custom radio button is checked **********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.all_rb).click()
            self.logger.info("**********  All radio button is checked **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectRuleForPolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.rulesForPolicy_cb).click()
            self.logger.info("**********  Rule is selected for the Policy **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickOutputDataSelection(self, context):
        try:
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.OutputDataSelection_tab).click()
            self.logger.info("**********  Output Data Selection Tab is opened **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def metadataSelectionForm(self, context):
        try:
            metaData = context.driver.find_element(By.XPATH, self.metadataSelection_dd)
            select = Select(metaData)
            option_value_to_select = "1"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Source Wafer Is Selected from Metadata Selection Form **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickManageException(self, context):
        try:
            context.driver.find_element(By.XPATH, self.manageException_tab).click()
            self.logger.info("**********  Manage Exception Tab is opened **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def verifySwmPolicy(self, context):
        try:
            time.sleep(2)
            latestRecord = context.driver.find_element(By.XPATH, "//tr[2]/td[4]")
            latestRecordText = latestRecord.text
            # assert latestRecordText == policyNameSWM, f"Expected '{policyNameSWM}'  but got '{latestRecordText}'"
            self.logger.info("********** Record is Successfully Created **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def deleteSWMPolicy(self, context):
        try:
            (WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.delete_btn))).click())
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.deletePopup_btn).click()
            self.logger.info("********** Record is deleted Successfully **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSwmAutomatePolicies(self, context):
        try:
            context.driver.find_element(By.XPATH, self.automateSwmPolices_lnk).click()
            self.logger.info("********** Automate SWM Polices Opened **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSwmAutomateNewPolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.automateSwmPolicy_btn).click()
            self.logger.info("********** Automate New SWM Polices button Is Clicked **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectEmailNotificationTabForAutomatePolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.emailPolicy_tab).click()
            self.logger.info("**********  Email Notification Tab Is Selected *********")
            time.sleep(3)

        except Exception as e:
            MyException.handle_exception(context, e)

            # **************************** Manual SWM ************************************

    def clickManualSwm(self, context):
        try:
            context.driver.find_element(By.XPATH, self.manualSwmPolices_lnk).click()
            self.logger.info("**********  Clicked On Manual SWM *********")
            time.sleep(3)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickGenerateManualSwm(self, context):
        try:
            context.driver.find_element(By.XPATH, self.generateManualSwm_btn).click()
            self.logger.info("**********  Clicked On Generate Manual SWM *********")
            time.sleep(2)
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSaveToYieldwerx(self, context):
        try:
            context.driver.find_element(By.XPATH, self.saveToYieldwerx_btn).click()
            self.logger.info("**********  Clicked On Save To Yieldwerx *********")
            time.sleep(2)
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSourceLegend(self, context):
        try:
            context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            context.driver.find_element(By.XPATH, self.sourceLegend_btn).click()
            self.logger.info("**********  Clicked On Source Legend *********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.closeLegendSource_btn).click()
            self.logger.info("**********  Legend is close *********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickTargetLegend(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetLegend_btn).click()
            self.logger.info("**********  Clicked On Target Legend *********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.closeLegendTarget_btn).click()
            self.logger.info("**********  Legend is close *********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickCombineLegend(self, context):
        try:
            context.driver.find_element(By.XPATH, self.combineLegend_btn).click()
            self.logger.info("**********  Clicked On Target Legend *********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.closeLegendCombine_btn).click()
            self.logger.info("**********  Legend is close *********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickSourceZoom(self, context):
        try:
            context.driver.find_element(By.XPATH, self.sourceZoom_btn).click()
            self.logger.info("**********  Clicked On Source Zoom *********")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            time.sleep(3)
            newWindow = context.driver.find_element(By.XPATH, self.newTabChart_ttl).is_displayed()
            assert newWindow is True
            self.logger.info("**********  Successfully Open new tab SOURCE BIN WAFER MAP  **********")
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            self.logger.info("**********  New Tab closed Successfully And back to previous Tab  **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickTargetZoom(self, context):
        try:
            context.driver.find_element(By.XPATH, self.targetZoom_btn).click()
            self.logger.info("**********  Clicked On Target Zoom *********")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            time.sleep(3)
            newWindow = context.driver.find_element(By.XPATH, self.newTabChart_ttl).is_displayed()
            assert newWindow is True
            self.logger.info("**********  Successfully Open new tab TARGET BIN WAFER MAP  **********")
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            self.logger.info("**********  New Tab closed Successfully And back to previous Tab  **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickCombineZoom(self, context):
        try:
            context.driver.find_element(By.XPATH, self.combineZoom_btn).click()
            self.logger.info("**********  Clicked On Combine Zoom *********")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            time.sleep(3)
            newWindow = context.driver.find_element(By.XPATH, self.newTabChart_ttl).is_displayed()
            assert newWindow is True
            self.logger.info("**********  Successfully Open new tab COMBINE BIN WAFER MAP  **********")
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            self.logger.info("**********  New Tab closed Successfully And back to previous Tab  **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def policyNameSWMTP(self, context):
        try:
            allSourceFacilitiesDiv = context.driver.find_element(By.XPATH, self.sourceFacilityDiv)
            s_Facility = allSourceFacilitiesDiv.find_elements(By.TAG_NAME, "option")
            s_FacilityValues = [option.get_attribute("textContent") for option in s_Facility]
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info(f"**********  Source Facilities Names Ahsan {s_FacilityValues} **********")

            allTargetFacilitiesDiv = context.driver.find_element(By.XPATH, self.targetFacilityDiv)
            t_Facility = allTargetFacilitiesDiv.find_elements(By.TAG_NAME, "option")
            t_FacilityValues = [option.get_attribute("textContent") for option in t_Facility]
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info(f"**********  Target Facilities Names {t_FacilityValues} **********")

            if "MPS" in s_FacilityValues and t_FacilityValues:
                if SWMClass.name.is_selected():
                    self.logger.info(f"Selected")
                    WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
                    context.driver.find_element(By.XPATH, self.Name_txt).send_keys("MPS Test Program Policy")
                elif "Silicon" in s_FacilityValues and t_FacilityValues:
                    self.logger.info("Yes")
                    context.driver.find_element(By.XPATH, self.Name_txt).send_keys("SWM Test Program Policy")
                else:
                    self.logger.info("No Facility is selected")

        except Exception as e:
            MyException.handle_exception(context, e)
