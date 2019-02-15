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

list1 = ['RX864992711CN\n',
'RX864954846CN\n',
'RX864956351CN\n',
'RX864921128CN\n',
'RX881009401CN\n',
'RX881023505CN\n',
'RX864931394CN\n',
'RX864947363CN\n',
'RX881002350CN\n',
'RX864956095CN\n',
'RX881019528CN\n',
'RX864990392CN\n',
'RX864986150CN\n',
'RX864929395CN\n',
'RX864908299CN\n',
'RX864891655CN\n',
'RX864907041CN\n',
'RX864996404CN\n',
'RX864906925CN\n',
'RX864919827CN\n',
'RX864955869CN\n',
'RX864950036CN\n',
'RX864933126CN\n',
'RX881003372CN\n',
'RX864931712CN\n',
'RX864944044CN\n',
'RX864921074CN\n',
'RX864919190CN\n',
'RX881018187CN\n',
'RX864944115CN\n',
'RX864956334CN\n',
'RX881026529CN\n',
'RX881017116CN\n',
'RX881003443CN\n',
'RX881035525CN\n',
'RX864951867CN\n',
'RX864957184CN\n',
'RX864978272CN\n',
'RX864978493CN\n',
'RX864919209CN\n',
'RX864979998CN\n',
'RX864990389CN\n',
'RX881017473CN\n',
'RX864979539CN\n',
'RX881002584CN\n',
'RX864991075CN\n',
'RX881022558CN\n',
'RX864990962CN\n',
'RX864815124CN\n',
'RX864849026CN\n',
'RX864937352CN\n',
'RX881024001CN\n',
'RX864923849CN\n',
'RX864848873CN\n',
'RX864958587CN\n',
'RX864903963CN\n',
'RX864848895CN\n',
'RX864979499CN\n',
'RX864980130CN\n',
'RX864943066CN\n',
'RX864944132CN\n',
'RX864950314CN\n',
'RX864898968CN\n',
'RX864851872CN\n',
'RX864889833CN\n',
'RX864902469CN\n',
'RX864891545CN\n',
'RX864906219CN\n',
'RX864897021CN\n',
'RX864918486CN\n',
'RX864918526CN\n',
'RX864908705CN\n',
'RX864919230CN\n',
'RX864941272CN\n',
'RX864939296CN\n',
'RX864934838CN\n',
'RX864920618CN\n',
'RX864934121CN\n',
'RX864923089CN\n',
'RX864930601CN\n',
'RX864900701CN\n',
'RX881009446CN\n',
'RX864909042CN\n',
'RX864930589CN\n',
'RX864919813CN\n',
'RX864894970CN\n',
'RX864958613CN\n',
'RX864893197CN\n',
'RX864891253CN\n',
'RX864907126CN\n',
'RX864933086CN\n',
'RX864931332CN\n',
'RX864905071CN\n',
'RX881009755CN\n',
'RX881028025CN\n',
'RX864925819CN\n',
'RX864936683CN\n',
'RX881016019CN\n',
'RX864933395CN\n']
content =''
def get_info():
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    times = len(list1)//40
    n = 1
    #print('即将访问')
    #br = webdriver.Chrome(chrome_options=chrome_options)
    br = webdriver.Chrome()
    br.get('https://www.17track.net/zh-cn')
    #print('访问完成')
    wait = WebDriverWait(br,10)
    br.save_screenshot('a1.png')
    #点击同意
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.modal-footer .text-capitalize")))
    button = br.find_element_by_css_selector('div.modal-footer .text-capitalize')
    button.click()
    time.sleep(2)
    #点击以输入
    while n<= times +1:
        input_ = br.find_element_by_xpath("//*[@id='jsTrackBox']")
        input_.click()
        #复制单号
        shipping_no = br.find_element_by_xpath("//*[@id='jsTrackBox']/div[1]/div/div[1]/textarea")
        if n < times +1:
            numbers = ''.join(list1[(n-1)*40:n*40])
        else:
            numbers = ''.join(list1[(n-1)*40:])
        #粘贴单号
        
        pyperclip.copy(numbers)
        
        shipping_no.send_keys('Keys.CONTROL,"v"')
        #shipping_no.send_keys(numbers)
        
        #搜索
        button = br.find_element_by_xpath("//*[@id='yqiTrackBtn']")
        button.click()
        
        #跳过指引
        if n ==1:
            br.save_screenshot('搜索后.png')
            wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/div/div[5]/a[1]/i")))
            button = br.find_element_by_xpath("/html/body/div[5]/div/div[5]/a[1]/i")
            button.click()
        #复制结果
        time.sleep(0.5)
        br.save_screenshot('复制按钮前.png')
        br.find_element_by_xpath("//*[@id='jcPacakgeMenu']/div/button[1]").click()
        br.save_screenshot('复制按钮后.png')
        paste = pyperclip.paste()
        print(paste)
        br.back()
        n += 1
        time.sleep(2)
    
    else:
        br.quit()


get_info()
# print(content)
# get_info(1)
