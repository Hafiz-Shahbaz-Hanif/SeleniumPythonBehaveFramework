from behave import *

from Logs.LoginPage import LoginClass
from Pages.PAT import PATClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
logger = LogGen.loggen()


# ******************************** Run the PAT Policy Manually End to End Cycle  **************************************

@given(u'Click on PAT Module.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-007  * * * * *  Run the PAT Policy Manually End to End Cycle  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)
    pt.clickPAT(context)
    pt.clickManualPat(context)


@when(u'Select the Facility From Manual PAT Module.')
def step_impl(context):
    pt.selectFacilityForManualPAT(context)


@when(u'Select the Work Center From Manual PAT Module.')
def step_impl(context):
    pt.selectWorkCenterForManualPAT(context)


@when(u'Select the Device From Manual PAT Module.')
def step_impl(context):
    pt.selectDeviceForManualPAT(context)


@when(u'Select the Test Program on which PAT Policy is created From Manual PAT Module.')
def step_impl(context):
    pt.selectTestProgramForManualPAT(context)


@when(u'Select the Lot From Manual PAT Module.')
def step_impl(context):
    pt.selectLotsForManualPAT(context)


@when(u'Select the wafer From Manual PAT Module.')
def step_impl(context):
    pt.selectWaferForManualPAT(context)


@when(u'Select the Created Policy From Manual PAT Module.')
def step_impl(context):
    pt.selectPolicyForManualPAT(context)


@when(u'Click on Calculate Manual PAT button From Manual PAT Module.')
def step_impl(context):
    pt.clickCalculateManualPAT(context)


@when(u'Verify that the Manual PAT Wafer Viewed From Manual PAT Module.')
def step_impl(context):
    pt.verifyManualPATWaferViewed(context)


@when(u'Select checked "Enable Multi Site DPAT Functionality" From Manual PAT Module.')
def step_impl(context):
    pt.clickEnableMultiSiteDPATFunctionality(context)


@when(u'Click on Execute button From Manual PAT Module.')
def step_impl(context):
    pt.clickOnExecuteButton(context)


@when(
    u'Click on Wafer Map tab and then click on Legend in Wafer Map Tab and then close the legend From Manual PAT '
    u'Module.')
def step_impl(context):
    pt.clickOnWaferTabAndLegend(context)


@when(u'Click on Histogram Tab and then click on Legend of Histogram and close the legend From Manual PAT Module.')
def step_impl(context):
    pt.clickOnHistogramTabAndLegend(context)


@when(u'Click on Trend Tab and then click on Legend of Trend and close the legend From Manual PAT Module.')
def step_impl(context):
    pt.clickOnTrendTabAndLegend(context)


@when(u'Click on Zoom button of Die Loss Section and close the tab From Manual PAT Module.')
def step_impl(context):
    pt.clickOnDieLossZoom(context)


@when(u'Click on Zoom button of By Wafer, Pass and Fail Count and Close the tab From Manual PAT Module.')
def step_impl(context):
    pt.clickOnByWaferZoom(context)


@when(u'Click on Zoom button of By Lot, Pass and Fail Count and Close the tab From Manual PAT Module.')
def step_impl(context):
    pt.clickOnByLotZoom(context)


@when(u'Select Die to downgrade and Click on downgrade button From Manual PAT Module.')
def step_impl(context):
    pt.clickOnDowngradeScrap(context)


@when(u'Click on Orignal Bin Wafer Map Zoom,Verify new window Open & close new Window & Back to Main window')
def step_impl(context):
    pt.clickZoomWaferMapOrignal(context)


@when(u'Click on PAT Both Limits Wafer Map Zoom,Verify new window Open & close new Window & Back to Main window')
def step_impl(context):
    pt.clickZoomPATWafer(context)


@when(u'Click on Save Button From Manual PAT Module.')
def step_impl(context):
    pt.clickSaveToYieldWerx(context)


@then(u'Verify success message From Manual PAT Module & Close Browser.')
def step_impl(context):
    pt.verifySuccessMessage(context)
    lg.quiteBrowser(context)
