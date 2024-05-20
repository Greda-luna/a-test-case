import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from 新的文件.SMP_URL import *
class smp_UI():
    def __init__(self):
        path = Service('F:\python_exercise\比赛练习\chromedriver.exe')
        self.browser = webdriver.Chrome(service=path)

    def login(self,username,password):
        self.browser.get(login_url)
        if username is not None:
            self.browser.find_element(By.ID,'username').send_keys(username)
        if password is not None:
            self.browser.find_element(By.ID,'password').send_keys(password)
        time.sleep(1)
        self.browser.find_element(By.ID,'loginBtn').click()

    def devicemodel(self,devicename,devicetype,minfee,expfee,desc,fee_rate):
        #输入设备名称
        name_ele = self.browser.find_element(By.CSS_SELECTOR,'.add-one-form .field > input')
        name_ele.clear()
        name_ele.send_keys(devicename)
        #选择设备类型
        type_ele= Select(self.browser.find_element(By.CSS_SELECTOR,'.add-one-form #rule_type_id'))
        type_ele.select_by_visible_text(devicetype)
        time.sleep(2)
        #由于选择不同的设备类型页面会发生更改，所以每个都要单独写。
        if devicetype == '预付费-下发业务量':
            min_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(3) > input[type=number]')
            min_ele.clear()
            min_ele.send_keys(minfee)
            exp_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(4) > input[type=number]')
            exp_ele.clear()
            exp_ele.send_keys(expfee)
            unit = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div.fee-rate-list > div > input[type=text]:nth-child(2)')
            unit.clear()
            unit.send_keys(fee_rate[0])
            u_fee = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div.fee-rate-list > div > input[type=number]:nth-child(4)')
            u_fee.clear()
            u_fee.send_keys(fee_rate[1])
            desc_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(6) > input')
            desc_ele.clear()
            desc_ele.send_keys(desc)
            time.sleep(2)
        if devicetype == '预付费-下发费用':
            min_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(3) > input[type=number]')
            min_ele.clear()
            min_ele.send_keys(minfee)
            exp_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(4) > input[type=number]')
            exp_ele.clear()
            exp_ele.send_keys(expfee)
            desc_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(5) > input')
            desc_ele.clear()
            desc_ele.send_keys(desc)
            time.sleep(2)
        if devicetype == '后付费-上报业务量':
            all = len(fee_rate)
            i = 1
            for rate in fee_rate:
                service_code = self.browser.find_element(By.CSS_SELECTOR,'.fee-rate-list .fee-rate:nth-of-type'+'('+str(i)+')'+ '>input')
                service_code.clear()
                service_code.send_keys(rate[0])
                unit = self.browser.find_element(By.CSS_SELECTOR,'.fee-rate-list .fee-rate:nth-of-type'+'('+str(i)+')'+ '>input:nth-of-type(2)')
                unit.clear()
                unit.send_keys(rate[1])
                u_fee = self.browser.find_element(By.CSS_SELECTOR,'.fee-rate-list .fee-rate:nth-of-type'+'('+str(i)+')'+ '>input:nth-of-type(3)')
                u_fee.clear()
                u_fee.send_keys(rate[2])
                if i == all:
                    break
                add_rate = self.browser.find_element(By.CSS_SELECTOR,'.fee-rate-list >div:nth-of-type('+str(i+1)+') >button')
                add_rate.click()
                i += 1
            desc_ele = self.browser.find_element(By.CSS_SELECTOR,'body > main > div.add-one-area > div > div:nth-child(4) > input')
            desc_ele.clear()
            desc_ele.send_keys(desc)
            time.sleep(2)
        btn = self.browser.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div .btn')
        btn.click()







