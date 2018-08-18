def main(): # 定义一个函数
    # 声明MoApp（注，一个小程序只能有一个MoApp）
    with MoApp(appid='wx263b9c72fc87b39c', name='下一世ta是你的谁？',naviBarTitle='下一世ta是你的谁？',naviBarColor='#FFFFFF',naviBarStyle='black'):
        # 定义一个小程序页面
        page1()#首页动画页
        page2()#选门页
        page3()#展示页
        page4()#分享页

class page1(Page):
    name='page1'   
    def UI():
        
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        
        with Box(pos=[0,0],size=[750,1334],effect = fadein(size=(0,1),d=0,t=2,c=1,s=0)):#载入动画
            Text(text='生命轮回不休',pos=['center',100],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=0,t=2,c=1,s=0))
            Text(text='下一世，那些你牵挂的人',pos=['center',200],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=1,t=2,c=1,s=0,w="*-*"))
            Text(text='还会跟你相遇吗？',pos=['center',300],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=2,t=2,c=1,s=0,w="*-*"))
            Image(src='http://material.motimaster.com/shiyimin1531473477000/lazhude.png',pos=['center',270],size=[464,613],effect = fadein(size=(0,1),d=3,t=2,c=1,s=0,w="*-*"))#蜡烛
        
        Button(text = '开启来世之旅 ',fontSize=30,background='http://material.motimaster.com/shiyimin1531818533000/button.jpg',lineHeight=70,pos =['center',920],size=[200,70], onTap=moui.goto('page2'))

class page2(Page):
    name='page2'   
    def UI():        
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        with Box(name='test',pos=[0,0],size=[750,1334],hidden=True):#选门动画
            
            Text(text='一扇门，一段缘',pos=['center',10],color='#FFFFFF',fontSize=30,effect = fadein(size=(0,1),d=0.5,t=2,c=1,p=1,s=0))
            Image(pos=['center',70],size=[40,33],src='http://material.motimaster.com/shiyimin1531473851000/jiantou.png',effect =[fadein(size=(0,1),d=1,t=2,c=1,p=1,s=0),move(path=[(10,70),(10,80)], t=1.2, c=0,p=1)]) # 小箭头
            Text(text='请选择下一世，你最想开启的门',pos=['center',130],color='#FFFFFF',fontSize=30,fontWeight=600,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0)) 
            Text( text='郑', pos=[43, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text( text='李', pos=[152, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text( text='红', pos=[259, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text( text='炯', pos=[364, 268],size=[63,63],textAlign='center',lineHeight=63,color='#3E4DD2', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            Text( text='燕', pos=[472, 268],size=[63,63],textAlign='center',lineHeight=63,color='#F56E6E', fontSize=36,effect=bounceindown(size=(0,1),d=1,t=0.6,c=1,p=1,s=0))
            
            # with Box(pos=[0,-60],size=[750,1000],effect = fadein(size=(0,1),d=2,t=2,c=1,p=1,s=0)):
            #     with Box(pos=[0,0],size=[750,700],effect=move(path=[(30,320), (30,360)], t=3, c=0,p=1)):
            #     # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
            #         Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[670,760],pos=[0,0])#大门
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[30,37],pos=[440,80],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#1左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[60,57],pos=[245,175],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#2左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,35],pos=[110,240],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,47],pos=[5,530],effect = fadein(d=0,t=1,c=0,p=1,s=0))#4左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,25],pos=[230,470],effect = fadein(d=0,t=1.2,c=0,p=1,s=0))#5左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,27],pos=[600,275],effect = fadein(d=0,t=1.1,c=0,p=1,s=0))#1右向光
            #         Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[405,420],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#2右向光
            #         Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,35],pos=[625,550],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3右向光
            #         Button(pos=[440,0],size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#1按钮
            #         Button(pos=[215,75],size=[130,226],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#2按钮
            #         Button(pos=[120,200],size=[80,116],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#3按钮
            #         Button(pos=[15,380],size=[150,196],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#4按钮
            #         Button(pos=[240,410],size=[75,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#5按钮
            #         Button(pos=[550,185],size=[80,166],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#1按钮
            #         Button(pos=[365,350],size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#2按钮
            #         Button(pos=[540,375],size=[120,186],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))#3按钮

            #     with Box(pos=[0,0],size=[150,330],effect=move(path=[(85,330), (85,370)], t=2, c=0,p=1)):#左上角门
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[80,176],pos=[0,0])#门
            #         Button(pos=[0,0],size=[80,176],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))

            #     with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,330), (640,330)], t=3, c=0,p=1)):#右上角门
            #         Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
            #         Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[60,132],pos=[0,0])#门
            #         Button(pos=[0,0],size=[60,132],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))

            #     with Box(pos=[0,0],size=[150,330],effect=move(path=[(175,930), (195,930)], t=3.5, c=0,p=1)):#左下角门
            #         Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
            #         Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[90,198],pos=[0,0])#门
            #         Button(pos=[0,0],size=[90,198],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))

            #     with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,940), (600,970)], t=3, c=0,p=1)):#右下角门
            #         Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
            #         Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[80,176],pos=[0,0])#门
            #         Button(pos=[0,0],size=[80,176],border=0,background = 'rgba(150,150,150,0)',onTap=moui.goto('page3'))
    def onInit():
        page.test.hidden = False

class page3(Page):
    name='page3'
    def UI():       
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        
        Image(pos=[120,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='我的好友缘分部落图',pos=['center',20],fontSize=32,color='#FFFFFF')
        Image(pos=[540,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Image(pos=[0,0],size=[750,1400],src="http://pic.gaoloumi.com/attachments/forum/201807/17/081934aza6ttuh9a65am6z.jpg",position = 'fixed')
        with Box(pos=[0,-60],size=[750,450]):
            with Box(pos=[0,0],size=[750,450],effect=move(path=[(170,130), (170,140)], t=1.8, c=0,p=1)):
            # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[370,420],pos=[0,0])#大门
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[30,37],pos=[440,80],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#1左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[60,57],pos=[245,175],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#2左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,35],pos=[110,240],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,47],pos=[5,530],effect = fadein(d=0,t=1,c=0,p=1,s=0))#4左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,25],pos=[230,470],effect = fadein(d=0,t=1.2,c=0,p=1,s=0))#5左向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,27],pos=[600,275],effect = fadein(d=0,t=1.1,c=0,p=1,s=0))#1右向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[405,420],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#2右向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,35],pos=[625,550],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3右向光
                Box(background='#FFFFFF',borderRadius='50%',pos=[115,50],size=[45,45]) #主人头像

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(155,135), (155,140)], t=1.5, c=0,p=1)):#左上角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[50,110],pos=[0,0])#门
                Box(background='#FFFFFF',borderRadius='50%',pos=[0,0],size=[35,35]) #客人头像

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(530,145), (535,145)], t=1.6, c=0,p=1)):#右上角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[40,88],pos=[0,0])#门
                Box(background='#FFFFFF',borderRadius='50%',pos=[0,0],size=[35,35]) #客人头像

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(215,440), (225,440)], t=1.8, c=0,p=1)):#左下角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[60,132],pos=[0,0])#门
                Box(background='#FFFFFF',borderRadius='50%',pos=[0,0],size=[35,35]) #客人头像

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(550,440), (550,450)], t=1.2, c=0,p=1)):#右下角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[50,110],pos=[0,0])#门
                Box(background='#FFFFFF',borderRadius='50%',pos=[0,0],size=[35,35]) #客人头像

        
        Image(pos=[140,520],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='来世缘分详解',pos=['center',500],fontSize=32,color='#FFFFFF')
        Image(pos=[510,520],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点

        with Box(pos=['center',600],size=[680,400],background='rgba(37, 22, 63,0.6)'):
            
            Box(background='#FFFFFF',borderRadius='50%',pos=[155,20],size=[75,75]) #主人头像

            Text(text='缘份值24分',fontSize=28,color='#FFFFFF',pos=['center',8])
            Box(background='#4aaac0',size=[170,4],pos=['center',50])
            Text(text='相距XX光年',fontSize=28,color='#FFFFFF',pos=['center',58])

            Box(background='#FFFFFF',borderRadius='50%',pos=[460,20],size=[75,75]) #客人头像

            with Box(pos=[170,100],size=[20,30]):
                Text(text='张三',color='#FFFFFF',pos=['center',0],fontSize=25) #主人昵称
                Text(text='(XX门)',color='#FFFFFF',pos=[-5,30],fontSize=25) #主人选择的门的名字
            with Box(pos=[475,100],size=[20,30]):
                Text(text='李四',color='#FFFFFF',pos=['center',0],fontSize=25) #客人昵称
                Text(text='(XY门)',color='#FFFFFF',pos=[-5,30],fontSize=25) #客人选择的门的名字
 
            Text(text='来世Ta是你的',color='#c8f9ff',fontSize=28,pos=[10,180])
            Text(text='闺蜜',color='#FFFFFF',fontSize=28,pos=[190,180])
            Text(text='来世缘分详解',color='#c8f9ff',fontSize=28,pos=[10,240])
            Text(text='你会在最美的年华，遇见一个陪你笑、陪你',color='#FFFFFF',fontSize=28,pos=[190,240])
        Button(name='fenxiang',text='邀请好友来测', lineHeight= 80,size=[300,80],pos=['center',900],fontSize=30,background = '#5e5ca5',color = '#FFFFFF',boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',border = 0,onTap=moui.goto('page4'))



class page4(Page):
    name='page4'
    def UI():
        Image(pos=[0,0],size=[750,296],src='http://material.motimaster.com/shiyimin1531820626000/share.jpg') # 背景图
        #Text(text='下一世',pos=['center',50],color='#FFFFFF',fontSize=30,fontWeight=600)
        #Text(text='你是我的谁？',pos=['center',100],color='#FFFFFF',fontSize=30,fontWeight=600)
        Image(background='#000000',borderRadius='50%',size=[300,300],pos=['center',330]) #二维码
        Text(text='长按识别二维码',pos=['center',650],color='#000000',fontSize=25)
        Button(text='分享给朋友',size=[320,80],pos=['center',750],fontSize=33,background = '#5e5ca5',color = '#FFFFFF',border = 0,boxShadow ='3px 4px 3px 1px rgba(0,0,0,0.3)',)
        Button(text='保存朋友圈海报',size=[320,80],pos=['center',870],fontSize = 33,color = '#5e5ca5',border = '1px solid #5e5ca5',plain=True)



