import logging
import sys
import os
import random
from sys import path
path.append(r"/mogo/codes/")
from moapp.lib.client import *
os.chdir(os.path.dirname(sys.argv[0]))
############### momake auto add ###############
#问题
drama={'测试' :[
    {
        #问题
        'title': '1/3.如果你有一枚戒指，你认为戴在哪根手指最合适',
        'options': [
        {'text': '1.小拇指', 'value': '1'},
        {'text': '2.无名指', 'value': '2'},
        {'text': '3.中指', 'value': '3'},
        {'text': '4.食指', 'value': '4'},
        {'text': '5.大拇指', 'value': '5'}
    ],
        #答案(是第几个)
        'answer': 4
    },
    {
        'title': '2/3.你在沙漠里带着4只动物，此时必须抛弃一只，你会选',
        'options':[
        {'text' : '1.大象', 'value' : '1'},
        {'text' : '2.老虎' , 'value': '2'},
        {'text' : '3.狗' , 'value': '3'},
        {'text' : '4.猴子' , 'value': '4'},

    ],
        'answer': 2
    },
    {
        'title': '3/3.长途列车上，你会选择坐哪个位置',
        'options': [
        {'text' : '1' , 'value':'1'},
        {'text' : '2' , 'value':'2'},
        {'text' : '3' , 'value':'3'},
        {'text' : '4' , 'value':'4'},
    ],
        'answer': 2
    },
]
}

#问题图
questionImg = [
    'http://material.yurunyuan.cn/candy/ceshi/empty/be0f493345e1a3acf1e45ca84cc8c4a2.jpg',
    'http://material.motimaster.com/appmaker/yangyiyun/5296.jpg',
    'http://material.yurunyuan.cn/candy/a_a_xingzuo_/getdate/777c5a0c5a6347ea615386f559610660.jpg',
]

#结果图
# img_int = [
# 'http://material.motimaster.com/appmaker/yangyiyun/5204.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5205.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5206.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5207.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5208.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5209.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5210.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5211.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5229.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5230.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5231.jpg',
# 'http://material.motimaster.com/appmaker/yangyiyun/5232.jpg',
# ]
img_int = [
'http://material.motimaster.com/appmaker/yangyiyun/5340.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5341.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5342.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5343.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5344.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5345.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5346.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5347.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5348.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5349.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5350.jpg',
'http://material.motimaster.com/appmaker/yangyiyun/5351.jpg',
]




#这个地方放置的是公众号文章的二维码用于把用户导入到答题的页面 可以设置多个
erweima_a =[
    # "http://material.yurunyuan.cn/candy/ceshi/empty/4d77bc3e6efea451cc3296effb4b25b7.png",
    # "http://material.motimaster.com/appmaker/yangyiyun/5381.png",
    # #喵3
    # # "http://material.yurunyuan.cn/candy/ceshi/empty/c16bd0283a83e188e0c4045ac4d9681f.png",
    # #喵
    # "http://material.yurunyuan.cn/candy/ceshi/empty/d4ce2e310ddea28a32714407585b2d0e.png",
    # #ba3
    # "http://material.yurunyuan.cn/candy/ceshi/empty/b5aae077c6d2daed5e63a2b350abe3ad.png",
    #mz2
    'http://material.motimaster.com/harvey/5455/myrose/314dc7f227b7da5761269549addb2e9c.jpg'
]

AUDITING = False  # 审核的时候设置为True

adunitId = 'adunit-eb3305465fc4fcfe'  #这里先填写一个假的  申请到广点通之后填写微信分配给你的unitId 再重新审核一次
def main():
    with MoApp(appid='wx8978abc3aab37e9e', name='我的人生比重'):#设置小程序的基本信息
        with Page(name='first',background='http://material.motimaster.com/appmaker/yangyiyun/5288.jpg'):#第一个页面的名称和背景图
            this.onReady = firstReady
            with Button(effect=pulse(t=1,c=0),type='primary', pos=[275,700],text='开始',boxShadow='5px 5px 7px #7c9199',background='#0598cc',size=[200,200],borderRadius = '50%',lineHeight = 200,openType='getUserInfo'):
                this.onTap = moui.goto('paper',drama_list = '测试' )#首页的button，跳转到paper页面，同时读取的是上面准备的list内容
            #Image(name='guanggao', src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg', size=[750,125],bottom=0 )
            
            with Box(width=750,height='91px',top=950):
                AD(unitId=adunitId)
        with Page(name='paper',onReady =[ moui.showLoading('题目加载中'),RadioPageready ,moui.hideLoading()],background='http://material.motimaster.com/appmaker/yangyiyun/5290.jpg'):
            with Box(pos=[0, 0], width=322, height=250):#放置整个图片的box
                Image(id='questionImg',pos=[180,10],size=[380,270])#设置image的ID，通过云函数获取。
            Image(name='guanggao',onTap=GotoGame,src='http://material.motimaster.com/harvey/5455/myrose/ba2264a2db67acf35e52c6706d70baf9.gif', pos=[600,140], size=[150,150])
            with MoRadio(name = 'radio3',pos=[70,410, 660, 130],fontSize = 35,position='absolute'):#选项部分，选项被命名为radio3，下一步用云函数调用
                this.onChange = onNext
            Text(name = 'radiotext',padding=10,pos=[70,290],backgroundColor='#fbfdf7',fontSize = 35,borderRadius= '10px 10px 10px 10px',color = '#040404',width =600)#题目部分被命名为radiotext，通过云函数调用
            with Box(hidden=True,width=750,height='91px',top=1000):
                AD(unitId=adunitId)
            with Box(name='adbox', width=750,height=175,top=1000):
                Image(name='game_img',onTap=GotoGame,size=[750,175],src='http://material.motimaster.com/harvey/5455/myrose/f8b82a3642d8fceec30361ef3883431f.jpg')

        with Page(name='pageX',enableShare=True,onReady= [moui.showLoading('正在分析中'), onReadyPicPage, moui.hideLoading()],backgroundColor='#151c38'):#成绩单页面
            with Box(pos=[0, 0], width=750, height=750):#放置整个图片的box
                Image(id='mopicImage',pos=[0,0],size=[750,1123])#设置image的ID，通过云函数获取。
                ImageAvatar(name='nickname', pos=[293, 502],size=[164, 164],borderRadius='50%',onTap=moui.showTips('111'))
                #TextNickName(name='avatarUrl',pos=['center',20],fontSize=50,textAlign='center',color='#000000')
                #pos=[0, 20,750], fontSize=50, color=(0, 0, 0),align='center'
            with Box(pos=[0, 0], width=750, height=750):
                ShareButton(pos=[115, 1000, 200, 60],type='miniDefault',text='分享',color='#ffffff' ,fontSize = 26,lineHeight=60,background='#0598cc')#分享button
            Button(text='保存图片', pos=[435,1000,200,60], openType='getUserInfo',background='#0598cc', color='#ffffff' ,type='miniDefault',fontSize = 26,lineHeight=60,onTap=onSaveImage)#保存图片的button
            Button(name='morefun',hidden=True, onTap=onMoreFunTap,text='更多好玩', fontSize = 26,background='#0598cc', color='#ffffff' ,pos = [115,1080],size=[520,60],type='plainDefault',lineHeight=60 )

async def GotoGame(user, app, page, mo):
    mo.gotoMiniProgram('wxb52b11c4dd14b6fc','/pages/index/index?gdt_vid=xiakedao001&weixinadinfo=0001&channel=xiakedao.h5ddz.3004053701')

async def onMoreFunTap(user, app, page, mo):
    #mo.gotoMiniProgram('')
    mo.console('morefun')
    mo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx8')

topAdvertising = [
    #{"id":1,"src":"http://material.motimaster.com/harvey/5455/myrose/c47d59877186440c77a9f1a1ba9c0107.jpg"},
    {"id":2,"src":"http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg"}]

async def firstReady(user, app, page, mo):
    #firstReady
    # if AUDITING == False:
    #     page.swiperGuangGao.hidden=False
    # page.imgUrls.data = topAdvertising
    # page.swiperGuangGao.interval=2000
    # page.swiperGuangGao.duration = 500
    # page.swiperGuangGao.autoplay = True
    # if adShow ==True:
    #     page.ad.unitId = adunitId
    pass


async def advertisingTap(user, app, page, mo, params):
    #mo.console(params.id)
    if params.id == 2:
        #mo.gotoMiniProgram('wx71d589ea01ce3321','pages/pageentrance/pageentrance')
        #mo.gotoMiniProgram('wx71d589ea01ce3321','pages/main/main?from=xingzuoxiaowo&position=ad')
        mo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx8')
    else:
        #mo.gotoMiniProgram('wx01434b3ed0010d28','pages/pageentrance/pageentrance')
        pass

async def RadioPageready(user,app,page,mo):#页面题目准备
    questions = drama['测试']#获取字典的内容

    page.data.set('pagenum',0)#设置第几题
    page.data.set('curnum',0)#当前第几题
    user.set('ans',[])
    page.radiotext.text = questions[0]['title']
    page.radio3.data = questions[0]['options']
    # if AUDITING == False:
    #     page.swiperGuangGao.hidden = False
    # page.imgUrls.data = topAdvertising
    # page.swiperGuangGao.interval=2000
    # page.swiperGuangGao.duration = 500
    # page.swiperGuangGao.autoplay = True
    page.questionImg.src = questionImg[0]
    

async def onNext(user,app,page,mo):#答题&计分&结果判断
    questions = drama['测试']#定义问题
    pagenum = page.data.get('pagenum')#第几道题
    curnum = page.data.get('curnum')#答对了几题

    ans = user.get('ans')
    ans.append(page.radio3.value)
    user.set('ans',ans)#记录用户选的答案
    page.data.set('curnum',curnum)
    if pagenum == None:
        pagenum = 0
    pagenum +=1

    if pagenum != 0:
        page.adbox.top = 1000

    if pagenum >= len(questions):
        ansint = 0
        for row in ans:
            ansint += int(row)
        k = 0 #标记开始
        for i in [6,8,10,12,14,16,17,19,21,23,24]:
            if ansint <= i:
                break
            k += 1 #判断下一个图片
        user.set('imgurl',img_int[k])
        mo.goto('pageX')
        return
    page.data.set('pagenum',pagenum)
    page.radiotext.text = questions[pagenum]['title']
    page.radio3.data = questions[pagenum]['options']
    page.questionImg.src = questionImg[pagenum]

#生成成绩单&添加二维码&添加用户昵称&分享页面设置
async def onReadyPicPage(user,app,page,mo):
    imgsrc = user.get('imgurl')
    #创建最后展示页的画布
    page.mopicImage.src = imgsrc

    #设置页面分享的标题、图片、用户进入页、传递的参数
    page.share.title = "你的朋友邀请你查看你的人生比重"
    page.share.imageUrl = 'http://material.motimaster.com/appmaker/yangyiyun/5291.jpg'
    page.share.page = 'first'
    page.share.options = {'a':1,'b':user.nickName}
    if AUDITING == False:
        #canvas.addImage(erweima, pos=[565, 813, 150, 150])
        #canvas.addImage("http://material.motimaster.com/harvey/5455/myrose/19aa9e485dea98a09fb58a1218dcc3cd.pic_hd", pos=[565, 813, 150, 150])
        page.morefun.hidden = False


#点击“保存图片”按钮的操作
# async def onSaveImage(user, app, page, mo):
#     page.nickname.hidden = True
#     page.avatarUrl.hidden = True
#     imgsrc = user.get('imgurl')
#     canvas = mo.mopic.createCanvas(750,1123)
#     #在画布上加上背景图
#     canvas.addImage(imgsrc, pos=[0, 0, 750, 1000])
#     #在画布上加上用户头像
#     # canvas.addImage(user.avatarUrl, pos=[277, 103, 197, 197],mask='circle')
#     #在画布上加上文字
#     canvas.addText(user.nickName, pos=[0, 20,750], fontSize=50, color=(0, 0, 0),align='center')
#     canvas.addText('获取你的人生比重：', pos=[50, 870], fontSize=40,color=(0, 0, 0))

#     #res = canvas.makeImage()

#     #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
#     # erweima = None
#     # params = {
#     #     'page': 'first',
#     #     'width': 150,
#     #     'options':{'a':1,'b':user.nickName}
#     # }
#     # retParams = mo.acode.getWxAcodeUrl(params)
#     # if retParams['ret'] == 0:
#     #     erweima = retParams['url']

#     #把二维码添加到画布上
#     if AUDITING == False:
#         #canvas.addImage(erweima, pos=[565, 813, 150, 150])
#         canvas.addImage("http://material.motimaster.com/harvey/5455/myrose/19aa9e485dea98a09fb58a1218dcc3cd.pic_hd", pos=[565, 813, 150, 150])
#         page.morefun.hidden = False
#     #生成图片
#     res_erweima = canvas.makeImage()

#     #判断生成图片是否成功
#     if res_erweima['ret'] == 0:
#         #在页面上展示结果图
#         page.mopicImage.src = res_erweima['url']
#         #生成“保存图片”按钮操作需要的图片链接
#         #page.data.set('url',res_erweima['url'])
#     #url = page.data.get('url')#提取分享图片的地址
#     mo.saveImage(page.mopicImage.src)
    # pass
async def onSaveImage(user, app, page, mo):
    page.share.title = user.nickName + "邀请你查看你的人生比重"
    page.nickname.hidden = True
    imgsrc = user.get('imgurl')
    canvas = mo.mopic.createCanvas(720,1078)
    #在画布上加上背景图
    canvas.addImage(imgsrc, pos=[0,0,720,1078])
    #在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=['center',  480, 157, 157],mask='circle')
    #在画布上加上文字
    #canvas.addText(user.nickName, pos=[0, 20,750], fontSize=50, color=(0, 0, 0),align='center')
    #canvas.addText('测测你十年后是什么样：', pos=[50, 870], fontSize=40,color=(0, 0, 0))
    
    #res = canvas.makeImage()

    #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
    # erweima = None
    # params = {
    #     'page': 'first',
    #     'width': 150,
    #     'options':{'a':1,'b':user.nickName}
    # }
    # retParams = mo.acode.getWxAcodeUrl(params)    
    # if retParams['ret'] == 0:
    #     erweima = retParams['url']
#
    #把二维码添加到画布上
    if AUDITING == False:
        #canvas.addImage(erweima, pos=[565, 813, 150, 150])
        canvas.addImage(random.choice(erweima_a), pos=[560, 923, 150, 150])
        page.morefun.hidden = False
    #生成图片
    res_erweima = canvas.makeImage()

    #判断生成图片是否成功
    if res_erweima['ret'] == 0:
        #在页面上展示结果图
        page.mopicImage.src = res_erweima['url']
        #生成“保存图片”按钮操作需要的图片链接
        #page.data.set('url',res_erweima['url'])
    #url = page.data.get('url')#提取分享图片的地址
    mo.saveImage(page.mopicImage.src)
