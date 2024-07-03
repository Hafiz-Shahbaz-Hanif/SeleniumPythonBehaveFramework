import time

from faker import Faker
from behave import *

from Pages.ActionsPage import ActionsClass
from Pages.DashboardPage import DashboardClass
from Pages.NewStaticPatWindowPage import NewStaticPatRuleWindowClass

actions = ActionsClass()
dc = DashboardClass()
pt = NewStaticPatRuleWindowClass()


@given('After login click on "Quality & PAT" in the left menu bar')
def step_impl(context):
    actions.login(context)
    dc.click_quality_and_pat_heading(context)


@when('Click on "PAT Rules"')
def step_impl(context):
    dc.click_pat_heading(context)
    dc.click_pat_rules_heading(context)


@when('Click "{text}" button from PAT Rules window')
def step_impl(context, text):
    pt.click_new_static_pat_link(context)


@when('Create PAT Rule window will be open and enter rule name as "{name}" and description in "{text}" tab')
def step_impl(context, name, text):
    pt.click_on_general_tab(context)
    fake = Faker()
    context.rule_name = fake.name()
    pt.enter_into_name_field(context, context.rule_name)


@when('Navigate into the parameters tab and select "{text}" as "{Facility}"')
def step_impl(context, text, Facility):
    pt.click_on_parameters_tab(context)
    pt.click_on_facility_option(context)


@when('After selecting "Facility" data will be populated automatically for work center, device and test program')
def step_impl(context):
    pt.click_on_workcenter_option(context)
    pt.click_on_device_option(context)
    pt.click_on_testprogram_option(context)


@when('Select the "{Parameter_Number}"')
def step_impl(context, Parameter_Number):
    pt.click_on_parameternumber_option(context)


@when('Keep default settings for "{text}" check box')
def step_impl(context, text):
    pt.verify_validate_pat_limits_checkbox_display(context)


@when('Select Bin Type from drop down')
def step_impl(context):
    pt.select_bin_type_option(context, "Hard Bin")


@when('Navigate to the "Static Limits" tab and enter value for as "{Low_Seed_Limit}" and  as "{High_Seed_Limit}"')
def step_impl(context, Low_Seed_Limit, High_Seed_Limit):
    pt.click_on_static_limit_tab(context)
    pt.enter_into_low_seed_limit_field(context, Low_Seed_Limit)
    pt.enter_into_high_seed_limit_field(context, High_Seed_Limit)


@when('Click on the "Calculate Seed" button')
def step_impl(context):
    pt.click_on_calculate_seed_button(context)


@when('Create PAT Rule window will open after clicking "Calculate Seed" button and available Lots will appear')
def step_impl(context):
    pt.verify_lots_number_display(context)


@when('Select Lot and click "Calculate" button')
def step_impl(context):
    pt.click_lot_option(context, "73631")
    pt.click_on_lots_calculate_button(context)


@when('Value for "{Low_Seed_Limit}" and "{High_Seed_Limit}" will be calculated automatically')
def step_impl(context, Low_Seed_Limit, High_Seed_Limit):
    pt.verify_lots_field_display(context)


@when('Enter the lot number for "{After_Every_Lots}"')
def step_impl(context, After_Every_Lots):
    pt.enter_into_after_every_lot_field(context, After_Every_Lots)


@when('Provide the "{Value_of_K}"')
def step_impl(context, Value_of_K):
    pt.enter_into_value_of_k_field(context, Value_of_K)


@when('Select option from "{PAT_limit_to_Apply}" dropdown')
def step_impl(context, PAT_limit_to_Apply):
    pt.select_pat_limit_to_apply(context, PAT_limit_to_Apply)


@when('Provide "{hard_bin_lower_pat_limit}" and "{soft_bin_lower_pat_limit}"')
def step_impl(context, hard_bin_lower_pat_limit, soft_bin_lower_pat_limit):
    pt.enter_into_hard_bin_lower_pat_limit(context, hard_bin_lower_pat_limit)
    pt.enter_into_soft_bin_lower_pat_limit(context, soft_bin_lower_pat_limit)


@when('Then provide the "{hard_bin_upper_pat_limit}" and "{soft_bin_upper_pat_limit}"')
def step_impl(context, hard_bin_upper_pat_limit, soft_bin_upper_pat_limit):
    pt.enter_into_hard_bin_upper_pat_limit(context, hard_bin_upper_pat_limit)
    pt.enter_into_soft_bin_upper_pat_limit(context, soft_bin_upper_pat_limit)


@when('Click "{Save}" button')
def step_impl(context, Save):
    pt.click_on_save_button(context)
    pt.verify_newly_created_pat_rule_name(context, context.rule_name)
    actions.logout(context)
