import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class NewSWMRulWindowClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    new_swm_rule_window_xpath = "//span[normalize-space()='New SWM Rule']"
    new_swm_rule_name_id = "Name"
    new_swm_rule_description_id = "Description"
    input_data_selection_tab_id = "input-data-selection-tab"
    source_web_small_dataset_xpath = "//select[@id='SourceFacility']/option[@value='WEB SMALL DATASET']"
    target_web_small_dataset_xpath = "//select[@id='TargetFacility']/option[@value='WEB SMALL DATASET']"
    source_probe_xpath = "(//option[@value='1|M'][normalize-space()='1|M'])[1]"
    target_probe_xpath = "(//option[@value='1|M'][normalize-space()='1|M'])[2]"
    level_dropdown_id = "Level"
    bin_type_dropdown_id = "BinTypeID"
    rule_validation_xpath = "(//input[@id='rulesValiditions'])[2]"
    rule_definition_tab_id = "bin-rule-tab"
    bin_rule_details_dropdown_xpath = "(//select[@id='RuleMissingDieID'])[1]"
    source_wafer_bin_id = "SourceRuleBinID"
    target_wafer_bin_id = "TargetRuleBinID"
    combine_wafer_bin_xpath = "(//select[@id='RuleBinTypeID'])[1]"
    hard_bin_number_field_xpath = "(//input[@id='custom-bin-number'])[1]"
    hard_bin_name_field_xpath = "(//input[@id='custom-bin-name'])[1]"
    soft_bin_number_field_xpath = "(//input[@id='custom-soft-bin-number'])[1]"
    soft_bin_name_field_xpath = "(//input[@id='custom-soft-bin-name'])[1]"
    bin_flag_dropdown_xpath = "(//select[@id='custom-pass-fail-flag'])[1]"
    other_fields_data_xpath = "(//select[@id='OtherFiledsDataID'])[1]"
    die_type_xpath = "(//select[@id='CustomDieTypeID'])[1]"
    copy_parametric_data_xpath = "(//select[@id='ParametricDataCopyID'])[1]"
    email_notification_tab_id = "email-notification-tab"
    owner_name_field_id = "OwnerName"
    owner_email_address_field_id = "OwnerEmailAddress"
    additional_email_field_id = "SecondaryEmailAddresses"
    save_btn_id = "btn-save"
    new_swm_rule_name_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[4]"
    source_work_center_xpath = "(//option[@value='WAFER SORT'])[1]"
    source_device_xpath = "(//option[@value='4670'])[1]"
    target_work_center_xpath = "(//option[@value='WAFER SORT'])[1]"
    target_device_xpath = "(//option[@value='4670'])[2]"
    select_rule_type_dropdown_xpath = "(//select[@id='RuleTypeID'])[1]"
    copy_bin_number_checkbox_xpath = "(//input[@id='PopulateBinParametersData'])[1]"
    source_test_program_xpath = "(//select[@id='SourceTestProgram'])[1]"
    target_test_program_xpath = "(//select[@id='TargetTestProgram'])[1]"
    swm_rule_table_xpath = "(//div[@id='gview_RulesGrid'])[1]"
    swm_rule_edit_button_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[2]/button"
    swm_rule_copy_button_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[3]/button"
    swm_rule_delete_button_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[13]/button"
    swm_rule_delete_alert_accept_option_xpath = "(//button[normalize-space()='Yes'])[1]"
    swm_delete_success_popup_css = "div.bootstrap-growl.alert.alert-success"

    def verify_swm_rule_delete_success_popup_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.swm_delete_success_popup_css)))

    def click_swm_rule_copy_button(self, context):
        context.driver.find_element(By.XPATH, self.swm_rule_copy_button_xpath).click()

    def click_swm_rule_delete_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.execute_script("window.scrollBy(0,document.body.scrollWidth);")
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_rule_delete_button_xpath))).click()

    def accept_swm_rule_delete_alert(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.swm_rule_delete_alert_accept_option_xpath))).click()

    def verify_swm_rule_delete_alert_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_rule_delete_alert_accept_option_xpath)))
        element = context.driver.find_element(By.XPATH, self.swm_rule_delete_alert_accept_option_xpath)
        element.is_displayed()

    def click_swm_rule_edit_button(self, context):
        context.driver.find_element(By.XPATH, self.swm_rule_edit_button_xpath).click()

    def verify_swm_rule_table_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.swm_rule_table_xpath)
        element.is_displayed()

    def verify_newly_created_swm_rule_name(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.new_swm_rule_name_xpath)))
        element = context.driver.find_element(By.XPATH, self.new_swm_rule_name_xpath)
        return element.text.__eq__(expected_text)

    def verify_deleted_swm_rule_name(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.new_swm_rule_name_xpath)
        return element.text

    def verify_deleted_swm_rule_name_is_removed(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.new_swm_rule_name_xpath)
        return element.text.__ne__(expected_text)

    def click_source_work_center(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.source_work_center_xpath).click()

    def click_source_device(self, context):
        context.driver.find_element(By.XPATH, self.source_device_xpath).click()

    def click_target_work_center(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.target_work_center_xpath).click()

    def click_target_device(self, context):
        context.driver.find_element(By.XPATH, self.target_device_xpath).click()

    def click_save_btn(self, context):
        context.driver.find_element(By.ID, self.save_btn_id).click()

    def click_new_swm_rule_window(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.new_swm_rule_window_xpath).click()

    def click_input_data_selection_tab(self, context):
        context.driver.find_element(By.ID, self.input_data_selection_tab_id).click()

    def click_rule_definition_tab(self, context):
        context.driver.find_element(By.ID, self.rule_definition_tab_id).click()

    def click_source_facility(self, context):
        context.driver.find_element(By.XPATH, self.source_web_small_dataset_xpath).click()

    def click_source_probe(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.source_probe_xpath).click()

    def click_target_facility(self, context):
        context.driver.find_element(By.XPATH, self.target_web_small_dataset_xpath).click()

    def click_target_probe(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.target_probe_xpath).click()

    def click_rule_validation_radiobutton(self, context):
        element = context.driver.find_element(By.XPATH, self.rule_validation_xpath)
        element.click()
        assert element.is_selected()

    def click_copy_bin_number_checkbox(self, context):
        element = context.driver.find_element(By.XPATH, self.copy_bin_number_checkbox_xpath)
        if element.is_enabled():
            element = context.driver.find_element(By.XPATH, self.copy_bin_number_checkbox_xpath)
            element.click()
            assert element.is_selected()

    def enter_into_swm_rule_name_field(self, context, name_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.new_swm_rule_name_id).send_keys(name_value)

    def verify_swm_rule_window_display(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.new_swm_rule_name_id)
        element.is_displayed()

    def edit_swm_rule_name_field(self, context, name_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.new_swm_rule_name_id)
        element.clear()
        element.send_keys(name_value)

    def click_email_notification_tab(self, context):
        context.driver.find_element(By.ID, self.email_notification_tab_id).click()

    def enter_into_hard_bin_if_enabled(self, context, name_value):
        element = context.driver.find_element(By.XPATH, self.hard_bin_number_field_xpath)
        if element.is_enabled():
            element.send_keys(name_value)
        time.sleep(2)

    def enter_into_hard_bin_number_field(self, context, name_value):
        context.driver.find_element(By.XPATH, self.hard_bin_number_field_xpath).send_keys(name_value)
        time.sleep(2)

    def enter_into_hard_bin_name_field(self, context, name_value):
        context.driver.find_element(By.XPATH, self.hard_bin_name_field_xpath).send_keys(name_value)

    def enter_into_soft_bin_number_field(self, context, name_value):
        context.driver.find_element(By.XPATH, self.soft_bin_number_field_xpath).send_keys(name_value)
        time.sleep(2)

    def enter_into_soft_bin_name_field(self, context, name_value):
        context.driver.find_element(By.XPATH, self.soft_bin_name_field_xpath).send_keys(name_value)

    def enter_into_swm_rule_description_field(self, context, description):
        context.driver.find_element(By.ID, self.new_swm_rule_description_id).send_keys(description)

    def enter_into_owner_name_field(self, context, description):
        context.driver.find_element(By.ID, self.owner_name_field_id).send_keys(description)

    def enter_into_owner_email_field(self, context, description):
        context.driver.find_element(By.ID, self.owner_email_address_field_id).send_keys(description)

    def enter_into_additional_email_field(self, context, description):
        context.driver.find_element(By.ID, self.additional_email_field_id).send_keys(description)

    def edit_owner_name_field(self, context, description):
        element = context.driver.find_element(By.ID, self.owner_name_field_id)
        element.clear()
        element.send_keys(description)

    def edit_owner_email_field(self, context, description):
        element = context.driver.find_element(By.ID, self.owner_email_address_field_id)
        element.clear()
        element.send_keys(description)

    def edit_additional_email_field(self, context, description):
        element = context.driver.find_element(By.ID, self.additional_email_field_id)
        element.clear()
        element.send_keys(description)

    def select_level(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = Select(context.driver.find_element(By.ID, self.level_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def select_bin_type(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.ID, self.bin_type_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def select_bin_rule_details(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.bin_rule_details_dropdown_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_source_wafer_bin(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.source_wafer_bin_id)
        if element.is_enabled():
            element = Select(context.driver.find_element(By.ID, self.source_wafer_bin_id))
            element.select_by_visible_text(visible_text_value)

    def select_target_wafer_bin(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.ID, self.target_wafer_bin_id)
        if element.is_enabled():
            element = Select(context.driver.find_element(By.ID, self.target_wafer_bin_id))
            element.select_by_visible_text(visible_text_value)



    def select_combine_wafer_bin(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.combine_wafer_bin_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_bin_flag_if_enabled(self, context, visible_text_value):
        element = context.driver.find_element(By.XPATH, self.bin_flag_dropdown_xpath)
        if element.is_enabled():
            select_element = Select(context.driver.find_element(By.XPATH, self.bin_flag_dropdown_xpath))
            select_element.select_by_visible_text(visible_text_value)



    def select_bin_flag(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.bin_flag_dropdown_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_other_field_data(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.other_fields_data_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_die_type_if_enabled(self, context, visible_text_value):
        element = context.driver.find_element(By.XPATH, self.die_type_xpath)
        if element.is_enabled():
            select_element = Select(context.driver.find_element(By.XPATH, self.die_type_xpath))
            select_element.select_by_visible_text(visible_text_value)

    def select_die_type(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.die_type_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_copy_parametric_data(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.copy_parametric_data_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_rule_type_dropdown(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.select_rule_type_dropdown_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_source_test_program(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.source_test_program_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_target_test_program(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.target_test_program_xpath))
        element.select_by_visible_text(visible_text_value)





