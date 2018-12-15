from base.base import Base
import page

class PageLogin(Base):
    def page_input_username(self, username):
        self.base_input(page.loc_username, username)

    def page_input_pwd(self, password):
        self.base_input(page.loc_pwd, password)

    def page_click_login_btn(self):
        self.base_click(page.loc_btn)

    # def page_login(self, username, password):
    #     self.page_input_username(username)
    #     self.page_input_password(password)
    #     self.page_click_login_btn()