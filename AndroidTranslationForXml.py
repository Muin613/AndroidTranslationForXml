import urllib.request
import urllib.parse
import json
import xlrd
import time
import os
from datetime import date,datetime
#开发环境为python 3.7版本
#输出文件的位置
path='C:\\Users\\M\\Desktop'
#读取excel的文件位置及文件
ExcelFile = xlrd.open_workbook(r'C:\Users\M\Downloads\3.xlsx')
sheet = ExcelFile.sheet_by_name("Sheet1")
print(sheet.name)
print(sheet.nrows)
print(sheet.ncols)
language = sheet.col_values(0)
file_names = sheet.col_values(1)
string_names = sheet.col_values(2)
string_values = sheet.col_values(3)
print(language)
print(file_names)
print(string_names)
print(string_values)
print(sheet.row_values(1))
len0 =len(language)
num =0
for i in range(0,len0):
    if ''==language[i]:
        num+=1
int_len=int(len0)-num
print(int_len)
def getResult(values,lan):
             url = 'https://aidemo.youdao.com/trans'
             data = {}
             data['from'] = 'zh-CHS'
             data['q'] = values
             data['to'] = lan
             data = urllib.parse.urlencode(data).encode('utf-8')
             response = urllib.request.urlopen(url, data)
             html = response.read().decode('utf-8')
             target = json.loads(html)
             time.sleep(0.5)
             print(target)
             if 'translation' in target:
                 return target['translation'][0]
             return getResult(values,lan)

for j in range(1,int_len):
    lan=language[j]
    result=[]
    for i in range(1,sheet.nrows):
          data =getResult(string_values[i],lan)
          result.append(data)
    print("结果")
    print(result)
    temp_path=path+'\\'+file_names[j]+'.xml'
    if os.path.exists(temp_path):
        os.remove(temp_path)
    f=open(temp_path,'w',encoding='utf-8')
    str="<resources> \n"
    for i in range(1,len(string_names)):
        str+="<string name=\""
        str+=string_names[i]
        str+="\">"
        str+=result[i-1]
        str+="</string>\n"
        str+="</resources>"
    f.write(str)
    f.close()
    print("文件生成成功！")
