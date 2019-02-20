import os
import requests
import base64
import requests

def judge(img):
    headers = {'content-type':'application/json'}
    url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = {"access_token":"24.e713df2e8ea7c32e002a974dff8afe72.2592000.1552461447.282335-15529236"}
    payload = f"image_type=BASE64&image={img}&face_field=beauty"
    response = requests.post(url, data=payload, params=params)
    print(response.json())
    # print(response.json()['result']['face_list'])


pics = os.listdir('pic')
# for i in pics:
#     img = fr'C:\Users\SI-GZ-1314\OneDrive - business\YR\home\hupu\pic\{i}'
    
#     with open(img,'rb') as f:
#         base64_ = base64.b64encode(f.read())
#         base64_ = str(base64_,'utf-8')
#         print(img)
#         print(base64_)
#     try:
#         judge(base64_)
#     except Exception as e:
#         print(e)
#     break