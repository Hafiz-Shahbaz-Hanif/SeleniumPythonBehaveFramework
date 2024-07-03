from behave import *

from Logs.LoginPage import LoginClass
from Pages.PAT import PATClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
logger = LogGen.loggen()


# ******************************** Creating Dynamic Test Program Level PAT Rule **************************************
@given(u'Launch Chrome Browser.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-001  * * * * *  Creating Dynamic Test Program Level PAT Rule  **********")
    logger.info("")
    lg.launchBrowser(context)


@when(u'yieldWerx Web Module Launched.')
def step_impl(context):
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)


@when(u'Verified that the application logged In successfully.')
def step_impl(context):
    lg.verifyDashboard(context)


@when(u'Clicked on PAT Dropdown.')
def step_impl(context):
    pt.clickPAT(context)


@when(u'Clicked on PAT Rules.')
def step_impl(context):
    pt.clickPATRules(context)


@when(u'Verified that the PAT Rules page has been Opened.')
def step_impl(context):
    pt.verifyDashboard(context)


@when(u'Clicked on New Dynamic PAT.')
def step_impl(context):
    pt.clickNewDynamicPATRule(context)


@when(u'Verified that the Create PAT Rule page has been displayed.')
def step_impl(context):
    pt.verifyCreateNewRuleScreen(context)


@when(u'Enter the PAT Rule Name.')
def step_impl(context):
    pt.enterNameForPATRule(context)
    pt.enterDescriptionForPATRule(context)


@when(u'Select the Parameter Tab.')
def step_impl(context):
    pt.selectParameterTab(context)


@when(u'Select the Facility from Parameter Tab.')
def step_impl(context):
    pt.selectFacility(context)


@when(u'Select the Work Center from Parameter Tab of that facility.')
def step_impl(context):
    pt.selectWorkcenter(context)


@when(u'Select the Device from Parameter Tab of that facility and work center.')
def step_impl(context):
    pt.selectDevice(context)


@when(u'Select the Test Program related to Facility, work center and device.')
def step_impl(context):
    pt.selectTestProgram(context)


@when(u'Selected the Parameter from that selected test program.')
def step_impl(context):
    pt.selectTestParameter(context)


@when(u'Select the Dynamic Limit Tab.')
def step_impl(context):
    pt.selectDynamicLimitTab(context)


@when(u'Selected PAT Distribution to Unknown and verify')
def step_impl(context):
    pt.selectPATDistribution(context)


@when(u'Find and Enter Bin Number.')
def step_impl(context):
    pt.enterBinNumber(context)


@when(u'Find and Enter Bin Name.')
def step_impl(context):
    pt.enterBinName(context)


@when(u'Click on that Save Button.')
def step_impl(context):
    pt.clickSave(context)


@when(u'Get the Success Message.')
def step_impl(context):
    pt.verifySaved(context)


@when(u'Close the browser.')
def step_impl(context):
    lg.quiteBrowser(context)


# ******************************** PAT Policy Creation **************************************

@given(u'Now we were at PAT Rules Screen after creating one PAT Rule.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-002  * * * * *  PAT Policy Creation  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)


@when(u'Created rule displayed on dashboard then click on PAT Policies.')
def step_impl(context):
    pt.clickPAT(context)


@when(u'Check that the PAT Policy page displayed.')
def step_impl(context):
    pt.clickPATPolicy(context)
    pt.verifyPatPolicyPageDisplayed(context)


@when(u'Click on New Policy.')
def step_impl(context):
    pt.clickNewPolicy(context)


@when(u'Give the Policy Name in the Policy Name Text Field.')
def step_impl(context):
    pt.enterPolicyName(context)


@when(u'Select the type of policy that it is device level or program level by using Type dropdown.')
def step_impl(context):
    pt.selectTypeOnPolicy(context)


@when(u'Selected the device from devices dropdown.')
def step_impl(context):
    pt.selectDeviceOnPolicy(context)


@when(u'Selected the Test Program from Test Programs dropdown.')
def step_impl(context):
    pt.selectTestProgramOnPolicy(context)


@when(u'Click on the checkbox of created rule.')
def step_impl(context):
    pt.clickCheckBoxOfCreatedRule(context)


@when(u'Click on Save Button.')
def step_impl(context):
    pt.savePolicy(context)


@then(u'Verify policy is created.')
def step_impl(context):
    pt.verifyPolicySaved(context)
    lg.quiteBrowser(context)


# ******************************** Automate Business Rules For  **************************************

@given(u'We were at Home screen after creating PAT policy.')
def step_impl(context):
    logger.info("")
    logger.info("**********  TEST-003  * * * * *  Automate Business Rules For  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)


@when(u'Click on Automate business rule from PAT dropdown.')
def step_impl(context):
    pt.clickPAT(context)


@when(u'Click on Create Automate Business Policy Rule.')
def step_impl(context):
    pt.clickAutomateBusinessRules(context)
    pt.clickCreateAutomateBusinessPolicyRule(context)


@when(u'Select the Facility.')
def step_impl(context):
    pt.selectFacilityOnCreateAutomateBusinessPolicyRule(context)


@when(u'Select the Work Center.')
def step_impl(context):
    pt.selectWorkCenterOnCreateAutomateBusinessPolicyRule(context)


@when(u'Select the Device')
def step_impl(context):
    pt.selectDeviceOnCreateAutomateBusinessPolicyRule(context)


@when(u'Select the Test Program')
def step_impl(context):
    pt.selectTestProgramOnCreateAutomateBusinessPolicyRule(context)


@when(u'Selected the created policy from policies section in Create Automate Business Policy Rule Page.')
def step_impl(context):
    pt.selectPolicyOnCreateAutomateBusinessPolicyRule(context)


@when(u'Click on the Save Button.')
def step_impl(context):
    pt.clickSaveOnCreateAutomateBusinessPolicyRule(context)


@then(u'Verify Record is created and Delete it.')
def step_impl(context):
    pt.verifyAutomateBusinessPolicyRuleSaved(context)
    pt.deleteAutomateBusinessPolicyRuleSaved(context)
    lg.quiteBrowser(context)


# ******************************** Automate the Created Business Rule Setup  **************************************

@given(u'Now the Automated Business Rule Setup Created.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-004  * * * * *  Automate the Created Business Rule Setup  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)
    pt.clickPAT(context)
    pt.clickAutomateBusinessRules(context)
    pt.clickCreateAutomateBusinessPolicyRule(context)
    pt.selectFacilityOnCreateAutomateBusinessPolicyRule(context)
    pt.selectWorkCenterOnCreateAutomateBusinessPolicyRule(context)
    pt.selectDeviceOnCreateAutomateBusinessPolicyRule(context)
    pt.selectTestProgramOnCreateAutomateBusinessPolicyRule(context)
    pt.selectPolicyOnCreateAutomateBusinessPolicyRule(context)
    pt.clickSaveOnCreateAutomateBusinessPolicyRule(context)


@when(u'Verify that the rule is created and displayed.')
def step_impl(context):
    pt.verifyAutomateBusinessPolicyRuleSaved(context)


@when(u'Click on the unchecked check box and mark as checked.')
def step_impl(context):
    pt.clickAutomateBusinessPolicyCheckBox(context)


@when(u'Verify that the pop up window appears & Click on the Yes to automate the policy.')
def step_impl(context):
    pt.clickYesOnAutomateConfirmationPopup(context)


@when(u'Automated Successfully Message Displayed.')
def step_impl(context):
    pt.verifySuccessMessage(context)


@when(u'Check the status is completed.')
def step_impl(context):
    pt.verifyStatusCompletedAndDelete(context)


# ******************************** Run the PAT Policy Manually  **************************************

@given(u'Click on Manual PAT.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-006  * * * * *  Run the PAT Policy Manually  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)
    pt.clickPAT(context)
    pt.clickManualPat(context)


@when(u'Select the Facility for Manual PAT.')
def step_impl(context):
    pt.selectFacilityForManualPAT(context)


@when(u'Select the Work Center for Manual PAT.')
def step_impl(context):
    pt.selectWorkCenterForManualPAT(context)


@when(u'Select the Device  for Manual PAT.')
def step_impl(context):
    pt.selectDeviceForManualPAT(context)


@when(u'Select the Test Program on which PAT Policy is created.')
def step_impl(context):
    pt.selectTestProgramForManualPAT(context)


@when(u'Select the Lot  for Manual PAT.')
def step_impl(context):
    pt.selectLotsForManualPAT(context)


@when(u'Select the wafer  for Manual PAT.')
def step_impl(context):
    pt.selectWaferForManualPAT(context)


@when(u'Select the Created Policy  for Manual PAT.')
def step_impl(context):
    pt.selectPolicyForManualPAT(context)


@when(u'Click on Calculate Manual PAT button.')
def step_impl(context):
    pt.clickCalculateManualPAT(context)


@when(u'Verify that the Manual PAT Wafer Viewed.')
def step_impl(context):
    pt.verifyManualPATWaferViewed(context)


@when(u'Click on Save to YieldWerx Button.')
def step_impl(context):
    pt.clickSaveToYieldWerx(context)


@then(u'Verify Success message of saved')
def step_impl(context):
    pt.verifySuccessMessage(context)


@then(u'Click on Export Button.')
def step_impl(context):
    pt.clickToExportManualPAT(context)


@then(u'Check the Wafer Exported  & Close Browser.')
def step_impl(context):
    pt.isDownloadFileExist(context)
    lg.quiteBrowser(context)
