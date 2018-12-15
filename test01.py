import allure
import pytest


class Test01():
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("测试步骤")
    def test01(self):
        allure.attach("123", "456")
        print("123456")
    def test02(self):
        print(123456)
    def test03(self):
        print("789456")
