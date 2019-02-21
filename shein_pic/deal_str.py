import re
import xlwings as xw

wb = xw.Book('zjs.xlsx')
values = wb.sheets[0].range('h3:h82').value
#for i in values:
    # try:
    #     print(re.findall('类别:(.*?);',i)[0])
    # except:
    #     print('s')

left = wb.sheets[0].range('h3:h82').value
right = wb.sheets[0].range('u3:u82').value
n = 0

for a,b in zip(left,right):
    n += 1
    if b:
        dict1 = {}
        items = re.findall('(.*?)\d+.0',b)
        numbers = re.findall('\d+.0',b)
        #total = sum([float(i) for i in numbers])
        for item,number in zip(items,numbers):
            dict1[item.replace(',','')] = float(number)
        group = ''
        for i in sorted(dict1,key=dict1.__getitem__,reverse=True):
            percentage = str(dict1[i]).replace('.0','%')
            i = i.replace(' ','')
            one = f'{i}{percentage}'
            if not group:
                group += one
            else:
                group = group +','+one

        print(group)
    
    else:
        aa = re.findall('含量:(.*?),',a)
        if aa:
            print(aa[0])

        else:
            print('右边没有')
            # aaa = re.findall('含量:(.*?);',a)
            # if aaa:
            #     aaa[0].replace(',','')
            #     pers = re.findall('(\d+%)',aaa[0])
            #     items = re.findall('[\u4E00-\u9FA5]+',aaa[0])
            #     total = ''
            #     for per,item in zip(pers,items):
            #         one = f'{item}{per}'
            #         if not total:
            #             total += one
            #         else:
            #             total = total +','+one
            #     print(total)

            # else:
                
                # print('两边都没有')