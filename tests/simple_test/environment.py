import common.environment as common
import os
import json


def before_all(context):
    common.before_all(context)
    config_file = os.getcwd() + '/tests/simple_test/config/config.json'

    with open(config_file) as data_file:
        config = json.load(data_file)
        context.pages_to_test = config["pages_to_test"]


def before_scenario(context, scenario):
    common.before_scenario(context, scenario)


def after_scenario(context, scenario):
    common.after_scenario(context, scenario)
