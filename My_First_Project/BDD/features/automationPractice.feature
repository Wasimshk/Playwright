Feature: Automation Practice in Cucumber BDD
    An automation site where you can perform different operation

    Scenario: Succesful login with valid credentials
      Given user is on the login page
      When user enters valid username and password
      And clicks on the login button
      Then the user should be redirected to the dashboard

    Scenario Outline: Unsuccessful login with invalid credential
      Given user is on the login page
      When user enters invalid <username> or <password>
      And clicks on the login button
      Then user should see an error message
      Examples:
        | username     | password |
        | Wasim@g.com  | 1234@WS  |

    Scenario: Mouse hover
      Given User is on the automation practice page
      When the user hover the mouse to Mouse hover button
      Then drop down options appear
      And user click on the top option


  Scenario: handle alert box
      Given User is on the automation practice page
      When user click on the confirm button and accept dialog
      Then user cofirms the dialog is disappeared


