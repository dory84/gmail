Feature: User Login

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters user "iamdory84" and secret password
    Then the user should see email account button
    When the user clicks Logout button
    Then the user should see sign in button 

Scenario: Login with invalid credentials
    Given the user is on the login page
    When the user enters user "iamdory84" and password "invalid_password"
    Then the user should see a password input
