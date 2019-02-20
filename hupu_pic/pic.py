import requests
from pyquery import PyQuery as pq
import re 
from fake_useragent import UserAgent
import os
import time
from aip import AipFace
import base64
import shutil
#爆照帖子url
def post_links(url):
    baseurl = f'https://bbs.hupu.com'
    r = requests.get(url)
    doc = pq(r.text)    
    links = []
    for i in doc('a.truetit').items():
        links.append(baseurl+i.attr('href'))
    
    return links
#找最后一个指定字符的位置
def find_last(string,str_):
    last_position=-1
    while True:
        position=string.find(str_,last_position+1)
        if position==-1:
            return last_position
        last_position=position


def get_images(url):
    r = requests.get(url)
    doc = pq(r.text)
    #替换特殊字符
    title = doc('div.subhead span').text().replace('，','').replace(r"'","").replace(',','').replace(':','').replace('/','')

    #imgs = doc('div.floor img')
    imgs = []
    imgs += [i.attr('src') for i in doc('div.quote-content img').items()]
    img_links = []
    pattern = re.compile('https://.*?.jpg',re.S)
    for i in imgs:
        try:
            img_link = pattern.findall(i)[0]
            img_links.append(img_link)
        except:
            continue
    
    n = 0
    try:
        #os.mkdir(title)

        for i in img_links:
            n+= 1
            suffix = i[find_last(i,'.'):]
            name = f'{title}-{n}{suffix}'   
            with open(f'pic/{name}','wb') as f:
                f.write(requests.get(i).content)
        if n == 0:
            #os.rmdir(title) 
            print(f'没有抓到照片')
        else:
            print(f'成功抓取{n}张照片')
        
    except Exception as e: 
        print(e)
        pass

def crawl_pic(page):
    ua = UserAgent()
    headers = {'user-agent':ua.random}
    for n in range(page):
        url = f'https://bbs.hupu.com/selfie-{n}'
        urls = post_links(url)
        for i in urls:
            print(f'正在抓取:{i}')
            get_images(i)

    
APP_ID = '15529236'
API_KEY = 'RA8xVgzORetzU6q1tZS2RHtW'
SECRET_KEY = 'xlB9mdeXSDdvqQY1z8jycwxAeCRLSa6u'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(dirname):
    #图片路径
    path = os.getcwd()
    files = os.listdir(dirname)
    names = [i for i in files]
    imgs = [f'{path}\\pic\\{i}' for i in names]
    #转base64
    base64_list = []
    for img in imgs:
        with open(img, 'rb') as fp:
            content = base64.b64encode(fp.read())
            b64 = content.decode('utf-8')
            base64_list.append(b64)
    return names,base64_list



def judge(name,image):
    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,gender,beauty"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"
    global total
    global n
    """ 带参数调用人脸检测 """
    a = client.detect(image, imageType, options)
    time.sleep(1)
    try:
        result = a['result']
        if result:
            for i in result['face_list']:
                total += 1
                mark = i['beauty'] 
                print(f'{total}张照片已打分,共出现{n}个高分小姐姐/小哥哥 {mark}分')
                if mark > 70:
                    n += 1
                    print(name,mark)
                    shutil.move(rf'C:\Users\Administrator\Desktop\hupu_pic\pic\{name}',rf'C:\Users\Administrator\Desktop\hupu_pic\70+\{mark}{name}')
                
    except Exception as e:
        print(e)
        pass
#crawl_pic(3)
names,base64_list = get_file_content('pic')
#名字，分数
try:
        os.mkdir('70+')
except:
    pass
#总共
total = 0
#高分
n = 0
for name,base64 in zip(names,base64_list):
    judge(name,base64)