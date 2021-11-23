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
        if deleteCard(aCardList):
            print('删除成功')
        else:
            print('删除失败')
        continue
    elif aSelect == '3':
        # 修改
        print('3')
        continue
    elif aSelect == '4':
        # 查询
        if searchCard(aCardList):
            print('搜索完成')
        else:
            print('搜索中断')
        continue
    elif aSelect == '5':
        # 一览
        if listCard(aCardList):
            print('一览完成')
        else:
            print('一览失败')
        continue
    elif aSelect == '6':
        # 退出
        print('系统已退出，感谢使用')
        break
    else:
        print("输入有误，请重新输入（1-6）：")
        continue



