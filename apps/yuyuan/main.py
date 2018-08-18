import random
import time

bling = "http://img.mogodeer.cn/images/yuan/4.png"
star = "http://img.mogodeer.cn/image/health/star.png"
liuxing = "http://img.mogodeer.cn/images/yuan/liuxing.png"
pageColor = '#FEB621'
guestColor = '#FEB621'


AUDITING = False  #是否是审核状态
ENABLE_PAY = True #是否开启支付

def starblink():
    efbkink1 = blink("0.8, 0.4, 0.8, 1.2")
    efbkink1 = blink("0.8, 0.4, 0.8, 1.2")
    efbkink2 = blink("0.8, 0.2, 0.3, 1.2")
    efbkink3 = blink("1.2, 0.5, 0.5, 1.2")
    efbkink4 = blink("0.5, 0.8, 0.7, 1.2")
    efmove1 = move(path=[(350,-20),(-80,350)],c=0,t=3.0)    
    efmove2 = move(path=[(550,-150),(-160,550)],c=0,t=3.5,d=1)
    efmove3 = move(path=[(770,200),(-150,850)],c=0,t=4.0,d=0.5)
    effade1 = fadeout(t=2.5,c=0)
    effade2 = fadeout(t=3.0,d=1,c=0)
    effade3 = fadeout(t=3.5,d=0.5,c=0)
    Image(src=star,pos=[30,20,25,25],effect=efbkink1) 
    Image(src=star,pos=[370,130,22,22],effect=efbkink1)  
    Image(src=star,pos=[200,40,15,15],effect=efbkink2) 
    Image(src=star,pos=[240,250,16,16],effect=efbkink3) 
    Image(src=star,pos=[160,290,20,20],effect=efbkink2)   
    Image(src=star,pos=[300,20,16,16],effect=efbkink4)
    Image(src=star,pos=[600,60,25,25],effect=efbkink1)
    Image(src=star,pos=[320,180,29,20],effect=efbkink3) 
    Image(src=star,pos=[560,220,15,15],effect=efbkink1) 
    Image(src=star,pos=[440,320,17,17],effect=efbkink1)
    Image(src=star,pos=[220,170,17,17],effect=efbkink4) 
    Image(size=[75,75], pos=[350,-20], src=liuxing, effect=relativeMove(t=3.0,p=0,c=0,rd=(-430,370)))
    Image(size=[80,80], pos=[550,-150], src=liuxing, effect=relativeMove(t=3.5,p=0,c=0,d=1,rd=(-710,700)))
    Image(src=liuxing,pos=[770, 200],size=[85,85],effect=relativeMove(t=4,p=0,c=0,d=0.5,rd=(-920,650)))

def main():
    with MoApp(appid='wx468ad783f165eea0', name='好友回忆墙',withLogin=True):
        with Page(name='begin',enableShare=True, onReady=beginReady):
            with Box(name='entrance',pos=[0,0], hidden=True,width=750):
                Image(position='fixed', top=0,size=[750,1500],src="img/bg1.jpg")
                starblink()
                ImageAvatar(pos=['center',430],size=[160,160],borderRadius='50%')
                Image(pos=[340,130],size=[300,70],src="http://material.motimaster.com/yuyuan/Duudle/create/4ad72652b048c5f9b890c624f88a7986.png",effect=fadein(d=0.5,t=2,c=0,p=1,s=0))
                Image(pos=[60,210],size=[300,70],src="http://material.motimaster.com/yuyuan/Duudle/create/bce9ecef06295fad6af331cd2e3a85f6.png",effect=fadein(d=1,t=2,c=0,p=1,s=0))
                Image(pos=[400,270],size=[300,70],src="http://material.motimaster.com/yuyuan/Duudle/create/4db38b7fd28b7ff588aa8b9d558bb9b8.png",effect=fadein(d=1.5,t=2,c=0,p=1,s=0))
                Image(pos=[100,340],size=[300,70],src="http://material.motimaster.com/yuyuan/Duudle/create/5be1b2f94b910ef607b3cbbd140702a9.png",effect=fadein(d=2,t=2,c=0,p=1,s=0))

                Image(pos=['center',620],size=[550,300],src="http://material.motimaster.com/yuyuan/Duudle/create/0b8149cc3aa0f85e11da99a04f26ccaf.png",effect=fadein(d=0.5,t=2,c=1,p=1,s=0))

                Button(text='创建我的好友回忆墙', name='begin',fontWeight=600,openType='getUserInfo',color='#663300',size=[430,90],pos=['center',1000],backgroundColor="#FEB621",borderRadius='10px',boxShadow='-1px 15px 30px -12px black',border="1rpx solid #FFD886",onTap = toBegin)
            # with Box(name='auditing_box', pos=[0,0], hidden=True, width=750):
            #     Image(name='image1',pos=[0,-40],size=[750,1325],src="img/bg2.jpg")
            #     ImageAvatar(pos=['center', 30], size=[160,160], borderRadius='50%')
            #     Text(name='text1',text='每个名字都有自己的点数', color='#FFFFFF', fontSize=24, pos=['center', 400])
            #     Input(name='input_host_name', pos= ['center',600], size=[480,80],
            #           placeholder = '请输入你的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            #     Button(name='button1', text = '提交', pos=['center',938],size=[360,78],background = 'rgba(242,64,64,0.82)',
            #                            lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', 
            #                            color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo',
            #                            onTap = [moui.showLoading('加载中...'), computeNameScore, moui.hideLoading()])

            with Box(name='loading_box', pos=[0,0], width=750):
               Image(src='img/loading.gif', size=[200, 40], pos=['center', 600])
               Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])    
            
        with Page(name='page1', barColor='#2a2c3b', barStyle='white',enableShare=True, onReady = page1Ready):
            Image(position='fixed', top=0,size=[750,1500],src="img/bg1.jpg")
            starblink()
            Image(name='hostAvatar',pos=['center', 20],  size=[150, 150], borderRadius='50%')
            with Box(size=[650, 120],marginBottom=20, pos=['center', 200]):
                Text(name='hostName', pos=['center', 0],size=['inherit', 'inherit'],color='#FFFFFF',textAlign='center')
            #Image(name='bkimg', pos=[0,0],size=[750,1500],src="img/bg0.jpg")  #背景设置
            ContactButton(name='helpBtn',hidden=True,plain=True, border="None", pos=[650,70], size=[70, 70],borderRadius='50%',boxShadow='0px 0px 0px 2rpx gray', background='http://material.motimaster.com/harvey/5455/myrose/13266bbea43f54ee7f32d9e979f0c7d5.png')
            with ScrollBox(pos=[30, 330], size=[690,650], scrollY=True):
                with Grid(name='things', column=3):
                    with Box(width=230,height=105):
                        with Box(size=[171, 80],pos=['center',0],marginBottom=25, border='1px solid #FFD886',borderRadius='8px', background='{item.background}', color='{item.color}',
                            onTap=moui.request(makeChioce, index='{item.index}'),  display='flex',flexDirection='row',alignItems='center',justifyContent='center'):
                            Text(text='{item.text}', fontSize=26, textAlign='center',position='relative')

            Button(name='btn', text='确定',pos=['center',1030], type='plainDefault', openType='getUserInfo',border="1rpx solid #FFD886",boxShadow='-1px 15px 30px -12px black',fontSize='18px',backgroundColor="#FEB621",borderRadius='8px', onTap=submit)
            
            #Button(name='btn2', text='我也要玩',pos=['center',1020], type='plainDefault', background=pageColor,
            #   onTap=moui.goto('index'), hidden=True)
            # with Box(name='shareBtn', top=350, hidden=True):
                # Button(text='保存', left=150, type='miniDefault', background=pageColor, 
                    # onTap=[moui.showLoading('制作中...'), onSaveImage, moui.hideLoading()])
                # ShareButton(text='分享',right=150, type='miniDefault', background=pageColor)
                    
        with Page(name='mainpage', background="#2A2C3B",onReady=mainPageReady, onPullDownRefresh=mainPageReady, barColor='#2a2c3b', barStyle='white', enableShare=True):
            Image(position='fixed', top=0,size=[750,1500],src="img/bg1.jpg")

            with Box(pos=[0,0],position='relative'):
                       
                Image(pos=[120,68],size=[70,2],src="img/line.png")
                Image(pos=[553,68],size=[70,2],src="img/line.png")
                Text(text='好友得分榜', color='#FFD886', fontSize=36, pos=['center', 40])
                Image(name='backLeida', pos=[49,135],size=[650,679],src="http://material.motimaster.com/yuyuan/Duudle/create/7029a94695b5c003052970aa0c4841bd.png")
                ef1 = rotate(deg=(0,360), c=0, p=0, t=5, s=0, o=(25.6,0))
                Image(name='leida',pos=[261,485],size=[439,330],src="img/leida2.png",effect=ef1)
                Image(pos=[323,437],size=[104,104],src="img/guangquan.png",effect=fadein(d=1,t=1,c=0,p=1,s=0))
                Image(name='authorAvatar', pos=[340, 453],  size=[70, 70], borderRadius='50%')
                Image(pos=[340, 453], size=[70, 70], borderRadius='50%')
                
                with List(name='guest_stars', background='blue'):
                    Image(position='absolute', top='{item.guangtop}', left='{item.guangleft}', src='img/guangquan.png', size=[104, 104], effect=fadeto(size=(1,0.5),d=1,t=1,c=0,p=1,s=0))
                    Image(position='absolute', top='{item.top}', left='{item.left}', src='{item.avatar}', size=[70, 70], borderRadius='50%',effect=fadeto(size=(1,0.5),d=1,t=1,c=0,p=1,s=0))
                    

                #星星闪烁
                efbkink1 = blink("0.8, 0.4, 0.8, 1.2")
                efbkink2 = blink("0.8, 0.2, 0.3, 1.2")
                efbkink3 = blink("1.2, 0.5, 0.5, 1.2")
                efbkink4 = blink("0.5, 0.8, 0.7, 1.2")
                star = "http://img.mogodeer.cn/image/health/star.png"
                Image(src=star,pos=[10,710,15,15],effect=efbkink1)  
                Image(src=star,pos=[300,130,15,15],effect=efbkink1)     
                Image(src=star,pos=[200,40,25,25],effect=efbkink2)
                Image(src=star,pos=[60,250,20,20],effect=efbkink3)  
                Image(src=star,pos=[60,490,20,20],effect=efbkink2)     
                Image(src=star,pos=[300,520,15,15],effect=efbkink4) 
                Image(src=star,pos=[400,660,25,25],effect=efbkink1) 
                Image(src=star,pos=[340,290,15,15],effect=efbkink3)
                Image(src=star,pos=[360,280,15,15],effect=efbkink1)
                Image(src=star,pos=[440,320,18,18],effect=efbkink1)


                ContactButton(name='helpBtn',hidden=True,plain=True, border="None", pos=[650,70], size=[70, 70],borderRadius='50%',boxShadow='0px 0px 0px 2rpx gray', background='http://material.motimaster.com/harvey/5455/myrose/13266bbea43f54ee7f32d9e979f0c7d5.png')
                
                #好友得分详情
                ef55 = slideindown(t=2,c=0)
                Image(pos=[120,883],size=[70,2],src="img/line.png")            
                Image(pos=[553,883],size=[70,2],src="img/line.png")
                Text(text='好友得分详情', pos=['center', 855], color='#FFD886', fontSize=36)
                Text(name='tip1',effect=ef55,hidden=True, text='点击底部按钮分享给好友来测吧！', pos=['center', 580], color='#FFFFFF', fontSize=36)
                Text(name='tip2', effect=ef55,hidden=True, text='↓↓↓', pos=['center', 650], color='#F0739B', fontSize=36)

                #详解框+内容
                with List(name='guest_records', pos=[37, 961], marginBottom=100):
                    with Box(width=684, height='{item.height}rpx',border='1px solid #5F4270',borderRadius='2%',background='#121639',marginBottom=20):
                        Box(pos=[128, 54], size=[90, 90],border='0px solid #fff',borderRadius='50%',background='#fff')
                        Image(src='{item.host_avatar}', pos=[133, 59], size=[80, 80], borderRadius='50%',)
                        Box(pos=[460, 54], size=[90, 90],border='0px solid #fff',borderRadius='50%',background='#fff')
                        Image(src='{item.guest_avatar}', pos=[465, 59], size=[80, 80], borderRadius='50%')
                        Box(pos=[269, 122], size=[140, 2],border='2px solid #F17093',borderRadius='0%',background='#F17093')
                        Text(text='{item.score}分', pos=['center', 34],color='#FFF', fontSize=42)
                        Text(text='{item.host_nick}', pos=[70, 160],size=[200,90],textAlign='center',color='#fff', fontSize=24)
                        Text(text='{item.guest_nick}', pos=[410, 160],size=[200,90],textAlign='center',color='#fff', fontSize=24)
                      
                        Button(hidden='{item.hide_show_momery}',text='查看与ta的回忆', pos=['center', 160], size=[175,40], color='#663300',fontSize=23, lineHeight=40,border="1rpx solid #FFD886",background='#FEB621',
                        onTap=moui.request(checkDetail, host_id='{item.host_openid}', guest_id='{item.guest_openid}'))
                        Button(hidden='{item.hide_pay}',text='查看与ta的回忆', pos=['center', 160], size=[175,40], color='#663300',fontSize=23, lineHeight=40,border="1rpx solid #FFD886",background='#FEB621',
                        onTap=moui.confirm('温馨提示:','查看全部好友的选择(包括未来进入的好友),只需支付金额3.99',moui.request(checkDetailPay, host_id='{item.host_openid}', guest_id='{item.guest_openid}')))
                        
                        
                        Text(text='友情结语：', pos=[60, 240],color='#ED6E91', fontSize=30)
                        Text(text='{item.fit_words}', pos=[210, 240],color='#FFF', fontSize=30,size=[430, 240])
                       
                        with Box(right=10,top=10,size=[40,40],hidden='{item.hide_delete}'):
                            with Image(name='delete',src='http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png',size=[40,40],pos=[0,0]):
                                this.onTap = moui.confirm('温馨提醒','删除的记录将不能恢复，您确认删除嘛?',moui.request(deleteRecord, rid='{item.id}'))
            
            with Mask(name='ansMask', hidden=True):
                with ScrollBox(scrollY=True, background='rgba(17,17,17,0.8)',borderRadius='10px',border='1px solid #FFD886',size=[550, 700], pos=['center',200]):
                    with List(name='guest_detail',position='relative'):
                        with Box(height=50):
                            Text(text='{item.answer}',fontSize=28,pos=['center',0],color="#FFFFFF")
            
            Box(name='bottomBox',size=[750, 100],background="#4E7ED8",border='0px solid #fff',position='fixed', bottom=0, borderRadius='0%')
                
            Button(name='shareBtn', hidden=True,formType='submit', onTap = goShare, text='邀请好友来测 >', size=[750, 110], position='fixed', bottom=0,borderRadius='0%', 
                lineHeight=110, background="#FEB621", color="#663300", fontSize=38, fontWeight=600,openType='getUserInfo')
            ShareButton(name='shareBtnAuditing', hidden=False, formType='submit', text='邀请好友来测 >', size=[750, 100], position='fixed', bottom=0,borderRadius='0%', 
                lineHeight=100, background="#FEB621", color="#663300", fontSize=36, fontWeight=600,openType='getUserInfo')
            
            # Box(name='midline',size=[2, 50],background="#FFF",hidden=True, border='0px solid #fff',position='fixed', right=380, bottom=28, borderRadius='0%')
               
            Button(name='beginPlay', hidden=True, position='fixed', bottom=0, text='创建我的好友回忆墙 >', size=[750, 100], 
                lineHeight=100, background="#FEB621", color="#663300", fontSize=36,openType='getUserInfo', fontWeight=900,onTap=toBegin)

        with Page(name='share',enableShare=True):
            this.onReady = shareReady

            Image(name='shareImage',hidden=True,src='http://material.motimaster.com/yuyuan/Duudle/create/93c539e06f357977dc224f88e952ba3f.jpg',pos=[23,23,704,704])
            ImageAvatar(name='avatar',pos=[297,393,149,149],borderRadius='50%')

            Button(name='saveShareImage', hidden=True,onTap=[moui.showLoading(),saveShareImage,moui.hideLoading()],text='保存',fontWeight=900,lineHeight=80,pos=[175,780,400,80], boxShadow='-1px 10px 5px -5px #BBBBBB',fontSize='16px', color='#663300',border='1px solid #FFD886',backgroundColor="#FEB621")
            ShareButton(text='分享到好友群',pos=[175,923,400,80], color='#FFD886',border="1rpx solid #FFD886",fontSize='16px',lineHeight=80,boxShadow='-1px 15px 30px -12px black',background='#000000',type='primary')
async def beginReady(user, app, page, mo):
    if AUDITING == True:
        page.loading_box.hidden=True
        mo.redirectTo('page1',mode='auditing')
        #page.auditing_box.hidden=False
    else:
        page.loading_box.hidden=True
        rets = mo.db.hosts.find({'openid':user.openid})
        page.entrance.hidden = False
        if len(rets) !=0:
            mo.redirectTo('mainpage',is_host=1, hostopenid=user.openid)
        
    

async def computeNameScore(user, app, page, mo):
    mo.showAlert('名字点数','您的名字点数为%s'% str(int(random.random()*100)))
    


async def checkDetailPay(user, app, page, mo, params):
    page.data.host_id = params.host_id
    page.data.guest_id = params.guest_id
    mo.console(page.data.host_id)
    mo.console(page.data.guest_id)
    mo.wxpay.pay('查看与ta的回忆', 0.1, onPaySuccess,  onPayFail)

async def onPaySuccess(user, app, page, mo):
    tmpRecord = mo.db.guests.find({'openid':page.data.host_id,'hostopenid':page.data.guest_id})
    click_list = tmpRecord[0]['clickState']
    page.guest_detail.data = []
    page.ansMask.hidden = False
    l = [e for idx, e in enumerate(events) if click_list[idx]==1]
    for i in range(len(l)):
        page.guest_detail.data.append({'answer': l[i]})

    user.unlockAll = True
    mainPageReady(user, app, page, mo)

async def onPayFail(user, app, page, mo):
    pass
async def toBegin(user, app, page, mo):
    mo.goto('mainpage', is_host = 1)
    
async def goShare(user, app, page, mo):
    mo.goto('share', hostopenid = user.openid)
    
async def saveShareImage(user, app, page, mo):
   mo.saveImage(page.data.url)
    
def shareReady(user, app, page, mo):
    if AUDITING == False:
        page.saveShareImage.text = '保存朋友圈海报'
        page.saveShareImage.hidden = False

    params = {
        "page":'page1',
        "width":140,
        'options':{
            "openid": user.openid,
            'avatar':user.avatarUrl,
            'nick':user.nickName
        }
    }
    retParams = mo.acode.getWxAcodeUrl(params)
    erweima = None
    if retParams['ret'] == 0:
        erweima = retParams['url']

        canvas = mo.mopic.createCanvas(750, 750)
    canvas.addImage('http://material.motimaster.com/yuyuan/Duudle/create/93c539e06f357977dc224f88e952ba3f.jpg', pos=[0,0,750,750])
    
    canvas.addImage(erweima, pos=[225,350,300,300], mask='circle')
    canvas.addImage(user.avatarUrl, pos=[305, 430,140,140], mask='circle')
    res = canvas.makeImage()
    mo.console(res)
    if res['ret'] == 0:
        page.shareImage.src=res['url']
        page.data.url = res['url']
        
    page.shareImage.hidden = False
    page.avatar.hidden = True
    page.share.title = '你和%s的友情能打几分？来试试！' % user.nickName
    page.share.imageUrl = 'http://material.motimaster.com/yuyuan/Duudle/create/1fb03a716bec6ee8742dcbd80a1a0c77.jpg'
    page.share.page = 'page1'
        
    page.share.options = {
        'openid': user.openid,
        'avatar':user.avatarUrl,
        'nick':user.nickName
    }

async def page1Ready(user, app, page, mo): 
    if page.options.mode == 'auditing' and page.options.openid == None:
        page.hostName.text = '在你心中，要一起做哪些事，才算是你的满分好友呢？'
        all_event = [{'index':x, 'text':events[x]} for x in range(30)]
        things_list = all_event.copy()
        for item in things_list:
            item['background'], item['color'] = 'rgba(17,17,17,0.39)', '#FFD886'
            mo.console('-%s-\n' %item['text'])
        page.things.data = things_list
        clickState = [0]*32
        page.data.set('clickState', clickState)
        page.data.set('things_list', things_list)
        page.btn.hide()

        return
    record = mo.db.guests.find({'hostopenid':page.options.openid, 'openid':user.openid})
    if page.options.openid == user.openid: # host进入跳转到mainpage
        mo.redirectTo('mainpage',is_host = 1)
        return
    if record: # guest答过跳转到mainpage
        mo.redirectTo('mainpage',is_host = 0, hostopenid=page.options.openid)
        return
    page.hostAvatar.src = page.options.avatar
    page.hostName.text = '来选出你和%s的共同回忆吧~看看你和TA的友情能拿多少分？' %page.options.nick
    all_event = [{'index':x, 'text':events[x]} for x in range(30)]
    things_list = all_event.copy()
    for item in things_list:
        item['background'], item['color'] = 'rgba(17,17,17,0.39)', '#FFD886'
        mo.console('-%s-\n' %item['text'])
    page.things.data = things_list
    clickState = [0]*32
    page.data.set('clickState', clickState)
    page.data.set('things_list', things_list)
    page.btn.hide()

async def checkDetail(user, app, page, mo, params):
    if params.host_id != user.openid and params.guest_id != user.openid:
        mo.showAlert('温馨提示:','亲，不好意思，该功能只对主人开放')
        return
    tmpRecord = mo.db.guests.find({'openid': params.guest_id,'hostopenid':params.host_id})
    click_list = tmpRecord[0]['clickState']
    page.guest_detail.data = []
    page.ansMask.hidden = False
    l = [e for idx, e in enumerate(events) if click_list[idx]==1]
    for i in range(len(l)):
        page.guest_detail.data.append({'answer': l[i]})
            
async def makeChioce(user, app, page, mo, params):
    all_event = [{'index':x, 'text':events[x]} for x in range(30)]
    clickState = page.data.get('clickState')
    things_list = page.data.get('things_list')
    for item in things_list:
        if item['index'] == params.index:
            if clickState[item['index']] == 0:
                item['background'], item['color'] = guestColor, 'black'
                clickState[item['index']] = 1
                if clickState.count(1) > 0:
                    page.btn.show()
            else: 
                item['background'], item['color'] = 'rgba(17,17,17,0.39)', '#FFD886'
                clickState[item['index']] = 0
                if clickState.count(1) == 0:
                    page.btn.hide()
            break
    page.data.set('clickState', clickState)
    page.data.set('things_list', things_list)
    page.things.data = things_list
    
async def submit(user, app, page, mo):
    if page.options.mode == 'auditing' and page.options.openid == None:
        mo.redirectTo('mainpage', is_host = 1, hostopenid=page.options.openid)
        return
    clickState = page.data.get('clickState')
    count = sum(clickState)
    
    if count==1:
        score = random.randint(40,43)
    elif count==2:
        score = random.randint(44,47)
    elif count==3:
        score = random.randint(48,51)
    elif count==4:
        score = random.randint(51,54)
    elif count==5:
        score = random.randint(55,58)
    elif count==6:
        score = random.randint(59,62)
    elif count==7:
        score = random.randint(63,66)
    elif count==8:
        score = random.randint(67,70)
    elif count==9:
        score = random.randint(71,74)
    elif count==10:
        score = random.randint(75,78)
    elif count==11:
        score = random.randint(79,82)
    elif count==12:
        score = random.randint(83,86)
    elif count==13:
        score = random.randint(87,90)
    elif count==14:
        score = random.randint(91,93)
    elif count==15:
        score = random.randint(94,96)
    elif count==16:
        score = random.randint(97,98)
    elif count==17:
        score = 99
    else:
        score = 100
    
    if count in list(range(1,6)):
        words = random.choice([
                '虽然共同的回忆有点少，但这样的友情不多不少刚刚好。',
                '我们之间还差点小默契，但合适的距离能产生最合适的友情。',
                '互斥又互相吸引，我们的故事不会轰轰烈烈，但细水长流。',
                '我们不一定是最合拍，但一定是对方心中的无可替代。',
                '虽然错过了很多风景，但是未来的旅途一定会携手同行。',
                '即使有各自不同的轨道，但也能给彼此带来不一样的光和热。',
                '见面会嫌弃，离开会想念，其实内心很想粘着你~',
                '冰与火也能摩擦出光亮，我们在磨合中彼此靠近，共同进步。'
                ])
    elif count in list(range(6,9)):
        words = random.choice([
                '是彼此的一道光，给对方带来无限温暖和正能量。',
                '或许我们之间还需要磨合，但未来一定可以成全最好的自己。',
                '相爱又相互伤害，但只要你需要我，我就会在。',
                '你和我都是自由的风，却总是会在相同的时空意外相逢。',
                '双商都高，沟通不累，心照不宣是我们独有的默契。',
                '相见恨晚，志趣相投，你我都是彼此最美丽的遇见。'
                ])
    elif count in [9,10]:
        words = random.choice([
                '是彼此的小幸运，未来一定要去看更美的风景。',
                '无论快乐还是悲伤，都是彼此最不设心防的倾诉对象。',
                '这个世界很善变，但我们之间的默契随时都经得起考验。',
                '你和我是贴合的两块拼图，是理性与感性的互补。',
                '势均力敌，惺惺相惜，你和我拥有相同的颜色。'
                ])
    elif count in [11,12,13]:
        words = random.choice([
                '因为遇见，所以欣赏；因为欣赏，所以陪伴。',
                '会互相拆台也会互相崇拜，若要仗剑天涯，你是最佳拍档。',
                '相处从不会累，因为在一起时快乐总是加倍。',
                '水乳交融，恰到好处，你的一个眼神，我就能懂。',
                '天生默契，彼此之间就像是磁铁般相互吸引靠近。',
                '吃喝玩乐，样样有你，你让我拥有了更有趣的人生。'
                ])
    elif count in [14,15,16]:
        words = random.choice([
                '和优秀的人在一起会更优秀，一起打造完美世界吧！',
                '可以一秒读懂对方，连沉默都是心照不宣的默契。',
                '心灵相通，一拍即合，是你让我看到了更大的世界。',
                '会把脆弱留给对方，因为在彼此面前无需筑起心防。',
                '吵着闹着，乐在其中，有你在的时候总是最舒心。',
                '同甘共苦，福祸相依，一起哭，一起笑，一起闹。'
                ])
    else:
        words = random.choice([
                '就算世界毁灭，我们都不离不弃，绝对不松手。',
                '相遇花光了所有的运气，所以未来一定要彼此珍惜。',
                '就像是连体婴，相互陪伴是最长情的生命告白。',
                '小秘密只愿和你分享，我最信任你，也最依赖你。',
                '天作之合，完美搭配，永远是彼此最坚实的后盾。'
                ])

    mo.db.guests.insert({
        'openid'     : user.openid,
        'nick'       : user.nickName,
        'avatar'     : user.avatarUrl,
        'hostopenid' : page.options.openid,
        'score'      : score,
        'statement'  : words,
        'clickState' : clickState,
        'timestamp'  : int(time.time())
    })
    mo.goto('mainpage', is_host = 0, hostopenid=page.options.openid)
    
async def mainPageReady(user, app, page, mo):

    hide_pay = True

    if int(page.options.is_host) == 1:
        if user.unlockAll != True:
            hide_pay = False
        host = mo.db.hosts.find({'openid':user.openid})

        if host == []:
            tmp_id = mo.db.hosts.insert({
                'openid'    : user.openid,
                'nick'      : user.nickName,
                'avatar'    : user.avatarUrl,
                'timestamp' : int(time.time())
            })
            host = mo.db.hosts.find({'id': tmp_id})
        page.shareBtn.show()
        page.beginPlay.hide()
    else:

        hide_pay = True
        host = mo.db.hosts.find({'openid':page.options.hostopenid})
        page.shareBtn.hide()
        page.beginPlay.show()
    page.helpBtn.show()
    page.authorAvatar.src = host[0]['avatar']

    page.guest_records.data = []
    page.guest_stars.data = []
    guests = mo.db.guests.find({'hostopenid':host[0]['openid']})
    guests = sorted(guests, key=lambda x:-x['timestamp'])
    if len(guests) == 0 and AUDITING == False:
        page.tip1.show()
        page.tip2.show()


    if AUDITING or ENABLE_PAY == False:
        hide_pay = True

    for guest in guests:
        if guest['nick'] is None:
            continue

        hide_delete = True
        if user.openid == guest['openid'] or user.openid == guest['hostopenid']:
            hide_delete = False
        

        
        page.guest_records.data.append({
            'id'              : guest['id'],
            'host_avatar'     : host[0]['avatar'],
            'guest_avatar'    : guest['avatar'],
            'host_nick'       : host[0]['nick'],
            'guest_nick'      : guest['nick'],
            'score'           : guest['score'],
            'fit_words'       : guest['statement'],
            'height': 360,
            'guest_openid': guest['openid'],
            'host_openid': host[0]['openid'],
            'hide_delete': hide_delete,
            'hide_pay': hide_pay,
            'hide_show_momery': not hide_pay,
        })

        score = guest['score']
        angle = random.randint(1, 89)

        dis   = 90 + 100 * (100 - score) / 24
        dtop  = dis * math.sin(math.radians(angle))
        dleft = dis * math.cos(math.radians(angle))

        top  = 488 + random.choice([-1, 1]) * dtop - 35
        left = 375 + random.choice([-1, 1]) * dleft - 35

        guangtop  = top - 17
        guangleft = left - 17

        page.guest_stars.data.append({
            'avatar' : guest['avatar'],
            'top' : '%drpx' % top,
            'left' : '%drpx' % left,
            'guangtop' : '%drpx' % guangtop,
            'guangleft' : '%drpx' % guangleft
        })
    count = len(page.guest_records.data)
    if count > 0:
        page.guest_records.data[count-1]['height'] = page.guest_records.data[count-1]['height'] + 130
        page.shareBtn.size = [750,100]
        page.shareBtn.left = 0
        page.shareBtn.text = '邀请好友来测'
        # page.midline.show()
    else:
        page.leida.hidden = True

    page.share.title = '你和%s的友情能打几分？来试试！' % host[0]['nick']
    page.share.imageUrl = 'http://material.motimaster.com/yuyuan/Duudle/create/1fb03a716bec6ee8742dcbd80a1a0c77.jpg'
    page.share.page = 'page1'
    page.share.options = {
        'openid':host[0]['openid'],
        'avatar':host[0]['avatar'],
        'nick':host[0]['nick']
    }

    if AUDITING:
        page.shareBtn.hidden = True
        page.shareBtnAuditing.hidden = False
        
    else:
        page.shareBtn.hidden = False
        page.shareBtnAuditing.hidden = True



    mo.console('mainready %s' % page.share.options)

async def deleteRecord(user, app, page, mo, params):
    mo.console('确定删除')
    rid = params.rid
    mo.console(rid)
    mo.db.guests.delete(rid)
    mainPageReady(user, app, page, mo)
        
events=[
'一起吃过饭',
'一起合过影',
'一起唱过K',
'一起看过电影',
'一起组过队打游戏',
'一起逛过街',
'一起打过球',
'一起喝过酒',
'一起熬过夜',
'一起煲过电话粥',
'一起庆过生',
'一起逃过课',
'一起罚过站',
'一起抄过作业',
'一起追过喜欢的人',
'一起打过架',
'一起通宵看过球',
'一起玩过桌游',
'一起做过饭',
'一起骑行过',
'一起爬过山',
'一起去过游乐园',
'一起旅过游',
'一起追过星',
'一起听过演唱会',
'一起穿过基友/闺蜜装',
'一起洗过澡',
'一起搓过背',
'一起同床睡过觉',
'一起哭过'
]