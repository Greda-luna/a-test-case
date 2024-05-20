import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from 新的文件.lib.WebUI_SMP import smp_UI
from 新的文件.SMP_URL import *
smp = smp_UI()

@pytest.fixture(scope='module')
def inService():
    smp.login('byhy',"sdfsdf")
    time.sleep(2)
    smp.browser.get(rule_url)
    return

@pytest.mark.parametrize('devicename,devicetype,minfee,expfee,desc,feerate',[
    ('第一个设备名称','预付费-下发费用',100,200,'第一个设备描述',None),
    ('第二个设备名称','预付费-下发业务量',200,300,'第二个设备描述',['千克','2']),
    ('第三个设备名称','后付费-上报业务量',None,None,'第三个设备描述',[
        ['1','厘米','1'],
        ['2','分米','2']
    ])
])
def test_device(inService,devicename,devicetype,minfee,expfee,desc,feerate):
    btn = smp.browser.find_element(By.CSS_SELECTOR,'.add-one-area .btn')
    if btn.text == '添加':
        btn.click()
        time.sleep(1)
    smp.devicemodel(devicename,devicetype,minfee,expfee,desc,feerate)
    time.sleep(3)
