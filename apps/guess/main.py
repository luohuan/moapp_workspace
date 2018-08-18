import random
import time

honorary_title_group = [
    {
        'level':'Lv.0',
        'title':'群众演员'
    },
    {
        'level':'Lv.1',
        'title':'跟组演员'
    },
    {
        'level':'Lv.2',
        'title':'特约演员'
    },
    {
        'level':'Lv.3',
        'title':'十八线明星'
    },
    {
        'level':'Lv.4',
        'title':'六线明星'
    },
    {
        'level':'Lv.5',
        'title':'五线明星'
    },
    {
        'level':'Lv.6',
        'title':'四线明星'
    },
    {
        'level':'Lv.7',
        'title':'三线明星'
    },
    {
        'level':'Lv.8',
        'title':'二线明星'
    },
    {
        'level':'Lv.9',
        'title':'一线明星'
    },
    {
        'level':'Lv.10',
        'title':'国际大腕'
    },
    {
        'level':'Lv.11',
        'title':'超级巨星'
    },
    {
        'level':'Lv.12',
        'title':'奥斯卡影帝/影后'
    },
]

def main():
    with MoApp(appid='wx91f13354f5356b6c', name='看动图猜影视', navigationBarTitleText='看动图猜影视', withLogin=True):
        with Page(name='mainPage', background='http://material.motimaster.com/liuhongjie1533704706000/猜影视-首页背景.jpg', onShow=onMainReady, onReady=onMainReady, enableShare=True):
            # 用户头像
            ImageAvatar(pos=['center', 160], size=[180, 180], borderRadius='50%')
            # 用户昵称
            TextNickName(pos=['center', 345], size=[600, 100], textAlign='center')

            Text(pos=['center', 420], size=[260, 70], background='white', borderRadius=30, opacity=0.6)
            Text(name='level_title', pos=['center', 420], size=[260, 70], color='color', textAlign='center')
            # “开始游戏”按钮背景图
            Image(src='http://material.motimaster.com/liuhongjie1533785739000/按钮.png', size=[300, 118], pos=['center', 540])
            Button(text='开始游戏', size=[300, 100], pos=['center', 540], plain=True, border='0px', openType='getUserInfo', onTap=onButtonClick)
            # “排行榜”按钮背景图
            Image(src='http://material.motimaster.com/liuhongjie1533785739000/按钮.png', size=[300, 118], pos=['center', 700])
            Button(text='排行榜', size=[300, 100], pos=['center', 700], plain=True, border='0px', openType='getUserInfo', onTap=onCheckToplist)

            Image(src='http://material.motimaster.com/liuhongjie1533785739000/按钮.png', size=[300, 118], pos=['center', 860])
            Button(text='更多好玩', size=[300, 100], pos=['center', 860], plain=True, border='0px', openType='getUserInfo', onTap=onMoreFun)

            ContactButton(name='helpBtn', plain=True, border="None", pos=[15, 15], size=[70, 70], background='http://material.motimaster.com/appmaker/zhaoyuanxue/2357.png')
            
            with Box(name='AD1', hidden=False, size=[750, 125], pos=[0, 990]):
                AD(unitId='adunit-e9f5564ad7f4db98')

        with Page(name='GuessPage', background='http://material.motimaster.com/liuhongjie1533704115000/猜影视-答题背景.jpg', onReady=onGuessReady, onShareSuccessed=shareOptions, enableShare=True):
            # 题目数量提示
            Text(name='q_num', fontSize=40, pos=['center', 0], color='#ff0000')

            # gif文件边框
            Image(src='http://material.motimaster.com/liuhongjie1532679648000/电视.png', size=[602, 474], pos=['center', 57])
            # 电影提示gif文件
            Image(name='picture', pos=[133, 149], size=[432, 270])
            
            # 金币数量提示
            Text(name='coin', text='💰金币:20', size=[240, 67], pos=[40, 548], lineHeight=67)

            # 寻求提示按钮
            Image(src='http://material.motimaster.com/liuhongjie1533785739000/按钮.png', size=[210, 85], pos=['center', 548])
            Button(name='tips', text='提示-30💰', size=[210, 67], pos=['center', 548], plain=True, border='0px', lineHeight=67, onTap=onTipsClick)
            Image(src='http://material.motimaster.com/liuhongjie1533785739000/按钮.png', pos=[520, 548, 210, 85])
            ShareButton(text='分享+10💰', pos=[520, 548, 210, 67], plain=True, border='0px', lineHeight=67)

            #更多好玩按钮
            Button(name='morefun', text='更多好玩', size=[210, 67], pos=[500, 20],  border='1px', borderRadius=20,lineHeight=67, onTap=onMoreFun)
            # 供 用户输入的电影名 格子
            with List(name='anslist', size=[750, 70], textAlign='center', pos=['center', 654], display='flex', flexDirection='row', alignItems='center', justifyContent='center'):
                Text(text='{item.text}', marginRight=30, size=[70,70], fontSize=40, background='#5785db', color='#ffffff',
                    display='inline-block', borderRadius=8, onTap=moui.request(onAnswerClick, id='{item.id}'))
            
            # 供用户选择的文字
            with Grid(name='dataGrid', pos=['center', 743], size=[690, 200], column=8):
                with View(size=[75, 85]):
                    Text(text='{item.word}', size=[75, 75], pos=['center', 0], fontSize=40, background='#ffffff', boxShadow='-1px 15px 30px -12px black',
                        textAlign='center', borderRadius=8, onTap=moui.request(onClick, tag='{item.tag}'))

            with Box(name='AD1', hidden=False, size=[750, 125], pos=[0, 990]):
                AD(unitId='adunit-e9f5564ad7f4db98')

            with Mask(name='mask01', opacity=0.7, locked=True):
                with Box(pos=['center', 'center', 510, 642], background='#5785db', borderRadius='10px'):
                    Image(src='http://material.motimaster.com/liuhongjie1534213684000/称号文字.png', pos=[0, 0], size=[510, 642])
                    Image(top=65, right=10, size=[50, 50], src="http://material.motimaster.com/appmaker/goupeng/4531.png", opacity=1, onTap=onContinuePlay)
                    ImageAvatar(pos=['center', 100], size=[150, 150], borderRadius='50%')
                    Text(name='current_count', pos=[318, 332], fontSize=58, color='#f35c5c')
                    Text(name='percent', pos=[219, 420], fontSize=57, color='#f35c5c')
                    with Box(size=[510, 120], bottom=10):
                        with Box(size=[170, 200], pos=[0, 0], onTap=onContinuePlay):
                            Image(src='http://material.motimaster.com/liuhongjie1533865308000/8aa3d6cc71e44ea7da24fce64da22ebc.png', size=[70, 70], pos=['center', 0])
                            Text(text='继续答题', pos=['center', 80], color='white', fontSize=30, lineHeight=32, borderBottom="3rpx solid #ffffff")
                        with Box(size=[170, 200], pos=['center', 0]):
                            ShareButton(pos=['center', 0], size=[70, 70], background='http://material.motimaster.com/liuhongjie1533810423000/share.png', borderRadius='50%')
                            Text(text='分享战绩', pos=['center', 80], color='white', fontSize=30, lineHeight=32, borderBottom="3rpx solid #ffffff")
                        with Box(size=[170, 200], pos=[340, 0], onTap=onSaveImage):
                            Image(src='http://material.motimaster.com/liuhongjie1533826120000/saveimg.png', size=[70, 70], pos=['center', 0])
                            Text(text='保存图片', pos=['center', 80], color='white', fontSize=30, lineHeight=32, borderBottom="3rpx solid #ffffff")

                with Box(pos=['center', 200, 690, 160], background='http://material.motimaster.com/liuhongjie1534172321000/横幅.png'):
                    Text(name='honorary_title', pos=['center', 62], fontSize=58, color='#ff0000')

        with Page(name='resultPage', background='http://material.motimaster.com/liuhongjie1533879038000/猜影视-通关页.jpg', onReady=onResultReady):
            Button(text='保存我的战绩图', size=[400, 90], pos=['center', 610], background='#fed201', lineHeight=90,
                boxShadow='-1px 15px 30px -12px black', effect=pulse(t=1, c=0), onTap=onSaveImage)
            ShareButton(text='分享给好友来比拼', size=[400, 90], pos=['center', 740], background='#fed201', lineHeight=90,
                boxShadow='-1px 15px 30px -12px black', effect=pulse(t=1, c=0))
            Button(text='重新开始答题', size=[400, 90], pos=['center', 870], background='#fed201', lineHeight=90,
                boxShadow='-1px 15px 30px -12px black', effect=pulse(t=1, c=0), onTap=resetIndexList)

            with Box(name='AD1', hidden=False, size=[750, 125], pos=[0, 990]):
                AD(unitId='adunit-e9f5564ad7f4db98')

        with Page(name='TopListPage', background='http://material.motimaster.com/liuhongjie1533139503000/排行榜.jpg', onReady=onToplistReady, onShareSuccessed=shareOptions, enableShare=True):
            with ScrollBox(size=[750, 960], scrollY=True):
                with List(name='list1', pos=['center', 35]):
                        #可用字典中字典{item.detail.color}的形式引用数据
                    with Box(width=680, height=158, pos=['center', 0], margin='0 10% 10px 10%', fontSize=35, color='black', background='#75aede',
                        borderRadius=12, opacity=0.9):
                        Text(text='{item.rank}', size=[80, 80], pos=[30, 'center'], textAlign='center', lineHeight=80,
                            background='#fed201', borderRadius='50%')#序号
                        Image(src='{item.detail.avatarUrl}', borderRadius='50%', size=[90,90], pos=['center', 10])
                        Text(text='{item.detail.name}', width=680, textAlign='center', pos=['center', 100])#玩家姓名
                        Text(text='💰{item.detail.coin}', pos=[520, 'center'])#玩家分数

            with Box(name='AD1', hidden=False, size=[750, 125], top=990):
                AD(unitId='adunit-e9f5564ad7f4db98')

async def onMoreFun(user, app, page, mo):
    mo.gotoMiniProgram('wx6acc1db2845590f6','pages/listPage/listPage?channel=swlpdxcx6')

async def onMainReady(user, app, page, mo):
    # mo.showLoading('加载中...')
    lv_title = user.get('level_title')
    if lv_title is None :
        user.set('level_title', honorary_title_group[0])
        page.level_title.text = honorary_title_group[0]['level'] + ' ' + honorary_title_group[0]['title']
    else :
        page.level_title.text = lv_title['level'] + ' ' + lv_title['title']
    # mo.hideLoading()
    pass

async def onContinuePlay(user, app, page, mo):
    page.mask01.hidden = True
    
    mo.console('set mask01hidden = true')

    # 如果猜对的题目数量为10的整数倍，则必然显示了蒙层，没有发生跳转，点击蒙层触发本函数以后，应该发生跳转
    if len(user.index_list_v2) % 10 == 0 :
        # 否则 跳转到 猜题页面，并将当前已答过的题目序列 作为参数传入
        mo.redirectTo('GuessPage',  num=int(page.options.num)+1)

async def resetIndexList(user, app, page, mo):
    mo.console('resetIndexList')
    user.set('index_list_v2', [])
    user.set('level_title',honorary_title_group[0])
    mo.redirectTo('GuessPage',  num=1)

async def onButtonClick(user, app, page, mo):
    mo.goto('GuessPage', index_list=[], num=1)

async def onCheckToplist(user, app, page, mo):
    mo.goto('TopListPage', index_list=[], num=1)

async def onToplistReady(user, app, page, mo):

    # 在数据库中查询
    # exist = mo.db.guess.find()
    
    # data =[]
    # if exist:
    #     for item in exist:
    #         temp = {}
    #         mo.console(item)
    #         temp['avatarUrl'] = item['avatarUrl']
    #         temp['coin'] = item['coin']
    #         #temp['id'] = item['id']
    #         temp['name'] = item['name']
    #         temp['openid'] = item['openid']
    #         #temp['time'] = item['time']
    #         data.append(temp)
    #     # 按照金币排序
    #for row in data :
    
    scoreData = mo.toplist.get('toplist_coin','Daily')
    page.list1.data = scoreData

# 分享成功后增加金币20
async def shareOptions(user, app, page, mo):
    page.data.userCoin = page.data.userCoin + 10
    mo.db.guess.update(mo.db.guess.find({'openid': user.openid})[0]['id'], {
                                             'coin': page.data.userCoin})
    page.coin.text = '💰金币:%s' % page.data.userCoin

# guess页面准备函数，初始化金币等变量，记录个人信息
async def onGuessReady(user, app, page, mo):
    page.mask01.hidden = True

    # 在后台数据库中查询用户信息
    exist = mo.db.guess.find({
        'openid': user.openid})
    
    if exist:
        # 查到用户信息，获取剩余金币数量
        userCoin = int(exist[0]['coin']) 
    else:
        # 没有查询到，该用户是新用户，第一次使用本小程序
        # 为该用户在数据库中建立一个记录
        db_id = mo.db.guess.insert({
                        'name': user.nickName,# 答题者name
                        'openid': user.openid,# 答题者openid
                        'avatarUrl': user.avatarUrl,# 答题者头像
                        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        'coin': 20})
        # 新用户初始金币数量为20
        userCoin = 20

    # 设置该页面的金币提示信息
    page.data.userCoin = userCoin
    page.coin.text = '💰金币:%s' % page.data.userCoin

    # 设置题号提示
    page.q_num.text = '%s' % page.options.num


    # 获取用户答题状态
    index_list = user.get('index_list_v2')
    if index_list == None:
        user.set('index_list_v2',[])
        index_list = []
    mo.console('index_list_v2  %s' % index_list)
    if (index_list != None and len(index_list) < len(questionDict)):
        page.data.index_list = index_list
        page.options.num = len(index_list)+1
        # 设置题号提示
        page.q_num.text = '%s' % page.options.num
        """
        if(len(index_list) == 7):
            mo.goto('resultPage')
            return
        """

    elif index_list == None:
        page.options.num = 1
        page.q_num.text = '%s' % page.options.num
        user.set('index_list_v2', [])
    elif len(index_list) == len(questionDict):
        mo.console('出现这种情况')
        mo.redirectTo('resultPage')
        return
    else:
        mo.console('出现这种情况2')
        return


    # 随机挑选出五个成语，并返回一个问答的index
    candidate = pick() # candidate是一个字符串，一次为5个成语
    page.data.index = page.options.num - 1
    index = page.data.index
    # 设置本题的gif与答案
    page.picture.src = questionDict[index]['image_src']
    new_ans = questionDict[index]['answer']

    mo.console("本题答案：{}".format(new_ans))

    # 设置24个格子中的字符集
    word_list = candidate[0:(24-len(new_ans))] + new_ans
    mo.console(word_list)

    # 打乱顺序
    shuffle = order_random(word_list)

    # 为24个格子准备数据
    list_data = []
    for i in range(24):
        tmp_dict = {}
        tmp_dict['word'] = shuffle[i]
        tmp_dict['tag'] = i
        list_data.append(tmp_dict)
    page.dataGrid.data = list_data
    page.data.show_data = list_data

    # 从问题数据中索引本题的答案，获取其长度
    answer_lens = len(questionDict[index]['answer'])
    anslist = []
    flag_list = []
    tmp_answer = []
    for i in range(answer_lens):
        ans_one = {}
        ans_one['text'] = ''
        ans_one['id'] = i
        anslist.append(ans_one)
        flag_list.append(0)
        tmp_answer.append([])

    # 设置页面上 答案列表中的数据
    page.anslist.data = anslist

    # 并将该数据设置为其他云函数也可见的数据
    page.data.anslist = anslist
    page.data.answer = tmp_answer#[[],[],[],[]]

    # page.data.flag_list 为答案格子中每个格子的标记   标记该格子是否输入过
    page.data.flag_list = flag_list

    page.share.title = "您的好友"+ user.nickName+ "邀请您来猜"
    page.share.page = 'mainPage'

    #page.data.honorary_titleText = page.honorary_title.text

async def onMakeImage(user, app, page, mo):
    canvas = mo.mopic.createCanvas(512, 568)
    canvas.addImage('http://material.motimaster.com/liuhongjie1534214989000/称号保存.png', pos=[0, 0], size=[512, 568])
    canvas.addText(page.data.honorary_titleText, fontSize=50, color='#ff0000', size=[500, 300], pos=[100, 50])
    canvas.addImage(user.avatarUrl, size=[130, 130], pos=[186, 135], mask='circle')
    canvas.addText(page.data.current_countText, fontSize=48, color='#f35c5c', pos=[301, 340])
    canvas.addText(page.data.percentText, fontSize=43, color='#f35c5c', pos=[227, 407])
    #canvas.addText(user.nickName, pos=[260, 190, 200], textAlign='center', width=200, color='#000000')
    canvas.addText('你是真正阅片无数的老司机吗？\n这些影视作品你都看过多少？快来挑战一下！',
        fontSize=16, pos=[70, 500, 600], color='#000000')

    params = {
        'page':'mainPage',
        'width': 150,
    }
    retParams = mo.acode.getWxAcodeUrl(params)
    erweima = None
    if retParams['ret'] == 0:
        erweima = retParams['url']
    canvas.addImage(erweima, pos=[385, 490, 60, 60], mask='circle')
    res = canvas.makeImage()

    if res['ret'] == 0:
        page.data.set('url', res['url'])
        mo.console(res['url'])
    else:
        mo.console(res)
    
# 点击提示后，随机填补一个正确词，金币-30
async def onTipsClick(user, app, page, mo):
    # 根据答案格子中每个格子的填写与否，统计总共填写了多少格子，若已填写格子数量小于答案字数
    if sum(page.data.flag_list)<len(questionDict[page.data.index]['answer']):

        # 如果用户的剩余金币数量>5
        if page.data.userCoin >=5:
            # 获取值为0的格子的下标
            l = [idx for idx, e in enumerate(page.data.flag_list) if e==0]
            # 从正确答案中还没有填写的位置随机取出一个字
            wordPos = random.sample(l, 1)[0]
            ans = questionDict[page.data.index]['answer'][wordPos] #获取wordPos答案
            
            # 将 提示字 显示在答案格子中正确的位置，并且从下方备选格子中抹去
            # 首先找到该字在备选格子中的下标tmp_tag
            tmp_tag = 0
            for t in range(24):
                if ans == page.data.show_data[t]['word']:
                    tmp_tag = t

            # 设置 答案格子 中的提示字
            page.data.anslist[wordPos]['text'] = page.data.show_data[tmp_tag]['word']
            # 刷新页面数据
            page.anslist.data = page.data.anslist

            # 并记录下该字的信息
            page.data.answer[wordPos]= [tmp_tag, page.data.show_data[tmp_tag]['word']]
            # 将该字所占位子的标志 置位
            page.data.flag_list[wordPos] = 1
            
            # ??
            page.data.flag_list = page.data.flag_list

            # 在下方备选格子中将该字 所在的格子 置位空 并刷新页面数据
            page.data.show_data[tmp_tag]['word'] = ''
            page.dataGrid.data = page.data.show_data
            page.data.show_data = page.dataGrid.data

            # ??
            page.data.answer = page.data.answer

            # 减掉金币数量 并刷新页面文字
            page.data.userCoin = page.data.userCoin - 30
            page.coin.text = '💰金币:%s' % page.data.userCoin
            
            # 修改数据库信息
            mo.db.guess.update(mo.db.guess.find({'openid':user.openid})[0]['id'],{
                            'coin': page.data.userCoin})

            if sum(page.data.flag_list) == len(questionDict[page.data.index]['answer']):
                # 如果答案格子填充满了
                ans = ''
                for v in page.data.answer:
                    ans = ans + v[-1]

                # 如果该答案与正确答案相符合
                if ans == questionDict[page.data.index]['answer']:
                    
                    # 将当前题目编号加入历史队列中
                    tmp = page.data.index_list
                    tmp.append(page.data.index)
                    page.data.index_list = tmp

                    # 添加金币
                    page.data.userCoin = page.data.userCoin + 10
                    page.coin.text = '💰金币:%s' % page.data.userCoin

                    mo.db.guess.update(mo.db.guess.find({'openid':user.openid})[0]['id'],{
                            'coin': page.data.userCoin})

                    mo.toplist.pushDaily('toplist_coin',user.openid,page.data.userCoin,{'name':user.nickName,'coin':page.data.userCoin, 'avatarUrl': user.avatarUrl})
                    # 设置用户答题状态
                    user.set('index_list_v2', page.data.index_list)
                    mo.console('点击提示，答题正确、添加金币、设置用户答题状态')

                    # 如果答完全部题目，跳转到结果页面
                    if (user.index_list_v2==(len(questionDict))):
                        mo.redirectTo('resultPage')
                        return

                     # 如果答对的题目数量 是 10 的 整数倍 开启蒙层显示，如果不是，立即跳转到下一题
                    if len(user.index_list_v2) % 10 == 0 :
                        #提示用户闯到第几关了
                        page.current_count.text = '{}'.format(len(user.index_list_v2))
                        page.data.current_countText = page.current_count.text
                        page.percent.text = str(random.randint(80, 100)) + '%'
                        page.data.percentText = page.percent.text

                        # 根据答题数量 索引对应的等级
                        index = int(len(user.index_list_v2) / 10) % len(honorary_title_group)
                        page.honorary_title.text = honorary_title_group[index]['level'] + ' ' + honorary_title_group[index]['title']
                        page.data.honorary_titleText = page.honorary_title.text
                        onMakeImage(user, app, page, mo)
                        page.mask01.hidden = False
                        mo.console('set mask01hidden = false')
                        # 将用户等级记录到数据库中
                        user.set('level_title', honorary_title_group[index])
                        

                    else :
                        mo.console("index is {}".format(len(user.index_list_v2)))
                        # 否则 跳转到 猜题页面，并将当前已答过的题目序列 作为参数传入
                        mo.redirectTo('GuessPage',  num=int(page.options.num)+1)

                    mo.console('HHHHHHHHH')
                        
                    return
                else:
                    mo.showAlert('❌答错了', '答案不正确哦，再仔细想想吧')
        else:
            mo.showTips('分享增加金币~', 3000)
    else:
        mo.showTips('请先删除错误答案', 2000)

# 点击上方答案格触发函数，每点一个词，该点击格为空，该词回到24个备选格
async def onAnswerClick(user, app, page, mo, params):
    mo.console(params.id)
    # params.id 为被点击的格子的下标

    # 如果该格子是填写过的
    if page.data.flag_list[params.id]:

        #将该格子中的文字 置位为空 并刷新页面数据
        page.data.anslist[params.id]['text'] = ''
        page.anslist.data = page.data.anslist

        # 取出该格子中的字的记录信息[pos,word]
        changeList = page.data.answer[params.id]
        page.data.answer[params.id] = []
        page.data.answer = page.data.answer

        # 将取出来的字 还原到备选格子中原来的位置 并刷新页面数据
        page.data.show_data[changeList[0]]['word'] = changeList[1]
        page.dataGrid.data = page.data.show_data
        page.data.show_data = page.dataGrid.data

        # 置该答案格子的填写状态为0，表示未填写
        page.data.flag_list[params.id] = 0
        page.data.flag_list = page.data.flag_list

# 24个备选格点击触发函数，每点一个词，填充上方首个空缺格，该点击格子随后为空
async def onClick(user, app, page, mo, params):
    # params.tag 为备选格子中用户按下的格子编号
    tag = params.tag

    # 如果该格子的内容不为空，之前没有被选过
    if page.data.show_data[tag]['word']:
        # 查找答案格子中 下标最小且没有填入内容的格子 下标
        for i in range(len(questionDict[page.data.index]['answer'])):
            if page.data.flag_list[i] == 0:
                page.data.pos = i
                break
        #if page.data.pos == 0:
            #page.ans0.text = page.data.show_data[tag]['word']
        pi = page.data.pos

        # 将被点击的备选格子中的字填入 答案格子中 下标最小且没有填入内容的格子
        page.data.anslist[pi]['text'] = page.data.show_data[tag]['word']

        # 并将该字原来在备选格子中的信息[pos,word]存入page.data.answer
        page.data.answer[pi]= [tag, page.data.show_data[tag]['word']]

        # 置该答案格子的填写状态为1，表示已填写
        page.data.flag_list[pi] = 1
        page.data.flag_list = page.data.flag_list

        # 将备选格子中的文字置为空字符串
        page.data.show_data[tag]['word'] = ''
        page.dataGrid.data = page.data.show_data
        page.data.show_data = page.dataGrid.data

        page.data.answer = page.data.answer
        page.anslist.data = page.data.anslist

        # 如果答案格子填充满了
        if sum(page.data.flag_list) == len(questionDict[page.data.index]['answer']):
            ans = ''
            for v in page.data.answer:
                ans = ans + v[-1]

            # 如果该答案与正确答案相符合
            if ans == questionDict[page.data.index]['answer']:
                tmp =  page.data.index_list
                tmp.append(page.data.index)
                page.data.index_list = tmp

                # 添加金币
                page.data.userCoin = page.data.userCoin + 10
                page.coin.text = '💰金币:%s' % page.data.userCoin

                mo.db.guess.update(mo.db.guess.find({'openid':user.openid})[0]['id'],{
                            'coin': page.data.userCoin})
                # 设置用户答题状态
                user.set('index_list_v2', page.data.index_list)
                mo.console('点击备选格子，答题正确、添加金币、设置用户答题状态')

                # 如果答对的题目数量 是 10 的 整数倍 开启蒙层显示，如果不是，立即跳转到下一题
                if len(user.index_list_v2) % 10 == 0 :
                    #提示用户闯到第几关了
                    page.current_count.text = '{}'.format(len(user.index_list_v2))
                    page.data.current_countText = page.current_count.text
                    page.percent.text = str(random.randint(80, 100)) + '%'
                    page.data.percentText = page.percent.text
                    # 根据答题数量 索引对应的等级
                    index = int(len(user.index_list_v2) / 10) % len(honorary_title_group)
                    page.honorary_title.text = honorary_title_group[index]['level'] + ' ' + honorary_title_group[index]['title']
                    page.data.honorary_titleText = page.honorary_title.text
                    onMakeImage(user, app, page, mo)
                    page.mask01.hidden = False
                    mo.console('set mask01hidden = false')
                    # 将用户等级记录到数据库中
                    user.set('level_title', honorary_title_group[index])
                else :
                    # 否则 跳转到 猜题页面，并将当前已答过的题目序列 作为参数传入
                    mo.console("index is {}".format(len(user.index_list_v2)))
                    mo.redirectTo('GuessPage',  num=int(page.options.num)+1)

                mo.console('HHHHHHHHH')

                # 如果答完全部题目，跳转到结果页面
                if (user.index_list_v2==(len(questionDict))):
                    mo.redirectTo('resultPage')
                    return

                return
            else:
                mo.showAlert('❌答错了', '答案不正确哦，再仔细想想吧')

async def onResultReady(user, app, page, mo):
    canvas = mo.mopic.createCanvas(720, 980)
    canvas.addImage('http://material.motimaster.com/liuhongjie1532920564000/通关页保存.jpg', pos=[0, 0], size=[720, 980])
    canvas.addImage(user.avatarUrl, size=[150, 150], pos=[285, 35], mask='circle')
    canvas.addText(user.nickName, pos=[260, 190, 200], textAlign='center', width=200, color='#000000')
    canvas.addText('你是真正阅片无数的老司机吗？\n这些影视作品你都看过多少？快来挑战一下吧！',
        fontSize=28, pos=[15, 850, 600], color='#000000')

    params = {
        'page':'mainPage',
        'width': 150,
    }
    retParams = mo.acode.getWxAcodeUrl(params)
    erweima = None
    if retParams['ret'] == 0:
        erweima = retParams['url']
    canvas.addImage(erweima, pos=[595, 850, 100, 100], mask='circle')
    res = canvas.makeImage()

    if res['ret'] == 0:
        page.data.set('url', res['url'])
        mo.console(res['url'])

    page.share.title = "您的好友"+ user.nickName+ "已经通关！快来挑战TA！"
    page.share.page = 'mainPage'

async def onSaveImage(user, app, page, mo):
    url = page.data.get('url')
    mo.saveImage(url)


# 随机挑选出五个成语，并返回一个问答的index
def pick():
    rand_list = random.sample(range(len(idiom)),6)
    candidatePool = ''
    for i in rand_list:
        candidatePool += idiom[i]
    return candidatePool

# 打乱每个词的顺序
def order_random(word_list):
    return random.sample(random.sample(word_list,len(word_list)),len(word_list)) # 两次打乱、更加无序

questionDict = [
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796639000/还珠格格.gif',
        'answer': '还珠格格'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533088069000/武林外传.gif',
        'answer':'武林外传'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798019000/新白娘子传奇.gif',
        'answer':'新白娘子传奇'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533044338000/爱情公寓.gif',
        'answer':'爱情公寓'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533881110000/9.1一起来看流星雨.gif',
        'answer':'一起来看流星雨'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796812000/欢乐颂.gif',
        'answer': '欢乐颂'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533087940000/情深深雨濛濛.gif',
        'answer':'情深深雨濛濛'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797960000/仙剑奇侠传一.gif',
        'answer':'仙剑奇侠传一'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532796158000/步步惊心.gif',
        'answer':'步步惊心'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532654930000/三生三世十里桃花.gif',
        'answer': '三生三世十里桃花'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796856000/加勒比海盗.gif',
        'answer': '加勒比海盗'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532796107000/变形金刚.gif',
        'answer':'变形金刚'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532600922000/爱乐之城.gif',
        'answer':'爱乐之城'
    },
    {
        'image_src': 'http://material.motimaster.com/harvey/5455/myrose/3bb6e4e1c3254d03ed7b4042801a8744.gif',
        'answer': '东方不败',
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533044392000/大话西游之大圣娶亲.gif',
        'answer':'大话西游二'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796919000/爵迹.gif',
        'answer': '爵迹'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532859738000/泰囧.gif',
        'answer':'泰囧'
    },
    {
        'image_src': 'http://material.motimaster.com/harvey/5455//677b08e6a1fed0cd2dfd44e0d4071718.gif',
        'answer': '东成西就'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796544000/复仇者联盟.gif',
        'answer': '复仇者联盟'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797749000/我不是药神.gif',
        'answer':'我不是药神'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796474000/恶作剧之吻.gif',
        'answer': '恶作剧之吻',
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798134000/延禧攻略.gif',
        'answer':'延禧攻略'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532797018000/亮剑.gif',
        'answer': '亮剑'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533044362000/白夜追凶.gif',
        'answer':'白夜追凶'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532857673000/金枝欲孽.gif',
        'answer': '金枝欲孽'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797455000/太阳的后裔.gif',
        'answer':'太阳的后裔'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798222000/甄嬛传.gif',
        'answer':'甄嬛传'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533881411000/春风十里不如你.gif',
        'answer':'春风十里不如你'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889218000/凤囚凰.gif',
        'answer':'凤囚凰'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797368000/神雕侠侣.gif',
        'answer':'神雕侠侣'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889914000/泰坦尼克号.gif',
        'answer': '泰坦尼克号'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798068000/猩球崛起.gif',
        'answer':'猩球崛起'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532857479000/小时代.gif',
        'answer':'小时代'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797394000/十面埋伏.gif',
        'answer':'十面埋伏'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532796251000/春娇与志明.gif',
        'answer':'春娇与志明'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797547000/唐伯虎点秋香.gif',
        'answer':'唐伯虎点秋香'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797895000/西游降魔篇.gif',
        'answer':'西游降魔篇'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797599000/唐人街探案二.gif',
        'answer':'唐人街探案二'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797811000/无间道.gif',
        'answer':'无间道'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533888628000/头号玩家.gif',
        'answer':'头号玩家'
    },
    

    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797689000/微微一笑很倾城.gif',
        'answer':'微微一笑很倾城'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797931000/仙剑奇侠传三.gif',
        'answer':'仙剑奇侠传三'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532796332000/盗墓笔记.gif',
        'answer':'盗墓笔记'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533088025000/我的前半生.gif',
        'answer':'我的前半生'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796779000/花千骨.gif',
        'answer': '花千骨'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796713000/何以笙箫默.gif',
        'answer': '何以笙箫默'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889546000/致我们单纯的小美好.gif',
        'answer': '致我们单纯的小美好'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532858345000/金粉世家.gif',
        'answer': '金粉世家'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797487000/太子妃升职记.gif',
        'answer':'太子妃升职记'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533087984000/杉杉来了.gif',
        'answer':'杉杉来了'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796990000/了不起的盖茨比.gif',
        'answer': '了不起的盖茨比'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796740000/红海行动.gif',
        'answer': '红海行动'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797252000/让子弹飞.gif',
        'answer':'让子弹飞'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797429000/食神.gif',
        'answer':'食神'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798099000/羞羞的铁拳.gif',
        'answer':'羞羞的铁拳'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798042000/星际穿越.gif',
        'answer':'星际穿越'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796887000/剪刀手爱德华.gif',
        'answer': '剪刀手爱德华'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533888534000/暮光之城.gif',
        'answer': '暮光之城'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798254000/终结者.gif',
        'answer':'终结者'
    },
    {
        'image_src': 'http://material.motimaster.com/harvey/5455/myrose/244f7f8f06b3779282514a12996394c4.gif',
        'answer': '疯狂的石头'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532797133000/芈月传.gif',
        'answer': '芈月传'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796599000/古剑奇谭.gif',
        'answer': '古剑奇谭'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889613000/择天记.gif',
        'answer': '择天记'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889128000/大唐荣耀.gif',
        'answer': '大唐荣耀'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533044428000/老九门.gif',
        'answer': '老九门'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532860542000/伪装者.gif',
        'answer':'伪装者'
    },
     {
        'image_src':'http://material.motimaster.com/liuhongjie1533889815000/扶摇.gif',
        'answer':'扶摇'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889170000/风云雄霸天下.gif',
        'answer':'风云雄霸天下'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798168000/余罪.gif',
        'answer':'余罪'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533881323000/楚乔传.gif',
        'answer':'楚乔传'
    },


    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889909000/生化危机.gif',
        'answer': '生化危机',
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889900000/老炮儿.gif',
        'answer': '老炮儿',
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889496000/釜山行.gif',
        'answer':'釜山行'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533889922000/我的少女时代.gif',
        'answer': '我的少女时代',
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798162000/英雄本色.gif',
        'answer':'英雄本色'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889448000/地心历险记2.gif',
        'answer':'地心历险记2'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798199000/战狼二.gif',
        'answer':'战狼二'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532798294000/捉妖记.gif',
        'answer':'捉妖记'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532797059000/龙门飞甲.gif',
        'answer': '龙门飞甲'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532600865000/2012.gif',
        'answer':'2012'
    },


    {
        'image_src':'http://material.motimaster.com/liuhongjie1533044469000/人民的名义.gif',
        'answer':'人民的名义'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889773000/烈火如歌.gif',
        'answer':'烈火如歌'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889670000/香蜜沉沉烬如霜.gif',
        'answer':'香蜜沉沉烬如霜'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532797157000/那年花开月正圆.gif',
        'answer': '那年花开月正圆'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1533881219000/白鹿原.gif',
        'answer': '白鹿原'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1533889415000/V字仇杀队.gif',
        'answer':'V字仇杀队'
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532796418000/敦刻尔克.gif',
        'answer': '敦刻尔克',
    },
    {
        'image_src': 'http://material.motimaster.com/liuhongjie1532797107000/驴得水.gif',
        'answer': '驴得水'
    },
    {
        'image_src':'http://material.motimaster.com/liuhongjie1532797658000/旺角卡门.gif',
        'answer':'旺角卡门'
    }, 

]
# 成语库
idiom = ['十月围城','逃学威龙','天龙八部','邪不压正','烈日灼心','雪国列车','幕后玩家',
         '一步之遥','乘风破浪','霸王别姬','大鱼海棠','阿甘正传','记忆大师','喜剧之王',
         '一代宗师','窃听风云','阿甘正传','怦然心动','匆匆那年','道士下山','倩女幽魂']

# 24个格子 done
# 随机从成语库中挑选5个成语+一个正确答案 done
# 随机打乱顺序，输出一个24维数组 done
# text 按照顺序赋值 done
# 对比正确答案 done
# 能否给位置动态赋值 done