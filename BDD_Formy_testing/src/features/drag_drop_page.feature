Feature: Drag and drop function
  As a guest
  I want to see if drag and drop works
  So that I will be able to click, drag and drop the image

  Scenario: Drag and drop
    Given I am a guest
    When I open the website
    And I navigate to drag and drop
    And I drag and drop it on the box area
    Then The image "Se" should be in the box