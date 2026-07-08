from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    username=('id','user-name')
    password=('id','password')
    button=('id','login-button')

    def user_name(self,values):
        self.send_keys(self.username,values)

    def pass_word(self,values):
        self.send_keys(self.password,values)

    def click_action(self):
        self.click(self.button)