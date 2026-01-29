from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.textarea import Textarea
from elements.input import Input


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title input')
        self.estimated_time_input = (
            Input(page, 'create-course-form-estimated-time-input', 'Estimated time input')
        )
        self.description_textarea = (
            Textarea(page, 'create-course-form-description-input', 'Description textarea')
        )
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score input')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str) -> None:
        self.title_input.fill(value=title)
        self.estimated_time_input.fill(value=estimated_time)
        self.description_textarea.fill(value=description)
        self.max_score_input.fill(value=max_score)
        self.min_score_input.fill(value=min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str) -> None:
        self.title_input.check_have_value(value=title)
        self.estimated_time_input.check_have_value(value=estimated_time)
        self.description_textarea.check_have_value(value=description)
        self.max_score_input.check_have_value(value=max_score)
        self.min_score_input.check_have_value(value=min_score)
