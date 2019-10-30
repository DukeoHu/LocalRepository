#可以对任意网站的第三方链接进行爬取！！！
#存在以下问题：一没有文件检验机制（会对所有链接进行爬取），二没有采取函数体进行设计（不能提供人机交互）
#只适用html页面中包含图片链接的页面

import re
import requests
import os
url = input("please input the links:")
r=requests.get(url,timeout=10)
html=r.text
pat = re.compile('[a-zA-z]+://[^\s]*"')#运用正则表达式将所有网址链接提取出来
urltext = pat.findall(html,re.S)
i = 0#为文件名称提供数字计数
for each in urltext:
    print(each)
    each1 = each.strip('"')#去除所有each最后一个双引号"
    try:
        pic = requests.get(each1,timeout=100)
        pic.raise_for_status()#检验网络链接情况

    except:
        print("【错误，无法下载改图片！】")
        continue
    try:
        string = "D://pics//photo//" + str(i) + each1.split('/')[-1]#给文件保存提供地址
        with open(string,'wb') as f:
            f.write(pic.content)
            f.close()
            i += 1
            print("success!")#图片文件保存！
    except:
        print("文件类型错误！")#对不能保存的异常文件进行报错
        continue#提高程序稳定性
