import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome title')

    def check_visible(self, username: str):
        with allure.step('Check title visible and have text: UI Course'):
            self.app_title.check_visible()
            self.app_title.check_have_text(text='UI Course')

        with allure.step(f'Check title visible and have text: Welcome, {username}!'):
            self.welcome_title.check_visible()
            self.welcome_title.check_have_text(text=f'Welcome, {username}!')
