import json
import logging
from behave.model_core import Status
from uitestcore.utilities import logger_handler
from uitestcore.utilities.browser_handler import BrowserHandler


def before_all(context):
    with open("config/config_file.json") as data_file:
        config = json.load(data_file)
        context.browser = config["browser"]
        context.implicit_wait = config["implicit_wait"]
        context.maximize_browser = config["maximize_browser"]
        context.url = config["base_url"]

    logger_handler.init_unique_log_file_logger(level=20)
    context.logger = logging.getLogger("dummy-ui-tests")

    BrowserHandler.prepare_browser(context)


def before_scenario(context, scenario):
    context.logger.log(20, "* * *")
    context.logger.log(20, "* Start scenario: " + scenario.name)
    context.logger.log(20, "* * *")


def after_scenario(context, scenario):
    context.logger.log(20, "* * *")
    context.logger.log(20, f"* Scenario '{scenario.name}' ended with status: '{scenario.status.name}'")
    context.logger.log(20, "* * *")

    if scenario.status == Status.failed:
        BrowserHandler.take_screenshot(context.browser, scenario.name)


def after_all(context):
    context.browser.quit()
