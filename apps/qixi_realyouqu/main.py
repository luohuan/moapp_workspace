import logging
import sys
import os
import random

############### momake auto add ###############
#问题
drama={'测试' :[
    {
        #问题
        'title': '1/3.月老问：你出生的季节是？',
        #选项
        'options': [
        {'text': '春季', 'value': '1'},
        {'text': '夏季', 'value': '2'},
        {'text': '秋季', 'value': '3'},
        {'text': '冬季', 'value': '4'},
    ],
        #答案(是第几个)
        'answer': 4
    },
    {
        'title': '2/3.月老问：你的性别是？',
        'options':[
        {'text' : '女', 'value' : '1'},
        {'text' : '男' , 'value': '2'},
        # {'text' : '3.狗' , 'value': '3'},
        # {'text' : '4.猴子' , 'value': '4'},

    ],
        'answer': 2
    },
    {
        'title': '3/3.月老问：你觉得图中哪对情侣的相处模式最温馨？',
        'options': [
        {'text' : 'A' , 'value':'1'},
        {'text' : 'B' , 'value':'2'},
        {'text' : 'C' , 'value':'3'},
        {'text' : 'D' , 'value':'4'},
    ],
        'answer': 2
    },
]
}
#问题图
questionImg = [
    'http://material.motimaster.com/appmaker/yangyiyun/5262.png',
    'http://material.motimaster.com/appmaker/yangyiyun/5262.png',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodan/wentitu1.jpg',
]

img_int = [
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/1.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/2.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/3.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/4.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/5.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/6.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/7.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/8.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/9.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/10.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/11.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/12.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/13.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/14.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/15.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/16.jpg',
    'http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/17.jpg',
]




#这个地方放置的是公众号文章的二维码用于把用户导入到答题的页面 可以设置多个
erweima_a =[
    'http://img.mogodeer.cn/image/xixi/qcode/tuodanluodi1.png',
    'http://img.mogodeer.cn/image/xixi/qcode/tuodanluodi2.png',
    'http://img.mogodeer.cn/image/xixi/qcode/tuodanluodi3.png'
]

AUDITING = False  # 审核的时候设置为True

adunitId = 'wx47b494af03bd0aae'  #这里先填写一个假的  申请到广点通之后填写微信分配给你的unitId 再重新审核一次
def main():
    with MoApp(appid='wx47b494af03bd0aae', name='脱单问题'):#设置小程序的基本信息
        with Page(name='first'):#第一个页面的名称和背景图
            this.onReady = firstReady
            Image(width='100%',height='100%',src='http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/bg11.jpg')
            with Button(effect=pulse(t=1,c=0),type='primary', pos=[275,700],text='开始',boxShadow='5px 5px 7px #7c9199',background='#0598cc',size=[200,200],borderRadius = '50%',lineHeight = 200,openType='getUserInfo'):
                this.onTap = moui.goto('paper',drama_list = '测试' )#首页的button，跳转到paper页面，同时读取的是上面准备的list内容
            #Image(name='guanggao', src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg', size=[750,125],bottom=0 )
            
            with Box( width=750,height='91px',top=950):
                AD(unitId=adunitId)
            with Box(name='adbox', hidden=True,width=750,height=175,top=950):
                Image(name='game_img',onTap=GotoGame,size=[750,175],src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg')
        with Page(name='paper',onReady =[ moui.showLoading('题目加载中'),RadioPageready ,moui.hideLoading()]):
            Image(width='100%',height='100%',src='http://img.mogodeer.cn/image/xixi/yuelaotuodanwx/bg22.jpg')
            with Box(pos=[0, 0], width=322, height=250):#放置整个图片的box
                Image(id='questionImg',pos=[180,10],size=[380,270],onTap=previewimage)#设置image的ID，通过云函数获取。
            with MoRadio(name = 'radio3',pos=[70,410, 660, 130],fontSize = 35,position='absolute'):#选项部分，选项被命名为radio3，下一步用云函数调用
                this.onChange = onNext
            Text(name = 'radiotext',padding=10,pos=[70,290],backgroundColor='#fbfdf7',fontSize = 35,borderRadius= '10px 10px 10px 10px',color = '#040404',width =600)#题目部分被命名为radiotext，通过云函数调用
            with Box( width=750,height='91px',top=1000):
                AD(unitId=adunitId)
            with Box(name='adbox', hidden=True,width=750,height=175,top=1000):
                Image(name='game_img',onTap=GotoGame,size=[750,175],src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg')
        with Page(name='pageX',enableShare=True,onReady= [moui.showLoading('正在分析中'), onReadyPicPage, moui.hideLoading()],backgroundColor='#151c38'):#成绩单页面
            with Box(pos=[0, 0], width=750, height=750):#放置整个图片的box
                Image(id='mopicImage',pos=['center',0],size=[600,1047],onTap=previewimage2)#设置image的ID，通过云函数获取。
                ImageAvatar(name='avtar',hidden=True, pos=[293, 502],size=[164, 164],borderRadius='50%',onTap=moui.showTips('111'))
                #TextNickName(name='avatarUrl',pos=['center',20],fontSize=50,textAlign='center',color='#000000')
                #pos=[0, 20,750], fontSize=50, color=(0, 0, 0),align='center'
            #with Box(pos=[0, 0], width=750, height=750):
            ShareButton(pos=[115, 1000, 200, 100],type='miniDefault',text='分享',color='#ffffff' ,fontSize = 26,lineHeight=100,background='#0598cc')#分享button
            Button(text='保存图片', pos=[435,1000,200,100], openType='getUserInfo',background='#0598cc', color='#ffffff' ,type='miniDefault',fontSize = 26,lineHeight=100,onTap=onSaveImage)#保存图片的button
            Button(name='morefun',hidden=True, onTap=onMoreFunTap,text='更多好玩', background='#0598cc', color='#ffffff' ,fontSize = 26,pos = [115,1080],size=[520,60],type='plainDefault',lineHeight=60 )
async def previewimage(user, app, page, mo):
    pagenum = page.data.get('pagenum')
    mo.previewImage([questionImg[pagenum]])
async def previewimage2(user, app, page, mo):
    mo.previewImage([page.data.mopicImage])
async def GotoGame(user, app, page, mo):
    #@mo.gotoMiniProgram('wxb52b11c4dd14b6fc','/pages/index/index?gdt_vid=xiakedao001&weixinadinfo=0001&channel=xiakedao.h5ddz.3004053701')
    mo.gotoMiniProgram('wx6acc1db2845590f6','pages/listPage/listPage?channel=swlpdxcx2')
async def onMoreFunTap(user, app, page, mo):
    mo.console('morefun')
    #mo.gotoMiniProgram('wxb52b11c4dd14b6fc','/pages/index/index?gdt_vid=xiakedao001&weixinadinfo=0001&channel=xiakedao.h5ddz.3004053701')
    mo.gotoMiniProgram('wx6acc1db2845590f6','pages/listPage/listPage?channel=swlpdxcx2')
topAdvertising = [
    #{"id":1,"src":"http://material.motimaster.com/harvey/5455/myrose/c47d59877186440c77a9f1a1ba9c0107.jpg"},
    {"id":2,"src":"http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg"}]

async def firstReady(user, app, page, mo):
    #firstReady
    if AUDITING == False:
        page.adbox.hidden = False
    page.game_img.src="http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg"


async def advertisingTap(user, app, page, mo, params):
    #mo.console(params.id)
    if params.id == 2:
        #mo.gotoMiniProgram('wx71d589ea01ce3321','pages/pageentrance/pageentrance')
        #mo.gotoMiniProgram('wx71d589ea01ce3321','pages/main/main?from=xingzuoxiaowo&position=ad')
        #mo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx8')
        mo.gotoMiniProgram('wx6acc1db2845590f6','pages/listPage/listPage?channel=swlpdxcx2')
    else:
        #mo.gotoMiniProgram('wx01434b3ed0010d28','pages/pageentrance/pageentrance')
        pass

async def RadioPageready(user,app,page,mo):#页面题目准备
    page.game_img.src="http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg"
    if AUDITING == False:
        page.adbox.hidden = False
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
    if pagenum >= len(questions):
        # ansint = 0
        # for row in ans:
        #     ansint += int(row)
        # k = 0 #标记开始
        # for i in [6,8,10,12,14,16,17,19,21,23,24]:
        #     if ansint <= i:
        #         break
        #     k += 1 #判断下一个图片
        user.set('imgurl',random.choice(img_int))
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
    canvas = mo.mopic.createCanvas(643,1123)
    #在画布上加上背景图
    canvas.addImage(imgsrc, pos=[0,0,643,1123])
    #在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=[527,115,100])
    canvas.addImage(user.avatarUrl, pos=[527,352,100])
    canvas.addImage(random.choice(erweima_a), pos=[547,1020,86])
    canvas.addText('扫码问月老', pos=[562,1108,97,13],fontSize=13, color=(0,0,0))
    res = canvas.makeImage()
    if res['ret'] == 0:
        #在页面上展示结果图
        page.mopicImage.src = res['url']
        page.data.mopicImage = res['url']
    page.share.title = "你的朋友%s邀请你来回答脱单问题"%user.nickName
    page.share.imageUrl = 'http://material.motimaster.com/appmaker/yangyiyun/5364.jpg'
    page.share.page = 'first'
    page.share.options = {}
    if AUDITING == False:
        #canvas.addImage(erweima, pos=[565, 813, 150, 150])
        #canvas.addImage("http://material.motimaster.com/harvey/5455/myrose/19aa9e485dea98a09fb58a1218dcc3cd.pic_hd", pos=[565, 813, 150, 150])
        page.morefun.hidden = True

async def onSaveImage(user, app, page, mo):
    # page.share.title = user.nickName + "邀请你查看你的人生比重"
    # page.nickname.hidden = True
    mo.saveImage(page.data.mopicImage)
    