import time

from Pages.DashboardPage import DashboardClass
from Logs.LoginPage import LoginClass
from utilities.customLogger import LogGen

logger = LogGen.loggen()
lg = LoginClass()
dc = DashboardClass()


class ActionsClass:
    def __init__(self):
        pass

    def login(self, context):
        lg.launchBrowser(context)
        lg.openWebsite(context)
        lg.verifyLoginPageOpened(context)
        lg.enterUsernamePassword(context)
        lg.hitLoginButton(context)
        lg.verifyDashboard(context)

    def logout(self, context):
        time.sleep(5)
        dc.click_on_logout_avatar(context)
        dc.click_on_logout_link(context)
        lg.verifyLoginPageOpened(context)
        lg.quiteBrowser(context)

