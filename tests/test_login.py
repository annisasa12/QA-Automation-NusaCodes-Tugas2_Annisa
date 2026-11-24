
from data.login_data import LOGIN_DATA
from pages.login_page import LoginPage


def test_login_positive(page):
    login = LoginPage(page)

    login.open()

    login.input_email(
        LOGIN_DATA["valid_email_valid_password"]["email"]
    )

    login.input_password(
        LOGIN_DATA["valid_email_valid_password"]["password"]
    )

    login.click_login()

    page.wait_for_timeout(3000)

    assert page.url != "https://nusacodes.com/login"


def test_login_negative_password_salah(page):
    login = LoginPage(page)

    login.open()

    login.input_email(
        LOGIN_DATA["valid_email_invalid_password"]["email"]
    )

    login.input_password(
        LOGIN_DATA["valid_email_invalid_password"]["password"]
    )

    login.click_login()

    page.wait_for_timeout(3000)

    assert page.url == "https://nusacodes.com/login"


def test_login_negative_email_salah(page):
    login = LoginPage(page)

    login.open()

    login.input_email(
        LOGIN_DATA["invalid_email_valid_password"]["email"]
    )

    login.input_password(
        LOGIN_DATA["invalid_email_valid_password"]["password"]
    )

    login.click_login()

    page.wait_for_timeout(3000)

    assert page.url == "https://nusacodes.com/login"


def test_login_negative_data_kosong(page):
    login = LoginPage(page)

    login.open()

    login.input_email(
        LOGIN_DATA["empty_email_empty_password"]["email"]
    )

    login.input_password(
        LOGIN_DATA["empty_email_empty_password"]["password"]
    )

    login.click_login()

    assert page.url == "https://nusacodes.com/login"
