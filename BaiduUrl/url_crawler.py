from fake_useragent import FakeUserAgent
import requests
from pyquery import PyQuery as pq
import PySimpleGUI as sg

ua = FakeUserAgent()
headers = {'user-agent':ua.random}

def crawl(url,keyword):
    if url:
        r = requests.get(url,headers=headers)
        doc = pq(r.text)
        count = 0
        for i in doc('div.result .t').items():
            count += 1
            print([count,i.text(),keyword])
        href = doc('div#page a:last-child').attr('href')
        if href:
            next_ = 'https://www.baidu.com'+ href
        #print(next_)
        else:
            next_ = []
        return next_
def title_crawl(keyword):
    
    url = f'https://www.baidu.com/s?wd={keyword}'
    next_ = crawl(url,keyword)
    if next_:
        n = 1
        while n< 10:
            n += 1
            next_ = crawl(next_,keyword)

# str_ = input('输入网站,quit结束\n')
# total = [str_]
# while True:
#     str_ = input()
#     if str_ != 'quit':
#         total.append(str_)

#     else:
#         break
# for i in total:
#     title_crawl(i)
#title_crawl('www.hu.com')

def gui():
    layout = [        
            [sg.Text('请输入网址', size=(15, 1)),sg.RButton('运行'),sg.Button('退出')],
            [sg.Text('留着写说明')],
            [sg.Multiline(focus=True,size=(40,10),do_not_clear=True)],
            [sg.Text('结果：',size=(40,1))],
            [sg.Output(size=(88, 20))],   
            ]      
    window = sg.Window('爬取空运头程信息').Layout(layout)

    while True:
        event,value = window.Read()
        if event == '运行':
            list1 = value[0].split('\n')
            for i in list1:
                title_crawl(i)
        if event == '退出' or event is None:
            break
if __name__ == '__main__':
    gui() 