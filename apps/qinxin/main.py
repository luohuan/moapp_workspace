import random
pr=['蛇皮怪','小黄人','老巫婆','精致肥宅','伏地魔','皮皮虾']
nan00 = [{'text':'高冷',},
    {'text':'成熟',},
    {'text':'喜感',},
    {'text':'可爱',},
    {'text':'土豪',},
    {'text':'高富帅',},
    {'text':'暖男',},
    {'text':'情商高',},
    {'text':'男神'}
]
nan01 = [{'text':'逗b',},
    {'text':'绅士',},
    {'text':'孩子气',},
    {'text':'大叔',},
    {'text':'气质好',},
    {'text':'学霸',},
    {'text':'衣品好',},
    {'text':'温柔',},
    {'text':'不爱说话'}
]
nan02 = [{'text':'智商高',},
    {'text':'吃货',},
    {'text':'很高',},
    {'text':'很凶',},
    {'text':'热情',},
    {'text':'乐观',},
    {'text':'帅',},
    {'text':'气场强',},
    {'text':'机智'}
]
nv00 = [{'text':'高冷',},
    {'text':'可爱',},
    {'text':'女神',},
    {'text':'御姐',},
    {'text':'大长腿',},
    {'text':'贵妇',},
    {'text':'漂亮',},
    {'text':'温柔',},
    {'text':'吃货'}
]
nv01 = [{'text':'气质好',},
    {'text':'害羞',},
    {'text':'小仙女',},
    {'text':'小公举',},
    {'text':'土豪',},
    {'text':'逗b',},
    {'text':'孩子气',},
    {'text':'情商高',},
    {'text':'小清新'}
]
nv02 = [{'text':'学霸',},
    {'text':'文静',},
    {'text':'很高',},
    {'text':'成熟',},
    {'text':'萝莉',},
    {'text':'智商高',},
    {'text':'气场强',},
    {'text':'女汉子',},
    {'text':'喜感'}
]
nan10 = [{'text':'逗b',},
    {'text':'二狗子',},
    {'text':'老司机',},
    {'text':'装b侠',},
    {'text':'蛇皮怪',},
    {'text':'作死',},
    {'text':'肥宅',},
    {'text':'伏地魔',},
    {'text':'智障'}
]
nan11 = [{'text':'浪',},
    {'text':'脾气大',},
    {'text':'小黄人',},
    {'text':'颜值担当',},
    {'text':'老骚包',},
    {'text':'大痞子',},
    {'text':'老哥',},
    {'text':'有毒',},
    {'text':'二次元'}
]
nan12 = [{'text':'傲娇',},
    {'text':'闷骚',},
    {'text':'智商高',},
    {'text':'吃货',},
    {'text':'话多',},
    {'text':'神经病',},
    {'text':'中央空调',},
    {'text':'自恋',},
    {'text':'皮皮虾'}
]
nv10 = [{'text':'吃货',},
    {'text':'强迫症',},
    {'text':'猪猪女孩',},
    {'text':'老巫婆',},
    {'text':'自拍狂魔',},
    {'text':'傲娇',},
    {'text':'老司机',},
    {'text':'伏地魔',},
    {'text':'二狗子'}
]
nv11 = [{'text':'现充',},
    {'text':'装b侠',},
    {'text':'心机',},
    {'text':'肥宅',},
    {'text':'事儿多',},
    {'text':'小黄人',},
    {'text':'蛇皮怪',},
    {'text':'神婆子',},
    {'text':'老骚包'}
]
nv12 = [{'text':'自恋',},
    {'text':'闷骚',},
    {'text':'皮皮虾',},
    {'text':'贵妇',},
    {'text':'神经病',},
    {'text':'智障',},
    {'text':'话多',},
    {'text':'颜值担当',},
    {'text':'脾气大'}
]

# a=['啦啦啦啦','bbb','cccc','dd','e','ffff','g','h','i']
AUDITING = False 
def main():
    with MoApp(appid='wx777413533a93b0cf',name='印象'):
        page1()
        page2()
class page1(Page):
    background='#140620'
    naviBarColor='#191b44'
    def UI():
        Image(src='http://material.motimaster.com/aelegy1531980817000/WechatIMG307.jpeg',     
         size=[750,1334],pos=[0,-100],position = 'fixed')
        
        # Image(src='http://material.motimaster.com/aelegy1531980817000/WechatIMG307.jpeg',     
        #  size=[750,1334],pos=[0,-100],position = 'fixed',effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
        with Box(name='box',size=[750, 1200],hidden=True):
            Image(src='http://material.motimaster.com/aelegy1532010630000/初次.png',
                size=[160,40],pos=[100,100],effect=bounceinleft(t=2,c=1))
            Image(src='http://material.motimaster.com/aelegy1532010646000/第一.png',
                size=[510,85],pos=[150,170],effect=bounceinright(t=2,c=1))
            # Text(name='xh',hidden=True,text='下面还有哦',size=[25,150],effect=fadeout(c=1,t=2.5,d=20),pos=[15,1000],fontSize = 25,textAlign='center',lineHeight='30rpx',color='white')
            # Image(name='xht',hidden=True,src='http://material.motimaster.com/aelegy1532484054000/b9da3ff14071928c16804ccdf74a546d副本.png',
                # pos=[5,1150],size=[60,40],effect=flash(c=0,t=6))

            with Box(id='sbya',size=[650,410],pos=['center',450],effect=fadein(c=1,t=2.5,d=1)):
                Image(src='http://material.motimaster.com/aelegy1531999676000/aa1.png',
                    size=[650,410])
                with Box(name='dy0box',size=[540, 300],pos=['center',30], ):
                    with Grid(name='dy0',size=[540, 300], column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(dy, yx='{item.text}'))
                with Box(name='dy1box',size=[540, 300],hidden=True,pos=['center',30], ):
                    with Grid(name='dy1',size=[540, 300], column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(dy, yx='{item.text}'))
                with Box(name='dy2box',size=[540, 300],hidden=True,pos=['center',30], ):
                    with Grid(name='dy2',size=[540, 300], column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(dy, yx='{item.text}'))
                with Box(size=[93,43],pos = [500,340],):
                    Image(src='http://material.motimaster.com/aelegy1532001050000/未标题-10.png',size=[93,43])
                    Text(
                        text = '换一批',
                        size = [90,40],
                        pos = [1,0],
                        fontSize = 25,
                        textAlign='center',
                        color = 'white',
                        onTap=hyp0
                    )
            # with Box(size=[550,107],pos=['center',550]):
            #     Text(size=[550,100],background='rgba(25,25,25,0.4)',borderRadius = '5px 5px 0px 0px')

            #     with Input(name='first',pos=[15,10],size=[520,80],placeholder = '第一印象',textAlign='center',borderRadius = '5px',background='rgba(238,238,238,0.05)',color='white'):
            #         this.placeholderStyle.color='white'
            with Box(size=[563,110],pos=['center',300],effect=fadein(c=1,t=2.5,d=1)):
                Image(src='http://material.motimaster.com/aelegy1532000061000/未标题-1.png',size=[563,110])
                with Input(name='first',maxlength='9',pos=[20,10],size=[520,80],placeholder = '✎第一印象',textAlign='center',borderRadius = '5px',background='rgba(238,238,238,0.05)',color='white'):
                    this.placeholderStyle.color='#8b8989'
                Text(text='可以输入不超过九个字哦~',color='white',fontsize=25,pos=[300,110],size=[300,20],effect=flash(c=0,t=6))
            Button(
                text = '﹀',
                size = [110,110],
                pos = ['center',1000],
                background = 'linear-gradient(150deg, #ffffff , #b3b3b3)',
                lineHeight = 110,
                fontSize=30,
                fontWeight = 'bolder',
                borderRadius = '50%',
                color = '#404040',
                boxShadow ='0px 0px 3px 4px rgba(255,255,255,0.3)',
                onTap =xyt,
                effect =pulse(t=1,c=0)
                )
        with Box(name='box1',size=[750, 1200],hidden=True):
            Image(src='http://material.motimaster.com/aelegy1532052924000/认识.png',
                size=[220,55],pos=[150,100],effect=fadein(c=1,t=2.5,d=1))
            Image(src='http://material.motimaster.com/aelegy1532052945000/现在.png',
                size=[390,65],pos=[160,170],effect=fadein(c=1,t=2.5,d=1))

            with Box(size=[650,410],pos=['center',450],effect=fadein(c=1,t=2.5,d=1)):
                Image(src='http://material.motimaster.com/aelegy1531999676000/aa1.png',
                    size=[650,410])
                with Box(name='xz0box',size=[540, 300],pos=['center',30], ):
                    with Grid(name='xz0',size=[540, 300], column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(xz, yx1='{item.text}'))
                with Box(name='xz1box',size=[540, 300],pos=['center',30], hidden=True):
                    with Grid(name='xz1',size=[540, 300],column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(xz, yx1='{item.text}'))
                with Box(name='xz2box',size=[540, 300],pos=['center',30], hidden=True ):
                    with Grid(name='xz2',size=[540, 300],column=3):
                        with Box(size=[180,100]):
                            Text(text='{item.text}',lineHeight='70rpx',pos=[15,15],borderRadius = '5px',textAlign='center',size=[145, 70],color='#ffffff',border='1px dotted white',onTap=moui.request(xz, yx1='{item.text}'))
                with Box(size=[93,43],pos = [500,340],):
                    Image(src='http://material.motimaster.com/aelegy1532001050000/未标题-10.png',size=[93,43])
                    Text(
                        text = '换一批',
                        size = [90,40],
                        pos = [1,0],
                        fontSize = 25,
                        textAlign='center',
                        color = 'white',
                        onTap=hyp1
                    )
            with Box(size=[563,110],pos=['center',300],effect=fadein(c=1,t=2.5,d=1)):
                Image(src='http://material.motimaster.com/aelegy1532000061000/未标题-1.png',size=[563,110])
                with Input(name='now',pos=[20,10],maxlength='9',size=[520,80],placeholder = '✎现在的印象',textAlign='center',borderRadius = '5px',background='rgba(238,238,238,0.05)',color='white'):
                    this.placeholderStyle.color='#8b8989'
                Text(text='可以输入不超过九个字哦~',color='white',fontsize=25,pos=[300,110],size=[300,20],effect=flash(c=0,t=6))
            Button(
                text = '提交',
                size = [110,110],
                pos = ['center',1000],
                background = 'linear-gradient(150deg, #ffffff , #b3b3b3)',
                lineHeight = 110,
                fontSize=30,
                fontWeight = 'bolder',
                borderRadius = '50%',
                color = '#404040',
                boxShadow ='0px 0px 3px 4px rgba(255,255,255,0.3)',
                openType='getUserInfo',
                onTap =commit,
                effect =pulse(t=1,c=0)
                )
            # Text(text='  ',size=[100,50],pos=['center',2100])
            # Button(
            #     text = '提交',
            #     size = [220,70],
            #     pos = ['center',2100],
            #     background = '#0060ca',
            #     fontSize = 28,
            #     borderRadius = '8px',
            #     color = '#090089',
            #     border = '1px solid #91ceff',
            #     openType='getUserInfo',
            #     onTap =commit
            #     )
        with Box(name='create',size=[750, 1234],hidden=True,):
            Image(src='http://material.motimaster.com/aelegy1532330990000/不同.png',
                pos=['center',100],size=[500,500])
            Image(src='http://material.motimaster.com/aelegy1532317449000/答案.png',
                pos=['center',800],size=[660,110])
            Button(
                text = '创建',
                size = [110,110],
                pos = ['center',620],
                background = 'linear-gradient(150deg, #ffffff , #b3b3b3)',
                lineHeight = 110,
                fontSize=30,
                fontWeight = 'bolder',
                borderRadius = '50%',
                color = '#404040',
                boxShadow ='0px 0px 3px 4px rgba(255,255,255,0.3)',
                effect =pulse(t=1,c=0),
                openType='getUserInfo',
                onTap =create
                )
        with Box(name='loading_box', pos=[0,0], size=[750,1333]):
           
            #Image(src='img/loading.png', size=[200, 200], pos=[275, 200],effect=rotate(deg=(0,360),d=0,t=2,c=0,p=0,s=0,o=(50,50)))
            Text(text='加载中,请稍后...', width=750, textAlign='center', color='#ffffff', pos=['center', 700])
        with Box(name='auditing_box',hidden=True,pos=[0,0], size=[750,1333]):
            Text(text='我猜大家对你的印象是',pos=['center',200],fontsize=40,textAlign='center',size=[500,100],color='white')
            Text(name='yinxiang',pos=['center',300],fontsize=60,textAlign='center',size=[200,100],color='white')
            Image(src='http://material.motimaster.com/aelegy1532398329000/368680BF15785BF8B68A6BA735689C3B.gif',
                pos=['center',500],size=[300,300])
        Text(name='wgd',text='',size = [60,220],pos = [690,550],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '5px 0px 0px 5px',)
        Button(
            name='wg',
            hidden=True,
            text = '只想围观',
            plain=True,
            size = [50,160],
            pos = [697,580],
            # background=None,
            fontSize = 30,
            textAlign='center',
            lineHeight='40rpx',
            # borderRadius = '',
            border='none',
            color = 'white',
            onTap =wga,
            )


    def preOnInit():
        # page.loading_box.show()
        page.dy0.data = nv00
        page.dy1.data = nv01
        page.dy2.data = nv02
        page.xz0.data = nv10
        page.xz1.data = nv11
        page.xz2.data = nv12
        user.set('huan',0)
        user.set('huan1',0)
        if mo.token.isHost():
            mo.console('1') #如果是主态
            tokenid = user.get('tokenid4') #判断是否创建过令牌token
            if tokenid != None: # 已经发起过匹配
                mo.console('2')
                pd=user.get('pd')
                if pd!=None:
                    mo.console('2.1')
                    user.set('pd',None)
                    xb=user.gender
                    if xb!=2:
                        page.dy0.data = nan00
                        page.dy1.data = nan01
                        page.dy2.data = nan02
                        page.xz0.data = nan10
                        page.xz1.data = nan11
                        page.xz2.data = nan12
                    page.loading_box.hide() 
                    page.box.show()
                    # if user.openid not in mo.token.get('fklb',[]):
                    #     page.xh.show()
                    #     page.xht.show()
                else:
                    token = mo.getToken(tokenid)
                    token.redirectTo('page2') #带着令牌token跳转
            else:
                mo.console('3')
                page.loading_box.hide() 
                page.create.show()
        else: #如果是客态
            xb=mo.token.get('host_gender')
            if xb!=2:
                page.dy0.data = nan00
                page.dy1.data = nan01
                page.dy2.data = nan02
                page.xz0.data = nan10
                page.xz1.data = nan11
                page.xz2.data = nan12
            if user.openid in mo.token.get('fklb',[]): #如果该用户已经匹配过用token
                pd=user.get('pd1')
                if pd!=None:
                    user.set('pd1',None)
                    page.loading_box.hide() 
                    page.box.show()
                else:
                    mo.console('4')
                    mo.token.redirectTo('page2') 
            else:   # 没有输入过名字，显示输入框
                mo.console('5')
                page.loading_box.hide() 
                page.box.show()
                page.wgd.show()
                page.wg.show()
                # page.xh.show()
                # page.xht.show()
    def onInit():
        mo.setNavibarColor('#ffffff', '#191b44')
        page.loading_box.show()
        
        # page.loading_box.hidden = True
        # page.auditing_box.hidden = False
        
        #inputNameBoxInit()
        if AUDITING == True:
            page.loading_box.hidden = True
            page.auditing_box.hidden = False
            page.yinxiang.text = pr[random.randint(0,5)]
        else:
            preOnInit()

    def xyt():
        page.box.hide()
        page.box1.show()

    def hyp0():
        huan=user.get('huan',0)
        if huan==2:
            page.getElement('dy'+str(huan)+'box').hidden = True
            page.getElement('dy'+str(0)+'box').hidden = False
            user.set('huan',0)
        else:
            page.getElement('dy'+str(huan)+'box').hidden = True
            page.getElement('dy'+str(huan+1)+'box').hidden = False
            user.set('huan',huan+1)
    def hyp1():
        huan=user.get('huan1',0)
        if huan==2:
            page.getElement('xz'+str(huan)+'box').hide()
            page.getElement('xz'+str(0)+'box').show()
            user.set('huan1',0)
        else:
            page.getElement('xz'+str(huan)+'box').hide()
            page.getElement('xz'+str(huan+1)+'box').show()
            user.set('huan1',huan+1)
    def dy():
        page.first.value=params.yx
    def xz():
        page.now.value=params.yx1
    def create():
        user.set('tokenid4', mo.token.id)
        #token = mo.getToken(user.get('tokenid3'))
        mo.token.set('host_name', user.nickName) 
        mo.token.set('host_url', user.avatarUrl)
        mo.token.set('host_gender', user.gender)#设置令牌token信息
        mo.token.redirectTo('page2')
    def commit():
        f=page.first.value
        n=page.now.value

        mo.console(mo.token.get('host_name'))
        fklb=mo.token.get('fklb',[])
        fklb.append(user.openid)
        mo.console(fklb)
        mo.token.set('fklb',fklb)
        lb=mo.token.get('lb',[])
        lb.append({
            'name':user.nickName,
            'url': user.avatarUrl,
            'gender':user.gender,
            'f':f,
            'n':n
        })
        mo.token.set('lb',lb)
            
        mo.token.redirectTo('page2')
    def wga():
        mo.token.redirectTo('page2')

class page2(Page):
    enableShare=True
    background='#140620'
    naviBarColor='#191b44'
    def UI():
        
        Image(src='http://material.motimaster.com/aelegy1531980817000/WechatIMG307.jpeg',     
        size=[750,1334],pos=[0,-100],position = 'fixed')
        # Image(src='http://material.motimaster.com/aelegy1531894737000/QQ20180718-01.jpg',     
        #  size=[750,1334],pos=[0,0],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
        # Image(src='http://material.motimaster.com/aelegy1532071414000/上瘾.png',
        #     pos=[80,30],size=[100,100])
        with ScrollBox(name='box',hidden=True,size=[750, 1234], scrollY=True):
            Text(name='my',textAlign='center',color='white',hidden=True,fontsize=35,pos=['center',500],size=[500,20])

            Text(name='chats',text='点击红叉可以删除哦~',color='white',effect=fadeout(d=10,t=2,c=1),hidden=True,fontsize=25,pos=[450,280],size=[300,20])
            Image(name='xy',hidden=True,src='http://material.motimaster.com/aelegy1532071513000/下瘾.png',
                pos=[565,115],size=[100,100],effect=flash(c=0,t=4))
            Image(name='ztx',pos=[141,73],size=[130,130],borderRadius='50%',effect=bounceindown(t=1,c=1))
            Image(name='qq',hidden=True,src='http://material.motimaster.com/aelegy1532068254000/b885b4c063fa0e7d17d8392934321164.png',
                pos=[130,60],size=[155,155],effect=bounceindown(t=1,c=1))
            Image(name='sd',hidden=True,src='http://material.motimaster.com/aelegy1532069627000/印象.png',
                pos=[290,100],size=[300,75],effect=bouncein(t=1,c=1,d=0.5))
            #Image(src='http://material.motimaster.com/aelegy1532075579000/框框.png',pos=['center', 220],size=[654,215])
            with Box(pos=['center', 320],width=654,effect=fadein(c=1,t=2.5,d=0.5)):
                with List(name='zgrid'):
                    with Box(size=[654,225],):
                        Image(src='http://material.motimaster.com/aelegy1532075579000/框框.png',pos=[0,0],size=[654,215])
                        Image(src='{item.url}',pos=[55,40],size=[120,120],borderRadius='50%')
                        Image(Text='',pos=[200,20],size=[400,160],background='rgba(238,238,238,0.3)',borderRadius = '5px')
                        Text(text='{item.name}'+'：',pos=[220,45],size=[400,20],fontsize='18px',lineHeight='20rpx',color='white')
                        # Text(text='{item.f}',pos=[220,70],size=[150,60],lineHeight='35rpx',textAlign='center',fontsize='18px',color='white')
                        # Text(text='{item.n}',pos=[430,70],size=[150,60],lineHeight='35rpx',textAlign='center',fontsize='18px',color='white')
                        # Text(text='→',pos=[375,50],size=[30,10],textAlign='center',fontsize='30px',color='white')
                        Text(text='{item.f}'+' → '+'{item.n}',pos=[220,80],size=[370,60],lineHeight='35rpx',fontsize='18px',color='white')

                        Image(name='cha',size=[40,40],pos=[585,5],hidden=True,onTap=moui.confirm('提示','是否确认删除',moui.request(shan,fs='{item.f}',ns='{item.n}')),
                            src='http://material.motimaster.com/aelegy1532309104000/6657e831422976be16417e982a3bd617副本.png')
        Text(name='wxd',text='',size = [60,220],pos = [0,550],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '0px 5px 5px 0px',)
        Button(
            name='wx',
            hidden=True,
            text = '自己试试',
            plain=True,
            size = [50,160],
            pos = [5,580],
            fontSize = 30,
            textAlign='center',
            lineHeight='40rpx',
            border='none',
            color = 'white',
            onTap =zjx,
            )
        Text(name='hyd',text='',size = [60,250],pos = [690,400],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '5px 0px 0px 5px',)
        ShareButton(
            name='hy',
            hidden=True,
            text = '分享给好友',
            size = [50,200],
            pos = [697,425],
            fontSize = 30,
            plain=True,
            textAlign='center',
            lineHeight='40rpx',
            border='none',
            color = 'white',
            )
        Text(name='pyqd',text='',size = [60,290],pos = [690,700],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '5px 0px 0px 5px',)
        Button(
            name='pyq',
            hidden=True,
            
            size = [50,240],
            pos = [697,725],
            fontSize = 30,
            plain=True,
            textAlign='center',
            lineHeight='40rpx',
            border='none',
            color = 'white',
            onTap=showMask,
            )

        Text(name='zxd',text='',size = [60,220],pos = [0,550],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '0px 5px 5px 0px',)
        Button(
            name='zx',
            hidden=True,
            text = '再写一个',
            plain=True,
            size = [50,160],
            pos = [5,580],
            # background=None,
            fontSize = 30,
            textAlign='center',
            lineHeight='40rpx',
            # borderRadius = '',
            border='none',
            color = 'white',
            onTap =brx,
            )
        Text(name='lwd',text='',size = [60,220],pos = [690,550],hidden=True,background='rgba(238,238,238,0.4)',borderRadius = '5px 0px 0px 5px',)
        Button(
            name='lw',
            hidden=True,
            text = '我也来玩',
            plain=True,
            size = [50,160],
            pos = [697,580],
            # background=None,
            fontSize = 30,
            textAlign='center',
            lineHeight='40rpx',
            # borderRadius = '',
            border='none',
            color = 'white',
            onTap =czj,
            )

        with Mask(name='mask01', opacity = 0.7):
            Image(name='pyqt',pos=['center',300],  mode='aspectFill')
            Button(text='保存图片', pos=['center',800], type='primary', onTap=onSaveImage)

    def onInit():
        # guests = mo.token.getGuestList()
        # mo.conso le(guests)
        mo.setNavibarColor('#ffffff', '#191b44')
        if AUDITING == False:
            page.pyq.text='分享到朋友圈'
            page.my.text = '还什么都没有收到呢，快去分享给好友或者朋友圈吧~'
        if mo.token.isHost()==False:
            page.my.text = 'ta还没有收到印象呢，快去给ta写一个吧~'
        if mo.token.isHost():
            if user.get('tokenid4')==None:
                user.set('tokenid4', mo.token.id)
                mo.token.set('host_name', user.nickName) 
                mo.token.set('host_url', user.avatarUrl)
                mo.token.set('host_gender', user.gender)
        params = {
            'page': 'page1',
            'width': 350,
        }
        page.box.hidden=False
        retParams = mo.acode.getWxAcodeUrl(params)
        erweima = None
        if retParams['ret'] == 0:
            erweima = retParams['url']
        canvas = mo.mopic.createCanvas(900, 600,saveStrategy='permanent')
        canvas.addImage('http://material.motimaster.com/aelegy1532399032000/pyq1.jpg', pos=[0, 0, 900, 600])
        canvas.addImage(erweima, pos=[260, 90, 350, 350],)
        canvas.addImage('http://material.motimaster.com/aelegy1532964684000/baibai.jpg',pos=[390,220,90,90],borderRadius = '5px 5px 5px 5px',)
        canvas.addImage(user.avatarUrl, pos=[395, 225, 80, 80],borderRadius = '5px 5px 5px 5px', )#mask='circle'
        res = canvas.makeImage()

        if res['ret'] == 0:
            page.pyqt.src=res['url']
            user.set('tu',res['url'])

        page.share.title = "快告诉我你对我的印象吧~"
        page.share.imageUrl = 'http://material.motimaster.com/harvey/5455//09ead0e232fb73827b0045ff0525f14d.jpg'
        page.share.page = 'page1'
        page.ztx.src=mo.token.get('host_url')
        page.zgrid.data =mo.token.get('lb',[])
        page.zgrid.data.reverse()
        mo.console(mo.token.get('fklb',[]))
        lb=mo.token.get('lb',[])
        if mo.token.isHost():
            if lb==[]:
                page.my.show()
            else:
                page.chats.show()
            page.qq.show()
            page.sd.show()
            page.xy.show()
            page.cha.show()
            page.wx.show()
            page.pyq.show()
            page.hy.show()
            page.wxd.show()
            page.pyqd.show()
            page.hyd.show()
        else:
            if lb==[]:
                page.my.show()
            page.qq.show()
            page.sd.show()
            page.xy.show()
            page.zx.show()
            page.lw.show()
            page.zxd.show()
            page.lwd.show() 
    def showMask():  
        mo.console('fsl')
        page.mask01.hidden = False
    def onSaveImage():

        mo.saveImage(user.get('tu'))
    def shan():
        mo.console('hh')
        lb=mo.token.get('lb',[])
        for i in lb:
            if i['f']==params.fs and i['n']==params.ns:
                mo.console('xx')
                lb.remove(i)
                mo.token.set('lb',lb)
        if AUDITING == False:
            page.pyq.text='分享到朋友圈'
            page.my.text = '还什么都没有收到呢，快去分享给好友或者朋友圈吧~'
        page.ztx.src=mo.token.get('host_url')
        page.zgrid.data =mo.token.get('lb',[])
        page.zgrid.data.reverse()
        mo.console(page.zgrid.data)
        # mo.console(mo.token.get('lb',[]))
        lb=mo.token.get('lb',[])
        if mo.token.isHost():
            if lb==[]:
                page.my.show()
            else:
                page.chats.show()

            page.cha.show()
            page.wx.show()
            page.pyq.show()
            page.hy.show()
            page.wxd.show()
            page.pyqd.show()
            page.hyd.show()
                
        else:
            page.zx.show()
            page.lw.show()
            page.zxd.show()
            page.lwd.show()
    def zjx():
        user.set('pd',1)
        mo.token.redirectTo('page1')
    def brx():
        user.set('pd1',1)
        mo.token.redirectTo('page1')
    def czj():
        if user.nickName!=None:
            if user.get('tokenid4')==None:
                mo.redirectTo('page2')
            else:
                mo.redirectTo('page1')

        else:
            mo.redirectTo('page1')








