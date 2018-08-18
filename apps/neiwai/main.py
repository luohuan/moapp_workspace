drama={'测试' :[
    {
        'title': '1/3 第一眼，你先看到的是？',
        'url':'http://material.motimaster.com/liuhongjie1533616920000/133cb8bed9857cc4e5cc93a56607a4e4.png',
        #选项
        'options': [
        {'text': '小人', 'value': '1'},
        {'text': '箭头', 'value': '2'}
    ],
        #答案(是第几个)，不需要调用答案的值时，可以不用填
       #'answer': 4
    },
    {
        'title': '2/3 下面这五个水桶，哪个会最先装满？',
        'url':'http://material.motimaster.com/liuhongjie1533617052000/f93696919624c1f835f407473b8fd618.jpg',
        'options': [
        {'text' : '1' , 'value':'1'},
        {'text' : '2' , 'value':'2'},
        {'text' : '3' , 'value':'3'},
        {'text' : '4' , 'value':'4'},
        {'text' : '5' , 'value':'5'}
    ],
        #'answer': 2
    },
    {
        'title': '3/3 下面哪一幅日出让你觉得最温暖？',
        'url': 'http://material.motimaster.com/liuhongjie1533617210000/1f9f146966051924712c5f8dee596dd7.jpg',
        'options':[
        {'text' : '1' , 'value' : '1'},
        {'text' : '2' , 'value': '2'},
        {'text' : '3' , 'value': '3'},
        {'text' : '4' , 'value': '4'},
    ],
        #'answer': 2
    },
]
}#题目数量在模板代码里只设置了6题，A记为1分，B记为2分，C记为3分，D记为4分，因此分数范围是1——24分，所以如果需要增加题目数量，则需要同时在def onNxet里扩展（修改）分数范围，并且增加（修改）相应的图片数量
 #例如:题目数量为7的时候，分数范围应该是1——28;题目数量为8的时候，分数范围为1——32。
# erweima='http://material.motimaster.com/yuyuan/Duudle/create/e0605c1fef0f25244897b341a488a602.jpg'
pictman=[
    'http://material.motimaster.com/hn131/dongwuxi/main/533cfc1d0100fd248784fe1b311cb6ff.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/a21af8aa3fcf12a592b35773629bddf3.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/598588cb7f124afa75c70ae6f5bfa20a.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/2cab0ec7c15f47bcc87277e4a8476d16.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/53718f70f5b9565080183405fee89455.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/85fccc65ad6b2103136883889e05d46b.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/b23e0cba071ef3edda8fb26d4d9dde1d.jpg'
]

pictwoman=[
    'http://material.motimaster.com/hn131/dongwuxi/main/c3a00d0af7c3dd68e114bd69c3c16c5a.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/f1e5867b0c234b966bd79378c2cd2b8c.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/5eed067fc2e10192d82f262cddba2801.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/8928a57186a16dd2bf5f708a0b8dbceb.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/f1feea35559f3dc6fd2bc4e4bf02cb52.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/7c561907e327d359af7374b2d189c92e.jpg',
    'http://material.motimaster.com/hn131/dongwuxi/main/ba10493bdca6b69308ff473a87e55c8e.jpg'
]

erweimas = [
    'http://material.motimaster.com/5b6950d314506251099713fd.jpg',
    'http://material.motimaster.com/5b6950dd145062510ae3bb1e.jpg',
    'http://material.motimaster.com/5b6950de145062510ae3bb1f.jpg',
]


AUDITING = False

def main():
    with MoApp(appid='wxe2deea3328cc56e0', name='内外在年龄'):#设置小程序的基本信息
        with Page(name='first', background='http://material.motimaster.com/liuhongjie1533613403000/内外在-首页.jpg',onReady=firstReady):#第一个页面的名称和背景图
            Image(name='ggg',hidden=True, src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg',size=[750,125],pos=[0,0],onTap=ongg)
            with Button(text='开始测试', effect=pulse(t=1, c=0), pos=['center', 800], boxShadow='5px 5px 7px #7c9199', background='#ffffff', color='#000000', size=[200,200], borderRadius='50%', lineHeight=200, openType='getUserInfo'):
                this.onTap = moui.goto('paper', drama_list='测试')#首页的button，跳转到paper页面，同时读取的是上面准备的list内容
        with Page(name='paper', onReady=[moui.showLoading('题目加载中'), RadioPageready, moui.hideLoading()], background='http://material.motimaster.com/liuhongjie1533622143000/内外在-答题.jpg'):
            Image(name='ggg',hidden=True, src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg',size=[750,125],pos=[0,0],onTap=ongg)
            Image(name='hhh',hidden=False,size=[500,400],pos=['center',230])
            with MoRadio(name='radio3', pos=[70, 580, 620, 100], fontSize=35):#选项部分，选项被命名为radio3，下一步用云函数调用
                this.onChange = onNext
            Text(name='radiotext', pos=[70, 150], backgroundColor='#fbfdf7', fontSize=35, borderRadius='10px 10px 10px 10px', color='#040404', width=600)#题目部分被命名为radiotext，通过云函数调用
        with Page(name='pageX', enableShare=True, onReady=[moui.showLoading('正在分析中'), onReadyPicPage, moui.hideLoading()]):#成绩单页面
            with Box(pos=[0, 0], width=750, height='100%'):#放置整个图片的box
                Image(id='mopicImage', pos=[0, 20], size=[750, '100%'], height='100%')#设置image的ID，通过云函数获取。
            # with Box(pos=[0, 0], width=750, height=750):
            #     ShareButton(text='分享给好友', pos=[70, 1100, 290, 80], type='miniDefault', fontSize=35, lineHeight=80, background='#ff87ab', boxShadow='-1px 15px 30px -12px black')#分享button
            # Button(text='保存图片', pos=[430, 1100, 270, 80], background='#00d2ff', type='miniDefault', fontSize=35, lineHeight=80, boxShadow='-1px 15px 30px -12px black', onTap=onSaveImage)#保存图片的button
            with Box(size=[750,120], bottom=0, background='#f5c979',position='fixed'):
                with Box(size=[375,200],pos=[0,0]):
                    ShareButton(borderRadius='50%',background='http://material.motimaster.com/harvey/5455/myrose/7bb676398027715e9a86078075adff13.png',size=[70,70],pos=['center',0])
                    Text(text='转发到群', pos=['center', 70],color='black',fontSize=27 )
                
                with Box(size=[375,200], pos=[375,0], onTap=onSaveImage):
                    Image(src='imgs/saveimg.png',size=[70,70],pos=['center',0])
                    Text(text='保存图片', pos=['center', 70],color='black', fontSize=27)



async def firstReady(user, app, page, mo):
    # pass
    page.ggg.hidden = True
async def ongg(user, app, page, mo):
    # pass
    mogo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx6')

async def RadioPageready(user, app, page, mo):#页面题目准备
    questions = drama[page.options.drama_list]#获取字典的内容

    page.data.set('pagenum', 0)#设置第几题
    page.data.set('curnum', 0)#当前第几题
    user.set('ans', [])
    page.radiotext.text = questions[0]['title']
    page.hhh.src = questions[0]['url']
    page.radio3.data = questions[0]['options']

async def onNext(user, app, page, mo):#答题&计分&结果判断
    questions = drama[page.options.drama_list]#定义问题
    pagenum = page.data.get('pagenum')#第几道题
    curnum = page.data.get('curnum')#答对了几题

    ans = user.get('ans')   
    ans.append(page.radio3.value)
    user.set('ans', ans)#记录用户选的答案
    page.data.set('curnum', curnum)
    pagenum += 1
    if pagenum >= len(questions):
        ansint = 0
        for row in ans:
            ansint += int(row)
        k = 0 #标记开始
        for i in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
            if ansint <= i:
                break
            k += 1 #判断下一个图片
        if user.gender == 2:
            user.set('imgurl', pictman[k])
        else:
            user.set('imgurl', pictwoman[k])
        mo.goto('pageX') 
        return
    page.data.set('pagenum', pagenum)
    page.radiotext.text = questions[pagenum]['title']
    page.hhh.src = questions[pagenum]['url']
    page.radio3.data = questions[pagenum]['options']

#生成成绩单&添加二维码&添加用户昵称&分享页面设置
async def onReadyPicPage(user, app, page, mo):
    imgsrc = user.get('imgurl')
    #创建最后展示页的画布
    canvas = mo.mopic.createCanvas(748, 1301, saveStrategy='permanent')
    #在画布上加上背景图
    canvas.addImage(imgsrc, pos=[0, 0, 748, 1301])
    #在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=[309, 101, 122, 122], mask='circle')
    #在画布上加上文字
    canvas.addText(user.nickName, pos=[0, 236, 748], textAlign='center',fontSize=42, color=(0, 0, 0))
    canvas.addText("长按扫码>>",pos=[140,1200],fontsize=28,color=(0,0,0))
    canvas.addText("<<获取你的",pos=[465,1200],fontsize=28,color=(0,0,0))

    #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
    # erweima = None
    # params = {
    #     'page': 'first',
    #     'width': 150,
    #     'options': {'a': 1, 
    #                 'b': user.nickName
    #                 }
    #           }
    # retParams = mo.acode.getWxAcodeUrl(params)
    # if retParams['ret'] == 0:
    #     erweima = retParams['url']
    #把二维码添加到画布上
    if AUDITING == False:
        canvas.addImage(random.choice(erweimas), pos=[312, 1152, 120, 120])

    #生成图片
    res_erweima = canvas.makeImage()

    #判断生成图片是否成功
    if res_erweima['ret'] == 0:
        #在页面上展示结果图
        page.mopicImage.src = res_erweima['url']
        #生成“保存图片”按钮操作需要的图片链接
        page.data.set('url', res_erweima['url'])

    #设置页面分享的标题、图片、用户进入页、传递的参数 
    page.share.title = "来测测看你的内外在年龄分别是多少？"
    page.share.imageUrl = res_erweima['url']
    page.share.page = 'first'
    page.share.options = {'a': 1,
                          'b': user.nickName
                          }

#点击“保存图片”按钮的操作
async def onSaveImage(user, app, page, mo):
    url = page.data.get('url')#提取分享图片的地址
    mo.saveImage(url)
    # pass
