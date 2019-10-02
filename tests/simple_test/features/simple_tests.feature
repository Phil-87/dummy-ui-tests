#noinspection CucumberUndefinedStep
Feature: Simple Tests

  Scenario: Open a page
    Given I load the page to be tested
    Then the expected element is visible