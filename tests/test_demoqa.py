from selene import browser, be, have
import os


def test_registration_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('Ivanna')
    browser.element('#lastName').should(be.blank).type('Ivanova')
    browser.element('#userEmail').should(be.blank).type('ivanova@gamail.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').should(be.blank).type('123456789100')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1990"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/p.jpg'))
    browser.element('#currentAddress').should(be.blank).type('16th Street')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.table-responsive').should(have.text(
        'Ivanna Ivanova' and
        'ivanova@gamail.com' and
        'Female' and
        '123456789100' and
        '01 April,1990' and
        'Reading' and
        'p.jpg' and
        '16th Street' and
        'NCR Delhi'))
