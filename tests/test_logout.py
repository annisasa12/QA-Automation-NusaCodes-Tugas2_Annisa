from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from data.login_data import LOGIN_DATA


def test_logout_positive(page):
    login = LoginPage(page)
    logout = LogoutPage(page)

    # 1. Login dulu dengan akun valid
    login.open()
    login.input_email(LOGIN_DATA["valid_email_valid_password"]["email"])
    login.input_password(LOGIN_DATA["valid_email_valid_password"]["password"])
    login.click_login()

    # Pastikan sudah masuk ke halaman member sebelum klik logout
    expect(page).to_have_url("https://nusacodes.com/member/kelas")

    # 2. Klik tombol logout
    logout.click_logout()

    # 3. Pastikan sudah keluar dan kembali ke halaman login
    expect(page).to_have_url("https://nusacodes.com/login")


def test_logout_negative_belum_login(page):
    # Coba akses halaman member langsung tanpa login
    page.goto(
        "https://nusacodes.com/member/kelas",
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Pastikan sistem menolak dan mengarahkan balik ke halaman login
    expect(page).to_have_url("https://nusacodes.com/login")