Feature: Power BI Testing Suite
  As a BI developer
  I want to validate Power BI reports and semantic models
  So that I can ensure data quality and report functionality

  Scenario: Validate semantic model schema changes
    Given I have the current semantic model schema
    And I have the expected schema definition
    When I compare the schemas
    Then all required tables should be present
    And all required columns should have correct data types
    And no breaking changes should be detected

  Scenario: Validate calculated measures
    Given I have a set of test data
    And I have defined expected results
    When I execute the DAX queries
    Then the results should match expected values
    And performance should be within acceptable limits

  Scenario: Validate report visuals
    Given I have a Power BI report
    When I check all visual elements
    Then all visuals should load without errors
    And all filters should be functional
    And all cross-filtering should work correctly

  Scenario: Test data refresh
    Given I have a Power BI dataset
    When I trigger a data refresh
    Then the refresh should complete successfully
    And the last refresh time should be updated
    And no data quality issues should be detected 