from defx_CardSystemFunctions_20211112 import *

# 初始化名片列表
aCardList = initCard()
while True:
    printCardMenu()  # 打印菜单
    aSelect = input("请输入对应数字并回车选择功能:")
    if aSelect == '1':
        # 添加名片
        aCardList = addCard(aCardList)
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
        searchCard(aCardList)
        continue
    elif aSelect == '5':
        # 一览
        listCard(aCardList)
        continue
    elif aSelect == '6':
        # 退出
        print('系统已退出，感谢使用')
        break
    else:
        print("输入有误，请重新输入（1-6）：")
        continue



