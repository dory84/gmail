from pytest_bdd import given, when, then, scenarios, parsers
from pages.login_page import LoginPage
from pages.email_page import EmailPage
from playwright.sync_api import Page
import tests.test_login_steps as test_login_steps
from load_env import PASSWORD

scenarios('../features/send_email.feature')

@given(parsers.parse('user is logged in as user "{user}"'))
def login(page: Page, user):
    test_login_steps.open_login_page(page)
    test_login_steps.submit_valid_credentials(page, user)
    test_login_steps.verify_email_account_button_visible(page)
    email_page = EmailPage(page)
    email_page.delete_all_in_inbox()
    
@when(parsers.parse('the user send new message {"{recipient}", "{subject}", "{message}"}'))
def user_create_new_message(page: Page, recipient, subject, message):
    email_page = EmailPage(page)
    email_page.write_new_message(recipient, subject, message)

def go_to_email_page(page):
    login_page = LoginPage(page)
    login_page.goto_email()

@then(parsers.parse('the user should see that message count is "{count}"'))
def user_sees_email_sent_message(page: Page, count):
    email_page = EmailPage(page)	
    email_page.verify_inbox_count(int(count))
    
@when('the user clicks Logout button')
def click_logout_button(page: Page):
    email_page = EmailPage(page)
    email_page.click_email_label()
    email_page.click_logout_btn()
    
@then('the user should see sign in button')
def verify_sign_in_button(page: Page):
    emailPage = EmailPage(page)        
    emailPage.verify_sign_in_button()