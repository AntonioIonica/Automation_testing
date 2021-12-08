Feature: Login page
  As an admin
  I want to login
  So that I have full access to full operations

  Scenario Outline: Trying many credentials on login
    Given I open the website
    When I enter the input "<user>" and "<password>"
    And I click on login
    Then Display "<login_status>"
    Examples:
      | user     | password             | login_status |
      | tomsmith | SuperSecretPassword! | Success      |
      | user2    | password2            | Not_success  |
      | user3    | password3            | Not_success  |

    # TODO to parse test.json file and generate a xls file