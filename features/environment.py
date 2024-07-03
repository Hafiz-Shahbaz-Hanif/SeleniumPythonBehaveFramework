import subprocess
import os
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry


def before_feature(context, feature):
    for scenario in feature.scenarios:
        if "retry" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=1)


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)
