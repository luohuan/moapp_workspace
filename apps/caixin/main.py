import random
import time

bg="http://material.mogolane.cn/yuyuan/friendtest/create/ecfadc604f2eb4a077bf70655085c1fe.jpg"
top="http://material.mogolane.cn/yuyuan/friendtest/create/9b2058e18350de530178574d169bf87e.png"
bling = "http://img.mogodeer.cn/images/yuan/4.png"
star = "http://img.mogodeer.cn/image/health/star.png"
liuxing = "http://img.mogodeer.cn/images/yuan/liuxing.png"
mid="http://material.mogolane.cn/yuyuan/friendtest/create/749841d5fefd885b241f5b4d245d637f.png"

AUDITING = False

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
    with MoApp(appid='wx18610e0755615e2f', name='你懂我吗', navigationBarTitleText = '你懂我吗', barColor = '#eeeeee', withLogin=True):
        # 设置问题页面
        with Page(name='mainpage',onReady=mainpageReady, background=bg, navigationBarTitleText = '你懂我吗', barColor = '#eeeeee'):
            starblink()

            Image(src=top,pos=[75,150,600,150])
            Text(text="（开始出题吧，五道题，选出你自己的答案~）",pos=['center',300],color='#FEB621',fontWeight='bold',fontSize=32)
            Box(pos=['center',392],size=[190,190],borderRadius='50%',background='#FFFFFF')
            ImageAvatar(pos=['center',396],size=[180,180],borderRadius='50%')
            TextNickName(pos=['center',600], color='#ffffff')
            Button(text='开始出题', boxShadow='-1px 15px 30px -12px black',fontSize=40, openType='getUserInfo', border="1rpx solid #FFD886",pos=['center',720],lineHeight=95,
                size=[369,95], type='miniDefault', background='#FEB621', borderRadius='20px',onTap=moui.goto('questpage'))

            
        with Page(name='questpage', background=bg,
            navigationBarTitleText = '你懂我吗', barColor = '#eeeeee', onReady = onQuestPageReady):
            
            starblink()
            
            Box(pos=['center',6],size=[160,160],borderRadius='50%',background='#FFFFFF')
            ImageAvatar(pos=['center',10],size=[150,150],borderRadius='50%')
            Image(src=top,pos=[75,150,600,150])
            Text(text="（五道题，选出你自己的答案~）",pos=['center',270],color='#FEB621',fontWeight='bold',fontSize=32)
            
            Text(name='question',pos=['center',360],size=[650,60],textAlign='center',color='#FFFFFF',fontWeight='bold',fontSize=37)
            Button(name='setAns1', pos=[125,500,500,80],openType='getUserInfo',background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",onTap=setAns1)
            Button(name='setAns2',pos=[125,610,500,80],openType='getUserInfo',background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",onTap=setAns2)
            Button(name='setAns3',pos=[125,720,500,80],openType='getUserInfo',background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",onTap=setAns3)
            Button(name='setAns4',pos=[125,830,500,80],openType='getUserInfo',background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",onTap=setAns4)
        
        # 邀请页面，生成小程序码或sharebutton邀请
        with Page(name='resultpage', navigationBarTitleText = '好友成绩榜~', background=bg,enableShare=True, onShareSuccessed=onShare,onReady=resultPageReady):
            starblink()
  
            Box(pos=['center',16],size=[160,160],borderRadius='50%', background='#FFFFFF')
            Image(name='hostAvatar',pos=['center',20],size=[150,150],borderRadius='50%')
            Text(text="『 谁是最懂我的人 』",pos=['center',180],color='#FEB621',fontWeight='bold',fontSize=40)
            
            with Box(width='80%', height=120, pos=['center',270], borderRadius=8,border="1rpx solid #000000",background='#000000'):
                Text(name='hostName', fontSize=38,pos=['center',0],color='#FEB621')
                Text(name='shownum',pos=['center',55],fontSize=28, color='#FFFFFF')
            with ScrollBox(scrollY=True, size=[600, 500], pos=['center',380], background='#FFFFFF'):
                with List(name='oneQuestionList', position='relative', width='100%'):
                    with Box(height=145, background='#FFFFFF', fontSize=30, border='1px solid #cccccc'):
                        # Text(text='{item.time}', pos=['left',0])
                        Image(src='{item.portrait}', pos=[20,30], size=[90,90], borderRadius='50%')
                        Text(text='{item.a_name}', fontSize=33,color='#063078',pos=[120,32])
                        Text(text='{item.state}', pos=[120,85],fontSize=25,color='#7B7B7B')
                        Text(text='{item.score}',fontSize=65, fontWeight='bold',color='#750000',pos=[442,16])
                        Text(text='分', pos=['right',53])
                        # Button(hidden=True,name='showAns',text="看TA的选择",pos=[442,98],size=[130,37],boxShadow='-1px 15px 30px -12px black',fontSize=22, 
                        # border="1rpx solid #FFD886",lineHeight=37, color='black',background='#FEB621', borderRadius='10px', onTap = moui.request(showDetail, visit_id ='{item.openid}'))
                        Button(hidden=True,name='showShare',text="看TA的选择",pos=[442,98],size=[130,37],boxShadow='-1px 15px 30px -12px black',fontSize=22, 
                        border="1rpx solid #FFD886",lineHeight=37, color='black',background='#FEB621', borderRadius='10px', onTap = moui.request(maskShow, visit_id ='{item.openid}'))

                        Button(hidden=True,name='payBtn',text="看TA的选择",pos=[442,98],size=[130,37],boxShadow='-1px 15px 30px -12px black',fontSize=22, 
                        border="1rpx solid #FFD886",lineHeight=37, color='black',background='#FEB621', borderRadius='10px', onTap=moui.confirm('温馨提示:',"查看全部好友的答题详情（包括未来进入的好友），只需支付金额9.9元。",onPay))
                Text(name='noAnswer',pos=['center','center'])
            #Button(hidden=True,name='unlock',text="一键解锁所有答案", pos=[120,900,500,90])
            # Button(hidden=True,name='unlock',text="一键解锁所有答案",pos=[120,900,500,90],
            # border="1px solid #FFD886",color='#663300', boxShadow='-1px 15px 30px -12px black',background='#FEB621',fontSize=40, lineHeight=90,borderRadius='10px')

            Button(hidden=True,name='invitButton', text="邀请好友来做题",pos=[120,900,500,90],onTap=toInvitePage,
            effect=shake(t=2, c=0),border="1px solid #FFD886",color='#663300', boxShadow='-1px 15px 30px -12px black',background='#FEB621',fontSize=40, lineHeight=90,borderRadius='10px')
            # Image()
            Image(name='guanggao', hidden=True,onTap=onguanggao,src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg', size=[750,125],bottom=0 )
            ShareButton(hidden=True,name='shareButton',text="邀请好友来做题",pos=[120,950,500,90],
            effect=shake(t=2, c=0),border="1px solid #FFD886",color='#663300', boxShadow='-1px 15px 30px -12px black',background='#FEB621',fontSize=40, lineHeight=90,borderRadius='10px')

            # Button(hidden=True,name='QAagain',text="再玩一次",pos=[120,950,500,90],onTap=toInvitePage,
            # effect=shake(t=2, c=0),border="1px solid #FFD886",color='#663300', boxShadow='-1px 15px 30px -12px black',background='#FEB621',fontSize=40, lineHeight=90,borderRadius='10px')
            
            Button(hidden=True,name='showdetail',text="查看答案详情",pos=['center',900],size=[500,75],boxShadow='-1px 15px 30px -12px black',fontSize=40, border="1rpx solid #FFD886",lineHeight=75, background='#000000', color='#FEB621',borderRadius='10px',onTap=showDetail)

            Button(hidden=True,name='QAagain',text="我也要出题",pos=['center',1000],size=[500,90],border="1px solid #FFD886",color='#663300', boxShadow='-1px 15px 30px -12px black',background='#FEB621',fontSize=40, lineHeight=90,borderRadius='10px',effect=shake(t=2, c=0),
            onTap=moui.redirectTo('questpage'))
            ContactButton(name='helpBtn',hidden=True,plain=True, border="None", pos=[32,48], size=[64, 64],borderRadius='50%',boxShadow='0px 0px 0px 2rpx gray', background='http://material.motimaster.com/harvey/5455/myrose/13266bbea43f54ee7f32d9e979f0c7d5.png')
            with Mask(name='ansMask', hidden=True):
                with Box(background='rgba(17,17,17,0.8)',borderRadius='10px',border='1px solid #FFD886',size=[550, 700], pos=['center',200]):
                    with Box(position='relative',size=[550,50]):
                        Text(name='above', color="#FFD886",fontSize=33,fontWeight='bold',pos=['center',0])
                    with List(name='hostAns',position='relative'):
                        with Box(height=50):
                            Text(text='{item.trueAns}',fontSize=28,pos=['center',0],color="#FFFFFF")
                    with Box(position='relative',size=[550,50]):
                        Text(name='low', size=[550,50],width=550,textAlign='center',color="#FFD886",fontSize=33,fontWeight='bold',pos=['center',0])
                    with List(name='visitAns',position='relative'):
                        with Box(height=50):
                            Text(text='{item.guessAns}',fontSize=28,pos=['center',0],color="#FFFFFF")
            with Mask(name='mask', hidden=True, locked=True):
                with Box(size=[600,300],pos=['center',400],backgroundColor='white',borderRadius=2):
                    Text(text='温馨提示',fontSize=35, pos=['center',25], fontWeight='bold')
                    Text(text='分享给群好友,即可查看哦',fontSize=33,color='#888888',pos=['center',100])
                    # Text(text='让其他好友也来测测吧!',fontSize=30,color='#888888',pos=['center',120])
                    Button(text='取消',onTap=cancel,textAlign='center',size=[300,100],lineHeight=100,pos=[0,200],
                        color='black',borderTop='1rpx solid #eeeeee',borderRight='1rpx solid #eeeeee',backgroundColor='white',borderRadius='0')
                    ShareButton(text='分享',textAlign='center',size=[300,100],lineHeight=100,pos=[300,200],
                        color='#09BB07',borderTop='1rpx solid #eeeeee',backgroundColor='white',borderRadius='0')
        
        with Page(name='invitpage', navigationBarTitleText='邀请好友', background='#FFFFFF', enableShare=True, 
        onReady=[moui.showLoading('生成图片中...'), invitPageReady, moui.hideLoading()]):
            with Box(size=[750,750], pos=[0,0], textAlign='center'):
                Image(id='shareImage', src='http://material.motimaster.com/yuyuan/Duudle/create/8e82f60a1c3336215d3cff6454cfa85e.jpg',pos=[15,10,720,722])
            with Box(pos=['center', 800], width=750, height=750):
                Button(name='saveimg',text='保存图片', pos=['center',0,500,90], boxShadow='-1px 15px 30px -12px black',fontSize=40, border="1rpx solid #FFD886",lineHeight=90, background='#FEB621', color='black',borderRadius='10px',type='primary', onTap=save)
                ShareButton(text='邀请好友答题', pos=['center',150,500,90], type='primary',color='#FFD886', boxShadow='-1px 15px 30px -12px black',fontSize=40, border="1rpx solid #FFD886",lineHeight=90,borderRadius='10px',background='#000000')
        
        with Page(name='answerpage', navigationBarTitleText = '五道题，看看你能多少分~', background=bg, onReady=answerPageReady):
            starblink()

            Box(pos=['center',16],size=[160,160],borderRadius='50%', background='#FFFFFF')
            Image(name='hostimage', pos=['center',20],size=[150,150],borderRadius='50%',effect=rotatein(t=1,c=1))
            
            Text(name='subtitle',pos=['center',220],color='#FEB621',fontWeight='bold',fontSize=32)
            Text(name='question',pos=['center',310],size=[600,60],textAlign='center',color='#FFFFFF',fontWeight='bold',fontSize=37)
            Button(name='setAns1',pos=[125,450,500,80],background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",openType='getUserInfo', onTap=AnswerTap1)
            Button(name='setAns2',pos=[125,560,500,80],background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",openType='getUserInfo',onTap=AnswerTap2)
            Button(name='setAns3',pos=[125,670,500,80],background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",openType='getUserInfo',onTap=AnswerTap3)
            Button(name='setAns4',pos=[125,780,500,80],background='rgba(17,17,17,0.39)', fontSize=28,borderRadius='8px',color="#FFD886",border="1px solid #FEB621",openType='getUserInfo',onTap=AnswerTap4)

async def onguanggao(user, app, page, mo):
    mo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx6')
async def onShare(user, app, page, mo):
    visit_id = page.data.visit_id
    if visit_id == None:
        return
    page.ansMask.hidden = False
    
    #if page.options.visit_id:
    if mo.db.simQuestion.find({'id': page.options.ID})[0]['openid'] == user.openid: # host进入  ###条件判断有问题
        hostData = list(mo.db.simQuestion.find({'id': page.options.ID})[0]['hostRecord'])
        visitData = list(mo.db.simAnswer.find({'quest_id': page.options.ID, 'openid': visit_id})[0]['visitRecord']) #############
        mo.console(hostData)
        mo.console(visitData)
        host =[]
        visit = []
        for i in range(len(hostData)):
            host_dict = {}
            visit_dict = {}
            host_dict['guessAns'] = str(hostData[i])
            visit_dict['trueAns'] = str(visitData[i])
            host.append(host_dict)
            visit.append(visit_dict)
        page.above.text = 'TA的猜测：'
        page.low.text = '我的答案：'
        # -------------------host, visit回答顺序调转----------------
        mo.console(visit)
        mo.console(host)
        page.hostAns.data = visit
        page.visitAns.data = host
    page.mask.hidden = True
async def cancel(user, app, page, mo):
    page.mask.hidden = True
async def maskShow(user, app, page, mo, params):
    # page.data.visit_id = params.visit_id
    # page.mask.hidden = False
    page.data.visit_id = params.visit_id
    onShare(user, app, page, mo)


async def onPay(user, app, page, mo):
    mo.wxpay.pay('查看详情', 9.9, onPaySuccessed2, onPayFailed2)

async def onPaySuccessed2(user, app, page, mo):
    currentQuestion = mo.db.simQuestion.find({'id':page.options.ID})[0]
    currentQuestion['unlock'] = True
    mo.db.simQuestion.update(page.options.ID, currentQuestion)
    page.payBtn.hidden = True
    page.payBtn.hidden = False

async def onPayFailed2(user, app, page, mo):
    pass

async def mainpageReady(user, app, page, mo):
    recoreds = mo.db.simQuestion.find({'openid': user.openid})
    if len(recoreds) > 0:
        mo.redirectTo('resultpage', openid=user.openid, ID = recoreds[0]['id'])
    # pass
    # id = mo.db.simQuestion.insert({
    #         'name': user.nickName,
    #         'openid': user.openid,
    #         'avatarUrl': user.avatarUrl,
    #         'QAdata': page.data.QAdata,
    #         'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    #         'hostRecord':page.data.hostRecord})
        
# 显示问题页面的问题、选项
async def onQuestPageReady(user, app, page, mo):
    if user.gender == 1:
        QAdata=man_data[random.choice([0,3])]
        page.data.QAdata = QAdata
        page.question.text = QAdata[0]['question']
        ans_length = len(QAdata[0]['answer'])
        
        if ans_length == 4:
            page.setAns4.hidden = False
            page.setAns3.hidden = False
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
            page.setAns3.text = QAdata[0]['answer'][2]
            page.setAns4.text = QAdata[0]['answer'][3]
        elif ans_length == 3:
            page.setAns4.hidden = True
            page.setAns3.hidden = False
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
            page.setAns3.text = QAdata[0]['answer'][2]
        else:
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
    else:
        QAdata=female_data[random.choice([0,4])]
        page.data.QAdata = QAdata
        page.question.text = QAdata[0]['question']
        ans_length = len(QAdata[0]['answer'])
        if ans_length == 4:
            page.setAns4.hidden = False
            page.setAns3.hidden = False
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
            page.setAns3.text = QAdata[0]['answer'][2]
            page.setAns4.text = QAdata[0]['answer'][3]
        elif ans_length == 3:
            page.setAns4.hidden = True
            page.setAns3.hidden = False
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
            page.setAns3.text = QAdata[0]['answer'][2]
        else:
            page.setAns1.text = QAdata[0]['answer'][0]
            page.setAns2.text = QAdata[0]['answer'][1]
    page.data.count = 0
    page.data.hostRecord = []
   
async def toInvitePage(user, app, page, mo):
    mo.goto('invitpage', id = page.options.ID)
    return
async def save(user, app, page, mo):
    mo.saveImage(page.data.url)

async def setAns1(user, app, page, mo):
    tmpRecord = page.data.hostRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][0])
    page.data.hostRecord = tmpRecord
    
    if page.data.count == len(page.data.QAdata)-1:
        id = mo.db.simQuestion.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'QAdata': page.data.QAdata,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'hostRecord':page.data.hostRecord})
        mo.redirectTo('resultpage', openid=user.openid, ID = id)
        return
    setAnswer(user, app, page, mo)
async def setAns2(user, app, page, mo):
    tmpRecord = page.data.hostRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][1])
    page.data.hostRecord = tmpRecord
    
    if page.data.count == len(page.data.QAdata)-1:
        id = mo.db.simQuestion.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'QAdata': page.data.QAdata,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'hostRecord':page.data.hostRecord})
        mo.redirectTo('resultpage', openid=user.openid, ID = id)
        return
    setAnswer(user, app, page, mo)
async def setAns3(user, app, page, mo):
    tmpRecord = page.data.hostRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][2])
    page.data.hostRecord = tmpRecord
    
    if page.data.count == len(page.data.QAdata)-1:
        id = mo.db.simQuestion.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'QAdata': page.data.QAdata,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'hostRecord':page.data.hostRecord})
        mo.redirectTo('resultpage', openid=user.openid, ID = id)
        return
    setAnswer(user, app, page, mo)
async def setAns4(user, app, page, mo):
    tmpRecord = page.data.hostRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][3])
    page.data.hostRecord = tmpRecord
    
    if page.data.count == len(page.data.QAdata)-1:
        id = mo.db.simQuestion.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'QAdata': page.data.QAdata,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'hostRecord':page.data.hostRecord})
        mo.redirectTo('resultpage', openid=user.openid, ID = id)
        return
    setAnswer(user, app, page, mo)
async def setAnswer(user, app, page, mo):
    count = int(page.data.count)+1
    page.question.text = page.data.QAdata[count]['question']
    ans_length = len(page.data.QAdata[count]['answer'])
    if ans_length == 4:
        page.setAns4.hidden = False
        page.setAns3.hidden = False
        page.setAns1.text = page.data.QAdata[count]['answer'][0]
        page.setAns2.text = page.data.QAdata[count]['answer'][1]
        page.setAns3.text = page.data.QAdata[count]['answer'][2]
        page.setAns4.text = page.data.QAdata[count]['answer'][3]
    elif ans_length == 3:
        page.setAns4.hidden = True
        page.setAns3.hidden = False
        page.setAns1.text = page.data.QAdata[count]['answer'][0]
        page.setAns2.text = page.data.QAdata[count]['answer'][1]
        page.setAns3.text = page.data.QAdata[count]['answer'][2]
    else:
        page.setAns4.hidden = True
        page.setAns3.hidden = True
        page.setAns1.text = page.data.QAdata[count]['answer'][0]
        page.setAns2.text = page.data.QAdata[count]['answer'][1]
    page.data.count = count
  
async def resultPageReady(user, app, page, mo):
    page.guanggao.hidden=True
    page.helpBtn.hidden = False
    a_list = mo.db.simAnswer.find({'quest_id':page.options.ID})
    page.shownum.text = '(目前已有'+str(len(a_list))+'个好友答题)'
    page.hostAvatar.src = mo.db.simQuestion.find({'id':page.options.ID})[0]['avatarUrl']
    page.hostName.text = mo.db.simQuestion.find({'id':page.options.ID})[0]['name']
    if a_list:
        reverse_alist = a_list[::-1] 
        ans4oneQuest = []
        for item in reverse_alist:
            A41Q_dict = {}
            A41Q_dict['time'] = item['time']
            A41Q_dict['a_name'] = item['name']
            A41Q_dict['score'] = item['score']
            A41Q_dict['state'] = statement[int(item['score']/20)]
            A41Q_dict['portrait'] = item['avatarUrl']
            A41Q_dict['openid'] = item['openid']
            ans4oneQuest.append(A41Q_dict)
        page.oneQuestionList.data = ans4oneQuest
    else:
        page.noAnswer.text = '好友的答题得分会出现在这里哦'
    if mo.db.simQuestion.find({'id':page.options.ID})[0]['openid'] == user.openid:
        if AUDITING == True:
            page.shareButton.hidden = False
        else:
            page.invitButton.hidden = False
            #page.showShare.hidden = False
            #page.payBtn.hidden = False
            currentQuestion = mo.db.simQuestion.find({'id':page.options.ID})[0]
            if 'unlock' in currentQuestion and currentQuestion['unlock'] == True:
                page.showShare.hidden = False
                page.payBtn.hidden = True
            else:
                page.payBtn.hidden = False
                page.showShare.hidden = True
        
        #page.invitButton.hidden = False
        #page.unlock.hidden = False
    else:
        page.QAagain.hidden = False
        page.showdetail.hidden = False

    # page.shareButton.hidden = False
    page.share.page = 'answerpage'
    page.share.title = "五道题，看看你对"+ str(user.nickName) + "到底了解多少？"
    page.share.imageUrl = 'http://material.motimaster.com/yuyuan/Duudle/create/2faa88acf89c5f482c5f49f5cafccdff.jpg'
    page.share.options = {
        "openid": user.openid,
        "nickName": user.nickName,
        "avatarUrl": user.avatarUrl,
        "db_id": page.options.ID # 出题id
    }

    

async def invitPageReady(user, app, page, mo):
    if AUDITING == False:
        page.saveimg.text = '保存朋友圈海报'
    page.share.page = 'answerpage'
    page.share.title = "五道题，看看你对"+ str(user.nickName) + "到底了解多少？"
    page.share.options = {
        "openid": user.openid,
        "nickName": user.nickName,
        "avatarUrl": user.avatarUrl,
        "db_id": page.options.id # 出题id
    }
    # 参数设置
    params = {
        'page': 'answerpage',
        'width': 150,
        'options': {
            'openid': user.openid,
            'nickName': user.nickName,
            'avatarUrl': user.avatarUrl,
            'db_id': page.options.id
        }
    }
    retParams = mo.acode.getWxAcodeUrl(params)

    erweima = None
    if retParams['ret'] == 0:
        erweima = retParams['url']
    else:
        mo.console(retParams)

    canvas = mo.mopic.createCanvas(705, 712)
    canvas.addImage('http://material.motimaster.com/yuyuan/Duudle/create/8e82f60a1c3336215d3cff6454cfa85e.jpg', pos=[0,0,705,712])
    canvas.addImage(erweima, pos=[250,300,248,248], mask='circle')
    canvas.addImage(user.avatarUrl, pos=[312,362,124,124], mask='circle')
    res = canvas.make()
    if res['ret'] == 0:
        page.shareImage.src = res['data']['url']
        page.data.url = res['data']['url']
    else:
        mo.console(res)
    mo.console(res)
async def answerPageReady(user, app, page, mo):
    cur_ans = mo.db.simAnswer.find({'quest_id': page.options.db_id, 'openid':user.openid})
    if cur_ans or page.options.openid == user.openid:
        # 重复点击分享\自问自答，跳转到单题答题记录
        mo.redirectTo('resultpage', ID = page.options.db_id)
        return
    db_data = mo.db.simQuestion.find({'id':page.options.db_id})[0]
    page.hostimage.src = db_data['avatarUrl']
    page.subtitle.text="五道题，来猜猜"+str(db_data['name'])+"的选择是什么？"
    page.data.QAdata = db_data['QAdata']
    page.data.count = 0
    page.question.text = page.data.QAdata[0]['question']
    ans_length = len(page.data.QAdata[0]['answer'])
    if ans_length == 4:
        page.setAns4.hidden = False
        page.setAns3.hidden = False
        page.setAns1.text = page.data.QAdata[0]['answer'][0]
        page.setAns2.text = page.data.QAdata[0]['answer'][1]
        page.setAns3.text = page.data.QAdata[0]['answer'][2]
        page.setAns4.text = page.data.QAdata[0]['answer'][3]
    elif ans_length == 3:
        page.setAns4.hidden = True
        page.setAns3.hidden = False
        page.setAns1.text = page.data.QAdata[0]['answer'][0]
        page.setAns2.text = page.data.QAdata[0]['answer'][1]
        page.setAns3.text = page.data.QAdata[0]['answer'][2]
    else:
        page.setAns1.text = page.data.QAdata[0]['answer'][0]
        page.setAns2.text = page.data.QAdata[0]['answer'][1]
    page.data.visitRecord = []
    page.data.score = 0
    page.data.hostRecord = db_data['hostRecord']
async def AnswerTap1(user, app, page, mo):
    tmpRecord = page.data.visitRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][0])
    page.data.visitRecord = tmpRecord
    if str(page.data.hostRecord[int(page.data.count)]) == str(page.data.QAdata[int(page.data.count)]['answer'][0]):
        score = page.data.score+20
        page.data.score = score
    if page.data.count == len(page.data.QAdata) - 1:
        mo.db.simAnswer.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'score': page.data.score,
            'quest_id': page.options.db_id,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'visitRecord':page.data.visitRecord})
        mo.redirectTo('resultpage', ID = page.options.db_id)
        return
    setAnswer(user, app, page, mo)
async def AnswerTap2(user, app, page, mo):
    tmpRecord = page.data.visitRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][1])
    page.data.visitRecord = tmpRecord
    if str(page.data.hostRecord[int(page.data.count)]) == str(page.data.QAdata[int(page.data.count)]['answer'][1]):
        page.data.score += 20
    
    if page.data.count == len(page.data.QAdata) - 1:
        mo.db.simAnswer.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'quest_id': page.options.db_id,
            'score': page.data.score,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'visitRecord':page.data.visitRecord})
        mo.redirectTo('resultpage', ID = page.options.db_id)
        return
    setAnswer(user, app, page, mo)
async def AnswerTap3(user, app, page, mo):
    tmpRecord = page.data.visitRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][2])
    page.data.visitRecord = tmpRecord
    if str(page.data.hostRecord[int(page.data.count)]) == str(page.data.QAdata[int(page.data.count)]['answer'][2]):
        page.data.score += 20
    
    if page.data.count == len(page.data.QAdata) - 1:
        mo.db.simAnswer.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'quest_id': page.options.db_id,
            'score': page.data.score,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'visitRecord':page.data.visitRecord})
        mo.redirectTo('resultpage', ID = page.options.db_id)
        return
    setAnswer(user, app, page, mo)
async def AnswerTap4(user, app, page, mo):
    tmpRecord = page.data.visitRecord
    tmpRecord.append(page.data.QAdata[page.data.count]['answer'][3])
    page.data.visitRecord = tmpRecord
    if str(page.data.hostRecord[int(page.data.count)]) == str(page.data.QAdata[int(page.data.count)]['answer'][3]):
        page.data.score += 20
    
    if page.data.count == len(page.data.QAdata) - 1:
        mo.db.simAnswer.insert({
            'name': user.nickName,
            'openid': user.openid,
            'avatarUrl': user.avatarUrl,
            'quest_id': page.options.db_id,
            'score': page.data.score,
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'visitRecord':page.data.visitRecord})
        mo.redirectTo('resultpage', ID = page.options.db_id)
        return
    setAnswer(user, app, page, mo)
    
async def showDetail(user, app, page, mo, params):
    page.ansMask.hidden = False
    
    #if page.options.visit_id:
    if mo.db.simQuestion.find({'id': page.options.ID})[0]['openid'] == user.openid: # host进入  ###条件判断有问题
        hostData = list(mo.db.simQuestion.find({'id': page.options.ID})[0]['hostRecord'])
        visitData = list(mo.db.simAnswer.find({'quest_id': page.options.ID, 'openid': params.visit_id})[0]['visitRecord']) #############
        mo.console(hostData)
        mo.console(visitData)
        host =[]
        visit = []
        for i in range(len(hostData)):
            host_dict = {}
            visit_dict = {}
            host_dict['guessAns'] = str(hostData[i])
            visit_dict['trueAns'] = str(visitData[i])
            host.append(host_dict)
            visit.append(visit_dict)
        page.above.text = 'TA的猜测：'
        page.low.text = '我的答案：'
        # -------------------host, visit回答顺序调转----------------
        mo.console(visit)
        mo.console(host)
        page.hostAns.data = visit
        page.visitAns.data = host
    else:# visit进入
        hostData = list(mo.db.simQuestion.find({'id': page.options.ID})[0]['hostRecord'])
        visitData = list(mo.db.simAnswer.find({'quest_id': page.options.ID, 'openid':user.openid})[0]['visitRecord'])
        host =[]
        visit = []
        for i in range(len(hostData)):
            host_dict = {}
            visit_dict = {}
            host_dict['trueAns'] = str(hostData[i])
            visit_dict['guessAns'] = str(visitData[i])
            host.append(host_dict)
            visit.append(visit_dict)
        page.above.text = 'TA的答案：'
        page.low.text = '我的猜测：'
        page.hostAns.data = host
        page.visitAns.data = visit
    
    
man_data1 = [
    {
        'question': '1/5:和喜欢的人看电影，我会选择哪个类型的片？',
        'answer': ['A.爱情片，营造浪漫气氛','B.喜剧片，一起开心','C.惊悚片，制造暧昧机会']
    },
    {
        'question':'2/5:下面四首歌，我会喜欢哪首？',
        'answer': ['A.五月天-《温柔》','B.赵雷-《成都》','C.周杰伦-《告白气球》','D.大壮-《我们不一样》']
    },
    {
        'question':'3/5:周末，下雨天，我会怎么度过？',
        'answer': ['A.拉上窗帘关上灯看电影','B.一直睡到第二天','C.给房间大扫除','D.打游戏']
    },
    {
        'question':'4/5:我和我暗恋的人现在是什么关系？',
        'answer': ['A.放下了，她已经有了爱人','B.成功俘获，已经在一起啦','C.放不下，还喜欢着她','D.追求ing']
    },
    {
        'question':'5/5:被恋人背叛了我会怎么做？',
        'answer': ['A.把劈腿对象狂扁一顿','B.果断分手，潇洒离开','C.嘴上祝幸福，背后喝醉到吐','D.我也立马绿了她']
    }
]
man_data2 = [
    {
        'question':'1/5:准备向喜欢的人表白，我会选择哪种方式？',
        'answer': ['A.约她出来，当面跟她说我喜欢你','B.深夜微信跟她说','C.拉上兄弟组织一场告白仪式','D.让身边人都知道，传话到她耳朵里']
    },
    {
        'question':'2/5:下面四份生日礼物，我会最喜欢哪个？',
        'answer': ['A.最新款篮球鞋','B.她亲手做的一顿生日餐','C.一件最爱球星的签名球衣','D.最新的游戏皮肤']
    },
    {
        'question':'3/5:朋友借我钱迟迟不还，我会怎么做？',
        'answer': ['A.不断暗示他最近自己很穷','B.直接跟他说该还了','C.算了，小事，不要了','D.不要了，同时跟他绝交']
    },
    {
        'question':'4/5:我和前任现在是什么关系？',
        'answer': ['A.老死不相往来','B.会说新年快乐的普通朋友','C.放不下，还喜欢着，复合努力中','D.没有前任']
    },
    {
        'question':'5/5:如果一夜暴富，我想做的第一件事是什么？',
        'answer': ['A.换个新身份','B.立马把老板炒了','C.打电话给前任，问她后悔吗','D.捐给慈善机构']
    }
]
man_data3 = [
    {
        'question':'1/5:表白被女神拒绝，我会怎么做？',
        'answer': ['A.不放弃，穷追不舍','B.做回普通朋友，争取用陪伴打动她','C.果断放下，寻觅下一个','D.变得更优秀让她主动追我']
    },
    {
        'question':'2/5:下面四项运动，我最热爱哪个？',
        'answer': ['A.足球','B.篮球','C.羽毛球','D.排球'],
    },
    {
        'question':'3/5:发现和好兄弟喜欢上了同一个女生，我会怎么做？',
        'answer': ['A.不想太多，公平竞争','B.兄弟情更重要，选择默默退出','C.主动找兄弟坦白，好好谈一谈','D.先向女神表明心意，再选择放下']
    },
    {
        'question':'4/5:下面四种类型的爸爸，我最想成为哪种？',
        'answer': ['A.黄磊式，温柔的厨神爸爸','B.陈小春式，又凶又软的妻管严','C.刘畊宏式，暖心又硬汉的女儿奴','D.林志颖式，青春不老的孩子王']
    },
    {
        'question':'5/5:我会怎么看待女朋友迷恋的男偶像？',
        'answer': ['A.表示鄙视，不男不女','B.支持她，找机会让她亲眼见偶像','C.表示生气，你眼中只能有我一个男人']
    }
]

man_data4 = [
    {
        'question':'1/5:觉得别人和我做朋友的原因是？',
        'answer': ['A.可爱的性格','B.有钱','C.有内涵，三观正','D.当然是颜值啦']
    },
    {
        'question':'2/5:表白被女神拒绝，我会怎么做？',
        'answer': ['A.不放弃，穷追不舍','B.做回普通朋友，争取用陪伴打动她','C.果断放下，寻觅下一个','D.变得更优秀让她主动追我']
    },
    {
        'question':'3/5:下面四种恋人类型，我会最喜欢哪个？',
        'answer': ['A.能让我天天都大笑的','B.能无微不至照顾我的','C.能督促我进步的','D.长得好看的']
    },
    {
        'question':'4/5:因为打游戏没接女朋友电话，我会怎么安抚生气的她？',
        'answer': ['A.跪搓衣板跪键盘','B.给她买鲜花买包包','C.直接给她发大红包','D.不哄，爱咋咋地'],
    },
    {
        'question':'5/5:我会怎么看待女朋友迷恋的男偶像？',
        'answer': ['A.表示鄙视，不男不女','B.支持她，找机会让她亲眼见偶像','C.表示生气，你眼中只能有我一个男人']
    }
]
man_data=[man_data1,man_data2,man_data3,man_data4]

female_data1 = [
    {
        'question': '1/5:和喜欢的人看电影，我会选择哪个类型的片？',
        'answer': ['A.爱情片，营造浪漫气氛','B.喜剧片，一起开心','C.惊悚片，制造暧昧机会']
    },
    {
        'question':'2/5:下面四首歌，我会喜欢哪首？',
        'answer': ['A.五月天-《温柔》','B.TFBOYS-《青春修炼手册》','C.周杰伦-《告白气球》','D.陈奕迅-《十年》']
    },
    {
        'question':'3/5:周末，下雨天，我会怎么度过？',
        'answer': ['A.拉上窗帘关上灯看电影','B.一直睡到第二天','C.给房间大扫除','D.打游戏']
    },
    {
        'question':'4/5:我和我暗恋的人现在是什么关系？',
        'answer': ['A.放下了，TA已经有了爱人','B.成功俘获，已经在一起啦','C.放不下，还喜欢着TA','D.追求ing']
    },
    {
        'question':'5/5:被恋人背叛了我会怎么做？',
        'answer': ['A.拉上死党去找小三','B.果断分手，潇洒离开','C.嘴上祝幸福，背后扎小人','D.我也立马绿了TA']
    }
]

female_data2 = [
    {
        'question': '1/5:和喜欢的人第一次约会，我会选择做什么？',
        'answer': ['A.看电影','B.去游乐场','C.逛美食街','D.去TA家做饭']
    },
    {
        'question':'2/5:我最喜欢什么样的天气？',
        'answer': ['A.晴天','B.阴天','C.雨天','D.下雪天']
    },
    {
        'question':'3/5:地铁上遇到色狼想占我便宜，我会怎么做？',
        'answer': ['A.不敢声张，悄悄躲开，尽快下地铁','B.大声斥责并警告他','C.悄悄偷拍他，发到朋友圈和微博','D.上去就是一脚']
    },
    {
        'question':'4/5:我和前任现在是什么关系？',
        'answer': ['A.老死不相往来','B.会说新年快乐的普通朋友','C.放不下，还喜欢着，复合努力中','D.没有前任']
    },
    {
        'question':'5/5:闺蜜和我男朋友在一起了，我会怎么做？',
        'answer': ['A.写一篇长帖，发到朋友圈和微博','B.果断分手和绝交，潇洒离开','C.祝他们幸福，是我耽误了他们','D.立马和男朋友的好兄弟在一起']
    }
]

female_data3 = [
    {
        'question': '1/5:准备向喜欢的人表白，我会选择哪种方式？',
        'answer': ['A.当面跟他说我喜欢你','B.深夜微信跟他说','C.悄悄把表白信放在他桌上','D.让身边人都知道，传话到他耳朵里']
    },
    {
        'question':'2/5:下面四份生日礼物，我会最喜欢哪个？',
        'answer': ['A.一封走心的信','B.TA亲手做的一顿生日餐','C.一个大牌的包包','D.偶像的见面会门票']
    },
    {
        'question':'3/5:放学，下暴雨，没带伞，我会怎么做？',
        'answer': ['A.向男神求救，让他送我回家','B.打电话给爸妈','C.一直发呆到雨停','D.回教室再撸三百道题']
    },
    {
        'question':'4/5:我和我暗恋的人现在是什么关系？',
        'answer': ['A.放下了，TA已经有了恋人','B.成功俘获，已经在一起啦','C.放不下，还喜欢着TA','D.追求ing']
    },
    {
        'question':'5/5:被恋人背叛了我会怎么做？',
        'answer': ['A.拉上死党去找小三','B.果断分手和绝交，潇洒离开','C.嘴上祝幸福，背后扎小人','D.立马和男朋友的好兄弟在一起']
    }
]

female_data4 = [
    {
        'question': '1/5:下面四份生日礼物，我会最喜欢哪个？',
        'answer': ['A.一套全色号口红','B.TA亲手做的一顿生日餐','C.偶像祝我生日快乐的签名照','D.一个厚实的大红包']
    },
    {
        'question':'2/5:下面四种男朋友类型，我会最喜欢哪个？',
        'answer': ['A.闷骚内敛的眼镜男','B.幽默开朗的运动男','C.成熟稳重的大叔','D.体贴可爱的忠犬弟弟']
    },
    {
        'question':'3/5:表白被男神拒绝，我会怎么做？',
        'answer': ['A.不放弃，穷追不舍','B.做回普通朋友，争取用陪伴打动他','C.果断放下，寻觅下一个','D.变得更优秀让他主动追我']
    },
    {
        'question':'4/5:发现和闺蜜喜欢上了同一个男生，我会怎么做？',
        'answer': ['A.不想太多，公平竞争','B.闺蜜情更重要，选择默默退出','C.主动找闺蜜坦白，好好谈一谈','D.先向男神表明心意，再选择放下']
    },
    {
        'question':'5/5:男朋友打游戏时不接我电话，我会是什么态度？',
        'answer': ['A.包容，人总有点自己的爱好','B.大发脾气，下一次这样就分手','C.失望伤心，我在你心中还比不上游戏','D.决心苦练游戏打败他']
    }
]

female_data5 = [
    {
        'question':'1/5:下面四种恋人类型，我会最喜欢哪个？',
        'answer': ['A.能让我天天都大笑的','B.能无微不至照顾我的','C.能带领我一起进步的','D.长得好看的']
    },
    {
        'question':'2/5:觉得别人和我做朋友的原因是？',
        'answer': ['A.可爱幽默的性格','B.体贴、会照顾人','C.有内涵，三观正','D.当然是颜值啦']
    },
    {
        'question':'3/5:表白被男神拒绝，我会怎么做？',
        'answer': ['A.不放弃，穷追不舍','B.做回普通朋友，争取用陪伴打动他','C.果断放下，寻觅下一个','D.变得更优秀让他主动追我']
    },
    {
        'question':'4/5:发现和闺蜜喜欢上了同一个男生，我会怎么做？',
        'answer': ['A.不想太多，公平竞争','B.闺蜜情更重要，选择默默退出','C.主动找闺蜜坦白，好好谈一谈','D.先向男神表明心意，再选择放下']
    },
    {
        'question':'5/5:男朋友打游戏不接我电话，我会是什么态度？',
        'answer': ['A.包容，人总有点自己的爱好','B.大发脾气，下一次这样就分手','C.失望伤心，我在你心中还比不上游戏','D.决心苦练游戏打败他']
    }
]

female_data=[female_data1,female_data2,female_data3,female_data4,female_data5]
# 对某个答题情况的评价
statement = ['让我们重新认识一次吧', '是时候吃个饭让你更了解我了', '你保住了我们革命情谊的火苗', '嘻嘻我们还有努力空间！','我是不是你的小可爱！','你太懂我了！灵魂伴侣！']
