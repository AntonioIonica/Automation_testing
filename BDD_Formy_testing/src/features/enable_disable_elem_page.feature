Feature: Enabled and disabled elements
  As a guest
  I want to see if the elements status is right
  So that I will be able to interact with them

  Scenario: Enabled box
    Given I am a guest
    When I open the website
    And I navigate to Enabled and disabled elements
    And I click on "Input here..." box
    And I type "abc123"
    Then The box should be enabled

  Scenario: Disabled box
    Given I am a guest
    When I open the website
    And I navigate to Enabled and disabled elements
    And I click on "Disabled input here..."
    Then The box should be disabled