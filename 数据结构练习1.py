import random
# 1. 判断输入用户的值是否以'ai'开头 是则输出'是的'
"""content = input("输入内容:").strip()
if content.startswith('ai'):
    print("是的")
else:
    print("不是")"""

# 2. 判断字符串是否以”Nb“结尾
"""content = input("输入内容:").strip()
if content.endswith("Nb"):
    print("是的")
else:
    print("不是")"""

# 将name变量中所有的'l'变成'p'
"""name = 'alex is lighter'
result = name.replace('l', 'p')
print(result)"""

# 对用户输入的值进行判断,是否为整数,如果是 则转为整型
# 不是 则输出 请输入数字
"""content = input("输入值:").strip()
if content.isdecimal():
    content = int(content)
else:
    print("输入格式有误, 请输入数字")"""

# 对用户输入的值进行判断,按照”+“分割,且输入的内容必须得是 12 + 13 的格式
# TODO: 有可能输入的是 12++13
""" 
    content = input("请输入内容:").strip()
    con_1 = content.split("+", 1)
    if con_1[0].isdecimal() and con_1[1].isdecimal():
        print("输入的格式正确")
    else:
        print("输入的格式有误")"""

# 补充代码
"""code = random.randrange(1000, 9999)
code = str(code)
msg = "欢迎登录系统, 您的验证码为:{}, 手机号为:{}".format(code, '15241526933')
print(msg)
code = msg.split(',')[1].split(':')[1]
phone = msg.split(',')[2].split(':')[1]
print(code, phone)
input_code = input("请输入验证码:").strip().lower()
input_phone = input("请输入手机号:").strip()
if input_code == code and phone == input_phone:
    print("登录成功!")"""

# 补充代码
data_list = []
while True:
    hobby = input("请输入你的爱好(Q/q退出):")
    if hobby.upper() == 'Q':
        break
    data_list.append(hobby)
    # 将所有的爱好通过符号 ‘、’拼接并输出
result = "、".join(data_list)
print(result)
