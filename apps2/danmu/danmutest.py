def main():
    with MoApp(name='testdanmu',appid='wx263b9c72fc87b39c'):
        with Page(name='index', background='http://material.motimaster.com/harvey1536219255000/bgk2.jpg'):
            this.onReady = indexReady
            TextNickName(pos=['center',50], color='red', fontSize=40)
            Text(text='你有什么要对我说的',pos=['center',100], color='red', fontSize=40)
            ImageAvatar(pos=['center',300], borderRadius='50%', size=[200,200])
            with Box(size=[750,600], pos=[0,200]):
                Barrage(name='danmu',fontSize=25, itemtap=barrageItemTap,avatarStyle='width:35rpx;height:35rpx;left:0;',lineHeight=35, height=35,
                    margin=20,rowNumber=5,background='linear-gradient(to right, rgba(255,255,255,1), rgba(255,255,255,0))')

            Box(size=[4,190], background='rgb(253, 225, 167)', position='fixed', right=100, top=0, boxShadow='0 0 40rpx 2rpx rgb(253, 225, 167)')
            Button(text='留言管理',size=[120, 60], position='fixed', right=45, top=190,background='rgb(253, 225, 167)', borderRadius=30, boxShadow='0 0 40rpx 2rpx rgb(253, 225, 167)',  
                fontSize=27, lineHeight=60,textAlign='center', color='#444',onTap=moui.goto('second'))
            with Input(name='inputDanmu',color='white', onChange=InputOnChange,fontSize=27,lineHeight=60,borderBottom='1rpx solid white',left=50,bottom=320,size=[400,60]):
                this.placeholderStyle.color='white'
            Button(size=[140,55], text='发送',onTap = sendBarrage, color='white',fontSize=26, background='#08A070',borderRadius=15,type='primary',left=550,bottom=320,lineHeight=55,openType='getUserInfo')
            with List(name='recommands',left=50, bottom=150):
                Button(text='{item.text}', border='1px dashed #666', background='rgba(255,255,255,0.1)',color='white',
                      paddingRight='30rpx',paddingLeft='30rpx',float='left', 
                      marginRight=20,marginBottom=20, fontSize=26, width=300,height=53,lineHeight=53, onTap = moui.request(onRecommandTap,id='{item.id}'))

            with Box(size=[100,30], left=550, bottom=200,display='flex'):
                Image(src='img/huanyipi.png',size=[28,28])
                Text(text='换一批',pos=[30,0],color='white', fontSize=22, lineHeight=30)
            # with Button(text='评论管理',size=[100,60],lineHeight=60,fontSize=20,padding=0,pos=[550,100]):
            #     this.onTap=moui.goto('second')

            Button(text='邀请好友留言', size=[680,70], position='fixed', bottom=50, color='white',fontSize=30,
                lineHeight=70,textAlign='center', left=35, borderRadius=35,border='2rpx solid #08A070', background='rgba(8,160,112,0.6)')

            with Swiper(name ='tip2', size=[200,60], left=50,bottom=320,interval=2000,duration=500, autoplay=True, vertical=True, circular=True):
                with SwiperItem(name='imgUrls'):
                    # Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')
                    Text(text='{item}', color='gray', fontSize=27, lineHeight=60 )


        with Page(name='second',onReady=managerReady):
            with List(name='pinglun',pos=[25,0]):
                with Box(size=[700,200], border='1px solid black', marginBottom=20):
                      Image(src='{item.avatar}', size=[80,80], borderRadius='50%', pos=[50,50])
                      Text(text='{item.nick}', pos=[200,80])
                      Text(text='{item.pinglun}', pos=[400,80], color='red')
async def InputOnChange(user, app, page, mo):
    page.tip2.hidden=True

async def barrageItemTap(user, app, page, mo ):
    mo.console(page.danmu.value)
    #page.danmu.value 拿到是该条记录的id 用于操作数据知道点击的是哪一项
    

async def indexReady(user, app, page, mo):

    page.danmu.data = [{'id':1,'text':'我喜欢你萨达达大厦萨就是垃圾焚烧收到反馈数据反馈时间到发生了大空间','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':2,'text':'弹幕一','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},
        {'id':3,'text':'弹幕二','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':4,'text':'弹幕三','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':5,'text':'弹幕四','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':6,'text':'弹幕五','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':7,'text':'弹幕六','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':8,'text':'弹幕七 ','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        {'id':9,'text':'弹幕八','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},  ]

    page.imgUrls.data=['#吐槽一下#', '#调戏一波#', '#我喜欢你很久了#', '#你想干什么嘞#']
    #page.danmu.danmuStyle = 'font-size:25rpx;line-height:35rpx;height:35rpx;background: linear-gradient(to right, rgba(255,255,255,1), rgba(255,255,255,0));'
    # page.danmu.danmuFontSize=25
    # page.danmu.danmuLineHeight = 35
    # page.danmu.danmuBackground='linear-gradient(to right, rgba(255,255,255,1), rgba(255,255,255,0))'
    # page.danmu.danmuHeight = 35
    # page.danmu.danmuMargin = 30
    # page.danmu.danmuRowNumber = 4

    #page.danmu.tailImage = "http://material.motimaster.com/harvey///0d3f664b4a65c9f4dc21c3d60903a99f.png"
    page.recommands.data = [{'id':0,'text':'我喜欢你'},{'id':1,'text':'我喜欢讨厌你'},{'id':2,'text':'你赶紧滚吧'}]
    #page.danmu.danmuAvatarStyle = 'width:35rpx;height:35rpx;left:0;'
    page.data.danmuLength= 9
      
async def onRecommandTap(user, app, page, mo, params):
    mid = params.id
    text = page.recommands.data[mid]['text']
    page.inputDanmu.value = text

async def sendBarrage(user, app, page, mo):
    if page.inputDanmu.value == None or page.inputDanmu.value == '':
        mo.showTips('内容不能为空')
        return
    page.danmu.data.append({'id':page.data.danmuLength+1,'text':page.inputDanmu.value,'avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"})
    page.data.danmuLength+=1
    page.inputDanmu.value = ''

async def managerReady(user, app, page, mo):
    page.pinglun.data=[
        {'id':0,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'},
        {'id':1,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'},
        {'id':2,'nick':'harvey','pinglun':'测试','avatar':'http://material.motimaster.com/appmaker/lijiong/2315.png'}
    ]
