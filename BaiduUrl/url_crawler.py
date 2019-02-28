import requests
from pyquery import PyQuery as pq
import os
import PySimpleGUI as sg


def get_stopwords():
    folder = os.path.exists('stop_words.txt')
    if not folder:
        with open('stop_words.txt','w+') as f:
            content = ''
    else:
        with open('stop_words.txt','r') as f:
            content = f.read()
            return content

def add_stopwords(new):
    folder = os.path.exists('stop_words.txt')
    if folder:
        with open('stop_words.txt','a',encoding='gbk') as f:
            f.write(new)
    else:
        with open('stop_words.txt','w+',encoding='gbk') as f:
            f.write(new)

def crawl(url,keyword,count=0):
    global all_info
    words = get_stopwords().split('\n')
    if url:
        try:
        
            r = requests.get(url,headers=headers)
            doc = pq(r.text)
            #整条搜索结果
            first =  doc('#content_left #1 .t').text()
            if first:
                title = first
            #第一条没有标题则选第二条
            else :
                title =  doc('#content_left #2 .t').text()
            check = ''
            for stop_word in words:
                if stop_word in title and stop_word!= '':
                    print('违规词',stop_word)
                    check = '违规'
                    break
            if check != '违规':
                check = '不违规'
                stop_word = ''
            count += 1
            #site = keyword.replace('site:','')
            title = title.replace(',',' ')
            keyword = keyword.replace('site:','')
            info = f'{title},{keyword},{check},{stop_word}\n'
            all_info += info
            print(info)
            next_ = []
            # href = doc('div#page a:last-child').attr('href')
            # if href:
            #     next_ = 'https://www.baidu.com'+ href
            # #print(next_)
            # else:
            #     next_ = []
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
    folder = os.path.exists('result.csv')
    if folder:
        with open("result.csv",'a',errors='ignore') as f:
            f.write(all_info)
    else:
        with open('result.csv','w+') as f:
            f.write('标题,域名,是否违规,违规词\n')
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
                n = 0
                for i in list1:
                    n += 1
                    i = f'site:{i}'
                    title_crawl(i)
                    sg.OneLineProgressMeter('进度条', n,len(list1),'key', 'Optional message')
                    
        if event == '添加规避词':
            list2 = value[1]
            new = list(set([i.strip() for i in list2.split('\n') if i.strip() != '']))
            if get_stopwords():
                old = get_stopwords().split('\n')
            else:
                old = []
            #去重

            add = '\n'.join([i for i in new if i not in old])
            if add:
                print('已添加规避词:',add.replace('\n',','))
                if old != []:
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
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36'}
    gui()
