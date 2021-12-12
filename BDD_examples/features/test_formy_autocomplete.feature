Feature: Test autocomplete page
  As I user
  I want to type 2 letters
  So that full address to be visible

  Scenario: Check address field
    Given I clicked on autocomplete button
    When I type cl in address field
    Then Cluj should be visible