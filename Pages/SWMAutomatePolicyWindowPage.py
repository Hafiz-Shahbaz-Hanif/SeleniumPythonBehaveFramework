import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AutomateSWMPolicyWindowClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    automate_swm_policy_window_xpath = "(//a[@id='btn-new-rule'])[1]"
    policy_selection_tab_id = "auto-policy-selection-tab"
    source_facility_css = "select[id='SourceFacility'] option[value='WEB SMALL DATASET']"
    source_work_center_css = "select[id='SourceWorkCenter'] option[value='WAFER SORT']"
    source_device_css = "select[id='SourceDevice'] option[value='4670']"
    source_test_program_xpath = "(//option[@value='PREBAKE_A_4670'][normalize-space()='PREBAKE_A_4670'])[1]"
    target_facility_css = "select[id='TargetFacility'] option[value='WEB SMALL DATASET']"
    target_workcenter_css = "select[id='TargetWorkCenter'] option[value='WAFER SORT']"
    target_device_css = "select[id='TargetDevice'] option[value='4670']"
    target_test_program_xpath = "(//option[@value='POSTBAKE_A_4670'][normalize-space()='POSTBAKE_A_4670'])[2]"
    select_policy_xpath = "(//td[@title='SWM_Policy_TestProgram11'])[1]"
    save_btn_css = "#btn-save-automate-policy"
    automate_policy_name_xpath = "//td[@title='SWM_Policy_TestProgram']"
    automate_policy_checkbox_xpath = "//table[@id='AutmateSWMPolicies']/tbody/tr[2]/td[1]/input[1]"
    automate_policy_alert_yes_btn_xpath = "(//button[normalize-space()='Yes'])[1]"
    success_popup_css = "div.bootstrap-growl.alert.alert-success"
    un_automate_policy_alert_xpath = "(//button[normalize-space()='Yes'])[1]"
    delete_icon_xpath = "(//span[@class='ui-button-icon-primary ui-icon ui-icon-trash'])[1]"

    def verify_success_popup(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.success_popup_css)))

    def accept_automate_policy_checkbox_alert(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.automate_policy_alert_yes_btn_xpath))).click()

    def verify_automate_policy_checkbox_is_checked(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait = WebDriverWait(context.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.automate_policy_checkbox_xpath)))
        assert element.is_selected()

    def click_automate_policy_checkbox(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.save_btn_css)))
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.automate_policy_checkbox_xpath))).click()

    def verify_newly_created_swm_policy_name(self, context, expected_text):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.automate_policy_name_xpath)
        return element.text.__eq__(expected_text)

    def verify_deleted_swm_policy_name(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.automate_policy_name_xpath)))

    def click_automate_swm_policy_window(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.automate_swm_policy_window_xpath).click()

    def click_policy_selection_tab(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.ID, self.policy_selection_tab_id).click()

    def click_source_facility(self, context):
        context.driver.find_element(By.CSS_SELECTOR, self.source_facility_css).click()

    def click_source_workcenter(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.CSS_SELECTOR, self.source_work_center_css).click()

    def click_source_device(self, context):
        context.driver.find_element(By.CSS_SELECTOR, self.source_device_css).click()

    def click_source_testprogram(self, context):
        context.driver.find_element(By.XPATH, self.source_test_program_xpath).click()

    def click_target_facility(self, context):
        context.driver.find_element(By.CSS_SELECTOR, self.target_facility_css).click()

    def click_target_workcenter(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.CSS_SELECTOR, self.target_workcenter_css).click()

    def click_target_device(self, context):
        context.driver.find_element(By.CSS_SELECTOR, self.target_device_css).click()

    def click_target_testprogram(self, context):
        context.driver.find_element(By.XPATH, self.target_test_program_xpath).click()

    def click_policy(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.select_policy_xpath).click()

    def click_save_btn(self, context):
        context.driver.find_element(By.CSS_SELECTOR, self.save_btn_css).click()

    def verify_automate_swm_policy_window_is_displayed(self, context):
        element = context.driver.find_element(By.XPATH, self.automate_swm_policy_window_xpath)
        assert element.is_displayed()

    def uncheck_automate_policy_checkbox(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.automate_policy_checkbox_xpath))).click()

    def verify_un_automate_alert_is_displayed(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.un_automate_policy_alert_xpath))).is_displayed()

    def click_un_automate_alert_yes_btn(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.un_automate_policy_alert_xpath))).click()

    def click_delete_btn(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.delete_icon_xpath))).click()

    def verify_automate_policy_checkbox_is_unchecked(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait = WebDriverWait(context.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.automate_policy_checkbox_xpath)))
        assert element.is_selected() is False




