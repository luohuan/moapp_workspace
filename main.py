from calc import *
import random
# 入口函数，在这里声明MoApp，定义页面
def main():
    with MoApp(appid='wxa9b01a93c80e98e9', name='姓名契合度', backgroundColor="#383838"):
        entrance()
        match()
        share()
        #share2()

def makeShareImage():
    ret = mo.acode.make('entrance', {})

    headimg = mo.token.get('host_headimg')
    canvas = mo.mopic.createCanvas(500, 500)
    canvas.addImage('http://img.mogodeer.cn/images/diudiu/name/erweima.jpg', pos=[0, 0, 500, 500])
    canvas.addImage(ret['url'], pos=[150, 250, 200, 200])
    canvas.addImage(headimg, pos=[204, 305, 94, 94], mask='circle')
    mo.console( headimg)


    res = canvas.makeImage()
    if res['ret'] == 0:
        mo.token.set('share_image', res['url'])

# 创建结果相关的ui
def makeResultUI(name_header, x, y):
        with Box(pos=[0, 60]):
            Box(pos=[128, 74], size=[90, 90],border='0px solid #F56E6E',borderRadius='50%',background='#D03F3F')
            Image(name='%shost_avatar' %name_header,src='http://material.motimaster.com/appmaker/lijiong/2315.png', pos=[133, 79], size=[80, 80], borderRadius='50%',)
            Box(pos=[460, 74], size=[90, 90],border='0px solid #3E4DD2',borderRadius='50%',background='#3E4DD2')
            Image(name='%sguest_avatar' %name_header,src='img/head2.jpg', pos=[464, 79], size=[80, 80], borderRadius='50%')
            Box(pos=[269, 142], size=[140, 2],border='2px solid #F56E6E',borderRadius='0%',background='#F17093')
            Text(name='%sscore' %name_header, text='87分', pos=[300, 58],color='#F56E6E', fontSize=42)
            Text(name='%shost_name' %name_header, pos=[70, 170],size=[200,90],textAlign='center',color='#F56E6E', fontSize=24)
            Text(name='%sguest_name' %name_header, pos=[400, 170],size=[200,90],textAlign='center',color='#3E4DD2', fontSize=24)
            Image(src='img/jisuan1.jpg', pos=[25, 253], size=[630, 96],effect=fadein(size=(0,1),d=1,t=1,c=1,p=1,s=0))
            
            Text(name='%sw0' %name_header, pos=[43, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw1' %name_header, pos=[152, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw2' %name_header, pos=[259, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw3' %name_header, pos=[364, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw4' %name_header, pos=[472, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text(name='%sw5' %name_header, pos=[579, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            
            Text(name='%snum00' %name_header, text='2', pos=[43, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum01' %name_header, text='8', pos=[152, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum02' %name_header, text='4', pos=[259, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum03' %name_header, text='6', pos=[364, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum04' %name_header, text='7', pos=[472, 334],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum05' %name_header, text='0',pos=[579, 334],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=30,effect=bounceindown(size=(0,1),d=1.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan2.jpg', pos=[72, 382], size=[544, 54],effect=fadein(size=(0,1),d=2,t=0.5,c=1,p=1,s=0))

            Text(name='%snum10' %name_header, text='4', pos=[101, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum11' %name_header, text='7', pos=[208, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum12' %name_header, text='8', pos=[313, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum13' %name_header, text='6', pos=[418, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Text(name='%snum14' %name_header, text='0',pos=[518, 419],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan3.jpg', pos=[128, 467], size=[422, 57],effect=fadein(size=(0,1),d=2.5,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum20' %name_header, text='4', pos=[152, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum21' %name_header, text='7', pos=[261, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum22' %name_header, text='8', pos=[366, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum23' %name_header, text='6', pos=[472, 505],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=2.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan4.jpg', pos=[182, 554], size=[324, 56],effect=fadein(size=(0,1),d=3,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum30' %name_header, text='7', pos=[206, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Text(name='%snum31' %name_header, text='8', pos=[313, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Text(name='%snum32' %name_header, text='6', pos=[421, 593],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan5.jpg', pos=[237, 643], size=[215, 54],effect=fadein(size=(0,1),d=3.5,t=0.5,c=1,p=1,s=0))
            
            Text(name='%snum40' %name_header, text='8', pos=[262, 679],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3.5,t=0.6,c=1,p=1,s=0))
            Text(name='%snum41' %name_header, text='7', pos=[368, 679],size=[63,63],textAlign='center',lineHeight=63,color='#333333', fontSize=30,effect=bounceindown(size=(0,1),d=3.5,t=0.6,c=1,p=1,s=0))
            Image(src='img/jisuan6.jpg', pos=[292, 724], size=[108, 61],effect=fadein(size=(0,1),d=4,t=0.5,c=1,p=1,s=0))
            Text(name='%stotal_num' %name_header, text='87', pos=[318, 785],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=45,effect=flipinx(size=(0,1),d=4,t=0.6,c=1,p=1,s=0))

# 名字叫home的页面
AUDITING = False
class entrance(Page):
    backgroundColor="#383838"
    background="#383838"
    barColor='#383838'
    barStyle='#383838'

    def UI():
        with Box(name='input_name_box', pos=[0,0], hidden=True, width=750):
            Image(name='image1',pos=[0,-40],size=[750,1325],src="img/bg2.jpg")
            ImageAvatar(pos=['center', 30], size=[160,160], borderRadius='50%')
            Text(name='text1',text='你们的名字配不配？', color='#FFFFFF', fontSize=24, pos=['center', 400])
            Text(name='text2',text='汉字码加和取个位', color='#FFFFFF', fontSize=24, pos=['center', 450])
            Text(name='text3',text='算出你们的缘分', color='#FFFFFF', fontSize=24, pos=['center', 500])

            
            Input(name='input_host_name', pos= ['center',600], size=[480,80],
                  placeholder = '请输入你的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Button(name='button1', text = '提交', pos=['center',938],size=[360,78],background = 'rgba(242,64,64,0.82)',
                                   lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', 
                                   color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo',
                                   onTap = [moui.showLoading('加载中...'), commitName, moui.hideLoading()])
        with Box(name='auditing_box', pos=[0,0], hidden=True, width=750):
            Image(name='image1',pos=[0,-40],size=[750,1325],src="img/bg2.jpg")
            ImageAvatar(pos=['center', 30], size=[160,160], borderRadius='50%')
            Text(name='text1',text='算算好友跟你的名字能得多少分', color='#FFFFFF', fontSize=24, pos=['center', 400])
            Input(pos= ['center',500], size=[480,80],
                  placeholder = '请输入你的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Input(pos= ['center',650], size=[480,80],
                  placeholder = '请输入对方的名字', border='2px solid #F24040',background='255 255 255 0.3',color='#F46060',textAlign='center')
            Button(name='button1', text = '提交', pos=['center',938],size=[360,78],background = 'rgba(242,64,64,0.82)',
                                   lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', 
                                   color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo',
                                   onTap = [moui.showLoading('加载中...'), computeNameScore, moui.hideLoading()])

        with Box(name='loading_box', pos=[0,0], size=[750,1333]):
           
           Image(src='img/loading.png', size=[200, 200], pos=[275, 200],effect=rotate(deg=(0,360),d=0,t=2,c=0,p=0,s=0,o=(50,50)))
           Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])

    def computeNameScore():
        mo.showAlert('好友名字契合度','你们名字契合度分数为%s分'% str(int(random.random()*100)))
    
    def onInit():
        mo.console('main page init')
        page.loading_box.show()
        #inputNameBoxInit()
        if AUDITING == True:
            
            page.auditing_box.hidden = False
            page.loading_box.hidden = True
        else:
            inputNameBoxInit()
        

    def onPullDownRefresh():
        onInit()

    def inputNameBoxInit():
        mo.console('on inputNameBox init')
        page.input_host_name.value = user.nickName 
        mo.setNavibarTitle('好友姓名默契度')
        if mo.token.isHost(): #如果是主态
            tokenid = user.get('tokenid') #判断是否创建过令牌token
            if tokenid != None: # 已经发起过匹配
                token = mo.getToken(tokenid)
                token.redirectTo('match') #带着令牌token跳转
            else:
                page.input_name_box.show() #没有匹配过 显示输入框
                page.loading_box.hide()
            
        else: #如果是客态
            if mo.token.getGuestInfo(user.openid) != None: #如果该用户已经匹配过用token redirectTo到match页面
                mo.token.redirectTo('match') 
            else:
                if user.get('name') != None:    # 已经全局输入过名字，直接使用自当匹配完
                    page.input_host_name.value = user.get('name')
                    #go_share2()
                    host_name = mo.token.get('host_name')
                    host = mo.token.getHostInfo()
                    mo.console('主人的信息 %s'% json.dumps(host))
                    mo.console('主人的名字%s' % host_name)
                    mo.console('客人的名字%s' % user.name )
                    #mo.console()
                    ret = calcName(host_name, host['gender'], user.get('name'), user.gender)
                    mo.console(ret)
                    mo.token.markAsGuest({
                        'result': ret,
                        'name': user.get('name')
                    })
                    mo.token.redirectTo('match')
                    
                else:   # 没有输入过名字，显示输入框
                    page.loading_box.hide() 
                    page.input_name_box.show()
                    name = mo.token.get('host_name')
                    page.text2.text = '算一算 %s 跟你' %name
                    mo.setNavibarTitle('好友姓名默契度')
    #提交输入得姓名
    def commitName():
        name = page.input_host_name.value

        if not (2<= len(name) <=3):
            mo.showAlert('提示', '请输入2~3个汉字')
            return

        if not isAllChineseText(name):
            mo.showAlert('提示', '请输入2~3个汉字')
            return

        
        if mo.token.isHost():  #如果是主态
            mo.token.set('host_name', name)
            mo.token.set('host_headimg', user.avatarUrl)
            page.input_name_box.hide()
           
            user.set('tokenid', mo.token.id) #保存令牌tokem信息
            user.set('name', name)

            #page.sample_box.show()
            #显示示例box 初始化示例Box
            mo.token.redirectTo('match',mode='sample_mode')
        else: # 如果是客人态
            host_name = mo.token.get('host_name')
            host = mo.token.getHostInfo()
            ret = calcName(host_name, host['gender'], user.name, user.gender)
            mo.console(ret)
            mo.token.markAsGuest({
                'result': ret,
                'name': user.name
                })
            mo.token.redirectTo('match')
            #显示结果页
    
    
#匹配页面 一个例子Box 一个是匹配的box
class match(Page):
    backgroundColor="#383838"
    background="#383838"
    barColor='#383838'
    barStyle='#383838'  

    def UI():
        with Box(name='sample_box', pos=[0,0], hidden=True, width=750,background='#383838'):
            Image(name='page2image1',pos=[0,0],size=[750,339],src="img/bg3.jpg")
             #默契度计算list
            with Box(name='guest_list', pos=[33, 340], size=[686, 3050],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)'):
                Text(text='示例', pos=['center', 10],color='#F14141', fontSize=40)        
                Text(text='汉字码加和取个位，算出我们的缘分', pos=['center', 65],color='#333333', fontSize=22)
                makeResultUI('', 0, -40)                
                Box(pos=[0,940],background='rgba(0,0,0,0)',size=[200,200])

            Button(name='sharebutton1', text = '跟朋友圈好友算', position='fixed', left=380,bottom=30,size=[330,78],background = 'rgba(242,64,64,0.82)',border='1px solid #F24040',
                lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '5px', color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',
                onTap=[moui.showLoading('请稍微等一下下...'), gotoSharePage, moui.hideLoading()])
            ShareButton(text='跟群好友算',position='fixed', left=50,bottom=30,size=[300,78], borderRadius = '5px',color='#FFFFFF',border='1px solid #F24040',
                fontSize=36,fontWeight = 'bolder',lineHeight=78,boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',background = 'rgba(242,64,64,0.82)',
                type='primary')
        
            
        with Box(name='match_box', pos=[0, 0], width=750, hidden=True, background='#383838'):
            Image(name='page2image1',pos=[0,0],size=[750,339],src="img/bg3.jpg")
            Text(name='tip1',text='暂时还没有好友来跟你匹配哦~',color='white',fontSize=40,pos=['center',420])
            Text(name='tip2',text='点击底部按钮邀请给好友开始计算',color='white',fontSize=40,pos=['center',520])
            with Box(name='guest_list', hidden=True, pos=[33, 335], size=[686, 940],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)',marginBottom=50):
                makeResultUI('', 0, -40)                
            with Box(pos=[0, 1330]):
                with List(name='rest_guests', position='relative', border='0px solid #FFFFFF',borderRadius='0%'):        
                    with Box(pos=[33, 0], size=[686, 150],border='0px solid #FFFFFF',borderRadius='0%',background='#D96363',boxShadow ='2px 2px 1px 2px rgba(255,255,255,1)',marginBottom=50):                        
                        Image(src='{item.host_avatar}', pos=[41, 15], size=[80, 80], border='4px solid #FFFFFF',borderRadius='50%')                
                        Image(src='{item.guest_avatar}', pos=[205, 15], size=[80, 80], border='4px solid #FFFFFF',borderRadius='50%')
                        Box(pos=[138, 58], size=[49, 2],border='2px solid #FFFFFF',borderRadius='0%',background='#FFFFFF')
                        Text(text='{item.score}分', pos=[373, 35],color='#FFFFFF', fontSize=42)
                        Text(text='{item.host_name}', pos=[36, 110],size=[90,24],textAlign='center',color='#FFFFFF', fontSize=20)
                        Text(text='{item.guest_name}', pos=[198, 110],size=[90,24],textAlign='center',color='#FFFFFF', fontSize=20)
                        Button(name='xiangqing', text = '查看详情', pos=[558, 50],size=[102,45],background = '#FFFFFF',
                               lineHeight = 45,fontSize=22,fontWeight = 'bolder',borderRadius = '500px', color = '#D96363',
                               onTap=moui.request(showDetail, guest_openid='{item.guest_openid}'))
                Box(position='relative',size=[100,200],background='rgba(0,0,0,0)')

            
            Button(name='createbutton', text = '创建我的', position='fixed', left=195,bottom=30,size=[360,78],background = 'rgba(242,64,64,0.82)',
                lineHeight = 78,fontSize=36,fontWeight = 'bolder',borderRadius = '500px', color = '#FFFFFF',boxShadow ='4px 8px 1px 3px rgba(0,0,0,0.2)',openType='getUserInfo', 
                onTap=[moui.showLoading('请耐心等待一下...'),onCreateTap, moui.hideLoading()])

            with Mask(name='match_detail_mask', hidden=True):
                with Box(pos=[33, 100], size=[686, 940],border='1px solid #FFFFFF',borderRadius='0%',background='http://img.mogodeer.cn/images/diudiu/ceshi1/wnagge.jpg',boxShadow ='3px 3px 1px 3px rgba(208,63,63,0.9)',marginBottom=50):
                    makeResultUI('detail_', 0, 60)


        with Box(name='loading_box', pos=[0,0], size=[750,1333]):           
           Image(src='img/loading.png', size=[200, 200], pos=[275, 200],effect=rotate(deg=(0,360),d=0,t=2,c=0,p=0,s=0,o=(50,50)))
           Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])

    #页面初始化
    def onInit():
        mode = page.options.mode

        if mode != None and mode =='sample_mode':  #如果是主人刚进来 会是例子展示的box显示
            page.loading_box.hidden = True
            page.sample_box.hidden = False
            sampleBoxInit()

        else: # 如果没有指定mode那就是显示匹配详情页面
             page.loading_box.hidden = True
             page.match_box.hidden = False
             matchBoxInit()

    def onPullDownRefresh():
        onInit()

    def matchBoxInit():
        if mo.token.isHost(): #主人态
            page.createbutton.text = '发送给好友开始计算'
            mo.setNavibarTitle('好友姓名默契度')
        else: #客人态
            page.createbutton.text = '创建我的'
            mo.setNavibarTitle('好友姓名默契度')

        guests = mo.token.getGuestList()
        mo.console(guests)
        host = mo.token.getHostInfo()
        mo.console(host)

        if len(guests)>0:
            page.tip1.hidden = True
            page.tip2.hidden = True
            last_guest_openid = None    # "最近的"访客openid
            if mo.token.isHost():       # 主人态，"最近的"就是最后一个
                last_guest_openid = guests[len(guests)-1]['openid']
            else:   # 客人态， "最近的"是"当前用户"
                last_guest_openid = user.openid

            host_name = mo.token.get('host_name')
            last_guest = mo.token.getGuestInfo(last_guest_openid)
            # last_guest['result'] = calcName(host_name, host['gender'], last_guest['name'], last_guest['gender'])
            page.host_avatar.src = host['avatarUrl']
            page.host_name.text = mo.token.get('host_name')            

            page.guest_avatar.src = last_guest['avatarUrl']
            page.guest_name.text = last_guest['name']

            page.score.text = '%d分' %last_guest['result']['score']

            page.w0.text = last_guest['result']['words'][0]
            page.w1.text = last_guest['result']['words'][1]
            page.w2.text = last_guest['result']['words'][2]
            page.w3.text = last_guest['result']['words'][3]            
            page.w4.text = last_guest['result']['words'][4]
            page.w5.text = last_guest['result']['words'][5]

            process = last_guest['result']['process']
            page.num00.text = process[0][0]
            page.num01.text = process[0][1]
            page.num02.text = process[0][2]
            page.num03.text = process[0][3]
            page.num04.text = process[0][4]
            page.num05.text = process[0][5]

            page.num10.text = process[1][0]
            page.num11.text = process[1][1]
            page.num12.text = process[1][2]
            page.num13.text = process[1][3]
            page.num14.text = process[1][4]

            page.num20.text = process[2][0]
            page.num21.text = process[2][1]
            page.num22.text = process[2][2]
            page.num23.text = process[2][3]

            page.num30.text = process[3][0]
            page.num31.text = process[3][1]
            page.num32.text = process[3][2]

            page.num40.text = process[4][0]
            page.num41.text = process[4][1]

            page.total_num.text = last_guest['result']['score']

            # 剩下的人
            page.rest_guests.data = []
            for i in range(len(guests)):
                guest = guests[len(guests)-1-i]
                #if guest['openid'] != last_guest_openid: #user.openid:
                page.rest_guests.data.append({
                        'host_name': host_name,
                        'host_avatar': host['avatarUrl'],
                        'guest_name': guest['name'],
                        'guest_openid': guest['openid'],
                        'guest_avatar': guest['avatarUrl'],
                        'score': guest['result']['score']
                    })

            page.guest_list.show()
        else:
            page.tip1.hidden = False
            page.tip2.hidden = False
    def sampleBoxInit():
        mo.console('on sampleBoxInit')
        mo.setNavibarTitle('好友姓名默契度')
        mo.console(mo.token.get('host_name'))

        host = mo.token.getHostInfo()
        mo.console(host)

        host_name = mo.token.get('host_name')       
        last_guest = {
            'name': '特朗普',
            'avatarUrl': 'http://img.mogodeer.cn/images/diudiu/name/telangpu.jpg',
            'gender': 1
        }

        last_guest['result'] = calcName(host_name, host['gender'], last_guest['name'], last_guest['gender'])
        page.host_avatar.src = host['avatarUrl']
        page.host_name.text = mo.token.get('host_name')            

        page.guest_avatar.src = last_guest['avatarUrl']
        page.guest_name.text = last_guest['name']

        page.score.text = '%d分' %last_guest['result']['score']

        page.w0.text = last_guest['result']['words'][0]
        page.w1.text = last_guest['result']['words'][1]
        page.w2.text = last_guest['result']['words'][2]
        page.w3.text = last_guest['result']['words'][3]
        page.w4.text = last_guest['result']['words'][4]
        page.w5.text = last_guest['result']['words'][5]

        process = last_guest['result']['process']
        page.num00.text = process[0][0]
        page.num01.text = process[0][1]
        page.num02.text = process[0][2]
        page.num03.text = process[0][3]
        page.num04.text = process[0][4]
        page.num05.text = process[0][5]

        page.num10.text = process[1][0]
        page.num11.text = process[1][1]
        page.num12.text = process[1][2]
        page.num13.text = process[1][3]
        page.num14.text = process[1][4]

        page.num20.text = process[2][0]
        page.num21.text = process[2][1]
        page.num22.text = process[2][2]
        page.num23.text = process[2][3]

        page.num30.text = process[3][0]
        page.num31.text = process[3][1]
        page.num32.text = process[3][2]

        page.num40.text = process[4][0]
        page.num41.text = process[4][1]

        page.total_num.text = last_guest['result']['score']
        page.guest_list.show()
        page.loading_box.hide()

    def onCreateTap(): 
        if mo.token.isHost(): #主人态去分享
            makeShareImage()
            mo.console('主人态，跳转到share Page')
            mo.token.goto('share')
        else: #客人态重定向为主人
            mo.console('客人态，重定向变为主态')
            #mo.redirectTo('create2'
            mo.redirectTo('entrance')

    def showDetail(): #显示匹配细节
        guest_openid = params.guest_openid
        host_name = mo.token.get('host_name')
        host = mo.token.getHostInfo()
        
        guest = mo.token.getGuestInfo(guest_openid)
        
        page.detail_host_avatar.src = host['avatarUrl']
        page.detail_host_name.text = mo.token.get('host_name')            

        page.detail_guest_avatar.src = guest['avatarUrl']
        page.detail_guest_name.text = guest['name']

        page.detail_score.text = '%d分' %guest['result']['score']

        page.detail_w0.text = guest['result']['words'][0]
        page.detail_w1.text = guest['result']['words'][1]
        page.detail_w2.text = guest['result']['words'][2]
        page.detail_w3.text = guest['result']['words'][3]                
        page.detail_w4.text = guest['result']['words'][4]
        page.detail_w5.text = guest['result']['words'][5]

        process = guest['result']['process']
        page.detail_num00.text = process[0][0]
        page.detail_num01.text = process[0][1]
        page.detail_num02.text = process[0][2]
        page.detail_num03.text = process[0][3]
        page.detail_num04.text = process[0][4]
        page.detail_num05.text = process[0][5]

        page.detail_num10.text = process[1][0]
        page.detail_num11.text = process[1][1]
        page.detail_num12.text = process[1][2]
        page.detail_num13.text = process[1][3]
        page.detail_num14.text = process[1][4]

        page.detail_num20.text = process[2][0]
        page.detail_num21.text = process[2][1]
        page.detail_num22.text = process[2][2]
        page.detail_num23.text = process[2][3]

        page.detail_num30.text = process[3][0]
        page.detail_num31.text = process[3][1]
        page.detail_num32.text = process[3][2]

        page.detail_num40.text = process[4][0]
        page.detail_num41.text = process[4][1]

        page.detail_total_num.text = guest['result']['score']

        page.match_detail_mask.show()

    def onShare():
        page.share.page = 'entrance'

    def gotoSharePage():
        makeShareImage()
        #mo.token.goto('share')
        tokenid = user.get('tokenid')
        token = mo.getToken(tokenid)
        token.goto('share')

class share(Page):
    disableScroll = True
    title='姓名默契度'

    def UI():
       #Image(name='shareImage',src='http://material.motimaster.com/yuyuan/Duudle/create/ec26c4802daf55428cbe6a79ec72f176.png',pos=[15,10,720,722])
       Image(name='shareImage',src='http://img.mogodeer.cn/images/diudiu/xingzuozhun/erweima5.jpg', pos=['center',23], size=[700,700])
       #ImageAvatar(name='avatar',pos=[297,393,149,149],borderRadius='50%')
       Button(name='saveShareImage',onTap=[moui.showLoading(),saveShareImage,moui.hideLoading()],text='保存朋友圈海报',fontWeight=900,lineHeight=80,pos=[175,780,400,80], boxShadow='-1px 10px 5px -5px #BBBBBB',fontSize='16px', color='#ffffff',border='1px solid #ffffff',backgroundColor="rgba(242,64,64,0.82)")
       ShareButton(text='分享到好友群',pos=[175,923,400,80], color='#F24040',border='1px solid #F24040',fontSize='16px',lineHeight=80,boxShadow='-1px 3px 5px -5px #BBBBBB',backgroundColor="#ffffff",type='primary')

    def onInit():
        page.shareImage.src = mo.token.get('share_image')

    def saveShareImage():
        mo.saveImage(mo.token.get('share_image'))

    def onShare():
        page.share.page = 'entrance'


