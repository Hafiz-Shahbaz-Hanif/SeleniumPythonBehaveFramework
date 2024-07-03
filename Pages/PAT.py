import os
import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utilities.Exceptions import MyException
from utilities.customLogger import LogGen
from utilities.randomTextGen import RandomTextGen


class PATClass:
    logger = LogGen.loggen()

    def __init__(self):
        pass

    # *****************************                             *****************************
    # *****************************     PAT Rule Locators       *****************************
    # *****************************                             *****************************
    qualityPAT_lnk = "//span[normalize-space()='Quality & PAT']"
    PAT_dd = "//a[@href='#PAT-report']"
    rulesPAT = "//a[@href='/Rules']"
    policyPAT = "//a[@href='/Policies']"
    dynamicRule_btn = "//div[@id='btn-new-dynamic-pat']//a[@id='btn-dynamic-rule']"
    staticRule_btn = "//span[normalize-space()='New Static PAT']"
    txtRuleName = "//input[@id='Rule_Name']"
    txtRuleDescription = "//textarea[@id='Rule_Description']"
    createPATRuleHeading = "//h6[@id='modal-form-label']"
    parameter_tab = "parameter-tab"
    dynamicLimit_tab = "dynamic-limit-tab"
    staticLimit_tab = "initial-limit-tab"
    emailNotification_tab = "//a[normalize-space()='Email Notification']"
    calculateSeed_Btn = "//input[@id='btn-calculate-static-seed-limit']"
    selectLotFromCalculateSeed_op = "//td[1]/select/option[1]"
    calculateSeedInPopup_Btn = "//input[@id='btn-calculate']"
    reCalculateLimitAfter_tb = "//input[@id='Notify_LotCount']"
    errorForLessThan7 = "//div[normalize-space()='( Value must be greater than 7 )']"
    PATDistribution_dd = "//select[@id='PatDistributionTypeId']"
    lowerBinNumber_txt = "//input[@id='custom-bin-number-lower']"
    upperBinNumber_txt = "//input[@id='custom-bin-number-upper']"
    lowerBinName_txt = "//input[@id='custom-bin-name-lower']"
    upperBinName_txt = "//input[@id='custom-bin-name-upper']"
    staticBinNumber_txt = "//input[@id='custom-bin-number2']"
    staticBinName_txt = "//input[@id='custom-bin-name2']"
    opFacility = "//option[@value='MPS']"
    opWorkCenter = "//option[@value='WAFER SORT']"
    opDevice = "//option[@value='DEV2']"
    opTestProgram = "//option[@value='TP_B2']"
    opParameter = "//td[contains(@title,', B22-18/T')]"
    applyPATToDevice_cb = "//input[@id='IsPAT_Rule_Applied_ToDevie']"
    ownerName_txt = "//input[@id='Owner_Name']"
    ownerEmail_txt = "//input[@id='Owner_Email']"
    ownerPATRule_cb = "//input[@id='HasOwner']"
    btnSave = "//input[@id='btn-save']"
    name = ""
    loader = "(//body[@class='loading'])[1]"

    # *****************************                             *****************************
    # *****************************     PAT Policy Locators     *****************************
    # *****************************                             *****************************

    policyName = ""
    newPolicy_btn = "btn-new-policy"
    policyName_txt = "PolicyName"
    type_dd = "//select[@id='ddlSelection']"
    device_dd = "//select[@id='Device']"
    testProgram_dd = "//select[@id='Test_Program']"
    rule_cb = "//tbody/tr[2]/td[1]/input[@role='checkbox']"
    savePolicy_btn = "button-save"

    # *****************************                                              *****************************
    # *****************************     PAT Automate Business rules Locators     *****************************
    # *****************************                                              *****************************

    automateBusinessRule_lnk = "//a[@href='/AutomateBusinessRules?IsGDBN=False']"
    createAutomateBusinessRule_btn = "//a[@id='btn-new-rule']"
    facilityForAutomate_op = "//option[@value='MPS']"
    workCenterForAutomate_op = "//option[@value='WAFER SORT']"
    deviceForAutomate_op = "//option[@value='DEV2']"
    testProgramForAutomate_op = "//option[@value='TP_B2']"
    policyForAutomate_op = "//tr[@role='row'][@id='1']/td[2]"
    automatePolicyName = ""
    deletePolicyForAutomate_btn = "//span[@class='ui-button-icon-primary ui-icon ui-icon-trash'][1]"
    deletePolicyForAutomateConfirmPopup_btn = "//button[normalize-space()='Yes']"
    policyForAutomate_cb = "//td[@role='gridcell']//input[@role='checkbox'][1]"
    AutomatePolicyConfirmPopup_btn = "//button[normalize-space()='Yes']"
    successMessage_alert = "//div[@class='bootstrap-growl alert alert-success']"
    automateSetupStatus_txt = "//tr[@role='row'][2]//td[@role='gridcell'][8]"

    # *****************************                                              *****************************
    # *****************************         PAT Policy Manual Locators          *****************************
    # *****************************                                              *****************************

    manualPAT_lnk = "//span[contains(text(),'Manual PAT')]"
    facilityManualPAT_op = "//option[contains(text(),'MPS')]"
    workCenterManualPAT_op = "//option[@value='WAFER SORT']"
    deviceManualPAT_op = "//body[1]/div[3]/div[4]/div[2]/div[2]/table[1]/tbody[1]/tr[2]/td[3]/div[1]/select[1]/option[1]"
    testProgramManualPAT_op = "//body[1]/div[3]/div[4]/div[2]/div[2]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/select[1]/option[1]"
    lotsManualPAT_op = "Lots"
    waferUnSelectManualPAT_op = "jqg_WafersGrid_167"
    waferSelectManualPAT_op = "jqg_WafersGrid_171"
    policyManualPAT_op = "//tbody/tr[@id='1']/td[2]"
    calculateManualPAT_btn = "btn-calculate"
    saveToYieldWerxManualPAT_btn = "btn-save-to-yieldwerx"
    exportMapManualPAT_btn = "exportMap"
    enableMultisiteDPATFunctionality_chkbox = "IsMultiSiteLimitCalculation"
    executeMultiSite_btn = "cmd-execute"
    waferMapTab = "wafer-map-tab"
    waferMapTabLegend = "panel2000_ChartContainer_legend"
    closeWaferMapTabLegend = "div[id='panel2000_ChartContainer_legend_data'] button[type='button']"
    zoomWaferMapOrignal_btn = "//button[@id='panel2000_ChartContainer_zoom']"
    zoomWaferMapPAT_btn = "//button[@id='panel2001_ChartContainer_zoom']"
    histogramMapTab = "histogram-map-tab"
    histogramMapTabLegend = "panel6000_ChartContainer_legend"
    closeHistogramTabLegend = "div[id='panel6000_ChartContainer_legend_data'] button[type='button']"
    trendMapTab = "trend-map-tab"
    trendMapTabLegend = "panel4000_ChartContainer_legend"
    closeTrendTabLegend = "div[id='panel4000_ChartContainer_legend_data'] button[type='button']"
    zoomDieLost_btn = "btn-die-lost"
    closeZoom = "div[id='my-modal'] button[type='button']"
    zoomByWaferByPassAndFail_btn = "btn-wafer-bin"
    zoomByLotPassAndFail_btn = "btn-lot-bin"
    downgrade_ScrapMe_btn = "//button[@id='btn-zoom']"
    downgradePopUp_btn = "//button[@id='btn-downgrade']"
    downgradeScrapClose_btn = "div[id='modal-content'] button[type='button']"
    # containerWaferMap = "//div[@id='highcharts-43']//*[name()='svg']"
    containerWaferMap = "panel1-patzoomwafer-chart-container"

    # *****************************                             *****************************
    # *****************************     PAT Rule Creation       *****************************
    # *****************************                             *****************************

    def clickPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.qualityPAT_lnk).click()
            self.logger.info("**********  Clicked on the Quality And PAT  **********")
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.PAT_dd).click()
            self.logger.info("**********  Clicked on the PAT DropDown  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def clickPATRules(self, context):
        try:
            context.driver.find_element(By.XPATH, self.rulesPAT).click()
            self.logger.info("**********  Clicked on the PAT Rules  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def verifyDashboard(self, context):
        try:
            status = context.driver.find_element(By.XPATH, self.staticRule_btn).is_displayed()
            assert status is True
            self.logger.info("**********  Dashboard Opened Successfully  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def clickNewDynamicPATRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.dynamicRule_btn).click()
            self.logger.info("**********  Create new dynamic rule button is clicked  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def clickNewStaticPATRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.staticRule_btn).click()
            self.logger.info("**********  Create new Static rule button is clicked  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def verifyCreateNewRuleScreen(self, context):
        try:
            status = context.driver.find_element(By.XPATH, self.createPATRuleHeading).is_displayed()
            assert status is True
            self.logger.info("**********  Verify create rule screen is opened successfully **********")
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def enterNameForPATRule(self, context):
        try:
            global name
            name = RandomTextGen.randomText()
            context.driver.find_element(By.XPATH, self.txtRuleName).send_keys(name)
            self.logger.info("**********  Name is written **********")
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def enterDescriptionForPATRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.txtRuleDescription).send_keys("New D A Rule Description")
            self.logger.info("**********  Description is written **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)
    def selectParameterTab(self, context):
        try:
            context.driver.find_element(By.ID, self.parameter_tab).click()
            self.logger.info("**********  Selected parameter **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def selectFacility(self, context):
        try:
            context.driver.find_element(By.XPATH, self.opFacility).click()
            self.logger.info("**********  Facility is selected **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def selectWorkcenter(self, context):
        try:
            context.driver.find_element(By.XPATH, self.opWorkCenter).click()
            self.logger.info("**********  WorkCenter Is selected **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def selectDevice(self, context):
        try:
            context.driver.find_element(By.XPATH, self.opDevice).click()
            self.logger.info("**********  Device Selected **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def selectTestProgram(self, context):
        try:
            context.driver.find_element(By.XPATH, self.opTestProgram).click()
            self.logger.info("**********  Test Program Selected **********")
            time.sleep(3)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def selectTestParameter(self, context):
        try:
            parameter = context.driver.find_element(By.XPATH, self.opParameter)
            self.logger.info("**********  Test Parameter Found **********")
            parameter.click()
            self.logger.info("**********  Test Parameter Clicked **********")
            time.sleep(2)
        except NoSuchElementException as e:
            # Handle element not found exception
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error("An error occurred: Test parameter is not found")
            self.logger.error(f"Error details: {str(e)}")

    def applyPATToDeviceCheck(self, context):
        try:
            context.driver.find_element(By.XPATH, self.applyPATToDevice_cb ).click()
            self.logger.info("********** Apply PAT to device Level CheckBox checked **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.info("********** Unable to locate the the checkBox **********")
            self.logger.error(f"An error occurred: {str(e)}")
            raise


    def selectDynamicLimitTab(self, context):
        try:
            context.driver.find_element(By.ID, self.dynamicLimit_tab).click()
            self.logger.info("********** Dynamic Limits Tab clicked **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectStaticLimitTab(self, context):
        try:
            context.driver.find_element(By.ID, self.staticLimit_tab).click()
            self.logger.info("********** Static Limits Tab Clicked **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def calculateSeedLimits(self, context):
        try:
            context.driver.find_element(By.XPATH, self.calculateSeed_Btn).click()
            self.logger.info("********** Click On Static Limit calculate Button **********")
            time.sleep(2)
            # context.driver.find_element(By.XPATH, self.selectLotFromCalculateSeed_op).click()
            # self.logger.info("********** Lot is selected **********")
            # time.sleep(1)
            context.driver.find_element(By.XPATH, self.calculateSeedInPopup_Btn).click()
            self.logger.info("********** Click on calculate Button On popup **********")
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def enterNumberForRecalculation(self, context):
        try:
            context.driver.find_element(By.XPATH, self.reCalculateLimitAfter_tb).send_keys(3)
            self.logger.info("********** 3 Enter for recalculation Lots  **********")
            # click outside to get the error message
            context.driver.find_element(By.ID, self.staticLimit_tab).click()
            status = context.driver.find_element(By.XPATH, self.errorForLessThan7).is_displayed()
            assert status is True
            time.sleep(1)
            self.logger.info("********** Error message for the less than 7 is found  **********")
            context.driver.find_element(By.XPATH, self.reCalculateLimitAfter_tb).send_keys(9)
            self.logger.info("********** 9 Enter for recalculation Lots  **********")
            context.driver.find_element(By.ID, self.staticLimit_tab).click()

            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise


    def selectPATDistribution(self, context):
        try:
            element = context.driver.find_element(By.XPATH, self.PATDistribution_dd)
            select = Select(element)
            Unkown_value_to_select = "83"
            select.select_by_value(Unkown_value_to_select)
            self.logger.info("********** PAT Distribution Unkown is Selected **********")
            time.sleep(1)

            context.driver.find_element(By.ID, self.parameter_tab).click()
            time.sleep(2)
            self.logger.info("********** Parameter TAB is Selected **********")

            checkBox = context.driver.find_element(By.XPATH, "//input[@id='IsValidate_PAT_Limits']")
            if not checkBox.is_enabled():
                self.logger.info("********** Validate PAT Limits Check Box is Disabled **********")
            else:
                self.logger.error("********** Validate PAT Limits Check Box is Enabled **********")
                context.driver.close()

            context.driver.find_element(By.ID, self.dynamicLimit_tab).click()
            self.logger.info("********** Dynamic Limits Tab clicked **********")
            time.sleep(2)

            element2 = context.driver.find_element(By.XPATH, self.PATDistribution_dd)
            select = Select(element2)
            default_value_to_select = "82"
            select.select_by_value(default_value_to_select)
            self.logger.info("********** PAT Distribution default is Selected **********")
            time.sleep(1)


        except Exception as e:
            error_message = ' '.join(str(e).split()[:40])
            self.logger.error(error_message)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise


    def enterBinNumber(self, context):
        try:
            findBinNumL = context.driver.find_element(By.XPATH, self.lowerBinNumber_txt)
            findBinNumL.send_keys("66")
            self.logger.info("********** Lower Bin Number is Entered **********")
            findBinNumU = context.driver.find_element(By.XPATH, self.upperBinNumber_txt)
            findBinNumU.send_keys("99")
            self.logger.info("********** Upper Bin Number is Entered **********")
            time.sleep(2)
        except Exception as e:
            error_message = ' '.join(str(e).split()[:40])
            self.logger.error(error_message)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise

    def enterBinName(self, context):
        try:
            findBinNameL = context.driver.find_element(By.XPATH, self.lowerBinName_txt)
            findBinNameL.send_keys("Lower PAT Bin")
            self.logger.info("********** Lower Bin Name Entered **********")

            findBinNameU = context.driver.find_element(By.XPATH, self.upperBinName_txt)
            findBinNameU.send_keys("Upper PAT Bin")
            self.logger.info("********** Upper Bin Name Entered **********")
            time.sleep(2)
        except Exception as e:
            error_message = ' '.join(str(e).split()[:40])
            self.logger.error(error_message)
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            raise


    def enterStaticBinNumber(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, self.staticBinNumber_txt)
            self.logger.info("********** Bin Number box found **********")
            findBinNum.send_keys("22")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def enterStaticBinName(self, context):
        try:
            findBinName = context.driver.find_element(By.XPATH, self.staticBinName_txt)
            self.logger.info("********** Bin Name box found **********")
            findBinName.send_keys("PAT Bin")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise


    def selectEmailNotificationTab(self, context):
        try:
            context.driver.find_element(By.XPATH, self.emailNotification_tab).click()
            self.logger.info("********** Email Notification Tab clicked **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise


    def enterEmailName(self, context):
        try:
            context.driver.find_element(By.XPATH, self.ownerPATRule_cb).click()
            self.logger.info("********** Owner of PAT rule checkBox is Checked **********")
            context.driver.find_element(By.XPATH, self.ownerName_txt).send_keys("yieldwerx owner")
            self.logger.info("********** Name is entered **********")
            context.driver.find_element(By.XPATH, self.ownerEmail_txt).send_keys("yieldwerxowner@yopmail.com")
            self.logger.info("********** Email is entered **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise


    def clickSave(self, context):
        try:
            context.driver.find_element(By.XPATH, self.btnSave).click()
            self.logger.info("**********  Save button clicked  **********")
            time.sleep(5)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifySaved(self, context):
        try:
            latestRecord = context.driver.find_element(By.XPATH, "//tr[2]/td[3]")
            latestRecordText = latestRecord.text
            assert latestRecordText == name, f"Expected '{name}'  but got '{latestRecordText}'"
            self.logger.info("********** Record is Successfully Created **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

        # *****************************                             *****************************
        # *****************************     PAT Policy Creation     *****************************
        # *****************************                             *****************************

    def clickPATPolicy(self, context):
        try:
            context.driver.find_element(By.XPATH, self.policyPAT).click()
            self.logger.info("********** Clicked On PAT Policy **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifyPatPolicyPageDisplayed(self, context):
        try:
            status = context.driver.find_element(By.ID, self.newPolicy_btn).is_displayed()
            assert status is True
            self.logger.info("********** PAT Policy Page Opened Successfully **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickNewPolicy(self, context):
        try:
            context.driver.find_element(By.ID, self.newPolicy_btn).click()
            self.logger.info("********** Clicked on New PAT Policy **********")
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def enterPolicyName(self, context):
        try:
            global policyName
            policyName = RandomTextGen.randomText()
            context.driver.find_element(By.ID, self.policyName_txt).send_keys(policyName)
            self.logger.info("********** Name Entered **********")
            time.sleep(1)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def verifyPolicySaved(self, context):
        try:
            latestRecord = context.driver.find_element(By.XPATH, "//tbody/tr[2]/td[4]")
            latestRecordText = latestRecord.text
            assert latestRecordText == policyName, f"Expected '{policyName}'  but got '{latestRecordText}'"
            self.logger.info("********** Record is Successfully Created **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")
            context.driver.close()
            raise

    def selectTypeOnPolicy(self, context):
        try:
            typeDD_element = context.driver.find_element(By.XPATH, self.type_dd)
            select = Select(typeDD_element)
            option_value_to_select = "2"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Type is Selected **********")
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectDeviceOnPolicy(self, context):
        try:
            deviceDD_element = context.driver.find_element(By.XPATH, self.device_dd)
            select = Select(deviceDD_element)
            option_value_to_select = "DEV2"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Device is Selected **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectTestProgramOnPolicy(self, context):
        try:
            testProgramDD_element = context.driver.find_element(By.XPATH, self.testProgram_dd)
            select = Select(testProgramDD_element)
            option_value_to_select = "TP_B2"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Test Program is Selected **********")
            time.sleep(3)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickCheckBoxOfCreatedRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.rule_cb).click()
            self.logger.info("********** Rule checkbox is checked **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def savePolicy(self, context):
        try:
            context.driver.find_element(By.ID, self.savePolicy_btn).click()
            self.logger.info("********** Clicked on the Save Policy button **********")
            time.sleep(5)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

        # *****************************                                    *****************************
        # *****************************     PAT Automate Business Rule     *****************************
        # *****************************                                    *****************************

    def clickAutomateBusinessRules(self, context):
        try:
            context.driver.find_element(By.XPATH, self.automateBusinessRule_lnk).click()
            time.sleep(2)
            self.logger.info("********** Clicked on Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.createAutomateBusinessRule_btn).click()
            time.sleep(2)
            self.logger.info("********** Clicked on Create Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectFacilityOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.facilityForAutomate_op).click()
            time.sleep(2)
            self.logger.info("********** Facility Selected For Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectWorkCenterOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.workCenterForAutomate_op).click()
            self.logger.info("********** work Center is Selected For Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectDeviceOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.deviceForAutomate_op).click()
            self.logger.info("********** Device is Selected For Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectTestProgramOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, self.testProgramForAutomate_op).click()
            self.logger.info("********** Test Program is Selected For Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectPolicyOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            policy = context.driver.find_element(By.XPATH, self.policyForAutomate_op)
            policy.click()
            self.logger.info("********** Policy is Selected For Automate Business Rules **********")
            global automatePolicyName
            automatePolicyName = policy.text
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickSaveOnCreateAutomateBusinessPolicyRule(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='btn-save-automate-policy']").click()
            time.sleep(6)
            self.logger.info("********** Saved Policy For Automate Business Rules **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifyAutomateBusinessPolicyRuleSaved(self, context):
        try:
            latestRecord = context.driver.find_element(By.XPATH, "//tr[@role='row'][@tabindex='-1']/td[3]")
            self.logger.info("********** Record is found **********")
            latestRecordText = latestRecord.text
            assert latestRecordText == automatePolicyName, f"Expected '{automatePolicyName}'  but got '{latestRecordText}'"
            self.logger.info("********** Record is Successfully Created **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def deleteAutomateBusinessPolicyRuleSaved(self, context):
        try:
            deleteBtn = context.driver.find_element(By.XPATH, self.deletePolicyForAutomate_btn)
            WebDriverWait(context.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.deletePolicyForAutomate_btn))).click()
            time.sleep(1)
            context.driver.find_element(By.XPATH, self.deletePolicyForAutomateConfirmPopup_btn).click()
            self.logger.info("********** Record is deleted Successfully **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

        # *****************************                                                       *****************************
        # *****************************     PAT Automate the Created Business Rule Setup     *****************************
        # *****************************                                                       *****************************

    def clickAutomateBusinessPolicyCheckBox(self, context):
        try:
            context.driver.find_element(By.XPATH, self.policyForAutomate_cb).click()
            time.sleep(1)
            self.logger.info("********** Policy Automate CheckBox is Checked **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickYesOnAutomateConfirmationPopup(self, context):
        try:
            popup = context.driver.find_element(By.XPATH, self.AutomatePolicyConfirmPopup_btn)
            self.logger.info("********** Pop up Is Appeared **********")
            popup.click()
            time.sleep(2)
            self.logger.info("********** Yes Button is Clicked on confirmation PopUp **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifySuccessMessage(self, context):
        try:
            WebDriverWait(context.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.successMessage_alert)))
            statusOfSuccessMessage = context.driver.find_element(By.XPATH, self.successMessage_alert).is_displayed()
            assert statusOfSuccessMessage is True
            self.logger.info("********** Success Message is Appeared **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifyStatusCompletedAndDelete(self, context):
        try:
            automationSetupStatus = context.driver.find_element(By.XPATH, self.automateSetupStatus_txt)
            status_text = automationSetupStatus.text.lower()

            if status_text == "completed":
                self.logger.info("********** Status Is Completed **********")
                context.driver.find_element(By.XPATH,
                                            "//span[@class='ui-button-icon-primary ui-icon ui-icon-trash']").click()
                time.sleep(1)
                self.logger.info("********** Clicked On Delete Icon **********")
                context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
                self.logger.info("********** Clicked Yes on Confirmation popup  **********")
                time.sleep(2)
            else:
                self.logger.info("********** Status Is Not Completed Yet **********")
                wait = WebDriverWait(context.driver, 90)
                wait.until(EC.text_to_be_present_in_element((By.XPATH, self.automateSetupStatus_txt), 'completed'))
                # WebDriverWait(context.driver, 60).until(EC.context.driver.find_element(By.XPATH, self.automateSetupStatus_txt).text.lower() == 'completed')
                self.logger.info("********** Status Is Completed Now **********")
                context.driver.find_element(By.XPATH,
                                            "//span[@class='ui-button-icon-primary ui-icon ui-icon-trash']").click()
                time.sleep(1)
                self.logger.info("********** Clicked On Delete Icon **********")
                context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
                self.logger.info("********** Clicked Yes on Confirmation popup  **********")
                time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

        # *****************************                                                       *****************************
        # *****************************              Run the PAT Policy Manually              *****************************
        # *****************************                                                       *****************************

    def clickManualPat(self, context):
        try:
            context.driver.find_element(By.XPATH, self.manualPAT_lnk).click()
            self.logger.info("********** Clicked on Manual PAT  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectFacilityForManualPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.facilityManualPAT_op).click()
            self.logger.info("********** Clicked on Manual PAT Facility  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectWorkCenterForManualPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.workCenterManualPAT_op).click()
            self.logger.info("********** Clicked on Manual PAT WorkCenter  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectDeviceForManualPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.deviceManualPAT_op).click()
            self.logger.info("********** Clicked on Manual PAT Device  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectTestProgramForManualPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.testProgramManualPAT_op).click()
            self.logger.info("********** Clicked on Manual PAT TestProgram  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectLotsForManualPAT(self, context):
        # context.driver.find_element(By.XPATH, self.lotsManualPAT_op).click()
        # self.logger.info("********** Clicked on Manual PAT Lots  **********")
        # time.sleep(2)
        try:
            element = context.driver.find_element(By.ID, self.lotsManualPAT_op)
            select = Select(element)
            Unkown_value_to_select = "94"
            select.select_by_value(Unkown_value_to_select)

            self.logger.info("********** Clicked on Lots  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectWaferForManualPAT(self, context):
        try:
            context.driver.find_element(By.ID, self.waferUnSelectManualPAT_op).click()
            self.logger.info("********** Wafer is Unselected  **********")
            time.sleep(2)
            context.driver.find_element(By.ID, self.waferSelectManualPAT_op).click()
            self.logger.info("********** Wafer is selected  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def selectPolicyForManualPAT(self, context):
        try:
            context.driver.find_element(By.XPATH, self.policyManualPAT_op).click()
            self.logger.info("********** Clicked on Manual PAT Policy  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickCalculateManualPAT(self, context):
        try:
            context.driver.find_element(By.ID, self.calculateManualPAT_btn).click()
            self.logger.info("********** Clicked on Manual PAT Calculate Button  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def verifyManualPATWaferViewed(self, context):
        try:
            WebDriverWait(context.driver, 60).until(
                EC.visibility_of_element_located((By.ID, self.saveToYieldWerxManualPAT_btn)))
            status = context.driver.find_element(By.ID, self.saveToYieldWerxManualPAT_btn).is_displayed()
            assert status is True
            self.logger.info("********** Manual PAT is successfully Executed  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickSaveToYieldWerx(self, context):

        try:
            # Wait for loader to disappear
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Loader is Invisible  **********")

            # Click on the 'Save to YieldWerx' button
            context.driver.find_element(By.ID, self.saveToYieldWerxManualPAT_btn).click()
            self.logger.info("********** Clicked on Save to YieldWerx Button  **********")
            time.sleep(1)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            # Optionally raise the exception to halt the script immediately
            raise

    def clickToExportManualPAT(self, context):
        try:
            # Click on the 'Export Button'
            context.driver.find_element(By.ID, self.exportMapManualPAT_btn).click()
            self.logger.info("********** Clicked on Export Button  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            # Optionally raise the exception to halt the script immediately
            raise

    def isDownloadFileExist(self, context):

        try:
            download_directory = "C:/Users/arslan.afzal/Downloads/"
            downloaded_file_name = "wafer map.png"

            def file_exists_in_directory(driver):
                return any(filename == downloaded_file_name for filename in os.listdir(download_directory))

            self.logger.info("********** Wait For File Download  **********")
            wait = WebDriverWait(context.driver, 60)
            wait.until(file_exists_in_directory)
            self.logger.info("********** File Download Successfully  **********")
            downloaded_file_path = os.path.join(download_directory, downloaded_file_name)
            assert os.path.exists(downloaded_file_path), "Downloaded file doesn't exist"
            self.logger.info("********** Downloaded File is Found  **********")
            os.remove(downloaded_file_path)
            self.logger.info("********** Downloaded File is Deleted  **********")
            time.sleep(2)
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise
        # download_directory = "C:/Users/arslan.afzal/Downloads/"
        # downloaded_file_name = "wafer map.png"
        #
        # def file_exists_in_directory(driver):
        #     return any(filename == downloaded_file_name for filename in os.listdir(download_directory))
        #
        # self.logger.info("********** Wait For File Download  **********")
        # wait = WebDriverWait(context.driver, 60)
        # wait.until(file_exists_in_directory)
        # self.logger.info("********** File Download Successfully  **********")
        # downloaded_file_path = os.path.join(download_directory, downloaded_file_name)
        # assert os.path.exists(downloaded_file_path), "Downloaded file doesn't exist"
        # self.logger.info("********** Downloaded File is Found  **********")
        # os.remove(downloaded_file_path)
        # self.logger.info("********** Downloaded File is Deleted  **********")
        # time.sleep(2)

    # *****************************                                                       *****************************
    # *****************************        Run the PAT Policy Manually End to End         *****************************
    # *****************************                                                       *****************************

    def clickEnableMultiSiteDPATFunctionality(self, context):
        try:
            # Wait for loader to disappear
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Loader is Invisible  **********")

            # Click on the 'Manual PAT Enable Multi Site Checkbox'
            context.driver.find_element(By.ID, self.enableMultisiteDPATFunctionality_chkbox).click()
            self.logger.info("********** Clicked on Manual PAT Enable Multi Site Checkbox  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise


    def clickOnExecuteButton(self, context):
        try:
            # Wait for loader to disappear
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Loader is Invisible  **********")

            # Click on the 'Manual PAT Execute Button'
            context.driver.find_element(By.ID, self.executeMultiSite_btn).click()
            self.logger.info("********** Clicked on Manual PAT Execute Button  **********")

            # Wait for loader to disappear again
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))
            self.logger.info("********** Manual PAT Execute Successfully  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnWaferTabAndLegend(self, context):
        try:
            # Click on the 'Wafer Map Tab'
            context.driver.find_element(By.ID, self.waferMapTab).click()
            self.logger.info("********** Clicked on Wafer Map Tab  **********")

            # Click on the 'Wafer Map Tab Legend'
            context.driver.find_element(By.ID, self.waferMapTabLegend).click()
            self.logger.info("********** Clicked on Wafer Map Tab Legend  **********")
            time.sleep(2)

            # Close the Wafer Map Tab Legend window
            context.driver.find_element(By.CSS_SELECTOR, self.closeWaferMapTabLegend).click()
            self.logger.info("********** Legend Window Closed  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnHistogramTabAndLegend(self, context):
        try:
            # Click on the 'Histogram Map Tab'
            context.driver.find_element(By.ID, self.histogramMapTab).click()
            self.logger.info("********** Clicked on Histogram Map Tab  **********")
            time.sleep(1)

            # Click on the 'Histogram Map Tab Legend'
            context.driver.find_element(By.ID, self.histogramMapTabLegend).click()
            self.logger.info("********** Clicked on Histogram Map Tab Legend  **********")
            time.sleep(2)

            # Close the Histogram Map Tab Legend window
            context.driver.find_element(By.CSS_SELECTOR, self.closeHistogramTabLegend).click()
            self.logger.info("********** Legend Window Closed  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnTrendTabAndLegend(self, context):
        try:
            # Click on the 'Trend Map Tab'
            context.driver.find_element(By.ID, self.trendMapTab).click()
            self.logger.info("********** Clicked on Trend Map Tab  **********")
            time.sleep(1)

            # Click on the 'Trend Map Tab Legend'
            context.driver.find_element(By.ID, self.trendMapTabLegend).click()
            self.logger.info("********** Clicked on Trend Map Tab Legend  **********")
            time.sleep(2)

            # Close the Trend Map Tab Legend window
            context.driver.find_element(By.CSS_SELECTOR, self.closeTrendTabLegend).click()
            self.logger.info("********** Legend Window Closed  **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnDieLossZoom(self, context):
        try:
            # Click on the 'Die Lost Zoom' button
            context.driver.find_element(By.ID, self.zoomDieLost_btn).click()
            self.logger.info("********** Clicked on Die Lost Zoom In Window  **********")
            time.sleep(2)

            # Close the Die Lost Zoom window
            context.driver.find_element(By.CSS_SELECTOR, self.closeZoom).click()
            self.logger.info("********** Die Lost Zoom Window Closed **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise
    def clickOnByWaferZoom(self, context):
        try:
            # Click on the 'Zoom By Wafer' button
            context.driver.find_element(By.ID, self.zoomByWaferByPassAndFail_btn).click()
            self.logger.info("********** Clicked on Zoom By Wafer  **********")
            time.sleep(2)

            # Close the Zoom By Wafer window
            context.driver.find_element(By.CSS_SELECTOR, self.closeZoom).click()
            self.logger.info("********** Zoom By Wafer Window Closed **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnByLotZoom(self, context):
        try:
            # Click on the 'Zoom By Lot' button
            context.driver.find_element(By.ID, self.zoomByLotPassAndFail_btn).click()
            self.logger.info("********** Clicked on Zoom By Lot  **********")
            time.sleep(2)

            # Close the Zoom By Lot window
            context.driver.find_element(By.CSS_SELECTOR, self.closeZoom).click()
            self.logger.info("********** Zoom By Lot Window Closed **********")
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def clickOnDowngradeScrap(self, context):

        try:
            # Click on the 'Downgrade/Scrap' button
            context.driver.find_element(By.XPATH, self.downgrade_ScrapMe_btn).click()
            self.logger.info("********** Clicked on Downgrade/Scrap Die Button **********")

            # Wait for loader to disappear
            WebDriverWait(context.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, self.loader)))

            # Locate the container element
            time.sleep(1)
            container = context.driver.find_element(By.ID, self.containerWaferMap)
            self.logger.info("********** Container Found **********")
            time.sleep(1)

            # Perform the click action on the specified coordinates within the container
            actions = ActionChains(context.driver)
            actions.move_to_element(container).click().perform()
            time.sleep(2)

            self.logger.info("********** Die Is Selected to Downgrade **********")

            context.driver.find_element(By.XPATH, self.downgradePopUp_btn).click()
            time.sleep(2)

            self.logger.info("********** Clicked on Downgrade/Scrap Die Window Closed **********")
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)

    def clickZoomWaferMapOrignal(self, context):
        try:
            context.driver.find_element(By.ID, self.waferMapTab).click()
            time.sleep(1)
            self.logger.info("********** Clicked on Wafer Map Tab  **********")
            context.driver.find_element(By.XPATH, self.zoomWaferMapOrignal_btn).click()
            self.logger.info("********** Clicked on Zoom Orignal Wafer Map Button  **********")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            time.sleep(3)
            newWindow = context.driver.find_element(By.ID, "chart-legend").is_displayed()
            assert newWindow is True
            self.logger.info("**********  Successfully Open new tab  **********")
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            self.logger.info("**********  New Tab closed Successfully And back to previous Tab  **********")
            time.sleep(1)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)


    def clickZoomPATWafer(self, context):


        try:
            context.driver.find_element(By.XPATH, self.zoomWaferMapPAT_btn).click()
            self.logger.info("********** Clicked on Zoom Wafer Map PAT Applied Both Limits Button  **********")
            time.sleep(1)
            context.driver.switch_to.window(context.driver.window_handles[1])
            time.sleep(3)
            newWindow = context.driver.find_element(By.ID, "chart-legend").is_displayed()
            assert newWindow is True
            self.logger.info("**********  Successfully Open new tab  **********")
            context.driver.close()
            context.driver.switch_to.window(context.driver.window_handles[0])
            self.logger.info("**********  New Tab closed Successfully And back to previous Tab  **********")
            time.sleep(1)
        except Exception as e:
            # Handle exceptions or failures
            MyException.handle_exception(context, e)
