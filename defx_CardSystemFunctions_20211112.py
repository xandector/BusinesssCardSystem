# Card Dict Info
# Key:No        Value:Int       序号
# Key:Name      Value:String    姓名
# Key:Sex       Value:String    性别
# Key:PhoneNo   Value:String    电话
# Key:SocialID  Value:String    社交媒体号码
# Key:Emial     Value:String    电子邮件
# Key:Adress    Value:String    地址
# Key:Memo      Value:String    备注


def initCard():
    #   初始化步骤，程序开始时调用，并返回初始化的名片字典cards
    cardlist = []   # 初始化名片列表
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
    print('----------------------------------')


def addCard(cardlist):
    # 添加新的card字典到cardList最后
    nname = inputName()
    nsex = inputSex()
    nphoneno = inputPhoneNo()
    nsocialid = inputSocialID()
    nemail = inputEmail()
    naddress = inputAddress()
    nmemo = inputMemo()
    nno = len(cardlist) + 1
    ncard = {'No':          nno,
             'Name':        nname,
             'Sex':         nsex,
             'PhoneNo':     nphoneno,
             'SocialID':    nsocialid,
             'Email':       nemail,
             'Address':     naddress,
             'Memo':        nmemo}
    cardlist.append(ncard)
    print('名片添加成功！')
    return cardlist


def inputName():
    # 输入姓名提示并返回string
    nname = input('请输入名字：')
    str(nname)
    return nname


def inputSex():
    # 输入性别提示，格式化后并返回string
    while True:
        nsex = input('请输入性别（男/女/F/M）：')
        if nsex == '男' or nsex == 'Men' or nsex == 'men' or nsex == 'M' or nsex == 'Male' or nsex == 'male':
            nsex = 'M'
            return str(nsex)
        elif nsex == '女' or nsex == 'Women' or nsex == 'women' or nsex == 'F' or nsex == 'Female' or nsex == 'female':
            nsex = 'F'
            return str(nsex)
        else:
            continue
    print('Sex Input Error!!')
    pass


def inputPhoneNo():
    # 输入电话提示，判断长度和内容并返回string
    while True:
        nphoneno = input('请输入电话号码：')
        if nphoneno.isdigit():
            if 7 < len(nphoneno) <= 11:
                str(nphoneno)
                return nphoneno
            else:
                print("手机号码格式不对，请检查位数(7-11位）")
                continue
        else:
            print('输入错误，请输入数字号码')
            continue
    print('Phone Number Input Error!!')
    pass


def inputSocialID():
    # 输入社交帐号提示，判断长度并返回string
    while True:
        nsocialid = input('请输入社交媒体账号(QQ/微信/Facebook）：')
        if 4 < len(nsocialid) < 20:
            str(nsocialid)
            return nsocialid
        else:
            print('输入长度不符，请输入4~20位账号ID')
            continue
    print('Social ID Input Error!!')
    pass


def inputEmail():
    # 输入电子邮箱提示，判断长度和格式并返回string
    while True:
        nemail = input('请输入电子邮件：')
        if nemail.count('@') == 1 and nemail.count('.') > 0 and nemail.index('@') < nemail.index('.'):
            str(nemail)
            return nemail
        else:
            print('请正确输入电子邮箱地址格式（如xxxxx@gmail.com)')
            continue
    print('Email Input Error!!')
    pass


def inputAddress():
    # 输入地址提示，判断长度并返回string
    while True:
        naddress = input('请输入地址：')
        if 4 <= len(naddress) <= 30:
            str(naddress)
            return naddress
        else:
            print('请输入合理的地址长度（4~30字）')
            continue
    print('Address Input Error!!')
    pass


def inputMemo():
    # 输入备注提示，返回string
    nmemo = input('请输入备注信息（没有请跳过）：')
    str(nmemo)
    return nmemo


def deleteCard():
    # 运行名片查询后删除对应card字典
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


def listCard(cardlist):
    # 遍历所有名片
    for card in cardlist:
        printCard(card)
    pass


def printCard(card):
    # 打印单张名片
    cardno = str(card['No'])
    cardname = card['Name']
    cardsex = card['Sex']
    cardphoneno = card['PhoneNo']
    cardsocilid = card['SocialID']
    cardemail = card['Email']
    cardaddress = card['Address']
    cardmemo = card['Memo']
    print('=================================')
    print('|  No.' + cardno + '        ' + cardname)
    print('|  性别:' + cardsex + '     电话:' + cardphoneno)
    print('|  社交账号:' + cardsocilid)
    print('|  电子邮件:' + cardemail)
    print('|  地址：' + cardaddress)
    print('|  备注：' + cardmemo)
    print('=================================')
    pass
