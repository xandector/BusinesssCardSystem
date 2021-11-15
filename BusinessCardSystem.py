from defx_CardSystemFunctions_20211112 import *

# 初始化名片列表
aCardList = initCard()
while True:
    aSelect = input("Please select(1-6):")
    if aSelect == '1':
        # 添加
        print('1')
        continue
    elif aSelect == '2':
        # 删除
        print('2')
        continue
    elif aSelect == '3':
        # 修改
        print('3')
        continue
    elif aSelect == '4':
        # 查询
        print('4')
        continue
    elif aSelect == '5':
        # 一览
        print('5')
        continue
    elif aSelect == '6':
        # 推出
        print('6')
        continue
    else:
        print("输入有误，请重新输入：")
        continue



