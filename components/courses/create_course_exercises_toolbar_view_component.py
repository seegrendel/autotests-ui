import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(
            page,
            'create-course-exercises-box-toolbar-create-exercise-button',
            'Create exercise button'
        )

    @allure.step('Check visible title text "Exercises"')
    def check_visible(self) -> None:
        self.create_exercise_button.check_visible()
        self.title.check_visible()
        self.title.check_have_text(text='Exercises')

    def click_create_exercise_button(self) -> None:
        self.create_exercise_button.click()
