Feature: Radio buttons testing
  As a guest
  I want to click the radio buttons
  So that they will stay selected

  Scenario: Button number 3
    Given I am a guest
    When I open the website
    And I navigate to "Radio buttons" page
    And I click on the buttons in this order: 2>1>3
    Then The button number 3 should be selected

  Scenario: Button number 2
    Given I am a guest
    When I open the website
    And I navigate to "Radio buttons" page
    And I click on the buttons in this order: 1>3>2
    Then The button number 2 should be selected

  Scenario: Button number 1
    Given I am a guest
    When I open the website
    And I navigate to "Radio buttons" page
    And I click on the buttons in this order: 3>2>1
    Then The button number 1 should be selected