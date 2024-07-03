from behave import *

from Logs.LoginPage import LoginClass
from Pages.NGC_Rules import swmNgcSiliconClass
from Pages.PAT import PATClass
from Pages.PF_DBConn.PF_DBQueries import PF_DBQueries
from Pages.PF_SWM.PF_SWMDashboard import SWMDashboard
from Pages.SWM import SWMClass
from Pages.SWM_TestProgram import swmTestProgramClass
from utilities.customLogger import LogGen


lg = LoginClass
PAT = PATClass
swm = SWMClass
SwmTP = swmTestProgramClass
ngc = swmNgcSiliconClass
logger = LogGen().loggen()
db = PF_DBQueries()
swmDash = SWMDashboard()


@step(u'Click on SWM Dashboard from dropdown')
def swmDashboardButton(context):
    swmDash.swmDashboard(context)


@step(u'Click on Source Facility from SWM Status by Devices Module in SWM Dashboard')
def swmDashboardStatusModule(context):
    swmDash.swmDashboardStatus(context)



