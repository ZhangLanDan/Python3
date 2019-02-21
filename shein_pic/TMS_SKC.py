import requests
import xlwings as xw


def skc(skc):
    cookies = {
        '_ga': 'GA1.2.229330571.1543376058',
        '_gid': 'GA1.2.1231692403.1550720822',
        'burypoint-sessionid-cookie': '11ce51e6-e7f1-4f50-bd4c-62574dd169bf',
        'PHPSESSID': 'quo67smvg6m6cirun2ssa1qec1',
        'SITE_ID': '9fd81843ad7f202f26c1a174c73575857b8eedd0',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://tmsus.dotfashion.cn/',
        'Connection': 'keep-alive',
        'If-Modified-Since': 'Thu, 21 Feb 2019 06:46:01 GMT',
    }

    params = (
        ('goods_sn', skc),
        ('page_index', '1'),
        ('per_page', '20'),
        ('language', 'zh'),
    )

    try:
        response = requests.get('http://tmsus.dotfashion.cn/index.php/Home/Goods/goodsInfoList', headers=headers, params=params, cookies=cookies)
        content = response.json()
        for i in content['info']['list']:
            
            tag = i['goods_tag']
            tms_skc = i['goods_sn']
            #全匹配
            if tms_skc == skc:
                print(f'{skc}@{tag}')
    except:
        pass

list1 = ['shorts180614291',
'shorts180615304',
'shorts180615701',
'shorts180620402',
'shorts180620405',
'shorts180622950',
'shorts180625163',
'shorts180625166',
'shorts180625373',
'shorts180625703',
'shorts180627704',
'shorts180704379',
'shorts180704383',
'shorts180704384',
'shorts180716162',
'shorts180717304',
'shorts180720403',
'shorts180720404',
'shorts180725408',
'shorts180808241',
'shorts180828701',
'shorts180912950',
'shortsmmc171226703',
'shotsmmc180523701',
'skirt160428001',
'skirt161010702',
'skirt170425702',
'skirt170501450',
'skirt170518704',
'skirt170524101',
'skirt170713701',
'skirt170801701',
'skirt171011450',
'skirt171016130',
'skirt171101130',
'skirt171109701',
'skirt171109703',
'skirt171229704',
'skirt180105330',
'skirt180108703',
'skirt180108704',
'skirt180116701',
'skirt180131203',
'skirt180309201',
'skirt180316031',
'skirt180316502',
'skirt180319030',
'skirt180327151',
'skirt180412051',
'skirt180418201',
'skirt180420201',
'skirt180423701',
'skirt180425900',
'skirt180425901',
'skirt180426701',
'skirt180427707',
'skirt180502082',
'skirt180504400',
'skirt180517704',
'skirt180523701',
'skirt180530302',
'skirt180601703',
'skirt180601704',
'skirt180604706',
'skirt180611703',
'skirt180614305',
'skirt180615703',
'skirt180615716',
'skirt180621950',
'skirt180622706',
'skirt180625302',
'skirt180625303',
'skirt180625411',
'skirt180629409',
'skirt180702705',
'skirt180710400',
'skirt180712402',
'skirt180716950',
'skirt180717705',
'skirt180719244']

for i in list1:
    skc(i)