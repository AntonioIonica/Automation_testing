Feature: Keyboard and mouse testing
  As a guest
  I want to see if I can interact with mouse and keyboard
  So that I should be able to enter some data and click on the button

  Scenario: Interacting with mouse and keyboard on the page
    Given I am a guest
    When I open the website
    And I navigate to Keyboard and mouse input
    And I input a random name as Full name
    And I click on the Button
    Then The button is selected
    And The name I typed is in the "Enter full name" box