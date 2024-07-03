from behave import *

from Logs.LoginPage import LoginClass
from Pages.PF_SWM.PF_MunualSWM import ManualSWM
from utilities.customLogger import LogGen

lg = LoginClass()
manualSwm = ManualSWM()
logger = LogGen.loggen()


@given(u'Now we are at Manual SWM Screen after creating SWM Policies')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-011  * * * * *  SWM Manual SWM Creation  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)


@when(u'Click on SWM Manual SWM')
def step_impl(context):
    manualSwm.clickSwmManualSWM(context)


@when(u'Click on the Manual SWM Source Facility')
def step_impl(context):
    manualSwm.selectSourceFacility_Silicon(context)


@when(u'Click on the Manual SWM Source Work Center')
def step_impl(context):
    manualSwm.selectSourceWorkCenter_Silicon(context)


@when(u'Click on the Manual SWM Source Device')
def step_impl(context):
    manualSwm.selectSourceDevice_Silicon(context)


@when(u'Click on the Manual SWM Source Test Program')
def step_impl(context):
    manualSwm.selectSourceTestProgram_Silicon(context)


@when(u'Click on the Manual SWM Source Lots Program')
def step_impl(context):
    manualSwm.selectSourceLots_Silicon(context)


@when(u'Click on the Manual SWM Source Wafers Program')
def step_impl(context):
    manualSwm.selectSourceWafers_Silicon(context)


@when(u'Click on the Manual SWM Target Facility')
def step_impl(context):
    manualSwm.selectTargetFacility_Silicon(context)


@when(u'Click on the Manual SWM Target Work Center')
def step_impl(context):
    manualSwm.selectTargetWorkCenter_Silicon(context)


@when(u'Click on the Manual SWM Target Device')
def step_impl(context):
    manualSwm.selectTargetDevice_Silicon(context)


@when(u'Click on the Manual SWM Target Test Program')
def step_impl(context):
    manualSwm.selectTargetTestProgram_Silicon(context)


@when(u'Click on the Manual SWM Target Lots Program')
def step_impl(context):
    manualSwm.selectTargetLots_Silicon(context)


@when(u'Click on the Manual SWM Target Wafers Program')
def step_impl(context):
    manualSwm.selectTargetWafers_Silicon(context)


@when(u'Click on Generate Manual SWM Button')
def step_impl(context):
    manualSwm.clickGenerateManualSWMButton(context)


@when(u'Get Data of Combine Bin Wafer Map from Manual SWM')
def step_impl(context):
    manualSwm.dataCombineBinWaferMap(context)


@when(u'Click on Save To Yieldwerx Button')
def step_impl(context):
    manualSwm.clickSaveToYieldwerx(context)


@when(u'Verify the Manual SWM Alert')
def step_impl(context):
    manualSwm.verifySuccessMessage(context)
