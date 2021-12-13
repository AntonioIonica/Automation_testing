Feature: Modal buttons page
  As a guest
  I want to open the modal
  So that I will be able to close it with both buttons

  Scenario: Open and close the modal with ok
    Given I am a guest
    When I open the website
    And I navigate to modal page
    And I click on "Open Modal"
    And I click on ok button
    Then The modal window closes

  Scenario: Open and close the modal with close
    Given I am a guest
    When I open the website
    And I navigate to modal page
    And I click on "Open Modal"
    And I click on close button
    Then The modal window closes