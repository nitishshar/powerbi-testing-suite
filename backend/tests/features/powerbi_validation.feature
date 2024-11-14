Feature: Power BI Model Validation
  As a BI developer
  I want to validate the Power BI semantic model
  So that I can ensure report stability

  Scenario: Validate semantic model schema
    Given I have a connection to Power BI
    When I retrieve the current model schema
    Then it should match the expected schema structure

  Scenario: Execute DAX queries
    Given I have a valid DAX query
    When I execute the query
    Then I should receive the expected results 