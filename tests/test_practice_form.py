from selene import browser, have, be
import os.path


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.main-header').should(have.text('Practice Form'))
    browser.element('#firstName').should(be.blank).type('Test')
    browser.element('#lastName').should(be.blank).type('Test')
    browser.element('#userEmail').should(be.blank).type('Test@test.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('89999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().type('November').click()
    browser.element('.react-datepicker__year-select').click().type('1991').click()
    browser.element('.react-datepicker__day--011').click()
    browser.element("#subjectsInput").set_value('Chemistry').press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    #   browser.driver.save_screenshot('./python_lesson_5.png')
    browser.element('#uploadPicture').send_keys(
        os.path.abspath('screenshot/python_lesson_5.png')
    )
    browser.element('#currentAddress').type('Test, Test, 13')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all("tbody tr td:last-child").should(
        have.exact_texts(
            'Test Test'
            'Test@test.com'
            'Male'
            '89999999999'
            '11 November,1991'
            'Chemistry'
            'Sports'
            'python_lesson_5.png'
            'Test,Test,13'
            'NCR Delhi'
        )
    )

    browser.element('#closeLargeModal').press_enter()
