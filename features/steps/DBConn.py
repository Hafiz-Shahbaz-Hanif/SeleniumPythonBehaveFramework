from behave import *
from selenium.webdriver.common.by import By

from Pages.PF_DBConn.PF_DBQueries import PF_DBQueries
from utilities.customLogger import LogGen


logger = LogGen.loggen()
db = PF_DBQueries()


@given(u'I fetch user details from the database')
def fetch_Wafer_Details(context):
    db.dataWaferTable(context)

@given(u'SQL Query To Fetch Wafer Details')
def fetch_Wafer_details(context):
    db.dataWaferTable(context)


@step(u'SQL Query To Fetch SWM Rule Details')
def fetch_SwmRule_Details(context):
    db.dataSWMRule(context)


@step(u'SQL Query to Fetch SWM Policy Details')
def fetch_SwmPolicy_Details(context):
    db.dataSWMPolicy(context)


@step(u'SQL Query to Fetch SWM Automated Policy')
def fetch_SwmAutomated_Policy_Details(context):

    db.dataSwmAutomatedPolicies(context)
    db.dataSwmAutomatedPolicies(context)

@step(u'SQL Query to Fetch Lot Data from the database')
def fetch_SwmLot_Data_Details(context):

    db.dataLotTableVerification(context)
    db.lotTableDataVerification(context)


@step(u'SQL Query to Fetch Parameters Data from Test Param Map Table')
def fetch_SwmParameters_Data_Details(context):

    db.dataTestParamMapVerification(context)


@step(u'SQL Query to Fetch Data from SWM Dashboard')
def fetch_SwmDashboard_Details(context):
    db.dataSwmDashboardVerification(context)
    db.testParamMapDataVerification(context)

