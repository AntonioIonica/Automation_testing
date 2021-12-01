Feature: Login page
  As an admin
  I want to login
  So that I have full access to full operations

  @smoke
  Scenario: Invalid login
    Given I already have an account
    When I open the website
    And I set the email popescu@gmail.com
    And I set the password abc1234
    Then Invalid login appears

  Scenario: Valid admin login
    Given I already have an account
    When I open the website
    And I set the email tomsmith
    And I set the password SuperSecretPassword!
    Then Successful login
    And User redirected to Secure Area
