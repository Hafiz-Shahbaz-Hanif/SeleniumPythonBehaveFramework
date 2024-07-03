from behave import *

from Logs.LoginPage import LoginClass
from Pages.PAT import PATClass
from Pages.SWM import SWMClass
from Pages.SWM_TestProgram import swmTestProgramClass
from utilities.customLogger import LogGen

lg = LoginClass()
pt = PATClass()
swm = SWMClass()
swmTP = swmTestProgramClass()
logger = LogGen.loggen()


@when(u"Selected the Level from Device and Test Program Dropdown and Select Test Program.")
def step_impl(context):
    swmTP.selectTestProgramFromRulesInputSelection(context)


@when (u"Click on General Tab.")
def step_impl(context):
    swmTP.clickOnGeneralTab(context)


# @when (u"Select Manage Exception Tab")
# def step_impl(context):
#     swm.manageExceptionTab(context)
#
