Feature: Google Maps suggestion test
  As an user
  I want to type 3 different cities
  So that suggestions will appear

  Scenario Outline: Input different cities
    Given I open Google maps website
    When I click on Search bar
    And I enter the input "<cities>"
    Then First suggestion should be "<suggestions>"
    Examples: Cities
      | cities    | suggestions |
      | Bucharest | Bucharest  |
      | Cluj      | Cluj       |
      | Sibiu     | Sibiu      |