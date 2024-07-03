import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardClass:

    def __init__(self):
        pass

    quality_and_pat_xpath = "//span[normalize-space()='Quality & PAT']"
    pat_rule_heading_xpath = "//a[@href='/Rules']"
    pat_heading_xpath = "//span[normalize-space()='PAT']"
    logout_avatar_xpath = "//img[@class='menu-avatar']"
    logout_link_xpath = "//span[normalize-space()='Logout']"
    loader = "(//body[@class='loading'])[1]"
    swm_heading_xpath = "//span[normalize-space()='SWM']"
    swm_rules_heading_xpath = "//span[normalize-space() = 'SWM Rules']"
    swm_dashboard_heading_xpath = "(//span[normalize-space()='SWM Dashboard'])[1]"
    automate_swm_policies_link_xpath = "(//span[normalize-space()='Automate SWM Policies'])[1]"
    swm_policies_heading_xpath = "(//span[contains(text(),'SWM Policies')])[1]"

    def click_on_logout_avatar(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, self.loader)))
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_avatar_xpath)))
        context.driver.find_element(By.XPATH, self.logout_avatar_xpath).click()

    def click_on_logout_link(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_link_xpath))).click()

    def click_quality_and_pat_heading(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.quality_and_pat_xpath))).click()

    def click_pat_heading(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.pat_heading_xpath))).click()

    def click_pat_rules_heading(self, context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.pat_rule_heading_xpath))).click()

    def click_swm_heading(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_heading_xpath))).click()

    def click_swm_rules_heading(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_rules_heading_xpath))).click()

    def click_swm_policies_heading(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_policies_heading_xpath))).click()

    def click_swm_dashboard_heading(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.swm_dashboard_heading_xpath))).click()

    def click_automate_swm_policies(self,context):
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.automate_swm_policies_link_xpath))).click()
