from moapp.lib.client import *
import random

drama2={'测试' :[
    {
        #问题
        'title': '1/3.你的性别是？',
        #选项
        'options': [
        {'text': '女', 'value': '1'},
        {'text': '男', 'value': '2'},
    ],
    
    },
    {
        'title': '2/3.上面这张图，你第一眼看到是什么？',
        'options':[
        {'text' : '一张人脸', 'value' : '1'},
        {'text' : '一弯月亮', 'value': '2'},
    ],
       
    },
    {
        'title': '3/3.以上这四个风格不同的女生，你第一眼觉得哪个最好看？',
        'options': [
        {'text' : '女生A' , 'value':'1'},
        {'text' : '女生B' , 'value':'2'},
        {'text' : '女生C' , 'value':'3'},
        {'text' : '女生D' , 'value':'4'},
    ],
       
    },
]
}
#问题图
questionImg2 = [
    'http://material.motimaster.com/appmaker/yangyiyun/5262.png',
    'http://material.motimaster.com/chenwei1535440956000/222.jpg',
    'http://material.motimaster.com/chenwei1535090983000/111.jpg',
]
#结果图
img_int2 = [
    'http://material.motimaster.com/chenwei1535091551000/1.jpg',
    'http://material.motimaster.com/chenwei1535091614000/6.jpg',
    'http://material.motimaster.com/chenwei1535091551000/2.jpg',
    'http://material.motimaster.com/chenwei1535091552000/4.jpg',
    'http://material.motimaster.com/chenwei1535091670000/10.jpg',
    'http://material.motimaster.com/chenwei1535091669000/9.jpg',
    'http://material.motimaster.com/chenwei1535091614000/5.jpg',
    'http://material.motimaster.com/chenwei1535091670000/12.jpg',
    'http://material.motimaster.com/chenwei1535091552000/3.jpg',
    'http://material.motimaster.com/chenwei1535091670000/11.jpg',
    'http://material.motimaster.com/chenwei1535091615000/7.jpg',
    'http://material.motimaster.com/chenwei1535091615000/8.jpg',
]


listcase2=[
    'http://material.motimaster.com/chenwei1535548993000/奔跑吧师弟二维码.jpg',
]

def yinxiangfazhan():
    page6()
    page7()
    page8()

class page6(Page):    
    background='http://material.motimaster.com/chenwei1535513828000/haoyouyinxiang.jpg'#第一个页面的名称和背景图
    
    def UI():
        #Image(src='http://material.motimaster.com/chenwei1535347735000/haoyouyinxiang.jpg', mode='aspectFit')
        Button(effect=pulse(t=1,c=0),type='primary', pos=[275,600],text='开始',boxShadow='5px 5px 7px #7c9199',
            background='#0598cc',size=[200,200],borderRadius = '50%',lineHeight = 200,openType='getUserInfo',
            onTap = moui.goto('page7',drama_list = '测试'))
           #首页的button，跳转到paper页面，同时读取的是上面准备的list内容

class page7(Page):
    background='http://material.motimaster.com/chenwei1535513828000/haoyouyinxiang2.jpg'
    
    def UI():  
        with Box(pos=['center', 20], width=512, height=250):#放置整个图片的box
            Image(id='questionImg2',pos=['center',120],size=[512,244])#设置image的ID，通过云函数获取。    
        MoRadio(name = 'radio3',pos=[70,510, 660, 130],fontSize = 35,onChange = onNext)#选项部分，选项被命名为radio3，下一步用云函数调用
        Text(name = 'radiotext',padding=10,pos=[70,390],backgroundColor='#fbfdf7',fontSize = 35,borderRadius= '10px 10px 10px 10px',color = '#040404',width =600)#题目部分被命名为radiotext，通过云函数调用
    def onInit():
        questions = drama2['测试']#获取字典的内容

        page.data.set('pagenum',0)#设置第几题
        page.data.set('curnum',0)#当前第几题
        user.set('ans',[])
        page.radiotext.text = questions[0]['title']
        page.radio3.data = questions[0]['options']
        page.questionImg2.src = questionImg2[0]

    def onNext():#答题&计分&结果判断
        questions = drama2['测试']#定义问题
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
            for i in [1,3,5,7,9,13,16]:
                if ansint <= i:
                    break
                k += 1 #判断下一个图片
            user.set('imgurl',img_int2[k])
            mo.goto('page8') 
            return
        page.data.set('pagenum',pagenum)
        page.radiotext.text = questions[pagenum]['title']
        page.radio3.data = questions[pagenum]['options']
        page.questionImg2.src = questionImg2[pagenum]

class page8(Page):
    enableShare=True
    backgroundColor='#151c38'
    def UI():        
        Image(id='mopicImage',pos=['center',0],size=[720,1220])#设置image的ID，通过云函数获取。
        ImageAvatar(name='avtar',hidden=True, pos=[293, 502],size=[164, 164],borderRadius='50%',onTap=moui.showTips('111'))
        #with Box(pos=[0, 0], width=750, height=750):
        #    Button(text='保存结果图片', pos=[95, 1100, 300, 150],background='#a40603', color='#ffffff' ,
        #    type='miniDefault',fontSize = 35,lineHeight=150,onTap=onSaveImage)#保存图片的butt

        #ShareButton(pos=[455,1100,300,150],type='miniDefault',text='邀请好友玩',color='#ffffff' ,fontSize = 35,lineHeight=150,background='#fb2471')#分享button

        #添加分享按钮
        ShareButton(pos=[115, 1000, 200, 100],type='miniDefault',text='分享',color='#ffffff' ,fontSize = 26,lineHeight=100,background='#0598cc')#分享button
        #添加保存图片按钮
        Button(text='保存图片', pos=[435,1000,200,100], openType='getUserInfo',background='#0598cc', color='#ffffff' ,type='miniDefault',fontSize = 26,lineHeight=100,onTap=onSaveImage)#保存图片的button
        #横线
        #Box(pos=[0,1200],size=[750,1],borderBottom='10px solid #ecf0f3') 
        #更多好玩的测试
        Text(pos=[500,1230],text='更多好玩的测试>',fontWeight='lighter',fontSize=30,onTap= moui.redirectTo('firstpage'))
        Box(pos=[0,1290],size=[750,1],borderBottom='1px solid #ecf0f3')  #横线

        #测试列表展示
        #with Box(pos=[0,1320],width=750,background='#222222'):   
        #with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
            #borderBottom= '1px solid #ecf0f3',marginBottom=15):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
            #Image(left=20,size=[150, 150], src='http://material.motimaster.com/linda123jiang/hi/main/d133f0c2982b5a9ef41a8ed87616fb3d.jpg' , mode='aspectFill',borderRadius= '10px')
            #Text(pos=[190,0],text='前世今生',color='#353535',fontSize=33)
            #Text(pos=[190,55],text='19.8万人在测',color='#808080',fontSize=28)
            #Text(pos=[190,110],text='你是什么投胎转世的？',fontSize=30,color='#808080')
           # Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
                        #color='#FF0000',background='#ffffff',border='1px solid red')
            #Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page3'))
        
        #with Box(pos=[0,1520],width=750,background='#222222'):   
        #with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
            #borderBottom= '1px solid #ecf0f3',marginBottom=15):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
            #Image(left=20,size=[150, 150], src='http://material.motimaster.com/jiangxiaoni1534579630000/微信截图_20180808171224.png' , mode='aspectFill',borderRadius= '10px')
            #Text(pos=[190,0],text='爱情告白',color='#353535',fontSize=33)
            #Text(pos=[190,55],text='21.09万人在测',color='#808080',fontSize=28)
            #Text(pos=[190,110],text='这是我写给你的情书，请查收',fontSize=30,color='#808080')
            #Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
                   # color='#FF0000',background='#ffffff',border='1px solid red')
           # Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page27'))
        
        #with Box(pos=[0,1720],width=750,background='#222222'):   
        #with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
               # borderBottom= '1px solid #ecf0f3',marginBottom=15):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
              #  Image(left=20,size=[150, 150], src='http://material.motimaster.com/jiangxiaoni1534579835000/anlian.jpg' , mode='aspectFill',borderRadius= '10px')
              # Text(pos=[190,0],text='暗恋理由',color='#353535',fontSize=33)
              #  Text(pos=[190,55],text='21.09万人在测',color='#808080',fontSize=28)
              #  Text(pos=[190,110],text='测你被人暗恋的5个理由',fontSize=30,color='#808080')
               # Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
               #         color='#FF0000',background='#ffffff',border='1px solid red')
              #  Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page22'))
               
        #with Box(pos=[0,1900],width=750,background='#222222'):   
        #with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
              #  borderBottom= '1px solid #ecf0f3',marginBottom=15):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
              #  Image(left=20,size=[150, 150], src='http://material.motimaster.com/jiangxiaoni1534579661000/微信截图_20180810155710.png' , mode='aspectFill',borderRadius= '10px')
              #  Text(pos=[190,0],text='好脾气指数',color='#353535',fontSize=33)
              #  Text(pos=[190,55],text='11.34万人在测',color='#808080',fontSize=28)
              #  Text(pos=[190,110],text='测你是不是老好人',fontSize=30,color='#808080')
               # Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
               #         color='#FF0000',background='#ffffff',border='1px solid red')
              #  Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page15'))
        
        #with Box(pos=[0,2100],width=750,background='#222222'):   
        #with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
              #  borderBottom= '1px solid #ecf0f3',marginBottom=15):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
              #  Image(left=20,size=[150, 150], src='http://material.motimaster.com/jiangxiaoni1534580478000/3.jpg' , mode='aspectFill',borderRadius= '10px')
              #  Text(pos=[190,0],text='有缘城市',color='#353535',fontSize=33)
              #  Text(pos=[190,55],text='21.09万人在测',color='#808080',fontSize=28)
              #  Text(pos=[190,110],text='哪一座城市跟你有缘',fontSize=30,color='#808080')
              #  Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
               #         color='#FF0000',background='#ffffff',border='1px solid red')
              #  Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page29'))
        



    def onInit(): #生成成绩单&添加二维码&添加用户昵称&分享页面设置
        imgsrc = user.get('imgurl')
        #创建最后展示页的画布
        page.mopicImage.src = imgsrc
        canvas = mo.mopic.createCanvas(720,1220)
        #在画布上加上背景图
        canvas.addImage(imgsrc, pos=[0,0,720,1220])
        #在画布上加上用户头像
        canvas.addImage(user.avatarUrl, pos=[33,27,150], mask='circle')
        #在画布上加上文字
        #canvas.addText(user.nickName+'的前世是：', pos=[250, 160], fontSize=32, color=(0, 0, 0))
    
        #res = canvas.makeImage()

        #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
        #erweima = None
        #params = {
        #    'page': 'first',
        #    'width': 150,
        #    'options':{'a':1,'b':user.nickName}
        #}
        #retParams = mo.acode.getWxAcodeUrl(params)    
        #if retParams['ret'] == 0:
        #    erweima = retParams['url']

        #把二维码添加到画布上
        canvas.addImage(random.choice(listcase2), pos=[11,1090,122])
        #加用户昵称
        canvas.addText(user.nickName, pos=[232,35, 424,62],fontSize=60, textAlign='left',color=(0,0,0))
        #生成图片
        res_erweima = canvas.makeImage()

        #判断生成图片是否成功
        if res_erweima['ret'] == 0:
            #在页面上展示结果图
            page.mopicImage.src = res_erweima['url']
            #生成“保存图片”按钮操作需要的图片链接
            page.data.set('url',res_erweima['url'])

        #设置页面分享的标题、图片、用户进入页、传递的参数 
        page.share.title =  "你的朋友邀请看看Ta的好友印象"
        page.share.imageUrl = 'http://material.motimaster.com/chenwei1535339977000/534ecc35e31cb.jpg'   #首页的图片
        page.share.page = 'first'
        page.share.options = {'a':1,'b':user.nickName}
        
    
#点击“保存图片”按钮的操作
    def onSaveImage():
        url = page.data.get('url')#提取分享图片的地址
        mo.saveImage(url)