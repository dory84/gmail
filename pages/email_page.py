from playwright.sync_api import Page,expect

class EmailPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.email_account_button = page.get_by_role("button", name="Google Account: Petronela (")
        self.compose_message_button = page.get_by_role("button", name="Compose")
        self.recipient = page.get_by_role("combobox", name="To recipients")
        self.subject = page.get_by_role("textbox", name="Subject")
        self.message = page.get_by_role("textbox", name="Message Body")
        self.send_message = page.get_by_label("Send ‪(Ctrl-Enter)‬")
        self.logout_button = page.locator("iframe[name=\"account\"]").content_frame.get_by_role("link", name="Sign out")
        self.sign_in_button = page.get_by_role("link", name="Sign in")
        self.sent = page.get_by_role("link", name="Sent")
        self.inbox = page.get_by_role("link", name="Inbox")
        self.select_all = page.get_by_role("button", name="Select", exact=True).get_by_role("checkbox")
        self.delete = page.get_by_role("button", name="Delete")

    def write_message_click(self):
        self.compose_message_button.click()
        
    def enter_recipient(self, recipient):
        self.recipient.fill(recipient)
        
    def enter_subject(self, subject):
        self.subject.fill(subject)
        
    def enter_message(self, message):
        self.message.fill(message)

        
    def click_send_message(self):
        self.send_message.click()
        
        
    def verify_email_account_button(self):
        self.page.wait_for_load_state('domcontentloaded')
        expect(self.email_account_button).to_be_visible()
        
    def click_email_label(self):
        self.email_account_button.click()
        
    def click_logout_btn(self):
        self.logout_button.click()
        
    def verify_sign_in_button(self):
        expect(self.sign_in_button).to_be_visible()
        
    def delete_all_in_inbox(self):
        self.inbox.click()
        self.select_all.click()
        if self.delete.is_visible():
            self.delete.click()
            
    def verify_inbox_count(self, expected_count):
        self.page.wait_for_load_state('domcontentloaded')
        count = int(self.page.get_by_role("row").count())-1
        assert count == expected_count
        
    def write_new_message(self, recipient, subject, message):
        self.write_message_click()
        self.enter_recipient(recipient)
        self.enter_subject(subject)
        self.enter_message(message)
        self.click_send_message()

