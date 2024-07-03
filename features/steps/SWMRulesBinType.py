import time

from behave import *

from faker import Faker

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewSWMRuleWindowPage import NewSWMRulWindowClass

actions = ActionsClass()
dc = DashboardClass()
sw = NewSWMRulWindowClass()


@given('The user has successfully launched Web Application and logged in')
def step_impl(context):
    actions.login(context)


@when('Clicks on SWM Dropdown from the menu displayed on left side')
def step_impl(context):
    dc.click_swm_heading(context)


@when('Click on SWM Rules')
def step_impl(context):
    dc.click_swm_rules_heading(context)


@when('Click "New SWM Rule" button from SWM Rules window')
def step_impl(context):
    sw.click_new_swm_rule_window(context)


@when('Enter a Rule Name and Description in the "General" tab')
def step_impl(context):
    fake = Faker()
    context.rule_name = fake.name()
    context_description = fake.text()
    sw.enter_into_swm_rule_name_field(context, context.rule_name)
    sw.enter_into_swm_rule_description_field(context, context_description)


@when('Select the "Input Data Selection" Tab')
def step_impl(context):
    sw.click_input_data_selection_tab(context)


@when('Select "{Source_or_Target_Data_Set_Size}", "{Source_or_Target_Probe}"')
def step_impl(context, Source_or_Target_Data_Set_Size, Source_or_Target_Probe):
    sw.click_source_facility(context)
    sw.click_source_probe(context)
    sw.click_target_facility(context)
    sw.click_target_probe(context)


@when('Then select "{Level}", "{Bin_Type}", "{Rule_Validation}"')
def step_impl(context, Level, Bin_Type, Rule_Validation):
    sw.select_level(context, Level)
    sw.select_bin_type(context, Bin_Type)
    sw.click_rule_validation_radiobutton(context)


@when('Click on "Rule Definition" tab')
def step_impl(context):
    sw.click_rule_definition_tab(context)


@when('After that select the "{Rule_Type}", "{Bin_Rule_Detail}", "{Combine_Wafer_Bin}"')
def step_impl(context, Rule_Type, Bin_Rule_Detail, Combine_Wafer_Bin):
    sw.select_bin_rule_details(context, "Die Exist in Both Source and Target Wafers")
    sw.select_source_wafer_bin(context, "Any")
    sw.select_target_wafer_bin(context, "Any")
    sw.select_combine_wafer_bin(context, Combine_Wafer_Bin)


@when('Enter the "{Hard_Bin_Number_or_Name}", "{Soft_Bin_Number_or_Name}"')
def step_impl(context, Hard_Bin_Number_or_Name, Soft_Bin_Number_or_Name):
    sw.enter_into_hard_bin_number_field(context, "30")
    sw.enter_into_hard_bin_name_field(context, "Rule 1H")
    sw.enter_into_soft_bin_number_field(context, 30)
    sw.enter_into_soft_bin_name_field(context, "Rule 1S")


@when('After that select "{Bin_Flag_or_Other_Fields_Data}", "{Die_Type}", "{Copy_Parametric_Data_From}"')
def step_impl(context, Bin_Flag_or_Other_Fields_Data, Die_Type, Copy_Parametric_Data_From):
    sw.select_bin_flag(context, "Fail")
    sw.select_other_field_data(context, "Source Wafer")
    sw.select_die_type(context, Die_Type)
    sw.select_copy_parametric_data(context, Copy_Parametric_Data_From)


@when('Click "Email Notification" tab')
def step_impl(context):
    sw.click_email_notification_tab(context)


@when('Enter valid "Owner Name", "Owner Email Address"')
def step_impl(context):
    fake = Faker()
    context.owner_name = fake.name()
    context.owner_email = fake.email()
    sw.enter_into_owner_name_field(context, context.owner_name)
    sw.enter_into_owner_email_field(context, context.owner_email)


@when('Enter "Additional emails" if needed')
def step_impl(context):
    fake = Faker()
    context.owner_email = fake.email()
    sw.enter_into_additional_email_field(context, context.owner_email)


@when('Click the "Save" button')
def step_impl(context):
    sw.click_save_btn(context)


@then('Verify that the rule has been saved successfully')
def step_impl(context):
    sw.verify_newly_created_swm_rule_name(context, context.rule_name)
    actions.logout(context)

