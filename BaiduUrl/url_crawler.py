from fake_useragent import FakeUserAgent
import requests
from pyquery import PyQuery as pq
import PySimpleGUI as sg

ua = FakeUserAgent()
headers = {'user-agent':ua.random}

def crawl(url):
    if url:
        r = requests.get(url,headers=headers)
        doc = pq(r.text)
        for i in doc('div.result .t').items():
            print(i.text())
        href = doc('div#page a:last-child').attr('href')
        if href:
            next_ = 'https://www.baidu.com'+ href
        #print(next_)
        else:
            next_ = []
        return next_
def title_crawl(keyword):
    
    url = f'https://www.baidu.com/s?wd={keyword}'
    next_ = crawl(url)
    if next_:
        n = 1
        while n< 10:
            n += 1
            print(n)
            next_ = crawl(next_)
title_crawl('www.hu.com')

def gui():
    layout = [        
            [sg.Text('请输入提单号', size=(15, 1)),sg.RButton('运行'),sg.Button('退出')],
            [sg.Text('''(使用前请确保已登录TMS系统,卡了无响应就是查询中,有问题及时反馈)
          
目前支持：直飞：784,176,160,880
中转：176,180''')],
            [sg.Multiline(focus=True,size=(40,10),do_not_clear=True)],
            [sg.Text('结果：',size=(40,1))],
            [sg.Output(size=(88, 20))],   
            ]      
    window = sg.Window('爬取空运头程信息').Layout(layout)

    while True:
        event,value = window.Read()
        if event == '运行':
            list1 = content.split('\n')
            while '' in list1 :
                        list1.remove('')
            if value == ['\n']:
                pass
            else:
                for i in list1:
                    print(i)
        if event == '退出' or event is None:
            break
