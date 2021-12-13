Feature: Datepicker test
  As a guest
  I want to see enter a date
  So that the calendar should display that date

  Scenario: Enter a date
    Given I am a guest
    When I open the website
    And I navigate to datepicker
    And I enter a date with keyboard
    Then The calendar should display the respective date