from selene import browser, have, be
from pathlib import Path
from tests import resources



def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.main-header').should(have.text('Practice Form'))
    browser.element('#firstName').should(be.blank).type('Test')
    browser.element('#lastName').should(be.blank).type('Test')
    browser.element('#userEmail').should(be.blank).type('Test@test.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('8999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().type('November').click()
    browser.element('.react-datepicker__year-select').click().type('1991').click()
    browser.element('.react-datepicker__day--011').click()
    browser.element("#subjectsInput").set_value('Chemistry').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').set_value(
        str(Path(resources.__file__).joinpath('resources/python_lesson_5.png').absolute()))

    browser.element('#currentAddress').type('Test,Test,13')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))


    browser.element('.table').all('td').should(
    have.texts(
        ('Student Name', 'Test Test'),
        ('Student Email', 'Test@test.com'),
        ('Gender', 'Male'),
        ('Mobile', '8999999999'),
        ('Date of Birth', '11 November,1991'),
        ('Subjects', 'Chemistry'),
        ('Hobbies', 'Sports'),
        ('Picture', 'python_lesson_5.png'),
        ('Address', 'Test,Test,13'),
        ('State and City', 'NCR Delhi'),
    )
)
browser.element('#closeLargeModal').press_enter()
