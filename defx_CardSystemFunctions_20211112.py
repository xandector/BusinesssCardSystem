def initCard():
    #   初始化步骤，程序开始时调用，并返回初始化的名片字典cards
    cardlist = ()   # 初始化名片列表
    printCardMenu()  # 打印菜单
    return cardlist


def printCardMenu():
    #   打印菜单
    print('----------------------------------')
    print('--------名片管理系统 v1.0---------')
    print('--------1.添加名片----------------')
    print('--------2.删除名片----------------')
    print('--------3.修改名片----------------')
    print('--------4.查询名片----------------')
    print('--------5.显示所有名片------------')
    print('--------6.退出系统----------------')
    print('------(输入数字回车选择功能)------')


def addCard():
    # 添加新的card字典到cardList最后
    pass


def deleteCard():
    # 运行名片查询后删除对应card字典
    listCard()
    pass


def editCard():
    # 运行名片查询后修改对应名片key的value
    pass


def searchCard(search_var):
    # 按输入信息搜寻，分序号、姓名、模糊
    pass


def searchCardNo(search_num):
    # 按序号搜索
    pass


def searchCardName(search_name):
    # 按姓名搜索
    pass


def SearchCardAll(search_text):
    # 模糊检索
    pass


def listCard():
    # 遍历所有名片
    pass


def exitBCS():
    # 退出系统
    pass
