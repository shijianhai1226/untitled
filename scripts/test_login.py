import sys
import os

sys.path.append(os.getcwd())
import pytest

from base.read_yaml import ReadYaml
from base.get_driver import get_driver
from page.page_login import PageLogin


def get_data():
    datas = ReadYaml('data_login.yaml').read_yaml()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("uesrname"), data.get("password")))
    return arrs


class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()

    def test_asd(self):
        print("132456")

    @pytest.mark.parametrize("username, password", get_data())
    def test_login(self, username, password):
        self.login.page_input_username(username)
        self.login.page_input_password(password)
        self.login.page_click_login_btn()


if __name__ == '__main__':
    pytest.main('-s')
