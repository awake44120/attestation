import requests
import getpass
import re


user_input = input('请输入用户名:')
user_password = getpass.getpass("请输入密码：")
user_type = input('请选择运营商(输入相应数字)：1.校园网(不建议) 2.中国电信 3.中国联通 4.中国移动\n')
login_type = ''
if int(user_type) == 1:
    login_type = ''
elif int(user_type) == 2:
    login_type = '@ctc'
elif int(user_type) == 3:
    login_type = '@cuc'
elif int(user_type) == 4:
    login_type = '@cmc'
else:
    print('请输入1-4以内的整数')
    exit()

# 请求头部
h = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# 请求体
d = 'DDDDD=' + user_input + login_type + '&upass=' + user_password

response = requests.post('http://192.168.125.21', headers=h, data=d)

c = re.findall('<title>(.*?)</title>', response.text)
print(str(c))
if c == ['认证成功页']:
    print('登录成功')
else:
    print('登录失败')
