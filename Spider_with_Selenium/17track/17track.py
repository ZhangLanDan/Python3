from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pyperclip
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlwings as xw


wb = xw.Book('a.xlsx')
sht = wb.sheets[0]
values = sht.range('a2:a84').options(transpose=True).value
total = [i+'\n' for i in values if i!= None]


def get_info():
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    times = len(total)//40
    n = 1
    #print('即将访问')
    #br = webdriver.Chrome(chrome_options=chrome_options)
    br = webdriver.Chrome()
    br.get('https://www.17track.net/zh-cn')
    #print('访问完成')
    wait = WebDriverWait(br,10)
    #点击同意
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='modal-gdpr']/div/div/div[3]/button")))
    button = br.find_element_by_xpath("//*[@id='modal-gdpr']/div/div/div[3]/button")
    button.click()
    time.sleep(2)
    #点击以输入
    while n<= times +1:
        input_ = br.find_element_by_xpath("//*[@id='jsTrackBox']")
        input_.click()
        #复制单号
        shipping_no = br.find_element_by_xpath("//*[@id='jsTrackBox']/div[1]/div/div[1]/textarea")
        if n < times +1:
            numbers = ''.join(total[(n-1)*40:n*40])
        else:
            numbers = ''.join(total[(n-1)*40:])
        #粘贴单号
        
        pyperclip.copy(numbers)
        
        shipping_no.send_keys(Keys.CONTROL,"v")
        #shipping_no.send_keys(numbers)
        
        #搜索
        button = br.find_element_by_xpath("//*[@id='yqiTrackBtn']")
        button.click()
        
        #跳过指引
        if n ==1:
            
            wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/div/div[5]/a[1]/i")))
            button = br.find_element_by_xpath("/html/body/div[5]/div/div[5]/a[1]/i")
            button.click()
        #复制结果
        time.sleep(3)
        br.find_element_by_xpath("//*[@id='jcPacakgeMenu']/div/button[1]").click()
        paste = pyperclip.paste()
        print(paste.replace('\n',''))
        br.back()
        n += 1
        time.sleep(2)
    
    else:
        br.quit()


get_info()
