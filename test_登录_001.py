import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from 新的文件.lib.WebUI_SMP import smp_UI
from 新的文件.SMP_URL import *
smp = smp_UI()
#登录成功
def test_login_success():
    smp.login('byhy','sdfsdf')
    time.sleep(1)
    nav = smp.browser.find_element(By.ID, 'top-right')
    assert nav != []


#登录失败有很多种情况，要和成功的分开写
#每次失败会有一个弹窗，需要转到弹窗那里点确定关掉，下面这个的作用是初始化
@pytest.fixture
def ClearAlert():
    yield
    try:
        smp.browser.switch_to.alert.accept()
    except Exception as e:
        print(e)
@pytest.mark.parametrize('username,password,expectedalert',[
    ('byhy','sgdhsd','登录失败： 用户名或者密码错误'),
    ('asdad','sgdhsd','登录失败： 用户名不存在'),
    (None,'sgdhsd','请输入用户名'),
    ('byhy', None, '请输入密码')
]
                         )
def test_login_fail(username,password,expectedalert,ClearAlert):
    smp.login(username,password)
    time.sleep(1)
    alert = smp.browser.switch_to.alert
    assert alert.text == expectedalert