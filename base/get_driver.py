from appium import webdriver


def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'emulator-5554'
    # app信息
    desired_caps['appPackage'] = 'com.vcooline.aike'
    desired_caps['appActivity'] = '.umanager.LoginActivity'
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 获取driver
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
