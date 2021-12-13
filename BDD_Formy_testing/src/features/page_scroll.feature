Feature: Scroll page
  As a guest
  I want to scroll the page down
  So that I will be able to enter a date and a name

  Scenario: Scroll to input date and name
    Given I am a guest
    When I open the website
    And I navigate to "Page scroll"
    And I scroll down the page
    And I enter a name in the "Full name" box
    And I enter a date in "Date" box
    Then The input name should be displayed
    And the input date should be displayed