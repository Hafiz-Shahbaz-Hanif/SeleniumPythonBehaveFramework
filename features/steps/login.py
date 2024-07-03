from behave import *
from selenium.webdriver.common.by import By

from Pages.DashboardPage import DashboardClass
from Logs.LoginPage import LoginClass
from utilities.customLogger import LogGen

logger = LogGen.loggen()
lg = LoginClass()
dc = DashboardClass()


@given('launch chrome browser')
def launch_chrome_browser(context):
    logger.info("")
    logger.info("********** Browser Launched successfully  **********")
    logger.info("")
    lg.launchBrowser(context)


@when('open Yieldwerx link')
def open_yieldwerx_link(context):
    lg.openWebsite(context)


@when(u'verify Yieldwerx link is opened successfully')
def verifyTitle(context):
    logger.info("********** Trying Login Screen Opened Successfully  **********")
    lg.verifyLoginPageOpened(context)
    status = context.driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
    assert status is True
    logger.info("**********  Login Screen Opened Successfully  **********")


@when(u'enter username and password')
def step_impl(context):
    lg.enterUsernamePassword(context)


@when(u'click on login button')
def hitLogin(context):
    lg.hitLoginButton(context)


@then(u'user must login to the main screen')
def verifyDashboardIsOpen(context):
    lg.verifyDashboard(context)


@then(u'close browser')
def step_impl(context):
    dc.click_on_logout_avatar(context)
    dc.click_on_logout_link(context)
    lg.quiteBrowser(context)
