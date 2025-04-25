from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[type='email']")
        self.submit_identifier = page.locator("[id='identifierNext']")
        self.password_input = page.locator("[type='password']")
        self.submit_password = page.locator("[id='passwordNext']")

    def navigate(self):
        self.page.goto("https://mail.google.com/mail/u/0/#inbox")

    def fill_and_submit_credentials(self, user_name, password):
        self.username_input.fill(user_name)
        self.submit_identifier.click()
        self.password_input.fill(password)
        self.submit_password.click()


    def click_login_btn(self):
        self.submit_password.click()
        
    def verify_password_input(self):
        expect(self.password_input).to_be_visible()
                
    def goto_email(self):
        self.email_label.click()