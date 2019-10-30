import os
from lxml import etree
import requests

#初始参数，自己输入的学号，密码。
studentnumber = "xxxxxxx"
password = "xxxxx"

#访问教务系统,前面分析过了，提交数据时要用这个值。先得到__VIEWSTATE的值。
s = requests.session()
url = "http://218.6.163.93/default2.aspx"
response = s.get(url)
selector = etree.HTML(response.content)
__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]

#获取验证码并下载到本地
imgUrl = "http://218.6.163.93/CheckCode.aspx?"
imgresponse = s.get(imgUrl, stream=True)
cooker=s.cookies#获取每一次登陆教务系统的cookies
print (s.cookies)#cookies检验端口
image = imgresponse.content
DstDir = os.getcwd()+"\\"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
with open(DstDir+"code.jpg" ,"wb") as jpg:
jpg.write(image)
except IOError:
print("IO Error\n")
finally:
jpg.close

#手动输入验证码

code =input("验证码是")

#构建post数据
data = {
"__VIEWSTATE":__VIEWSTATE,
"txtUserName":studentnumber,
"TextBox2":password,
"txtSecretCode":code,
"Button1":"",
}

#提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}

#登陆教务系统
response = s.post(url,data=data,headers=headers)
print ("成功进入")
print(response.text)#登陆成功检验端口

#获取成绩，gardeurl是课表页面url,为什么有个Referer参数,这个参数代表你是从哪里来的。就是登录后的主界面参数。这个一定要有。

head={
'Host':'218.6.163.93',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer':'http://218.6.163.93/xs_main.aspx?xh=201517120096',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8',
#'Cookie':'ASP.NET_SessionId=ky4vhczmhhzxs2455ossex55',#最开始我用的是固定的cookies所以出现大量问题，最后我使用了自动获取才解决
}


gardeurl = "http://218.6.163.93/xscj.aspx?xh=201517120096&xm=%BA%FA%B3%CC%EE%DA&gnmkdm=N121604"#成绩页面的地址，其中xh为学号，xm为密码，gnmkdm为成绩页面的代码

#向成绩页面post的表单数据，包含—VIEWSTATE页面状态，txtQSCJ为，Button2为在校学习成绩查询按钮，后面为按钮提交的值
formdata = {
    '__VIEWSTATE':'dDw0MTg3MjExMDA7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwxNT47aTwxNz47aTwyMz47aTwyNT47aTwyNz47aTwyOT47aTwzMD47aTwzMj47aTwzND47aTwzNj47aTw0OD47aTw1Mj47PjtsPHQ8dDw7dDxpPDE4PjtAPFxlOzIwMDEtMjAwMjsyMDAyLTIwMDM7MjAwMy0yMDA0OzIwMDQtMjAwNTsyMDA1LTIwMDY7MjAwNi0yMDA3OzIwMDctMjAwODsyMDA4LTIwMDk7MjAwOS0yMDEwOzIwMTAtMjAxMTsyMDExLTIwMTI7MjAxMi0yMDEzOzIwMTMtMjAxNDsyMDE0LTIwMTU7MjAxNS0yMDE2OzIwMTYtMjAxNzsyMDE3LTIwMTg7PjtAPFxlOzIwMDEtMjAwMjsyMDAyLTIwMDM7MjAwMy0yMDA0OzIwMDQtMjAwNTsyMDA1LTIwMDY7MjAwNi0yMDA3OzIwMDctMjAwODsyMDA4LTIwMDk7MjAwOS0yMDEwOzIwMTAtMjAxMTsyMDExLTIwMTI7MjAxMi0yMDEzOzIwMTMtMjAxNDsyMDE0LTIwMTU7MjAxNS0yMDE2OzIwMTYtMjAxNzsyMDE3LTIwMTg7Pj47Pjs7Pjt0PHA8O3A8bDxvbmNsaWNrOz47bDxwcmV2aWV3KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxUZXh0Oz47bDzlrablj7fvvJoyMDE1MTcxMjAwOTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWnk+WQje+8muiDoeeoi+mSsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m6Zmi77ya55S15a2Q5LiO5L+h5oGv5bel56iL57O7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrvvJo7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeUteWtkOS/oeaBr+W3peeoizs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86KGM5pS/54+t77yaMTXnlLXkv6EwMeePrTs+Pjs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPEhIWFk7Pj47Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+Oz4eb7m/pxfJff/rUMpEwpurKTUyZA==',
    'txtQSCJ':'0',
    'txtZZCJ':'100',
    'Button2':'%D4%DA%D0%A3%D1%A7%CF%B0%B3%C9%BC%A8%B2%E9%D1%AF'

}

#模拟浏览器的headers
header = {
'Cache-Control':'max-age=0',
'Connection':'Keep-Alive',
'Content-Length':'1461',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'218.6.163.93',
'Referer':'http://218.6.163.93/xscj.aspx?xh=201517120096&xm=%BA%FA%B3%CC%EE%DA&gnmkdm=N121604',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
'Origin':'http://218.6.163.93',
'Upgrade-Insecure-Requests':'1',
'Accept-Language':'zh-CN,zh;q=0.8',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate'
}

#向成绩页面post在校学习成绩的请求
m = requests.post(gardeurl,data=formdata,headers=header,cookies=cooker)
m.encoding=m.apparent_encoding
print(m.text)

#将获取到的成绩页面保存到本地
with open("D://pics//loginsystem.html",'wb') as f:
f.write(m.content)
f.close()
