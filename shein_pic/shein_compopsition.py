import requests
from pyquery import PyQuery as pq
# import xlwings as xw


def get_good(skc):
    headers = {
        'authority': 'www.shein.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer': 'https://www.shein.com/pdsearch/blouse170925106/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__zlcmid=pahp4ytSZRlvqx; _ga=GA1.2.1663756489.1543799883; scarab.visitor=%2275D3B93C32B2CB8C%22; optimizelyEndUserId=oeu1543799886037r0.9113552334105071; keepPrivacy=1; have_show=1; ry_ry-sh31nfid_realytics=eyJpZCI6InJ5XzIxMDA0QTJELTJCQzUtNDk5Qy1CMzkyLTNGNjNDRTE3RjQ4NyIsImNpZCI6bnVsbCwiZXhwIjoxNTc1MzM1OTA1OTg1fQ%3D%3D; cookieId=E8438499_A23E_3A74_69FE_7E5AD239F427; cto_lwid=97e89b2d-7f01-4471-8edc-a86778ae512c; RES_TRACKINGID=363295612092603; ResonanceSegment=1; cate_active_name=0; default_currency=USD; _gid=GA1.2.1188141488.1550733140; sessionID_shein=s%3Aje6wEH7H8O6yzC6N2o0lIZSBknJSANEn.cdz0N3iAsbG9vqFByJ0OmbauglSWjrnoWOl%2FRNgOXs0; country=CN; countryId=; _fbp=fb.1.1550733261627.235506265; G_ENABLED_IDPS=google; showInch=0; scarab.profile=%22527277%7C1550733289%22; scarab.mayAdd=%5B%7B%22i%22%3A%22527277%22%7D%2C%7B%22i%22%3A%22414371%22%7D%2C%7B%22i%22%3A%22557000%22%7D%2C%7B%22i%22%3A%22390542%22%7D%2C%7B%22i%22%3A%22383793%22%7D%5D; country_tag_outdated=China; hideCoupon=1; chat_dept=OTHERS; pt_s_79a25132=vt=1550733926007&cad=; abt-info=shein_pc_wishlist_RecommendationsForYou~106~311%7CshPcNewin~190~842%7Cshein_pc_category_RecommendationsForYou~289~1443%7Cshein_pc_product_detail_CustomersAlsoViewed~77~947; __atuvc=7%7C8; __atuvs=5c6e4feac8aa208d006; pt_79a25132=uid=NW0IPElVwTsleEdExG5/pg&nid=0&vid=Ho8RGiPN1AJp-zvdBjVG3A&vn=10&pvn=24&sact=1550733938770&to_flag=0&pl=LPC/0ug5uOErXSYjsNCQ1g*pt*1550733890037; RT="sl=24&ss=1550733139331&tt=140341&obo=1&bcn=%2F%2F36fb78dc.akstat.io%2F&sh=1550733929671%3D24%3A1%3A140341%2C1550733892574%3D23%3A1%3A134620%2C1550733421492%3D22%3A1%3A128784%2C1550733416297%3D21%3A1%3A121912%2C1550733384657%3D20%3A1%3A117634&dm=shein.com&si=2aa34fc2-e475-4383-89e7-31e2f8f524fd&ld=1550733929672&r=https%3A%2F%2Fwww.shein.com%2Fpdsearch%2Fblouse170925106%2F&ul=1550733938848"',
    }

    r = requests.get(f'https://www.shein.com/pdsearch/{skc}/', headers=headers)
    doc =pq(r.text)
    title = doc('.header-title').text()
    if title:
        url = doc('.c-goodsli-absolute .gds-li-ratiowrap a').attr('href')
        return url
    else:
        return ''

def get_info(skc):
    url = get_good(skc)
    baseurl = 'https://www.shein.com'
    url = f'{baseurl}{url}'
    if url:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(url,headers=headers)
        doc = pq(r.text)
        
        for i in doc('div.kv-row').items():
        
            item = i('.key').text()
            value = i('.val').text()
            if item == 'Composition:':
                print(f'{skc}@{item}@{value}')

# get_info('blouse170925106')

# wb = xw.Book('a.xlsx')
# values = wb.sheets[0].range('a3:a6322').value
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
n = 0
for i in list1:

    get_info(i)
