from fake_useragent import FakeUserAgent
import requests
from pyquery import PyQuery as pq
import PySimpleGUI as sg
import os


def get_stopwords():
    with open('stop_words.txt','r') as f:
        content = f.read()
        return content

def add_stopwords(new):
    with open('stop_words.txt','a') as f:
        f.write(new)

def crawl(url,keyword,count=0):
    global all_info
    words = get_stopwords().split('\n')
    if url:
        try:
        
            r = requests.get(url,headers=headers)
            doc = pq(r.text)
            for i in doc('div.result .t').items():
                check = ''
                title = i.text()
                for i in words:
                    if i in title:
                        print('违规词',i)
                        check = '违规'
                        break
                if check != '违规':
                    check = '不违规'
                count += 1
                site = keyword.replace('site:','')
                info = f'{count},{title},{site},{check}\n'
                all_info += info
                print(info)

            href = doc('div#page a:last-child').attr('href')
            if href:
                next_ = 'https://www.baidu.com'+ href
            #print(next_)
            else:
                next_ = []
            return next_,count
        except Exception as e:
            print(e)
            pass
        
            
def title_crawl(keyword):
    
    url = f'https://www.baidu.com/s?wd={keyword}'
    try:
        next_,count = crawl(url,keyword)
        if next_:
            n = 1
            while n< 10:
                n += 1
                if next_:
                
                    next_,count = crawl(next_,keyword,count)
    except:
        pass

def to_csv(all_info):
    with open("result.csv",'a') as f:
        f.write(all_info)
def gui():
    global all_info
    sg.SetOptions(background_color='#9FB8AD',      
           text_element_background_color='#9FB8AD',      
           element_background_color='#9FB8AD',      
           scrollbar_color=None,      
           #input_elements_background_color='#F7F3EC',      
           progress_meter_color = ('green', 'blue') ,     
           button_color=('white','#475841'))
    layout = [        
            #[sg.Text('', size=(15, 1))
            [sg.Text('左侧输入网址，右侧添加规避词'),sg.RButton('开始抓取')],
            [sg.Multiline(focus=True,size=(40,15),do_not_clear=True),sg.RButton('添加规避词'),sg.Multiline(focus=False,size=(20,15),do_not_clear=True)],
            [sg.RButton('导出CSV'),sg.Text('结果：',size=(20,1))],
            [sg.Output(size=(77, 20))],   
            ]      
    window = sg.Window('114link',font=('Any 11')).Layout(layout)

    while True:

        event,value = window.Read()
        if event == '开始抓取':
            
            list1 = value[0].split('\n')
            list1 = [i.strip() for i in list1 if i.strip()!='']
            # print(list1)
            if list1:
                for i in list1:
                    i = f'site:{i}'
                    title_crawl(i)
        if event == '添加规避词':
            list2 = value[1]
            new = list(set([i.strip() for i in list2.split('\n') if i.strip() != '']))
            old = get_stopwords().split('\n')
            #去重

            add = '\n'.join([i for i in new if i not in old])
            if add:
                print('已添加规避词:',add.replace('\n',','))
                if old != ['']:
                    add_stopwords('\n')
                
                add_stopwords(add)
                words = get_stopwords()
                print('现有规避词',words.replace('\n',','))
            else:
                print('无新增规避词')

        if event == '导出CSV':
            to_csv(all_info)
            print(f'已导出至{os.getcwd()}\\result.csv')
        if event is None:
            break
if __name__ == '__main__':
    all_info = ''
    ua = FakeUserAgent()
    headers = {'user-agent':ua.random}
    gui() 

