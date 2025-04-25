from pytest_bdd import given, when, then, scenarios, parsers
from pages.login_page import LoginPage
from pages.email_page import EmailPage
from playwright.sync_api import Page
from load_env import PASSWORD

scenarios('../features/login.feature')

# Step definitions
@given("the user is on the login page")
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

@when(parsers.parse('the user enters user "{user}" and password "{password}"'))
def submit_credentials(page: Page, user, password):
    login_page = LoginPage(page)
    login_page.fill_and_submit_credentials(user, password)
    
@when(parsers.parse('the user enters user "{user}" and secret password'))
def submit_valid_credentials(page: Page, user):
    login_page = LoginPage(page)
    login_page.fill_and_submit_credentials(user, PASSWORD)


@when('the user clicks the Next button')
def click_login_button(page: Page):
    login_page = LoginPage(page)
    login_page.click_login_btn()

@then('the user should see email account button')
def verify_email_account_button_visible(page: Page):
    email_page = EmailPage(page)
    email_page.verify_email_account_button()

@then('the user should see a password input')
def verify_error_message(page: Page):
    print("User can see an error message")
    login_page = LoginPage(page)
    login_page.verify_password_input()
    
@when('the user clicks Logout button')
def click_logout_button(page: Page):
    email_page = EmailPage(page)
    email_page.click_email_label()
    email_page.click_logout_btn()
    
@then('the user should see sign in button')
def verify_sign_in_button(page: Page):
    emailPage = EmailPage(page)        
    emailPage.verify_sign_in_button()
