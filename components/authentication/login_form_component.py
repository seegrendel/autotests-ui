from playwright.sync_api import Page, expect

from elements.input import Input
from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str) -> None:
        self.email_input.fill(value=email)
        self.password_input.fill(value=password)

    def check_visible(self, email: str, password: str) -> None:
        self.email_input.check_have_value(value=email)
        self.password_input.check_have_value(value=password)
