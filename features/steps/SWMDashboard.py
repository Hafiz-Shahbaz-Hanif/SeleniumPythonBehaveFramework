import time

from behave import *

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.SWMDashboardPage import SWMDashboardClass

actions = ActionsClass()
dc = DashboardClass()
sd = SWMDashboardClass()


@given('The user in on the main screen')
def step_impl(context):
    actions.login(context)


@when('User clicks on SWM Dropdown from Left Menu')
def step_impl(context):
    dc.click_swm_heading(context)


@when('Click on "SWM Dashboard"')
def step_impl(context):
    dc.click_swm_dashboard_heading(context)


@when('SWM Dashboard window will open with "{text1}" table and "{text2}')
def step_impl(context, text1, text2):
    sd.verify_swm_status_by_devices_display(context, text1)
    sd.verify_wafer_processed_list(context, text2)


@when('Verify that "SWM Status by Devices" table having "{text1}", "{text2}"')
def step_impl(context, text1, text2):
    sd.verify_display_of_source_facility(context, text1)
    sd.verify_display_of_source_work_center(context, text2)


@when('Also verify "{text1}", "{text2}", "{text3}"')
def step_impl(context, text1, text2, text3):
    sd.verify_display_of_source_device(context, text1)
    sd.verify_display_of_target_facility(context, text2)
    sd.verify_display_of_target_workcenter(context, text3)


@when('Also verify the display of "{text1}", "{text2}", "{text3}"')
def step_impl(context, text1, text2, text3):
    sd.verify_display_of_target_device(context, text1)
    sd.verify_display_of_no_of_policies_device(context, text2)
    sd.verify_display_of_is_automated(context, text3)


@when('And verify the "{text1}" and "{text2}" columns')
def step_impl(context, text1, text2):
    sd.verify_display_processed_wafers(context, text1)
    sd.verify_display_remaining_wafers(context, text2)


@when('Click on the device from available devices list in "SWM Status by Device" table')
def step_impl(context):
    sd.click_device(context)


@when('Verify that the "Show Inactive Wafers checkbox" is checked by default')
def step_impl(context):
    sd.verify_show_inactive_wafers_is_checked(context)


@when('Automated policy will appear in Wafer Processed List with')
def step_impl(context):
    sd.verify_policy_name(context, "SWM_Policy_TestProgram11")
    sd.verify_facility(context, "WEB SMALL DATASET")
    sd.verify_workcenter(context, "WAFER SORT_WAFER SORT")
    sd.verify_device(context, "4670")
    sd.verify_testprogram(context, "PREBAKE_A_4670_POSTBAKE_A_4670")
    sd.verify_wafer_status(context, "WAFER CREATED")


@then('All the related pending and processed wafer has been displayed')
def step_impl(context):
    sd.verify_facility(context, "WEB SMALL DATASET")
    sd.verify_wafer_status(context, "true")
    actions.logout(context)








