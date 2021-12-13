Feature: Buttons testing
  As a guest
  I want to see if the buttons work
  So that I will be able to hover and click them

  Scenario: Hover on buttons
    Given I am a guest
    When I open the website
    And I navigate to buttons
    And I hover on some buttons
    Then The buttons are not selected

  Scenario: Click on buttons
    Given I am a guest
    When I open the website
    And I navigate to buttons
    And I click on some buttons
    Then The buttons are selected

  Scenario: Click on dropdown
    Given I am a guest
    When I open the website
    And I navigate to buttons
    And I click on dropdown
    And I click on first option
    Then The dropdown closes