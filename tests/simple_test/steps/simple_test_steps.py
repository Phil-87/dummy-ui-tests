from behave import Step
from hamcrest import assert_that

from tests.simple_test.pages.simple_test_page import SimpleTestPage


@Step("I load the page to be tested")
def load_the_page_to_be_tested(context):
    context.simple_page = SimpleTestPage(context.browser, context.logger, context.implicit_wait)
    context.simple_page.endpoint = context.pages_to_test[0]
    context.simple_page.go_to_page(context.url)


@Step("the expected element is visible")
def expected_element_is_visible(context):
    assert_that(context.simple_page.expected_element_is_visible(), "The expected element was not visible")
