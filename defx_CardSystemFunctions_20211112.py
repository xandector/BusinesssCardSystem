# Card Dict Info
# Key:Name      Value:String    姓名
# Key:Sex       Value:String    性别
# Key:PhoneNo   Value:String    电话
# Key:SocialID  Value:String    社交媒体号码
# Key:Email     Value:String    电子邮件
# Key:Address    Value:String    地址
# Key:Memo      Value:String    备注


def initCard():
    #   初始化步骤，程序开始时调用，并返回初始化的名片字典cards
    cardlist = [{
                    'Name': 'Lee',
                    'Sex': '男',
                    'PhoneNo': '18620115364',
                    'SocialID': 'xanderlee',
                    'Email': 'xandector@gmail.com',
                    'Address': '广东省肇庆市',
                    'Memo': '111'
                 },
                {
                    'Name': 'Xander',
                    'Sex': '男',
                    'PhoneNo': '17728825364',
                    'SocialID': '103736346',
                    'Email': '103736346@qq.com',
                    'Address': '广东省广州市',
                    'Memo': '222'
                }]   # 初始化名片列表
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
    ncard = {'Name':        nname,
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
        nsex = input('请输入性别（男/M/Male、女/F/Female）：')
        if nsex == '男' or nsex == 'Men' or nsex == 'men' or nsex == 'M' or nsex == 'Male' or nsex == 'male':
            nsex = '男'
            return str(nsex)
        elif nsex == '女' or nsex == 'Women' or nsex == 'women' or nsex == 'F' or nsex == 'Female' or nsex == 'female':
            nsex = '女'
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


def deleteCard(cardlist):
    # 检测列表是否为空
    if len(cardlist) < 1:
        print('当前列表为空！')
        return False
    else:
        # 通过输入卡片序号，删除cardlist中对应位置的卡片
        del_num = input('请输入需要删除的名片编号（No.）:')
        del_num = int(del_num) - 1
        printCard(cardlist[del_num], del_num)
        del cardlist[del_num]
        return True


def editCard(cardlist):
    # 检测列表是否为空
    if len(cardlist) < 1:
        print('当前列表为空！')
        return False
    # 运行名片查询后修改对应名片key的value
    while True:
        edit_num = input('请输入需要编辑的名片序号(No.):')  # 输入编辑序号，检测序号
        if edit_num.isdigit():
            edit_num = int(edit_num)
            if edit_num > len(cardlist):
                print('序号超过列表范围，请重新输入')
                continue
            else:
                edit_num = edit_num - 1     # 转换序号为底标
                edit_card = cardlist[edit_num]
                printCard(edit_card, edit_num)     # 打印序号对应卡片
                # 顺序询问编辑内容，默认不修改
                # Name
                print('当前 {} 为 {}'.format('Name', edit_card['Name']))
                new_name = inputName()
                if new_name:
                    cardlist[edit_num]['Name'] = new_name
                # Sex
                print('当前 {} 为 {}'.format('Sex', edit_card['Sex']))
                new_sex = inputSex()
                if new_sex:
                    cardlist[edit_num]['Sex'] = new_sex
                # PhoneNo
                print('当前 {} 为 {}'.format('PhoneNo', edit_card['PhoneNo']))
                new_phoneno = inputPhoneNo()
                if new_phoneno:
                    cardlist[edit_num]['PhoneNo'] = new_phoneno
                # SocialID
                print('当前 {} 为 {}'.format('SocialID', edit_card['SocialID']))
                new_socialid = inputSocialID()
                if new_socialid:
                    cardlist[edit_num]['SocialID'] = new_socialid
                # Email
                print('当前 {} 为 {}'.format('Email', edit_card['Email']))
                new_email = inputEmail()
                if new_email:
                    cardlist[edit_num]['Email'] = new_email
                # Address
                print('当前 {} 为 {}'.format('Address', edit_card['Address']))
                new_address = inputAddress()
                if new_address:
                    cardlist[edit_num]['Address'] = new_address
                # Memo
                print('当前 {} 为 {}'.format('Memo', edit_card['Memo']))
                new_memo = inputMemo()
                if new_memo:
                    cardlist[edit_num]['Memo'] = new_memo
            # 打印编辑后内容
            printCard(cardlist[edit_num], edit_num)
            # print('修改完成')
            return True
        else:
            print('请输入正确的序号（No.)！')
            continue
        # return False


def searchCard(cardlist):
    # 按输入信息搜寻，选择序号、姓名、全局模糊搜索
    while True:
        nselect = input('1.按序号；2.按姓名；3.模糊搜索；4.返回')
        # 通过搜索函数返回search_result结果判断是否找到和找到数量
        if nselect == '1':
            search_result = searchCardNoWithPrint(cardlist)
        elif nselect == '2':
            search_result = searchCardName(cardlist)
        elif nselect == '3':
            search_result = searchCardAll(cardlist)
        elif nselect == '4':
            return False
        else:
            print('输入有误，请重新输入')
            continue
        if search_result:
            # 如果搜索成功则返回
            print('搜索完成，共找到{}个结果。'.format(search_result))
            return True
        else:
            # 没有搜索成功提醒继续搜索
            print('没有找到相关名片，请重试。')
            continue


def searchCardNoWithPrint(cardlist):
    # 检测列表是否为空
    if len(cardlist) < 1:
        print('当前列表为空！')
        return 0
    # 按序号搜索名片并打印
    while True:
        search_num = input('请输入名片的序号（No)：')
        if search_num.isdigit():
            # 判断输入信息是否为数字
            search_num = int(search_num) - 1
            if search_num <= len(cardlist):
                # 判断序号是否小于列表长度（即搜索内容在列表中）
                # for card in cardlist:
                #     # 遍历cardlist搜索no字段,并打印对应名片
                #     if int(card['No']) == int(search_num):
                #         printCard(card)
                #         return True
                # 去除序号字段，直接用底标代替
                printCard(cardlist[search_num], search_num)
                return 1    # 返回搜索数量1
            else:
                print('序号超出列表范围，请重新入序号。')
                continue
        else:
            if search_num == 'Q':   # 输入Q退出
                return 0
            else:
                print('请输入正确的序号（数字）！')
                continue
    print('Search Card No Error!!')
    return 0


# def searchCardNo(cardlist):     # 通过输入序号搜索并返回对应名片字典（不打印）
#     # 检测列表是否为空
#     if len(cardlist) < 1:
#         print('当前列表为空！')
#         return 0
#     while True:
#         search_num = input('请输入名片的序号（No)：')
#         if search_num.isdigit():
#             # 判断输入信息是否为数字
#             search_num = int(search_num) - 1    # 将入参传化为列表坐标
#             if search_num <= len(cardlist):
#                 # 判断序号是否小于列表长度（即搜索内容在列表中）
#                 return cardlist[search_num]
#             else:
#                 print('序号超出列表范围，请重新输入序号。')
#                 continue
#         else:
#             print('请输入正确的序号（数字）！')
#             continue


def searchCardName(cardlist):
    # 检测列表是否为空
    if len(cardlist) < 1:
        print('当前列表为空！')
        return 0
    # 按姓名搜索并打印
    while True:
        search_name = inputName()
        rt = 0              # 搜索结果计数，用于函数返回布尔值
        for card in cardlist:
            if card['Name'] == search_name:
                printCard(card, cardlist.index(card))
                rt += 1
        return int(rt)
    # print('Search Card Name Error!!')
    # return False


def searchCardAll(cardlist):
    if len(cardlist) < 1:
        print('当前列表为空！')
        return 0
    # 模糊检索卡片字段，并返回结果个数
    while True:
        search_value = input('请输入要搜索的内容（姓名、邮件、电话等）')
        rt = 0              # 搜索结果计数，用于函数返回数量
        for card in cardlist:
            for k in card:
                if search_value in str(card[k]):
                    printCard(card, cardlist.index(card))
                    rt += 1
                    break   # 如果在卡片内元素找到对应字段，计数器加1并退出到下一卡片
                else:
                    continue
        return int(rt)


def listCard(cardlist):
    # 遍历所有名片
    if len(cardlist) < 1:   # cardlist无元素时直接返回
        print('当前无名片')
        return True
    for card in cardlist:   # 遍历打印cardlist
        printCard(card, cardlist.index(card))
    return True


def printCard(card, index):
    # 格式打印单张名片
    cardno = str(index+1)
    cardname = card['Name']
    cardsex = card['Sex']
    cardphoneno = card['PhoneNo']
    cardsocilid = card['SocialID']
    cardemail = card['Email']
    cardaddress = card['Address']
    cardmemo = card['Memo']
    print('=================================')
    print('|  No.{}        {}'.format(cardno, cardname))
    print('|  性别:{}     电话:{}'.format(cardsex, cardphoneno))
    print('|  社交账号:{}'.format(cardsocilid))
    print('|  电子邮件:{}'.format(cardemail))
    print('|  地址：{}'.format(cardaddress))
    print('|  备注：{}'.format(cardmemo))
    print('=================================')
    print(' ')
    pass
