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
    pass


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


def searchCard(cardlist):
    # 按输入信息搜寻，选择序号、姓名、全局模糊搜索
    while True:
        nselect = input('1.按序号；2.按姓名；3.模糊搜索；4.返回')
        if nselect == '1':
            search_result = searchCardNo(cardlist)
        elif nselect == '2':
            search_result = searchCardName(cardlist)
        elif nselect == '3':
            search_result = searchCardAll(cardlist)
        elif nselect == '4':
            break
        else:
            print('输入有误，请重新输入')
            continue
        if search_result:       # 如果搜索成功则返回
            break
        else:
            continue


def searchCardNo(cardlist):
    # 按序号搜索
    while True:
        search_num = input('请输入欲查找名片的序号（No.)：')
        if search_num.isdigit():        # 判断输入信息是否为数字
            if int(search_num) <= len(cardlist) + 1:    # 判断序号是否小于列表长度（即搜索内容在列表中）
                for card in cardlist:                   # 遍历cardlist搜索no字段,并打印对应名片
                    if int(card['No']) == int(search_num):
                        printCard(card)
                        return True
                print('列表中找不到对应序号，请检查或使用其他方法搜索。')
                return False
            else:
                print('序号超出列表范围，请重新输入序号。')
                continue
        else:
            print('请输入正确的序号（数字）！')
            continue
    print('Search Card No Error!!')
    return False


def searchCardName(cardlist):
    # 按姓名搜索
    while True:
        search_name = inputName()
        rt = 0              # 搜索结果计数，用于函数返回布尔值
        for card in cardlist:
            if card['Name'] == search_name:
                printCard(card)
                rt += 1
        return bool(rt)
    # print('Search Card Name Error!!')
    # return False


def searchCardAll(cardlist):
    # 模糊检索
    while True:
        search_value = input('请输入要搜索的内容（姓名、邮件、电话等）')
        rt = 0              # 搜索结果计数，用于函数返回布尔值
        for card in cardlist:
            for k in card:
                if search_value in str(card[k]):
                    printCard(card)
                    rt += 1
                    break
        print('搜索完成，共{}项结果'.format(rt))
        return bool(rt)


def listCard(cardlist):
    # 遍历所有名片
    for card in cardlist:
        printCard(card)
        print(' ')


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
