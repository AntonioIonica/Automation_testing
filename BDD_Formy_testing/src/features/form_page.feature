Feature: Form page testing
  As a guest
  I want to enter some data
  So that I will submit the form

  Scenario Outline: Completing a form page with variable data
    Given I am a guest
    When I open the website
    And I click on Complete web form
    And I type "<first_name>" as First name
    And I type "<last_name>" as Last name
    And I type "<job>" as Job title
    And I choose a form of education
    And I choose a sex
    And I choose some years of experience
    And I sent "<date>" as Date birth
    And I click on submit
    Then The form will be successfully submitted
    Examples:
      | first_name | last_name | job      | date       |
      | Antonio    | Ion       | Engineer | 07/18/2006 |
      | Andrei     | Marian    | Student  | 07/18/1996 |