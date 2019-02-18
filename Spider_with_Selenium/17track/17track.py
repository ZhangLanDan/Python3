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
values = sht.range('a85:a167').options(transpose=True).value

total = ['3A5V483604539',
'CNELA0000029008YQ',
'CNELA0000028216YQ',
'CNELA0000027701YQ',
'3A5V483573912',
'CNELA0000027892YQ',
'CNELA0000024749YQ',
'CNELA0000028175YQ',
'CNELA0000027442YQ',
'CNELA0000026391YQ',
'CNELA0000024262YQ',
'3A5V483657568',
'CNELA0000028020YQ',
'CNELA0000028707YQ',
'CNELA0000028525YQ',
'CNELA0000028416YQ',
'CNELA0000027674YQ',
'CNELA0000028052YQ',
'CNELA0000028557YQ',
'3A5V483621171',
'CNELA0000028848YQ',
'CNELA0000024230YQ',
'CNELA0000028098YQ',
'3A5V483573275',
'3A5V483759616',
'CNELA0000024644YQ',
'3A5V483666380',
'CNELA0000024826YQ',
'3A5V483621973',
'CNELA0000027583YQ',
'3A5V483121027',
'CNELA0000028343YQ',
'CNELA0000024367YQ',
'CNELA0000026341YQ',
'CNELA0000001806YQ',
'3A5V483759645',
'CNELA0000022024YQ',
'CNELA0000024935YQ',
'3A5V483440949',
'CNELA0000026137YQ',
'CNELA0000027929YQ',
'CNELA0000029212YQ',
'CNELA0000028666YQ',
'CNELA0000028593YQ',
'CNELA0000028193YQ',
'CNELA0000029208YQ',
'3A5V483572806',
'CNELA0000024767YQ',
'3A5V483271309',
'3A5V483572969',
'CNELA0000024494YQ',
'CNELA0000029244YQ',
'CNELA0000029585YQ',
'CNELA0000023002YQ',
'3A5V483609153',
'CNELA0000027642YQ',
'3A5V483573189',
'3A5V483609114',
'3A5V483609208',
'3A5V483594546',
'3A5V483609258',
'3A5V483609206',
'CNELA0000024408YQ',
'3A5V483715531',
'CNELA0000024476YQ',
'3A5V483573201',
'CNELA0000026482YQ',
'3A5V483609118',
'3A5V483560669',
'3A5V483609220',
'3A5V483609201',
'3A5V483609116',
'3A5V483609142',
'3A5V483573183',
'3A5V483571709',
'3A5V483572850',
'CNELA0000027424YQ',
'CNELA0000024599YQ',
'CNELA0000026155YQ',
'3A5V483573179',
'3A5V483609127',
'CNELA0000024703YQ',
'CNELA0000026496YQ']

total = [i +'\n' for i in total]


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
        if n ==2:
            
            wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/div/div[5]/a[1]/i")))
            button = br.find_element_by_xpath("/html/body/div[5]/div/div[5]/a[1]/i")
            button.click()
        #复制结果
        time.sleep(8)
        br.find_element_by_xpath("//*[@id='jcPacakgeMenu']/div/button[1]").click()
        paste = pyperclip.paste()
        print(paste.replace('\n',''))
        br.back()
        n += 1
        time.sleep(2)
    
    else:
        br.quit()


get_info()
