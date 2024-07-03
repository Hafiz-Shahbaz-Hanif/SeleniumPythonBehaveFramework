from behave import *

from Logs.LoginPage import LoginClass
from Pages.PAT import PATClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
logger = LogGen.loggen()


# ******************************** Creating Static Test Program Level PAT Rule **************************************

@given(u'I am on the On the PAT Rule Page.')
def step_impl(context):
    logger.info("")
    logger.info("********** TEST-008  * * * * *  Creating Static Device Level PAT Rule  **********")
    logger.info("")
    lg.launchBrowser(context)
    lg.openWebsite(context)
    lg.enterCredentials(context)
    lg.hitLoginButton(context)
    lg.verifyDashboard(context)
    pt.clickPAT(context)
    pt.clickPATRules(context)
    pt.verifyDashboard(context)


@when(u'Clicked on New Static PAT Rule.')
def step_impl(context):
    pt.clickNewStaticPATRule(context)


@when(u'Check the Apply PAT Rule to device level CheckBox.')
def step_impl(context):
    pt.applyPATToDeviceCheck(context)


@when(u'Select the Static Limit Tab.')
def step_impl(context):
    pt.selectStaticLimitTab(context)


@when(u'Calculate the Seed Limits.')
def step_impl(context):
    pt.calculateSeedLimits(context)


@when(u'EnterRe-Calculate Static Limits After.')
def step_impl(context):
    pt.enterNumberForRecalculation(context)


@when(u'Find and Enter Static Bin Number.')
def step_impl(context):
    pt.enterStaticBinNumber(context)


@when(u'Find and Enter Static Bin Name.')
def step_impl(context):
    pt.enterStaticBinName(context)


@when(u'Select Email Notification Tab.')
def step_impl(context):
    pt.selectEmailNotificationTab(context)


@when(u'Enter Name & Email.')
def step_impl(context):
    pt.enterEmailName(context)
