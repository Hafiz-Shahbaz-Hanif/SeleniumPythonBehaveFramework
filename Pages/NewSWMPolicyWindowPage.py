import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class NewSWMPolicyClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    new_swm_policy_btn_xpath = "(//span[normalize-space()='New SWM Policy'])[1]"
    create_swm_policy_window_xpath = "//h6[@id='modal-form-label']"
    input_data_and_rule_selection_tab_xpath = "//a[@id='input-data-selection-tab']"
    select_rule_checkbox_xpath = "//table[@id='RulesGrid']/tbody/tr[2]/td[1]/input"
    output_data_selection_tab_xpath = "//a[@id='output-data-selection-tab']"
    select_all_source_dies_button_xpath = "(//button[@onclick='selectSourceAllDieTypeFilters()'])[1]"
    select_all_target_dies_button_xpath = "(// button[@ onclick='selectTargetAllDieTypeFilters()'])[1]"
    manage_exception_tab_xpath = "(//a[normalize-space()='Manage Exceptions'])[1]"
    create_policy_save_btn_xpath = "//input[@id='btn-save-policy']"
    new_swm_policy_name_xpath = "//table[@id='PoliciesGrid']/tbody/tr[2]/td[4]"
    custom_radio_btn_xpath = "(//input[@id='TestProgramOptions'])[2]"
    manage_test_programs_link_xpath = "//span[normalize-space()='Manage Test Programs']"
    policy_source_test_program_xpath = "//select[@id='sourceTestProgram']"
    policy_target_test_program_xpath = "//select[@id='targetTestProgram']"
    policy_add_btn_xpath = "(//input[@id='btn-save-policy'])[2]"
    policy_apply_btn_xpath = "(//input[@id='btn-save-policy'])[3]"

    def click_new_swm_policy_window(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.new_swm_policy_btn_xpath).click()

    def verify_create_swm_policy_window_display(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.create_swm_policy_window_xpath)
        return element.text.__eq__(expected_text)

    def click_input_data_and_rule_selection_tab(self, context):
        context.driver.find_element(By.XPATH, self.input_data_and_rule_selection_tab_xpath).click()

    def select_rules(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.select_rule_checkbox_xpath).click()

    def click_output_data_selection_tab(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.output_data_selection_tab_xpath)))
        context.driver.find_element(By.XPATH, self.output_data_selection_tab_xpath).click()

    def click_manage_exceptions_tab(self, context):
        context.driver.find_element(By.XPATH, self.manage_exception_tab_xpath).click()

    def click_select_all_source_dies_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.select_all_source_dies_button_xpath)))
        context.driver.find_element(By.XPATH, self.select_all_source_dies_button_xpath).click()

    def click_select_all_target_dies_button(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.select_all_source_dies_button_xpath)))
        context.driver.find_element(By.XPATH, self.select_all_target_dies_button_xpath).click()

    def click_create_policy_save_btn(self, context):
        context.driver.find_element(By.XPATH, self.create_policy_save_btn_xpath).click()

    def click_custom_radio_btn(self, context):
        context.driver.find_element(By.XPATH, self.custom_radio_btn_xpath).click()

    def click_manage_test_programs_link(self, context):
        context.driver.find_element(By.XPATH, self.manage_test_programs_link_xpath).click()

    def verify_newly_created_swm_policy_name(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait.until(EC.visibility_of_element_located((By.XPATH, self.new_swm_policy_name_xpath)))
        element = context.driver.find_element(By.XPATH, self.new_swm_policy_name_xpath)
        return element.text.__eq__(expected_text)

    def select_policy_source_test_program(self, context, visible_text_value):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.policy_source_test_program_xpath)))
        element = Select(context.driver.find_element(By.XPATH, self.policy_source_test_program_xpath))
        element.select_by_visible_text(visible_text_value)

    def select_policy_target_test_program(self, context, visible_text_value):
        element = Select(context.driver.find_element(By.XPATH, self.policy_target_test_program_xpath))
        element.select_by_visible_text(visible_text_value)

    def click_policy_add_btn(self, context):
        context.driver.find_element(By.XPATH, self.policy_add_btn_xpath).click()

    def click_policy_apply_btn(self, context):
        context.driver.find_element(By.XPATH, self.policy_apply_btn_xpath).click()
