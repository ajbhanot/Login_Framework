from pages.LoginPage import LoginPage

def test_login(setup):
    driver = setup

    login = LoginPage(driver)

    login.user_name("standard_user")
    login.pass_word("secret_sauce")
    login.click_action()