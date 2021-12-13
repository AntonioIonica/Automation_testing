Feature: Switch window page
  As a guest
  I want to interact with buttons
  So that a new window and an alert will open

  Scenario: Click on new tab
    Given I am a guest
    When I open the website
    And I navigate to "Switch window" page
    And I click on "Open new tab" button
    Then A new window will open

  Scenario: Click on alert button
    Given I am a guest
    When I open the website
    And I navigate to "Switch window" page
    And I click on "Open alert" button
    And An alert will pop up and I click on ok
    Then The alert will close