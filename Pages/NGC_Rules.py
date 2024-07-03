import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from utilities.customLogger import LogGen
from utilities.Exceptions import MyException


class swmNgcSiliconClass:
    logger = LogGen.loggen()
    createdPolicyName = None

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    probeDieType = "//select[@id='CustomDieTypeID']//option[normalize-space()='Probe Die(s)']"
    probeDieTypeD2 = "//select[@id='CustomDieTypeID2']//option[@value='16'][normalize-space()='Probe Die(s)']"
    mergeWorkCenterInput = "//input[@id='MergeWorkCenter']"
    targetCustomTestProgram = "//select[@id='targetTestProgram']"
    sourceCustomTestProgram = "//select[@id='sourceTestProgram']"
    customTPAdd = "//input[@value='Add']"

    swm_AutomateSwm_Create_PoliciesName = "//table[@id='PoliciesGrid']//td[@aria-describedby='PoliciesGrid_Name']"
    checkBox_AutomatePolicies = "//*[@id='AutmateSWMPolicies']//td[@title='Cassady Wilkins']/preceding-sibling::td/input"

    def enterName4670_PrePostMerge_Missing_F(self, context):
        try:
            nameSWM = "4670-PrePostMerge-Missing-F"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-Missing-F **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectCustomRules(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@value='Custom']").click()
            self.logger.info("**********  Custom radio button is checked **********")
            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectAllRules(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='cb_RulesGrid']").click()
            self.logger.info("**********  All rule button is checked **********")
            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def clickApplyButton(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//form[@action='/Swm/TestProgramMapping']//div[@class='button-list']//input[@id='btn-save-policy']").click()
            self.logger.info("**********  Apply button is clicked **********")
            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceFacility(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='SourceFacility']//option[@value='SILICON'][normalize-space()='SILICON']").click()
            self.logger.info("********** Source Facility Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetFacility(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='TargetFacility']//option[@value='SILICON'][normalize-space()='SILICON']").click()
            time.sleep(2)
            self.logger.info("********** Source Facility Is Selected  **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectSourceDevice(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='SourceDevice']//option[@value='4670'][normalize-space()='4670']").click()
            time.sleep(2)
            self.logger.info("********** Source Device Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTargetDevice(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='TargetDevice']//option[@value='4670'][normalize-space()='4670']").click()
            time.sleep(2)
            self.logger.info("********** Target Device Is Selected  **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def missingSourceBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='SourceRuleBinID']//option[@value='2']").click()
            self.logger.info("********** Missing Source Rule Bin is Selected **********")
            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def failingTargetBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='TargetRuleBinID']//option[@value='6']").click()
            self.logger.info("********** Failing Target Rule Bin is Selected **********")

            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def targetWaferBinInCombineWaferBin(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='RuleBinTypeID']//option[@value='2']").click()
            self.logger.info("********** Target Wafer Bin In Combine Wafer Bin Details **********")

            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def bothInCopyParametricData(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='ParametricDataCopyID']//option[@value='9']").click()
            self.logger.info("********** Select Both In Copy Parametric Data **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def enterName4670_PrePostMerge_F_Missing(self, context):
        try:

            nameSWM = "4670-PrePostMerge-F-Missing"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-F-Missing **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def failingSourceBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='SourceRuleBinID']//option[@value='6']").click()
            self.logger.info("********** Failing Source Rule Bin is Selected **********")
            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def missingTargetBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='TargetRuleBinID']//option[@value='2']").click()
            self.logger.info("********** Missing Target Rule Bin is Selected **********")

            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def sourceWaferBinInCombineWaferBin(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='RuleBinTypeID']//option[@value='1']").click()
            self.logger.info("********** Target Wafer Bin In Combine Wafer Bin Details **********")

            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 3rd Rule 4670-PrePostMerge-Missing-P

    def enterName4670_PrePostMerge_Missing_P(self, context):
        try:

            nameSWM = "4670-PrePostMerge-Missing-P"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-Missing-P **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def passingTargetBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='TargetRuleBinID']//option[@value='5']").click()
            self.logger.info("********** Passing Target Rule Bin is Selected **********")

            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    def customInCombineWaferBin(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='RuleBinTypeID']//option[@value='3']").click()
            self.logger.info("********** Custom in Combine Wafer Bin  **********")
            time.sleep(3)
            context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            MyException.handle_exception(context, e)

    def enter60BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number']")
            findBinNum.send_keys("60")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name']")
            findBinName.send_keys("60")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectDieType(self, context):
        try:
            findDieTypeBin1 = context.driver.find_element(By.XPATH, self.probeDieType).click()
            self.logger.info("********** Die Type Selected **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectDieTypeD2(self, context):
        try:

            findDieTypeBin2 = context.driver.find_element(By.XPATH, self.probeDieTypeD2).click()
            self.logger.info("********** Die Type Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def targetInOtherFieldsData(self, context):
        try:
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//select[@id='OtherFiledsDataID']//option[@value='5']").click()
            self.logger.info("********** Target Wafer Bin In Other fields data **********")

            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 4rd Rule 4670-PrePostMerge-P-Missing

    def enterName4670_PrePostMerge_P_Missing(self, context):
        try:

            nameSWM = "4670-PrePostMerge-P-Missing"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670_PrePostMerge_P_Missing **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def sourceInOtherFieldsData(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='OtherFiledsDataID']//option[@value='4']").click()
            self.logger.info("********** Target Wafer Bin In Other fields data **********")

            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def enter61BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number']")
            findBinNum.send_keys("61")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name']")
            findBinName.send_keys("61")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def passingSourceBinRuleDetails(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='SourceRuleBinID']//option[@value='5']").click()
            self.logger.info("********** Missing Source Rule Bin is Selected **********")
            time.sleep(2)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 5th Rule 4670-PrePostMerge-Missing-Missing

    def enterName4670_PrePostMerge_Missing_Missing(self, context):
        try:

            nameSWM = "4670-PrePostMerge-Missing-Missing"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-Missing-Missing **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 6th Rule 4670-PrePostMerge-NA-F

    def enterName4670_PrePostMerge_NA_F(self, context):
        try:

            nameSWM = "4670-PrePostMerge-NA-F"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-NA-F **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def targetInCopyParametricData(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='ParametricDataCopyID']//option[@value='8']").click()
            self.logger.info("********** Select Target Wafer In Copy Parametric Data **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def ifDieExistINOnlyTargetWafer(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='RuleMissingDieID']//option[@value='1']").click()
            self.logger.info("********** Select If Die Exist IN Only Target Wafer **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 7th Rule 4670-PrePostMerge-F-NA

    def enterName4670_PrePostMerge_F_NA(self, context):
        try:

            nameSWM = "4670-PrePostMerge-F-NA"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-F-NA **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def sourceInCopyParametricData(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='ParametricDataCopyID']//option[@value='7']").click()
            self.logger.info("********** Select Target Wafer In Copy Parametric Data **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def ifDieExistINOnlySourceWafer(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='RuleMissingDieID']//option[@value='3']").click()
            self.logger.info("********** Select If Die Exist IN Only Target Wafer **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 8th Rule 4670-PrePostMerge-F-NA

    def enterName4670_PrePostMerge_NA_P(self, context):
        try:

            nameSWM = "4670-PrePostMerge-NA-P"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-NA-P **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 9th Rule 4670-PrePostMerge-P-NA

    def enterName4670_PrePostMerge_P_NA(self, context):
        try:

            nameSWM = "4670-PrePostMerge-P-NA"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-P-NA **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 10th Rule 4670-PrePostMerge-F-F

    def enterName4670_PrePostMerge_F_F(self, context):
        try:

            nameSWM = "4670-PrePostMerge-F-F"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-F-F **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 11th Rule 4670-PrePostMerge-F-F

    def enterName4670_PrePostMerge_F_P(self, context):
        try:

            nameSWM = "4670-PrePostMerge-F-P"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-F-P **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 12th Rule 4670-PrePostMerge-F-F

    def enterName4670_PrePostMerge_P_F(self, context):
        try:

            nameSWM = "4670-PrePostMerge-P-F"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-P-F **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 13th Rule 4670-PrePostMerge-F-F

    def enterName4670_PrePostMerge_P_P(self, context):
        try:

            nameSWM = "4670-PrePostMerge-P-P"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-PrePostMerge-P-P **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 14th Rule 4670-Delta Merge

    def enterName4670_DeltaMerge(self, context):
        try:

            nameSWM = "4670-Delta Merge"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-Delta Merge **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def binRuleTypeBinParametricRule(self, context):
        try:
            typeDD_element = context.driver.find_element(By.XPATH, "//select[@id='RuleTypeID']")
            select = Select(typeDD_element)
            option_value_to_select = "2"
            select.select_by_value(option_value_to_select)
            self.logger.info("********** Bin Rule Type Bin & Parametric Rule is Selected **********")
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        except Exception as e:
            # Handle exceptions or failures
            allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.logger.error(f"An error occurred: {str(e)}")

            raise

    def sourceParameter62_iddPostStress_mA(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='source-parameter']").send_keys("62")
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//span[normalize-space()='Idd post-stress']").click()
            self.logger.info("********** Source Parameter Is Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def targetParameter3_iddPostBake_mA(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='target-parameter']").send_keys("3")
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//span[normalize-space()='Idd post-bake']").click()
            self.logger.info("********** Source Parameter Is Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def targetParameter2_iddPostBake_mA(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='target-parameter']").send_keys("2")
            time.sleep(3)
            # context.driver.find_element(By.XPATH, "//a[@id='ui-id-15']//span[contains(text(),'Idd post-bake')]").click()
            context.driver.find_element(By.XPATH, "//span[normalize-space()='Idd post-bake']").click()
            self.logger.info("********** Source Parameter Is Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def deltaParameter500_iddDeltaPostBake_mA(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='delta-parameter']").send_keys("500")
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//span[normalize-space()='idd delta postbake']").click()
            self.logger.info("********** Source Parameter Is Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def deltaParameter501_Delta1(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='delta-parameter']").send_keys("501")
            time.sleep(3)
            context.driver.find_element(By.XPATH, "//span[normalize-space()='Delta1']").click()
            self.logger.info("********** Source Parameter Is Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def enterTestDeltaValues(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@id='ParameterTestValue1']").send_keys("10")
            context.driver.find_element(By.XPATH, "//input[@id='ParameterTestValue2']").send_keys("0")
            self.logger.info("********** Test and Delta values are entered *******")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def enter41BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number']")
            findBinNum.send_keys("41")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name']")
            findBinName.send_keys("41")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def enter51BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number']")
            findBinNum.send_keys("51")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name']")
            findBinName.send_keys("51")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def enter40BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number2']")
            findBinNum.send_keys("40")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name2']")
            findBinName.send_keys("40")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def enter50BinNumberName(self, context):
        try:
            findBinNum = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-number2']")
            findBinNum.send_keys("50")
            self.logger.info("********** Bin Number Entered **********")
            findBinName = context.driver.find_element(By.XPATH, "//input[@id='custom-bin-name2']")
            findBinName.send_keys("50")
            self.logger.info("********** Bin Name Entered **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickCombineWaferBin2Details(self, context):
        try:
            context.driver.find_element(By.XPATH, "//a[@id='combine-wafer-bin2-detail-tab']").click()
            self.logger.info("**********  Combine Wafer Bin 2 Details Tab Is Selected *********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def customInCombineWaferBin2(self, context):
        try:
            context.driver.find_element(By.XPATH, "//select[@id='CustomRuleBinTypeID2']//option[@value='3']").click()
            self.logger.info("********** Custom in Combine Wafer Bin  **********")
            time.sleep(3)
            context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            MyException.handle_exception(context, e)

    def targetInOtherFieldsData2(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='CustomOtherFiledsDataID2']//option[@value='5']").click()
            self.logger.info("********** Target Wafer Bin In Other fields data  **********")

            time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def bothInCopyParametricData2(self, context):
        try:
            context.driver.find_element(By.XPATH,
                                        "//select[@id='CustomParametricDataCopyID2']//option[@value='9']").click()
            self.logger.info("********** Select Both In Copy Parametric Data **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    # **************** 15th Rule 4670-Delta Merge

    def enterName4670_Delta1Merge(self, context):
        try:

            nameSWM = "4670-Delta1 Merge"
            context.driver.find_element(By.XPATH, "//input[@id='Name']").send_keys(nameSWM)
            self.logger.info("**********                                           **********")
            self.logger.info("**********  4670-Delta1 Merge **********")
            self.logger.info("**********                                            **********")
            time.sleep(3)
        except Exception as e:
            MyException.handle_exception(context, e)

    def testProgramOptionAsCustom(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@value='Custom']").click()
            self.logger.info("**********  Custom radio button is checked **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickAdd(self, context):
        try:
            context.driver.find_element(By.XPATH, "//input[@value='Add']").click()
            self.logger.info("**********  Add button is Clicked **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def clickManageTestProgram(self, context):
        try:
            context.driver.find_element(By.XPATH, "//span[normalize-space()='Manage Test Programs']").click()
            self.logger.info("**********  ManageTestProgram is Clicked **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectTestProgramMapping(self, context):
        try:
            # Source Test Program
            source_element = context.driver.find_element(By.XPATH, self.sourceCustomTestProgram)
            s_options = source_element.find_elements(By.TAG_NAME, 'option')

            # Target Test Program
            target_element = context.driver.find_element(By.XPATH, self.targetCustomTestProgram)
            t_options = target_element.find_elements(By.TAG_NAME, 'option')

            # Extract the text from each option and store it in separate lists
            data_SourceTP = [option.text for option in s_options if
                             option.text.startswith('PREBAKE') and 'POSTBAKE' not in option.text]
            data_TargetTP = [option.text for option in t_options if option.text.startswith('POSTBAKE')]

            self.logger.info(f"********** Source Test Program Options: {data_SourceTP} **********")
            self.logger.info(f"********** Target Test Program Options: {data_TargetTP} **********")

            # Iterate through data_SourceTP and data_TargetTP
            for source_option, target_option in zip(data_SourceTP, data_TargetTP):
                Select(source_element).select_by_visible_text(source_option)
                self.logger.info(f"********** Selected Source Option: {source_option} **********")

                Select(target_element).select_by_visible_text(target_option)
                self.logger.info(f"********** Selected Target Option: {target_option} **********")

                add_button = context.driver.find_element(By.XPATH, "//input[@value='Add']")
                add_button.click()
                time.sleep(1)
        except Exception as e:
            MyException.handle_exception(context, e)

    def giveOrder(self, context):
        try:
            specific_numbers = {
                "4670-PrePostMerge-Missing-F": 6,
                "4670-PrePostMerge-F-Missing": 5,
                "4670-PrePostMerge-Missing-P": 7,
                "4670-PrePostMerge-P-Missing": 8,
                "4670-PrePostMerge-Missing-Missing": 9,
                "4670-PrePostMerge-NA-F": 2,
                "4670-PrePostMerge-F-NA": 1,
                "4670-PrePostMerge-NA-P": 3,
                "4670-PrePostMerge-P-NA": 4,
                "4670-PrePostMerge-F-F": 11,
                "4670-PrePostMerge-F-P": 12,
                "4670-PrePostMerge-P-F": 10,
                "4670-PrePostMerge-P-P": 14,
                "4670-Delta Merge": 13,
                "4670-Delta1 Merge": 15,
                # Add more names and their desired orders here
            }
            table = context.driver.find_element(By.XPATH, "//table[@id='RulesGrid']")
            self.logger.info("********** Table is found **********")

            rows = table.find_elements(By.XPATH, ".//tr[@class='ui-widget-content jqgrow ui-row-ltr']")
            self.logger.info("********** Rows is found **********")

            for row in rows:
                # Extract the name and number from the current row (you may need to adjust the selectors)
                name = row.find_element(By.XPATH, ".//td[@aria-describedby='RulesGrid_Name']").text
                if name in specific_numbers:
                    specific_number = specific_numbers.get(name)  # Get the specific number from the dictionary
                    number_field = row.find_element(By.XPATH, ".//input[@name='OrderSequence']")
                    number_field.clear()
                    number_field.send_keys(specific_number)
                    time.sleep(1)
                    self.logger.info(f"********** Order Sequence is Added for '{name}' **********")

        except Exception as e:
            MyException.handle_exception(context, e)

    def mergeWorkCenterInputField(self, context):
        try:
            context.driver.find_element(By.XPATH, self.mergeWorkCenterInput).clear()
            self.logger.info(f"Merge Work Center Input Field is Clear")
            context.driver.find_element(By.XPATH, self.mergeWorkCenterInput).send_keys("WAFER SORT")
            self.logger.info(f"Merge Work Center Added")
            time.sleep(3)

        except Exception as e:
            MyException.handle_exception(context, e)

    def selectDieTypesDetailOutputTab(self, context):
        try:
            context.driver.find_element(By.XPATH,"//button[@onclick='selectSourceAllDieTypeFilters()']").click()
            self.logger.info(f"All Source Die Type Selected from Policy Output Menu")
            time.sleep(2)
            context.driver.find_element(By.XPATH,"//button[@onclick='selectTargetAllDieTypeFilters()']").click()
            self.logger.info(f"All Target Die Type Selected from Policy Output Menu")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

        # Automate SWM Policy

    def clickAutomatePolicyDropdown(self, context):
        try:
            autoPolicyDropdown = context.driver.find_element(By.XPATH,
                                                             "//span[normalize-space()='Automate SWM Policies']").click()
            self.logger.info("********** Automate Policy Dropdown Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def automateSWMPolicyBtn(self, context):
        try:
            autoSWMPolicyBtn = context.driver.find_element(By.XPATH, "//a[@id='btn-new-rule']").click()
            self.logger.info("********** Automate Policy Dropdown Selected **********")
            time.sleep(2)

        except Exception as e:
            MyException.handle_exception(context, e)

    def createdPolicySelect(self, context):
        try:
            selectCreatedPolicy = context.driver.find_element(By.XPATH, self.swm_AutomateSwm_Create_PoliciesName)
            swmNgcSiliconClass.createdPolicyName = selectCreatedPolicy.text
            selectCreatedPolicy.click()
            self.logger.info(f"********** Policy selected for automation {swmNgcSiliconClass.createdPolicyName} **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def saveAutomatePolicy(self, context):
        try:
            saveAutoPolicy = context.driver.find_element(By.XPATH, "//input[@id='btn-save-automate-policy']").click()
            self.logger.info("********** Automated Policy has been saved **********")
            # time.sleep(3)

        except Exception as e:
            MyException.handle_exception(context, e)

    def automatePolicyCheckbox(self, context):
        try:
            WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
            time.sleep(5)

            table_xpath = "//table[@id='AutmateSWMPolicies']"
            table = context.driver.find_element(By.XPATH, table_xpath)
            # Find all rows in the table (excluding the header row)
            rows = table.find_elements(By.XPATH, ".//tr")[1:]
            for row in rows:
                policy_name_column = row.find_element(By.XPATH,".//td[@aria-describedby='AutmateSWMPolicies_PolicyName']")
                policy_name = policy_name_column.get_attribute("title")
                self.logger.info(f"********** Clicked on checkbox to automate {policy_name}  **********")
                if policy_name == swmNgcSiliconClass.createdPolicyName:
                    # If the policy name matches, click the checkbox in the same row
                    # checkbox = context.driver.find_element(By.XPATH,
                    #                                        f"//*[@id='AutmateSWMPolicies']//td[@title='{policy_name}']/preceding-sibling::td/input")
                    checkbox = row.find_element(By.XPATH, ".//td/input[@type='checkbox']")
                    checkbox.click()
                    WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
                    break
            time.sleep(4)
        except Exception as e:
            MyException.handle_exception(context, e)

    def automateConfirmation(self, context):
        WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        try:
            confirmationMessage = (context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']"))
            confirmationMessage.click()
            self.logger.info("********** Clicked on checkbox to automate **********")
            time.sleep(1)

        except Exception as e:
            MyException.handle_exception(context, e)

    def automateSuccessConfirmation(self, context):
        WebDriverWait(context.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        try:
            messageReceived = context.driver.find_element(By.XPATH, "//div[@id='alertmod_AutmateSWMPolicies']")
            self.logger.info("********** Confirmation Message Received **********")
            time.sleep(3)

        except Exception as e:
            MyException.handle_exception(context, e)
