import time

from behave import *

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.SWMAutomatePolicyWindowPage import AutomateSWMPolicyWindowClass

actions = ActionsClass()
dc = DashboardClass()
sa = AutomateSWMPolicyWindowClass()


@given('The user is successfully logged in the yieldWerx web application')
def step_impl(context):
    actions.login(context)


@when('Click on "SWM" in the left menu bar')
def step_impl(context):
    dc.click_swm_heading(context)


@when('Click "Automate SWM Policies" and new window will open')
def step_impl(context):
    dc.click_automate_swm_policies(context)


@when('Click on "Automate SWM Policy" and Create Automate SWM Policy window will open')
def step_impl(context):
    sa.click_automate_swm_policy_window(context)


@when('Select Source Facility as "{value1}", Source Work Center as "{value2}"')
def step_impl(context, value1, value2):
    sa.click_policy_selection_tab(context)
    sa.click_source_facility(context)
    sa.click_source_workcenter(context)


@when('Select Source Device as "{value1}", Source Test Program as "{value2}"')
def step_impl(context, value1, value2):
    sa.click_source_device(context)
    sa.click_source_testprogram(context)


@when('Select the Target Facility as "{value1}", Target Work Center as "{value2}"')
def step_impl(context, value1, value2):
    sa.click_target_facility(context)
    sa.click_target_workcenter(context)


@when('Select Target Device as "{value1}", Target Test Program as "{value2}"')
def step_impl(context, value1, value2):
    sa.click_target_device(context)
    sa.click_target_testprogram(context)


@when('Select policy from Policies as "{value1}" section and click on "Save" button')
def step_impl(context, value1):
    sa.click_policy(context)
    sa.click_save_btn(context)


@when('SWM Policy has been created and displayed in "Automate SWM Policies" window')
def step_impl(context):
    sa.verify_newly_created_swm_policy_name(context, "SWM_Policy_TestProgram")


@when('Enable check box available infront of each created Automate SWM Policy in Automate SWM Policies window to automate the policy')
def step_impl(context):
    sa.click_automate_policy_checkbox(context)
    sa.accept_automate_policy_checkbox_alert(context)
    sa.verify_automate_policy_checkbox_is_checked(context)


@then('Verify that the policy will be automated with success message')
def step_impl(context):
    sa.verify_success_popup(context)
    actions.logout(context)


@when('See the list of already created Automate SWM Policies')
def step_impl(context):
    sa.verify_automate_swm_policy_window_is_displayed(context)


@when('Uncheck the check box available infront of already automated SWM Policy')
def step_impl(context):
    sa.uncheck_automate_policy_checkbox(context)


@when('Confirmation Required pop-up window with options "Yes, No, Cancel" will open')
def step_impl(context):
    sa.verify_un_automate_alert_is_displayed(context)


@when('Click Yes to un-automate the Policy')
def step_impl(context):
    sa.click_un_automate_alert_yes_btn(context)


@then('Verify that the policy will be un-automated and window of Automate SWM Policies will be refresh')
def step_impl(context):
    sa.verify_success_popup(context)
    sa.verify_automate_policy_checkbox_is_unchecked(context)
    actions.logout(context)


@when('Click the "Delete" button available at the end of already created and automated SWM Policy')
def step_impl(context):
    sa.click_delete_btn(context)


@when('Click Yes to delete the policy')
def step_impl(context):
    sa.accept_automate_policy_checkbox_alert(context)


@then('Verify that the policy will be deleted from Automate SWM Policies window')
def step_impl(context):
    sa.verify_success_popup(context)
    sa.verify_deleted_swm_policy_name(context)
    actions.logout(context)










