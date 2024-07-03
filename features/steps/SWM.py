from behave import given, when, then

from Logs.LoginPage import LoginClass
from Pages.PAT import PATClass
from Pages.PF_SWM.PF_MunualSWM import ManualSWM
from Pages.SWM import SWMClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
swm = SWMClass()
logger = LogGen.loggen()
manualSWM = ManualSWM()


@given(u'I am on the home page')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-007  * * * * *  Create SWM Rule  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.verifyLoginPageOpened(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)


@when(u'Click on SWM Dropdown.')
def step_impl(context):
    swm.clickOnSWMDropDown(context)


@when(u'Click on SWM Rules.')
def step_impl(context):
    swm.clickSWMRules(context)


@when(u'Verify that SWM Rules Page has been opened.')
def step_impl(context):
    swm.verifySwmRulePageOpen(context)


@when(u'Click on New SWM Rule to create new rule.')
def step_impl(context):
    swm.clickNewSwmRule(context)


@when(u'Enter the SWM Rule Name.')
def step_impl(context):
    swm.enterNameForSWMRule(context)


@when(u'Enter the Description.')
def step_impl(context):
    swm.enterDescriptionForSWMRule(context)


@when(u'Click on Input Data Selection.')
def step_impl(context):
    swm.clickInputDataSelection(context)


@when(u'Selected the Level from "Device and Test Program" and Select Device.')
def step_impl(context):
    swm.selectLevelSwmRule(context)


@when(u'Click on Bin type dropdown and select Hard Bin.')
def step_impl(context):
    swm.selectBin(context)


@when(u'Click on Rules Validation radio button first Custom and then All.')
def step_impl(context):
    swm.clickRulesValidation(context)


@when(u'Click on the Source Facility.')
def step_impl(context):
    swm.selectSourceFacility(context)


@when(u'Click on Source Work Center.')
def step_impl(context):
    swm.selectSourceWorkCenter(context)


@when(u'Click on Source Device.')
def step_impl(context):
    swm.selectSourceDevice(context)


@when(u'Click on Source Test Program.')
def step_impl(context):
    swm.selectSourceTestProgram(context)


@when(u'Click on Source Probe.')
def step_impl(context):
    swm.selectSourceProbe(context)


@when(u'Click on the Target Facility.')
def step_impl(context):
    swm.selectTargetFacility(context)


@when(u'Click on Target Work Center.')
def step_impl(context):
    swm.selectTargetWorkCenter(context)


@when(u'Click on Target Device.')
def step_impl(context):
    swm.selectTargetDevice(context)


@when(u'Click on Target Test Program.')
def step_impl(context):
    swm.selectTargetTestProgram(context)


@when(u'Click on Target Probe.')
def step_impl(context):
    swm.selectTargetProbe(context)


@when(u'Click on Rule Definition Page.')
def step_impl(context):
    swm.clickRuleDefinition(context)


@when(u'Click on Select Rule Type dropdown and select Bin Rules.')
def step_impl(context):
    swm.selectRuleType(context)


@when(u'Selected Die Exist in both source and target wafer option from Bin Rule Detail Section.')
def step_impl(context):
    swm.selectBinRuleDetails(context)


@when(u'Selected "Passing" from Source Wafer Bin and "Passing" from target wafer bin.')
def step_impl(context):
    swm.selectSourceBin(context)
    swm.selectTargetBin(context)


@when(u'Selected Custom from "Combine Wafer Bin and Parametric Data Selection".')
def step_impl(context):
    swm.selectCustomBin(context)


@when(u'Enter Bin Number and Bin Name and Select Target from Other Fields Data in Combine Bin Wafer Detail Section.')
def step_impl(context):
    swm.selectBinNumberBinName(context)


@when(u'Click on Email Notification Tab.')
def step_impl(context):
    swm.selectEmailNotificationTab(context)


@when(u'Enter mailing information "Name in Owner Email" and "Email in Owner Email" fields and save.')
def step_impl(context):
    swm.enterNameEmail(context)
    swm.saveButton(context)


@then(u'Verify that SWM Rule has been created successfully.')
def step_impl(context):
    swm.verifySwmRule(context)

    # ******************************** SWM Policy Creation **************************************


# ---------------------------------------------------------------------------------------------------------------------------------------------


@when(u'Click on SWM Policies')
def step_impl(context):
    swm.clickSwmPolicy(context)


@when(u'Click on the New SWM Policy.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-008  * * * * *  New SWM Policy  **********")
    logger.info("")
    swm.clickNewSwmPolicy(context)


@when(u'Enter SWM Policy name and Descriptions')
def step_impl(context):
    swm.enterNameForSWMPolicy(context)
    swm.enterDescriptionForSWMPolicy(context)


@when(u'Enter SWM Policy Name as per Facility')
def step_impl(context):
    swm.policyNameSWMTP(context)


@when('I fetch user details from the database')
def fetch_user_details(context):
    swm.test(context)


@when(u'Click on the input data and rules selections')
def step_impl(context):
    swm.clickInputDataSelection(context)


@then(u'Click on Bin type dropdown and select Hard Bin.')
def step_impl(context):
    swm.selectBin(context)


@when(u'Click on Test Program Options radio button first Custom and then All.')
def step_impl(context):
    swm.clickTestProgramOptions(context)


@then(u'Click on the Source Facility.')
def step_impl(context):
    swm.selectSourceFacility(context)


@then(u'Click on Source Work Center.')
def step_impl(context):
    swm.selectSourceWorkCenter(context)


@then(u'Click on Source Device.')
def step_impl(context):
    swm.selectSourceDevice(context)


@then(u'Click on Source Probe.')
def step_impl(context):
    swm.selectSourceProbe(context)


@then(u'Click on the Target Facility.')
def step_impl(context):
    swm.selectTargetFacility(context)


@then(u'Click on Target Work Center.')
def step_impl(context):
    swm.selectTargetWorkCenter(context)


@then(u'Click on Target Device.')
def step_impl(context):
    swm.selectTargetDevice(context)


@then(u'Click on Target Probe.')
def step_impl(context):
    swm.selectTargetProbe(context)


@when(u'select the rule.')
def step_impl(context):
    swm.selectRuleForPolicy(context)


@when(u'Click on the output data Selection tab.')
def step_impl(context):
    swm.clickOutputDataSelection(context)


@when(u'Click mata data selection form and select Source Wafer')
def step_impl(context):
    swm.metadataSelectionForm(context)


@when(u'Click on the Manage Exception.')
def step_impl(context):
    swm.clickManageException(context)


@when(u'Click On Save And Verify Policy is Saved')
def step_impl(context):
    swm.saveButton(context)
    swm.verifySwmPolicy(context)
    # swm.deleteSWMPolicy(context)


@when(u'Click On Manual SWM')
def step_impl(context):
    swm.clickManualSwm(context)


@when(u'Click on Generate Manual SWM')
def step_impl(context):
    manualSWM.clickGenerateManualSWMButton(context)


@when(u'Click on Save To YieldWerx')
def step_impl(context):
    swm.clickSaveToYieldwerx(context)


@when(u'Click on Legend Source and Close')
def step_impl(context):
    swm.clickSourceLegend(context)


@when(u'Click on Legend Target and Close')
def step_impl(context):
    swm.clickTargetLegend(context)


@when(u'Click on Legend Combine and Close')
def step_impl(context):
    swm.clickCombineLegend(context)


@when(u'Click on Zoom Source and Close New Window')
def step_impl(context):
    swm.clickSourceZoom(context)


@when(u'Click on Zoom Target and Close New Window')
def step_impl(context):
    swm.clickTargetZoom(context)


@when(u'Click on Zoom Combine and Close New Window')
def step_impl(context):
    swm.clickCombineZoom(context)


@when(u'Click on Automate SWM Policies')
def step_impl(context):
    swm.clickSwmAutomatePolicies(context)


@when(u'Click Automate SWM Policy')
def step_impl(context):
    swm.clickSwmAutomateNewPolicy(context)


@then(u'Click on Source Test Program.')
def step_impl(context):
    swm.selectSourceTestProgram(context)


@then(u'Click on Target Test Program.')
def step_impl(context):
    swm.selectTargetTestProgram(context)


@when(u'Click on Email Notification Tab')
def step_impl(context):
    swm.selectEmailNotificationTabForAutomatePolicy(context)


@then(u'verify Swm policy is automated and Delete the automated and policy.')
def step_impl(context):
    # swm.verifySwmPolicy(context)
    swm.deleteSWMPolicy(context)
    swm.clickSwmPolicy(context)
    swm.deleteSWMPolicy(context)


