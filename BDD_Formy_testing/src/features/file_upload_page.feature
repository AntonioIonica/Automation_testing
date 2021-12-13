Feature: Buttons testing
  As a guest
  I want to see if file upload works
  So that I will be able to upload a given png

  Scenario: Uploading a picture
    Given I am a guest
    When I open the website
    And I navigate to File upload
    And I click on Choose button and upload a picture
    Then The box should had the name of the picture

  Scenario: Uploading a picture and reset it
    Given I am a guest
    When I open the website
    And I navigate to File upload
    And I click on Choose a file button and upload a picture
    And I press reset
    Then The box should be reset