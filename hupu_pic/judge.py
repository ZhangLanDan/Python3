import time
import os
from aip import AipFace
import base64


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

    """ 带参数调用人脸检测 """
    a = client.detect(image, imageType, options)
    try:
        list_ = a['result']['face_list']
        for i in list_:
            print(name,i['beauty'])
        time.sleep(1)
    except Exception as e:
        pass
        
names,base64_list = get_file_content('pic')
#名字，分数
for name,base64 in zip(names,base64_list):
    judge(name,base64)