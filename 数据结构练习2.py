import random


def func():
    pass


# 实现进制转换
"""v1 = 675
print(bin(v1))
v2 = "0b11000101"
print(int(v2, base=2))
v3 = "11000101"
print(int(v3, base=2))"""

# 将v1 = 123 和 v2 = 246 转换为二进制 将前缀0b去掉
# 再将两个二进制拼接起来 最后再转换为整型
"""bin_v1 = bin(123).split("0b")[1]
bin_v2 = bin(246).split("0b")[1]
bin_concat = bin_v1 + bin_v2
print(int(bin_concat, base=2))"""

# 将v1 = 123 和 v2 = 246 转换为二进制 将前缀0b去掉
# 再将两个二进制拼接起来 最后再转换为整型
"""bin_v1 = bin(123).split("0b")[1].rjust(16, '0')  zfill(16)
bin_v2 = bin(246).split("0b")[1].rjust(16, '0')
bin_concat = bin_v1 + bin_v2
print(int(bin_concat, base=2))"""

# 让用户输入一段文本, 过滤文本中的敏感词
# 苍老师 波波老师 输出替换后的文本
"""replace_words = ['苍老师', '波波老师']
content = input("输入文本:").strip()
for word in replace_words:
    content = content.replace(word, "***")
print(content)"""

# 变量 name="alex leNb" 完成如下操作
"""name = "alex leNb"
print(name.strip())
if name.startswith('al'):
    print("name以al开头")
if name.endswith('Nb'):
    print("name以Nb结尾")
replace_result = name.replace('l', 'p')
print(replace_result)
split_result = name.split('l')
print(split_result)
split_result_2 = name.split('l', 1)
print(split_result_2)
upper_result = name.upper()
print(upper_result)
lower_result = name.lower()
print(lower_result)"""

# 如何实现字符串的翻转
"""name = 'alex leNb'
print(name[::-1])"""

# 完成如下操作
"""name = '123a4b5c'
print(name[:3])
print(name[3:6])
print(name[-1])
print(name[-3::-2])"""

# 使用while循环 输出每个字符
"""message = "伤情最是晚凉天，憔悴厮人不堪言"
count = 0
while count < len(message):
    print(message[count])
    count += 1
for i in message:
    print(i)"""

# 利用for循环和range 进行倒序输出
"""message = "伤情最是晚凉天，憔悴厮人不堪言"
for i in range(len(message))[::-1]:   # range(len(message)-1, -1, -1)
    print(message[i])"""

# 利用for 输入倒计时效果
"""for i in range(1, 4)[::-1]:
    print(f"倒计时{i}秒")"""

# 让用户输入一段文本
# 计算浪出现的次数
"""count = 0
content = input("请输入文字:").strip()
for i in content:
    if i == '浪':
        count += 1
print(count)"""

# 获取用户两次输入的内容 并提起其中的数字 实现数字的相加
str1 = ''
str2 = ''
num1 = input("输入第一个:").strip()
num2 = input("输入第二个:").strip()
for i in num1:
    if i.isdecimal():
        str1 += i
for m in num2:
    if m.isdecimal():
        str2 += m
print(int(str1) + int(str2))
