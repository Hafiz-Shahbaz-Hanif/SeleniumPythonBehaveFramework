import time

from behave import *

from faker import Faker

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewSWMRuleWindowPage import NewSWMRulWindowClass

actions = ActionsClass()
dc = DashboardClass()
sw = NewSWMRulWindowClass()


@given('The user successfully opened the yieldWerx web application and login')
def step_impl(context):
    actions.login(context)


@when('Click on "SWM" in the left menu bar and click on SWM Rules')
def step_impl(context):
    dc.click_swm_heading(context)
    dc.click_swm_rules_heading(context)


@when('Click on "New SWM Rule" button from SWM Rules window')
def step_impl(context):
    sw.click_new_swm_rule_window(context)


@when('Create SWM Rules window will open and enter name as "{name}" And description in "General" tab')
def step_impl(context, name):
    fake = Faker()
    context.rule_name = name + fake.name()
    context_description = fake.text()
    sw.enter_into_swm_rule_name_field(context, context.rule_name)
    sw.enter_into_swm_rule_description_field(context, context_description)


@when('Click the "Input Data Selection" tab and Select level as "{level}", Rules Validation as "{rule_val}"')
def step_impl(context, level, rule_val):
    sw.click_input_data_selection_tab(context)
    sw.select_level(context, level)
    sw.click_rule_validation_radiobutton(context)


@when('Select the Source Facility as "{text1}", Source Work Center as "{text2}"')
def step_impl(context, text1, text2):
    sw.click_source_facility(context)
    sw.click_source_work_center(context)


@when('Select the source device as "{Source_Device}" and source probe as (1|M)')
def step_impl(context, Source_Device):
    sw.click_source_device(context)
    sw.click_source_probe(context)


@when('Select Target Facility  as "{value1}", Target Work Center  as "{value2}')
def step_impl(context, value1, value2):
    sw.click_target_facility(context)
    sw.click_target_work_center(context)


@when('Select Target Probe as (1|M) and Target Device as "{target_device}"')
def step_impl(context, target_device):
    sw.click_target_device(context)
    sw.click_target_probe(context)


@when('Click "Rule Definition" tab And Select rule Type from "{value}" drop down')
def step_impl(context, value):
    sw.click_rule_definition_tab(context)
    sw.select_rule_type_dropdown(context, value)


@when('Select one option from Die Exist in Wafers as "{value}"')
def step_impl(context, value):
    sw.select_bin_rule_details(context, value)


@when('Select Source Wafer Bin as')
def step_impl(context):
    context.data_set = []
    for row in context.table:
        value = row['Source Bin']
        if row['Source Bin'] != '':
            sw.select_source_wafer_bin(context, value)


@when('Select Target Wafer Bin as')
def step_impl(context):
    context.data_set = []
    for row in context.table:
        value = row['Target Bin']
        if row['Target Bin'] != '':
            sw.select_target_wafer_bin(context, value)


@when('Select "Combine Bin" option from Combine Wafer Bin Details as "{value}"')
def step_impl(context, value):
    sw.select_combine_wafer_bin(context, value)


@when('Provide Hard Bin Number as "{value1}", Soft Bin Number as "{value2}"')
def step_impl(context, value1, value2):
    sw.enter_into_hard_bin_if_enabled(context, value1)
    sw.enter_into_soft_bin_number_field(context, value2)


@when('Select Bin Flag and other fields data')
def step_impl(context):
    sw.select_bin_flag_if_enabled(context, "Fail")


@when('Select Die Type as "{value}"')
def step_impl(context, value):
    sw.select_die_type_if_enabled(context, value)


@when('Select the one option from "{value}"')
def step_impl(context, value):
    sw.select_copy_parametric_data(context, value)


@when('Enable "{value}" checkbox if needed')
def step_impl(context, value):
    sw.click_copy_bin_number_checkbox(context)


@when('Enter valid "{value1}", "{value2}" And Enter additional emails if needed')
def step_impl(context, value1, value2):
    fake = Faker()
    context.owner_name = fake.name()
    context.owner_email = fake.email()
    sw.enter_into_owner_name_field(context, context.owner_name)
    sw.enter_into_owner_email_field(context, context.owner_email)
    sw.enter_into_additional_email_field(context, context.owner_email)


@then('Verify that the rule will be saved and appear in the SWM Rules window')
def step_impl(context):
    sw.verify_newly_created_swm_rule_name(context, context.rule_name)
    actions.logout(context)