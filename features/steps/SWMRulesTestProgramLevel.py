import time

from behave import *

from faker import Faker

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewSWMRuleWindowPage import NewSWMRulWindowClass

actions = ActionsClass()
dc = DashboardClass()
sw = NewSWMRulWindowClass()


@when('Create SWM Rules window will open so enter name as "{name}" And description in "General" tab')
def step_impl(context, name):
    fake = Faker()
    context.test_program_level_rule_name = name + fake.name()
    context_description = fake.text()
    sw.enter_into_swm_rule_name_field(context, context.test_program_level_rule_name)
    sw.enter_into_swm_rule_description_field(context, context_description)


@when('Click "Input Data Selection" And Select level as "{level}"')
def step_impl(context, level):
    sw.click_input_data_selection_tab(context)
    sw.select_level(context, level)


@when('Select Source Device as "{source_device}"')
def step_impl(context, source_device):
    sw.click_source_device(context)


@when('Select Source Probe as "(1|M)" and Source Test Program as "{src_test_program}"')
def step_impl(context, src_test_program):
    sw.select_source_test_program(context, src_test_program)
    sw.click_source_probe(context)


@when('Select Target Device as "{value}"')
def step_impl(context, value):
    sw.click_target_device(context)


@when('Select Target Test Program as "{value}", Target Probe "(1|M)"')
def step_impl(context, value):
    sw.select_target_test_program(context, value)
    sw.click_target_probe(context)


@when('Click the tab "Rule Definition" and Select rule Type from "{select_rule_type}" drop down')
def step_impl(context, select_rule_type):
    sw.click_rule_definition_tab(context)
    sw.select_rule_type_dropdown(context, select_rule_type)


@when('Select the Die Exist in Wafers as "{die_exists_in_wafers}"')
def step_impl(context, die_exists_in_wafers):
    sw.select_bin_rule_details(context, die_exists_in_wafers)


@when('Select Source Wafer Bin as "{source_bin}"')
def step_impl(context, source_bin):
    sw.select_source_wafer_bin(context, source_bin)


@when('Select Target Wafer Bin as "{target_bin}"')
def step_impl(context, target_bin):
    sw.select_target_wafer_bin(context, target_bin)


@when('Select Combine Wafer Bin Details as "{combine_wafer_bin_details}"')
def step_impl(context, combine_wafer_bin_details):
    sw.select_combine_wafer_bin(context, combine_wafer_bin_details)


@when('Give Hard Bin Number as "{hard_bin_number}", Soft Bin Number as "{soft_bin_number}"')
def step_impl(context, hard_bin_number, soft_bin_number):
    sw.enter_into_hard_bin_if_enabled(context, hard_bin_number)
    sw.enter_into_soft_bin_number_field(context, soft_bin_number)


@when('Select the Bin Flag and the other fields data')
def step_impl(context):
    sw.select_bin_flag_if_enabled(context, "Fail")


@when('Select the Die Type "{die_type}"')
def step_impl(context, die_type):
    sw.select_die_type_if_enabled(context, die_type)


@when('Select from "{copy_parametric_data}"')
def step_impl(context, copy_parametric_data):
    sw.select_copy_parametric_data(context, copy_parametric_data)


@when('Enable the following checkbox if required')
def step_impl(context):
    sw.click_copy_bin_number_checkbox(context)


@when('Enter the valid "Owner Name", "Owner Email Address" and the Enter additional emails if needed')
def step_impl(context):
    fake = Faker()
    context.owner_name = fake.name()
    context.owner_email = fake.email()
    sw.enter_into_owner_name_field(context, context.owner_name)
    sw.enter_into_owner_email_field(context, context.owner_email)
    sw.enter_into_additional_email_field(context, context.owner_email)


@then('Verify that the test program level rule will be saved and appear in the SWM Rules window')
def step_impl(context):
    sw.verify_newly_created_swm_rule_name(context, context.test_program_level_rule_name)
    actions.logout(context)


@when('See the list of already created SWM rules')
def step_impl(context):
    sw.verify_swm_rule_table_is_displayed(context)


@when('Click "Edit" button available for each rule')
def step_impl(context):
    sw.click_swm_rule_edit_button(context)


@when('Make changes that you want')
def step_impl(context):
    fake = Faker()
    context.edited_rule_name = fake.name()
    sw.edit_swm_rule_name_field(context, context.edited_rule_name)


@when('Change Source Facility, Source Work Center')
def step_impl(context):
    sw.click_input_data_selection_tab(context)
    sw.select_level(context, "Test Program")
    sw.click_source_facility(context)
    sw.click_source_work_center(context)


@when('Change Source Device, Source test Program, Source Probe')
def step_impl(context):
    sw.click_source_device(context)
    sw.select_source_test_program(context, "PREBAKE_A_4670")
    sw.click_source_probe(context)


@when('Change Target Facility, Target Work Center')
def step_impl(context):
    sw.click_target_facility(context)
    sw.click_target_work_center(context)


@when('Change Target Device, Target test Program, Target Probe')
def step_impl(context):
    sw.click_target_device(context)
    sw.select_target_test_program(context, "POSTBAKE_A_4670")
    sw.click_target_probe(context)


@when('Click "Rule Definition" tab And Change rule Type from "{value}" drop down')
def step_impl(context, value):
    sw.click_rule_definition_tab(context)
    sw.select_rule_type_dropdown(context, "BIN Rule")


@when('Change "Bin Rule Details" combinations for "Die Exist in Both Source and Target Wafers"')
def step_impl(context):
    sw.select_bin_rule_details(context, "Die Exist in Both Source and Target Wafers")
    sw.select_source_wafer_bin(context, "Missing")
    sw.select_target_wafer_bin(context, "Failing")


@when('Change "Combine Bin" option from "Combine Wafer Bin Details" tab')
def step_impl(context):
    sw.select_combine_wafer_bin(context, "Source Wafer BIN")


@when('Change "Hard Bin Number" and "Soft Bin Number" details')
def step_impl(context):
    sw.enter_into_hard_bin_if_enabled(context, "30")
    sw.enter_into_soft_bin_number_field(context, "30")


@when('Change Bin Flag and other fields data')
def step_impl(context):
    sw.select_bin_flag_if_enabled(context, "Fail")


@when('Change "Die Type" like "Probe Die(s)" from available Die Type options')
def step_impl(context):
    sw.select_die_type_if_enabled(context, "NA")


@when('Change any option in Copy Parametric Data (PTR, FTR, and MPR)')
def step_impl(context):
    sw.select_copy_parametric_data(context, "None")


@when('Enable or Disable the checkbox')
def step_impl(context):
    sw.click_copy_bin_number_checkbox(context)


@when('Change valid "Owner Name", "Owner Email Address" And Change additional emails if needed')
def step_impl(context):
    fake = Faker()
    context.owner_name = fake.name()
    context.owner_email = fake.email()
    sw.edit_owner_name_field(context, context.owner_name)
    sw.edit_owner_email_field(context, context.owner_email)
    sw.edit_additional_email_field(context, context.owner_email)


@then('Verify that the edited rule will be saved and appear in the SWM Rules window')
def step_impl(context):
    sw.verify_newly_created_swm_rule_name(context, context.edited_rule_name)
    actions.logout(context)


@when('Click Copy button available infront of each already created rule')
def step_impl(context):
    sw.click_swm_rule_copy_button(context)


@when('Create SWM Rule window of already created SWM rule will open')
def step_impl(context):
    sw.verify_swm_rule_window_display(context)


@when('Change name and description from General tab')
def step_impl(context):
    fake = Faker()
    context.copied_rule_name = fake.name()
    sw.edit_swm_rule_name_field(context, context.copied_rule_name)


@then('Verify that the copied rule will be saved')
def step_impl(context):
    sw.verify_newly_created_swm_rule_name(context, context.copied_rule_name)
    actions.logout(context)


@when('Click "Delete" button available at the end of each rule')
def step_impl(context):
    context.deleted_swm_rule_name = sw.verify_deleted_swm_rule_name(context)
    sw.click_swm_rule_delete_button(context)


@when('Confirmation Required pop-up window will appear with "Yes" and "No" buttons')
def step_impl(context):
    sw.verify_swm_rule_delete_alert_is_displayed(context)


@when('Click "Yes" to delete the SWM rule')
def step_impl(context):
    sw.accept_swm_rule_delete_alert(context)


@then('Verify that the rule will be deleted')
def step_impl(context):
    sw.verify_swm_rule_delete_success_popup_is_displayed(context)
    sw.verify_deleted_swm_rule_name_is_removed(context, context.deleted_swm_rule_name)
    actions.logout(context)


