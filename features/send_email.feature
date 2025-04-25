Feature: User Send Email

Scenario: User successfully send email
    Given user is logged in as user "iamdory84"
    When the user send new message {"iamdory84@gmail.com", "subject", "message"}
    Then the user should see that message count is "1"
    When the user clicks Logout button
    Then the user should see sign in button 