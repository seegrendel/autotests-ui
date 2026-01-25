import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_be_visible()
    expect(header_courses).to_have_text('Courses')

    empty_tittle = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_tittle).to_be_visible()
    expect(empty_tittle).to_have_text('There is no results')

    empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon).to_be_visible()

    empty_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description).to_be_visible()
    expect(empty_description).to_have_text('Results from the load test pipeline will be displayed here')
