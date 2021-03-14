import random


def func():
    pass


# 1.
"""v1 = [] or "alex"
print(v1)  # v1 = 'alex'
v2 = [11, 22] and (1, 2, )
print(v2)  # v2 = '(1, 2, )'
# a 是列表 b为 一个包含三个整型的元组 c为包含三个元组的元组"""

# 2.
"""test = 'wu|alex|eric'
new_test = test.split("|")
print(new_test)
print(tuple(new_test))"""

# 3.
color_list = ['红桃', '方块', '梅花', '黑桃']
num_list = []
for num in range(1, 14):
    num_list.append(num)

result = []
card_list = []
for i in color_list:
    for j in num_list:
        card_tuple = (i, j)
        card_list.append(card_tuple)
print(card_list)
