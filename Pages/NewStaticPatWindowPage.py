import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class NewStaticPatRuleWindowClass:

    def __init__(self):
        pass

    lot_option_xpath = "//option[@value='3108']"
    new_static_pat_rule_window_xpath = "//div[@class='span2 action-nav-button btn-dynamic']//a[@id='btn-dynamic-rule']"
    general_tab_xpath = "//a[@id='general-tab']"
    name_field_xpath = "//input[@id='Rule_Name']"
    parameters_tab_id = "parameter-tab"
    static_limits_tab_id = "initial-limit-tab"
    facility_option_xpath = "//option[@value='WEB SMALL DATASET']"
    workcenter_option_xpath = "//option[@value='WAFER SORT']"
    device_option_xpath = "//option[@value='4670']"
    test_program_option_xpath = "//option[@value='PREBAKE_A_4670']"
    parameter_number_option_xpath = "//tr[@id='1']//td[contains(@title,'26')][contains(text(),'Idd_prewrite Idd_prewrite')]"
    bin_type_dropdown_xpath = "//select[@id='Points_GetBy_IsHardBin']"
    low_seed_limit_id = "Static_PAT_Lo_Limit"
    high_seed_limit_id = "Static_PAT_Hi_Limit"
    calculate_seed_button_id = "btn-calculate-static-seed-limit"
    select_lots_dropdown_id = "Lots"
    calculate_btn_id = "btn-calculate"
    every_lot_field_id = "Notify_LotCount"
    value_of_k_field_id = "Static_Val_K"
    pat_limit_to_apply_dropdown_id = "LimitToApplyId"
    hard_bin_lower_pat_limit_xpath = "(//input[@id='custom-bin-number-lower-static'])[1]"
    soft_bin_lower_pat_limit_xpath = "(//input[@id='custom-soft-bin-number-lower-static'])[1]"
    hard_bin_upper_pat_limit_xpath = "(//input[@id='custom-bin-number-upper-static'])[1]"
    soft_bin_upper_pat_limit_xpath = "(//input[@id='custom-soft-bin-number-upper-static'])[1]"
    save_button_xpath = "(//input[@id='btn-save'])[1]"
    pat_rule_name_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[3]"
    validate_pat_limits_checkbox_xpath = "//input[@id='IsValidate_PAT_Limits']"
    select_lots_field_id = "Notify_LotCount"
    loader = "(//body[@class='loading'])[1]"


    def select_pat_limit_to_apply(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.pat_limit_to_apply_dropdown_id))).is_displayed()
        element = Select(context.driver.find_element(By.ID, self.pat_limit_to_apply_dropdown_id))
        element.select_by_visible_text(visible_text_value)

    def click_lot_option(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.lot_option_xpath))).click()

    def select_bin_type_option(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.bin_type_dropdown_xpath))).is_displayed()
        element = Select(context.driver.find_element(By.XPATH, self.bin_type_dropdown_xpath))
        element.select_by_visible_text(visible_text_value)

    def click_on_save_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.save_button_xpath))).click()

    def click_on_parameternumber_option(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.execute_script("window.scrollBy(0,document.body.scrollWidth);")
        # time.sleep(3)
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.parameter_number_option_xpath))).click()
        # time.sleep(2)

    def click_on_calculate_seed_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.calculate_seed_button_id))).click()

    def click_on_lots_calculate_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.calculate_btn_id))).click()

    def click_on_testprogram_option(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.test_program_option_xpath))).click()

    def click_on_device_option(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.device_option_xpath))).click()
        time.sleep(2)


    def click_on_workcenter_option(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.workcenter_option_xpath))).click()

    def click_on_facility_option(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.facility_option_xpath))).click()

    def click_on_parameters_tab(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.parameters_tab_id))).click()

    def click_on_static_limit_tab(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.static_limits_tab_id))).click()
        time.sleep(3)

    def click_new_static_pat_link(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.new_static_pat_rule_window_xpath).click()

    def click_on_general_tab(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.general_tab_xpath).click()

    def enter_into_name_field(self, context, name_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.name_field_xpath))).send_keys(name_value)

    def enter_into_low_seed_limit_field(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.low_seed_limit_id))).send_keys(text)

    def enter_into_high_seed_limit_field(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.high_seed_limit_id))).send_keys(text)

    def enter_into_after_every_lot_field(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.every_lot_field_id))).send_keys(text)

    def enter_into_value_of_k_field(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.value_of_k_field_id))).send_keys(text)

    def enter_into_hard_bin_lower_pat_limit(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.hard_bin_lower_pat_limit_xpath))).send_keys(text)

    def enter_into_soft_bin_lower_pat_limit(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.soft_bin_lower_pat_limit_xpath))).send_keys(text)

    def enter_into_hard_bin_upper_pat_limit(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.hard_bin_upper_pat_limit_xpath))).send_keys(text)

    def enter_into_soft_bin_upper_pat_limit(self, context, text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.soft_bin_upper_pat_limit_xpath))).send_keys(text)

    def verify_newly_created_pat_rule_name(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.pat_rule_name_xpath))).is_displayed()
        element = context.driver.find_element(By.XPATH, self.pat_rule_name_xpath)
        return element.text.__eq__(expected_text)


    def verify_validate_pat_limits_checkbox_display(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.validate_pat_limits_checkbox_xpath))).is_displayed()

    def verify_lots_number_display(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.select_lots_dropdown_id))).is_displayed()

    def verify_lots_field_display(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.ID, self.select_lots_field_id))).is_displayed()




