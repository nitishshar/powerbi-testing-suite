Feature: Power BI Test Results API
  As a Power BI developer
  I want to manage and retrieve test results
  So that I can monitor the health of Power BI reports

  Background:
    Given the API is running
    And the database is initialized

  Scenario: Retrieve all test results
    When I request all test results
    Then the response status code should be 200
    And the response should contain a list of test results
    And each test result should have required fields

  Scenario: Filter test results by status
    When I request test results with status "Failed"
    Then the response status code should be 200
    And all returned tests should have "Failed" status

  Scenario: Filter test results by category
    When I request test results for category "Semantic"
    Then the response status code should be 200
    And all returned tests should be in "Semantic" category

  Scenario: Get test result details
    Given there is a test result with id "123"
    When I request details for test id "123"
    Then the response status code should be 200
    And the response should contain complete test details

  Scenario: Create new test result
    Given I have valid test result data
    When I submit a new test result
    Then the response status code should be 201
    And the test result should be stored in the database

  Scenario: Update test status
    Given there is a test result with id "123"
    When I update the test status to "Passed"
    Then the response status code should be 200
    And the test status should be updated in the database

  Scenario: Get test execution history
    Given there is a test result with id "123"
    When I request the execution history
    Then the response status code should be 200
    And the response should contain execution timestamps

  Scenario: Invalid test result creation
    Given I have invalid test result data
    When I submit a new test result
    Then the response status code should be 422
    And the response should contain validation errors 