import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SWMDashboardClass:

    def __init__(self):
        pass

    loader = "(//body[@class='loading'])[1]"
    swm_status_by_devices_table_xpath = "(//span[normalize-space()='SWM Status by Devices'])[1]"
    wafer_processed_list = "(//span[normalize-space()='Wafer Processed List'])[1]"
    source_facility_title_xpath = "(//div[@id='jqgh_SWMPolicies_SourceFacility'])[1]"
    source_workcenter_title_xpath = "(//div[@id='jqgh_SWMPolicies_SourceWorkCenter'])[1]"
    source_device_title_xpath = "(//div[@id='jqgh_SWMPolicies_SourceDevice'])[1]"
    target_facility_title_xpath = "(//div[@id='jqgh_SWMPolicies_TargetFacility'])[1]"
    target_work_center_xpath = "(//div[@id='jqgh_SWMPolicies_TargetWorkCenter'])[1]"
    target_device_xpath = "(//div[@id='jqgh_SWMPolicies_TargetDevice'])[1]"
    no_of_policies_xpath = "(//div[@id='jqgh_SWMPolicies_TotalPolicies'])[1]"
    is_automated_xpath = "(//div[@id='jqgh_SWMPolicies_IsAutomatedShow'])[1]"
    processed_wafers_xpath = "(//div[@id='jqgh_SWMPolicies_WafersProcessed'])[1]"
    remaining_wafers_xpath = "(//div[@id='jqgh_SWMPolicies_RemainingWafers'])[1]"
    select_device_xpath = "(//td[@aria-describedby='SWMPolicies_SourceDevice'][normalize-space()='4670'])[1]"
    show_inactive_wafers_id = "show-inactive-wafer"
    policy_name_xpath = "//td[@title='WEB SMALL DATASET'][1]"
    wafer_processed_list_policy_name_xpath = "//table[@id='SwmDashboardGrid']/tbody/tr[2]/td[1]"
    facility_css = "td[aria-describedby='SwmDashboardGrid_MergeFacility']"
    workcenter_css = "td[aria-describedby='SwmDashboardGrid_MergeWorkCenter']"
    device_css = "td[aria-describedby='SwmDashboardGrid_MergeDevice']"
    test_program_xpath = "(//td[@title='PREBAKE_A_4670_POSTBAKE_A_4670'][normalize-space()='PREBAKE_A_4670_POSTBAKE_A_4670'])[1]"
    wafer_status_css = "td[title='WAFER CREATED']"
    wafer_active_status = "td[title='true']"

    def click_device(self, context):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.policy_name_xpath).click()

    def verify_show_inactive_wafers_is_checked(self, context):
        element = context.driver.find_element(By.ID, self.show_inactive_wafers_id)
        assert element.is_selected()

    def verify_policy_name(self, context, expected_text):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        context.driver.find_element(By.XPATH, self.policy_name_xpath).click()
        time.sleep(2)
        element = context.driver.find_element(By.XPATH, self.wafer_processed_list_policy_name_xpath)
        return element.text.__eq__(expected_text)

    def verify_facility(self, context, expected_text):
        element = context.driver.find_element(By.CSS_SELECTOR, self.facility_css)
        return element.text.__eq__(expected_text)

    def verify_workcenter(self, context, expected_text):
        element = context.driver.find_element(By.CSS_SELECTOR, self.workcenter_css)
        return element.text.__eq__(expected_text)

    def verify_device(self, context, expected_text):
        element = context.driver.find_element(By.CSS_SELECTOR, self.device_css)
        return element.text.__eq__(expected_text)

    def verify_testprogram(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.test_program_xpath)
        return element.text.__eq__(expected_text)

    def verify_wafer_status(self, context, expected_text):
        element = context.driver.find_element(By.CSS_SELECTOR, self.wafer_status_css)
        return element.text.__eq__(expected_text)

    def verify_wafer_active_status(self, context, expected_text):
        element = context.driver.find_element(By.CSS_SELECTOR, self.wafer_active_status)
        return element.text.__eq__(expected_text)

    def verify_swm_status_by_devices_display(self, context, expected_text):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.swm_status_by_devices_table_xpath)
        return element.text.__eq__(expected_text)

    def verify_wafer_processed_list(self, context, expected_text):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        element = context.driver.find_element(By.XPATH, self.wafer_processed_list)
        return element.text.__eq__(expected_text)

    def verify_display_of_source_facility(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.source_facility_title_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_source_work_center(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.source_workcenter_title_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_source_work_center(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.source_workcenter_title_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_source_device(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.source_device_title_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_target_facility(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.target_facility_title_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_target_workcenter(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.target_work_center_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_target_device(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.target_device_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_no_of_policies_device(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.no_of_policies_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_of_is_automated(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.is_automated_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_processed_wafers(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.processed_wafers_xpath)
        return element.text.__eq__(expected_text)

    def verify_display_remaining_wafers(self, context, expected_text):
        element = context.driver.find_element(By.XPATH, self.remaining_wafers_xpath)
        return element.text.__eq__(expected_text)
