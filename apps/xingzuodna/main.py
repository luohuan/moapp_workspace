drama={'测试' :[
    {
        #问题
        'title': '1/3 平时打瞌睡你都是用哪种姿势？',
        'img': 'http://material.motimaster.com/appmaker/qiutianrui/5574.jpg',
        #选项
        'options': [
        {'text': ' 双手交叉型', 'value': '1'},
        {'text': '手肘撑脸型', 'value': '2'},
        {'text': '燃烧殆尽型', 'value': '3'},
        {'text': '自我世界型', 'value': '4'}
    
    ],
        #答案(是第几个)，不需要调用答案的值时，可以不用填
       #'answer': 4
    },
    {
        'title': '2/3 你认为云朵停在哪一处，画面才会更完美？',
        'img': 'http://material.motimaster.com/appmaker/qiutianrui/5576.jpg',
        'options': [
        {'text' : '1' , 'value':'1'},
        {'text' : '2' , 'value':'2'},
        {'text' : '3' , 'value':'3'},
        {'text' : '4' , 'value':'4'}
    
    ],
        #'answer': 2
    },
    {
        'title': '3/3 当你这森林里探险，其中哪一条路更吸引你？',
        'img': 'http://material.motimaster.com/appmaker/qiutianrui/5575.png',
        'options':[
        {'text' : '花丛中的路。', 'value' : '1'},
        {'text' : '通往山顶的山路。' , 'value': '2'},
        {'text' : '小丛林中下山的路。' , 'value': '3'},
        {'text' : '山脚下的大道。' , 'value': '4'}
      

    ],
        #'answer': 2
    },
    # {
    #     #问题
    #     'title': '4/6 大家一起吃饭的时候，你是',
    #     #选项
    #     'options': [
    #     {'text': '张罗点菜的人', 'value': '1'},
    #     {'text': '主动点自己喜欢的菜', 'value': '2'},
    #     {'text': '无所谓，总有自己喜欢吃的', 'value': '3'},
    #     {'text': '考虑价位', 'value': '4'}
    # ],
    #     #答案(是第几个)
    #     #'answer': 4
    # },
    #  {
    #     #问题
    #     'title': '5/6 一个人独处的时候，你会觉得',
    #     #选项
    #     'options': [
    #     {'text': '偶尔会享受一下', 'value': '1'},
    #     {'text': '心中忐忑不安', 'value': '2'},
    #     {'text': '很无聊而且孤单', 'value': '3'},
    #     {'text': '很正常啊，人就是孤独的', 'value': '4'}
    # ],
    #     #答案(是第几个)
    #     #'answer': 4
    # },
    #  {
    #     #问题
    #     'title': '6/6 几个同事正在讨论一个很恐怖的故事，你会',
    #     #选项
    #     'options': [
    #     {'text': '宛如身临其境的倾听', 'value': '1'},
    #     {'text': '讲一个更恐怖的故事', 'value': '2'},
    #     {'text': '安慰她们没什么可怕的', 'value': '3'},
    #     {'text': '绝对对方很幼稚很可笑', 'value': '4'}
    # ],
    #     #答案(是第几个)
    #     #'answer': 4
    # },

]
}#题目数量在模板代码里只设置了6题，A记为1分，B记为2分，C记为3分，D记为4分，因此分数范围是1——24分，所以如果需要增加题目数量，则需要同时在def onNxet里扩展（修改）分数范围，并且增加（修改）相应的图片数量
 #例如:题目数量为7的时候，分数范围应该是1——28;题目数量为8的时候，分数范围为1——32。

img_int= [
'http://material.motimaster.com/willing/goodguys/create/18fde2a7e86342782189b717c59bebe1.jpg',
'http://material.motimaster.com/willing/goodguys/create/1f57ca5d28db2dc1df3fc3a20b2bd48c.jpg',
'http://material.motimaster.com/willing/goodguys/create/345649752cd2340d70b9691601297644.jpg',
'http://material.motimaster.com/willing/goodguys/create/be259cc5916b89c38c8122ace2a91547.jpg',
'http://material.motimaster.com/willing/goodguys/create/3bb31662a516f0e019f4600abe4efd21.jpg',
'http://material.motimaster.com/willing/goodguys/create/c9d490b6591552eb05bcb07d6e16f179.jpg',
'http://material.motimaster.com/willing/goodguys/create/55a36724d913ac1902e9aab24d5dba47.jpg',
'http://material.motimaster.com/willing/goodguys/create/846079e0cc9f33b31f417588cd732474.jpg',
'http://material.motimaster.com/willing/goodguys/create/ce09c9c91d64ad42198704d61730b933.jpg',
'http://material.motimaster.com/willing/goodguys/create/a94e8b705d4f49d4e6685799a87fce3f.jpg',
'http://material.motimaster.com/willing/goodguys/create/58df338719afc637be6c1ef11d31e0ef.jpg',
'http://material.motimaster.com/willing/goodguys/create/d74134bca946ead82715f52d5c00eb4e.jpg',
'http://material.motimaster.com/willing/goodguys/create/0381a9398a814017f74b9060d76fdbc2.jpg',
'http://material.motimaster.com/willing/goodguys/create/3374e14d5cd3cebe15f2028d8a801a2f.jpg',
'http://material.motimaster.com/willing/goodguys/create/b048f740b7d9cd47512a544202414fe9.jpg',
'http://material.motimaster.com/willing/goodguys/create/d923cf18eb057c28555f0d6d4c0aaf93.jpg'
]

baiyang = 'http://material.motimaster.com/appmaker/qiutianrui/5548.jpg'

jinniu='http://material.motimaster.com/appmaker/qiutianrui/5549.jpg'

shuangzi='http://material.motimaster.com/appmaker/qiutianrui/5550.jpg'

juxie='http://material.motimaster.com/appmaker/qiutianrui/5551.jpg'

shizi='http://material.motimaster.com/appmaker/qiutianrui/5552.jpg'

chunv='http://material.motimaster.com/appmaker/qiutianrui/5553.jpg'

tiancheng='http://material.motimaster.com/appmaker/qiutianrui/5554.jpg'

tianxie='http://material.motimaster.com/appmaker/qiutianrui/5555.jpg'

sheshou='http://material.motimaster.com/appmaker/qiutianrui/5556.jpg'

mojie='http://material.motimaster.com/appmaker/qiutianrui/5557.jpg'

shuiping='http://material.motimaster.com/appmaker/qiutianrui/5558.jpg'

shuangyu='http://material.motimaster.com/appmaker/qiutianrui/5559.jpg'

xingzuo = [
    [baiyang,   '0321', '0419'],
    [jinniu,    '0420', '0520'],
    [shuangzi,  '0521', '0621'],
    [juxie,     '0622', '0722'],
    [shizi,     '0723', '0822'],
    [chunv,     '0823', '0922'],
    [tiancheng, '0923', '1023'],
    [tianxie,   '1024', '1122'],
    [sheshou,   '1123', '1221'],
    [mojie,     '1222', '1231'],
    [mojie,     '0101', '0119'],
    [shuiping,  '0120', '0218'],
    [shuangyu,  '0219', '0320']
]

soc = []
for i in range(60,101):
    soc.append(i)

xingzuo2 = [
'http://material.motimaster.com/appmaker/qiutianrui/3990.png',

'http://material.motimaster.com/appmaker/qiutianrui/3992.png',

'http://material.motimaster.com/appmaker/qiutianrui/3998.png',

'http://material.motimaster.com/appmaker/qiutianrui/3993.png',

'http://material.motimaster.com/appmaker/qiutianrui/4003.png',

'http://material.motimaster.com/appmaker/qiutianrui/3991.png',

'http://material.motimaster.com/appmaker/qiutianrui/4000.png',

'http://material.motimaster.com/appmaker/qiutianrui/4001.png',

'http://material.motimaster.com/appmaker/qiutianrui/4006.png',

'http://material.motimaster.com/appmaker/qiutianrui/3981.png',

'http://material.motimaster.com/appmaker/qiutianrui/4008.png',

'http://material.motimaster.com/appmaker/qiutianrui/4008.png',

'http://material.motimaster.com/appmaker/qiutianrui/4007.png',
]

months = [['01月', '02月','03月','04月','05月', '06月','07月','08月','09月','10月','11月','12月'], ['01日', '02日', '03日', '04日', '05日','06日', '07日', '08日', '09日', '10日','11日', '12日', '13日', '14日','15日','16日', '17日', '18日', '19日', '20日','21日', '22日', '23日', '24日','25日', '26日', '27日', '28日', '29日','30日','31日']] 
AUDITING = True # 审核模式的开关
def main():
    with MoApp(appid='', name='星座DNA'):#设置小程序的基本信息
        
        with Page(name='first',background='http://material.motimaster.com/appmaker/qiutianrui/5568.jpg'):#第一个页面的名称和背景图
            with Button(effect=pulse(t=1,c=0),type='primary', pos=[275,700],text='开始测试',boxShadow='5px 5px 7px #7c9199',background='#ff99cc',size=[200,200],borderRadius = '50%',lineHeight = 200,openType='getUserInfo'):
                this.onTap = moui.goto('select',drama_list = '测试' )#首页的button，跳转到paper页面，同时读取的是上面准备的list内容
        with Page(name='select',background='http://material.motimaster.com/appmaker/qiutianrui/5569.jpg', onReady=[setdata]):    
            with MultiSelectorPickerButton(id='picker',text='点击选择',range=months,type='primary',background='#ff99cc',pos=['center',650],
                size=[200,80],color='white',fontSize=40,lineHeight=80,effect=pulse(t=1,c=0),boxShadow='5px 5px 7px #7c9199'):
                    this.onChange = [save_birth, moui.goto('paper',drama_list = '测试' )]
        
        with Page(name='paper',onReady =[ moui.showLoading('题目加载中'),RadioPageready ,moui.hideLoading()],background='http://material.motimaster.com/appmaker/qiutianrui/5481.jpg'):
            with MoRadio(name = 'radio3',pos=[70,600, 620, 140],fontSize = 35):#选项部分，选项被命名为radio3，下一步用云函数调用
                this.onChange = onNext
            Text(name = 'radiotext',padding=30,pos=[70,30],backgroundColor='#fbfdf7',fontSize = 35,borderRadius= '10px 10px 10px 10px',color = '#040404',width =600,lineHeight= 50)#题目部分被命名为radiotext，通过云函数调用
            Image(name = 'radioim',padding=30,pos=['center',250],size=[300,300])

        with Page(name='pageX',enableShare=True,onReady= [moui.showLoading('正在生成中'),onReadyPicPage, moui.hideLoading()],backgroundColor='#151c38'):#成绩单页面
            with Box(pos=[0, 0], width=750, height=750):#放置整个图片的box
                Image(id='mopicImage',pos=[0,0],size=[750,1206])#设置image的ID，通过云函数获取。
            with Box(pos=[0, 0], width=750, height=750):
                ShareButton(pos=[115, 1100, 200, 60],type='miniDefault',text='分享',color='#ffffff' ,fontSize = 26,lineHeight=60,background='#A2E3F7')#分享button
            #Text(name = 'birthday',pos=[70,80], color='black')
            Button(text='保存图片', pos=[435,1100,200,60],background='#F29EC2', color='#ffffff' ,type='miniDefault',fontSize = 26,lineHeight=60,onTap=onSaveImage)#保存图片的button

async def setdata(user,app,page,mo):
    #page.picker.range = months
    pass

async def save_birth(user,app,page,mo):
    chooseResult = months[0][page.picker.value[0]] + months[1][page.picker.value[1]]
    user.set('birth', chooseResult)


async def RadioPageready(user,app,page,mo):#页面题目准备
    questions = drama[page.options.drama_list]#获取字典的内容

    page.data.set('pagenum',0)#设置第几题
    page.data.set('curnum',0)#当前第几题
    user.set('ans',[])
    page.radiotext.text = questions[0]['title']
    page.radio3.data = questions[0]['options']
    page.radioim.src = questions[0]['img']

async def onNext(user,app,page,mo):#答题&计分&结果判断
    questions = drama[page.options.drama_list]#定义问题
    pagenum = page.data.get('pagenum')#第几道题
    curnum = page.data.get('curnum')#答对了几题

    ans = user.get('ans')   
    ans.append(page.radio3.value)
    user.set('ans',ans)#记录用户选的答案
    page.data.set('curnum',curnum)
    pagenum +=1
    if pagenum >= len(questions):
        ansint = 0
        for row in ans:
            ansint += int(row)
        k = 0 #标记开始
        for i in [6,8,10,12,14,16,17,19,21,23,24]:
            if ansint <= i:
                break
            k += 1 #判断下一个图片
        user.set('imgurl',random.choice(img_int))
        mo.goto('pageX') 
        return
    page.data.set('pagenum',pagenum)
    page.radiotext.text = questions[pagenum]['title']
    page.radio3.data = questions[pagenum]['options']
    page.radioim.src = questions[pagenum]['img']
#生成成绩单&添加二维码&添加用户昵称&分享页面设置
async def onReadyPicPage(user,app,page,mo):
    # 获取生日对应的图片
    msg = user.get('birth')[0:2] + user.get('birth')[-3:-1]
    nickname = user.nickName
    #age.birthday.text = msg
    if len(msg) == 4 and msg.isdigit():
        bg = None
        for item in xingzuo:
            if item[1] <= msg <= item[2]:
                bg = bgboy = item[0]
                break
        if bg:
            otherimg = chooseby(xingzuo2, nickname)
            x = 0 
            y = 0
            for i in xingzuo:
                if i[0] == bg:
                    break
                else:
                    x+=1 
            for i in xingzuo2:
                if i == otherimg:
                    break
                else:
                    y+=1
            if x==y:
                otherimg = xingzuo2[(y+3)%13]

    # 分数
    soc1 = chooseby(soc,nickname)
    soc2 = 100 - soc1
    soc1 = str(soc1)
    soc2 = str(soc2)
    mo.console(bg +  ';   ' + otherimg)
    # imgsrc = random.choice(seq)
    #imgsrc = user.get('imgurl')
    #创建最后展示页的画布
    canvas = mo.mopic.createCanvas(750, 1206,saveStrategy='permanent')
    #在画布上加上背景图
    canvas.addImage(bg, pos=[0, 0, 750, 1206])
    canvas.addImage(otherimg, pos=[375, 0, 750, 1206])
    #canvas.addImage(imgsrc, pos=[0, 0, 750, 1206])
    #在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=[300,150,160,160],mask='circle')
    #在画布上加上文字
    canvas.addText(user.nickName, pos=[230, 320,280], fontSize=50,color=(0, 0, 0),align='center',fontWeight=50)
    canvas.addText(soc1 + '%', pos=[10, 400,280], fontSize=80,color=(0, 0, 0),align='center',fontWeight=50)
    canvas.addText(soc2 + '%', pos=[360, 400,280], fontSize=80,color=(0, 0, 0),align='center',fontWeight=50)
    #res = canvas.makeImage()

    #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
    erweima = None
    if AUDITING == False:
        params = {
            'page': 'first',
            'width': 150,
            'options':{'a':1,'b':user.nickName}
        }
        retParams = mo.acode.getWxAcodeUrl(params)    
        if retParams['ret'] == 0:
            erweima = retParams['url']

        #把二维码添加到画布上
        canvas.addImage(erweima, pos=[324,1090,90, 90])
    canvas.addText('长按识别此码', pos=[130, 1110], fontSize=28, color=(0, 0, 0))
    canvas.addText('获取星座DNA', pos=[435, 1110], fontSize=28, color=(0, 0, 0))

    #生成图片
    res_erweima = canvas.makeImage()

    #判断生成图片是否成功
    if res_erweima['ret'] == 0:
        #在页面上展示结果图
        page.mopicImage.src = res_erweima['url']
        #生成“保存图片”按钮操作需要的图片链接
        page.data.set('url',res_erweima['url'])

    #设置页面分享的标题、图片、用户进入页、传递的参数 
    page.share.title = user.nickName + "送你一只福粽"
    page.share.imageUrl = 'http://material.motimaster.com/willing/goodguys/create/6740f046701238e90d485bbdfd666a01.jpg'
    page.share.page = 'first'
    page.share.options = {'a':1,'b':user.nickName}

#点击“保存图片”按钮的操作
async def onSaveImage(user, app, page, mo):
    url = page.data.get('url')#提取分享图片的地址
    mo.saveImage(url)
    # pass

def chooseby(offers,keys):
    index = 0
    charCode = 0
    msg_length = len(keys)#获取输入字符的长度
    for index in range(msg_length):
        charCode += int(ord(keys[index]))
    key = offers[(int(charCode%(len(offers))))] #显示结果的下标 从0开始
    return key