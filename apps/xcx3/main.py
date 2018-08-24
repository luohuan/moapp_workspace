
import requests
import hashlib
import json
dormitorydata=[
   

    {
        'id':0,
        'cover':'http://material.motimaster.com/harvey/5455/myrose/29c83079b0f9ffaa2b75c2ce0b90644d.png',
        'title':'八字合婚',
        'people':'429.533万人在测',
        'details':'夫妻情缘的深浅，看八字日柱便知...',
        "path":"https://xcx2-zxcs.lingji666.com/newhehun/index.html",
        'appid':'',
        'button_name':'测试',
        "type":'protest',
    },
    {
        'id':1,
        'cover':'http://material.motimaster.com/harvey/5455/myrose/cdddb5693da5559e2d9964f494184b14.png',
        'title':'恋爱配对',
        'people':'824.23万人在测',
        'details':'十二星座配对幸福指数，看看你跟谁最配',
        "path":"https://xcx2-zxcs.lingji666.com/lianaipeidui/index.html",
        'appid':'',
        'button_name':'测试',
        "type":'protest',
    },
    {
        'id':2,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/92920857d821b82764dd7d6b51fe2bcb.jpg',
        'title':'深度个人占星',
        'people':'19.8万人在测',
        'details':'个人星盘分析，透彻解读你的命运！',
        "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
        'appid':'',
        'button_name':'测试',
        "type":'protest',
    },
    {
        'id':3,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/312e5c10b62539a3bd5f6f9237b3d5a0.jpg',
        'title':'2018狗年运程',
        'people':'46.03万人在测',
        'details':'2018狗年运程解析，助您催旺桃花姻缘...',
        "path":"https://xcx2-zxcs.lingji666.com/mllyuncheng/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':4,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/e490c2f427c3fe96f8644e48f14d6622.jpg',
        'title':'你有多好命？',
        'people':'47.02万人在测',
        'details':'分析命中富贵格局，解读今生吉凶祸福...',
        "path":"https://xcx2-zxcs.lingji666.com/liunianyuncheng/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':5,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/cbe9068f79faeff1a6ab40d5f1df682b.jpg',
        'title':'感情支招',
        'people':'27.44万人在测',
        'details':'八字姻缘解析，看你何时恋爱结婚？',
        "path":"https://xcx2-zxcs.lingji666.com/baziyinyuan/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':6,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/a4c6ebdb29a93a0c96a395e5420176fd.jpg',
        'title':'爱情塔罗牌',
        'people':'47.3万人在测',
        'details':'三张塔罗牌，解决你的爱情烦恼！',
        "path":"https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':6,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/4fba6a7a432b118a57e6e5d659c52738.jpg',
        'title':'你今生有着怎样的命运？',
        'people':'49.53万人在测',
        'details':'通晓八字，乐知天命，道尽你今生命中...',
        "path":"https://xcx2-zxcs.lingji666.com/forecastbazijingpibundle/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':7,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/e04ef01bcbbfe3e2ece047cdc7f3ffd5.jpg',
        'title':'前世今生',
        'people':'49.53万人在测',
        'details':'知晓前世姻缘，重结今生善果！',
        "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    {
        'id':8,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/69f671568b6f20fee220bffaab711c6b.jpg',
        'title':'前世姻缘',
        'people':'49.53万人在测',
        'details':'今生的相遇相知，是前世修来的何种缘...',
        "path":"https://xcx2-zxcs.lingji666.com/qianshiyinyuan/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'开玩',
    }

    #############################################################

    # {
    #     'index':1,
    #     'cover':'http://material.motimaster.com/shiyimin1534211266000/haoyouhuawo.jpg',
    #     'title':'好友画我',
    #     'people':'98.03万人在测',
    #     'details':'好友眼中的你是什么样子的？',
    #     'path':'pages/index/index',
    #     'appid':'wx02207e6022e44158',
    #     'button_name':'开玩'
    # },
    # {
    #     'index':2,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/fabb5b1021d7c043d1b7628f34856f34.jpg',
    #     'title':'心理年龄',
    #     'people':'78.21万人在测',
    #     'details':'你的性格是成熟型还是幼稚型？',
    #     'path':'pages/page6/page6',
    #     'appid':'wx9f918c171334a22a',
    #     'button_name':'开玩'
    # },

    # {
    #     'index':3,
    #     'cover':'http://material.motimaster.com/jiangxiaoni1533089743000/6.jpg',
    #     'title':'看你怎么说',
    #     'people':'129.35万人在测',
    #     'details':'说说你对我的印象吧！',
    #     'path':'pages/page1/page1',
    #     'appid':'wxc1a59dd1befff332',
    #     'button_name':'开玩'
    # },
    # {
    #     'index':4,
    #     'cover':'http://material.motimaster.com/shiyimin1534212291000/pingxing.jpg',
    #     'title':'平行世界',
    #     'people':'69.89万人在测',
    #     'details':'平行世界里，你会遇到哪些缘分？',
    #     'path':'pages/page1/page1',       
    #     'appid':'wx628e03240351132c',
    #     'button_name':'开玩'
    # },
    # {
    #     'index':5,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/417a21294755bea737cefda07585213a.jpg',
    #     'title':'名字价值',
    #     'people':'89.08万人在测',
    #     'details':'测你名字都包含哪些特性？' ,
    #     'path':'pages/page9/page9',
    #     'appid':'wx9f918c171334a22a', 
    #     'button_name':'开玩'

    # },

    # {
    #     'index':6,
    #     'cover':'http://material.motimaster.com/jiangxiaoni1533094978000/123.jpg',
    #     'title':'八月关键词',
    #     'people':'21.09万人在测',
    #     'details':'愿你有人爱，有事做，也有所期待。',
    #     'path':'pages/page13/page13',
    #     'appid':'wx9f918c171334a22a', 
    #     'button_name':'开玩'
    # }

]

griditems1 = [
    {
        'id':0,
        'src':'http://material.motimaster.com/harvey/5455/myrose/29c83079b0f9ffaa2b75c2ce0b90644d.png',
        'title':'八字合婚',
        'people':'',
        'details':'夫妻情缘的深浅，看八字日柱便知...',
        "path":"https://xcx2-zxcs.lingji666.com/newhehun/index.html",
        'appid':'',
        "type":'protest',
    },
    {
        'id':1,
        'src':'http://material.motimaster.com/harvey/5455/myrose/cdddb5693da5559e2d9964f494184b14.png',
        'title':'恋爱配对',
        'people':'',
        'details':'十二星座配对幸福指数，看看你跟谁最配',
        "path":"https://xcx2-zxcs.lingji666.com/lianaipeidui/index.html",
        'appid':'',
        'button_name':'测试',
        "type":'protest',
    },
    {
        'id':2,
        'src':'http://material.motimaster.com/linda123jiang/hi/main/92920857d821b82764dd7d6b51fe2bcb.jpg',
        'title':'个人占星',
        'people':'',
        'details':'个人星盘分析，透彻解读你的命运！',
        "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
        'appid':'',
        'button_name':'测试',
        "type":'protest',
    },
    {
        'id':3,
        'src':'http://material.motimaster.com/linda123jiang/hi/main/312e5c10b62539a3bd5f6f9237b3d5a0.jpg',
        'title':'狗年运程',
        'people':'',
        'details':'2018狗年运程解析，助您催旺桃花姻缘...',
        "path":"https://xcx2-zxcs.lingji666.com/mllyuncheng/index.html",
        "type":'protest',
        'appid':'',
        'button_name':'测试',
    },
    # {   'id':1,
    #     'src': 'http://material.motimaster.com/shiyimin1534153254000/xingming.png',
    #     'people':'111万人在测',
    #     'title': '姓名契合度',
    #     'path':'pages/entrance/entrance',
    #     'appid':'wxa9b01a93c80e98e9',
    #     'type': 'protest'
    #    },
    # {
    #     'id':2,
    #     'src': 'http://material.motimaster.com/shiyimin1534153129000/xingzuoxiaowo.png',
    #     'people':'1200万人在测',
    #     'title': '星座小屋',
    #     'path':'pages/pageentrance/pageentrance',
    #     'appid':'wx01434b3ed0010d28',
    #     'type': 'protest'
    # },
    # {
    #     'id':3,
    #     'src': 'http://material.motimaster.com/shiyimin1534153552000/huiyiqiang.png',
    #     'people':'30万人在测',
    #     'title': '好友回忆墙',
    #     'path':'pages/begin/begin',
    #     'appid':'wx468ad783f165eea0',
    #     'type': 'protest'

    # },
    # {
    #     'id':4,
    #     'src': 'http://material.motimaster.com/shiyimin1534154048000/quce.png',
    #     'people':'87万人在测',
    #     'title': '趣测小窝',
    #     'path':'pages/mainPage/mainPage',
    #     'appid':'wx91f13354f5356b6c',
    #     'type': 'protest'

    # },
    # {
    #     'id':5,
    #     'src':'http://material.motimaster.com/shiyimin1534153676000/haoyouhuawo.png',
    #     'title':'好友画我',
    #     'people':'98万人在测',
    #     'path':'pages/index/index',
    #     'appid':'wx02207e6022e44158',
    #     'type': 'protest'
    # }

]

dataswiper1=[
            {
                'id':3,
                'pic':'http://material.motimaster.com/yuyuan/Duudle/create/f234beb7d4e70116d3fe15c608fcf707.jpg',
                'title':'谁最懂我',
                'people':'78.21万人在玩',
                'details':'看看你们的名字契合度是多少？',
                'path':'pages/mainpage/mainpage',
                'appid':'wx18610e0755615e2f',
                
                'button_name':'可用',
                'type': 'picker'

            },
            {
                'id':2,
                'pic':'http://material.motimaster.com/liuhongjie1534411840000/banner.png',
                'title':'看动图猜影视闯关',
                'people':'78.21万人在玩',
                'details':'看动图猜影视闯关',
                'path':'pages/mainPage/mainPage',
                'appid':'wx91f13354f5356b6c',
                
                'button_name':'可用',
                'type': 'picker'

            },
            # {
            #     'id': 2,
            #     'pic': 'http://material.motimaster.com/shiyimin1534133267000/xingzuo.jpg',
            #     'title': '星座小窝',
            #     'path':'pages/pageentrance/pageentrance',
            #     'appid':'wx01434b3ed0010d28',
            #     'type': 'picker'
            # },
            # {
            #     'id': 1,
            #     'pic': 'http://material.motimaster.com/shiyimin1534137928000/huiyi.jpg',
            #     'title': '好友回忆墙',
            #     'path':'pages/begin/begin',
            #     'appid':'wx468ad783f165eea0',
            #     'type': 'input'
            # }
            ]



# 小猜心 Lite
def main():
    with MoApp(appid='wx6acc1db2845590f6',name='娱乐盒子'):
        listPage()
        webview()
        payment()

class listPage(Page):
    """docstring for gridPage"""
    def UI():
        #Box(size=[750,1],borderTop='3px solid LightGrey',pos=[0,610])  #横线
        with Box(name='auditing_box', pos=[0,0], hidden=True, width=750):
            Image(name='image1',pos=[0,-40],size=[750,1325],src="http://material.motimaster.com/harvey/5455/myrose/89c33fb1592b3b3289d94ff08dd984aa.jpg")
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
        with Box(name='neirong',pos=[0,0],hidden=True):
            with Swiper(id='swiper1',size=[750,310],interval=3000, duration=2000, autoplay=True) as a:
                a._add_attrs(['circular'])
                this.circular = True
                with SwiperItem(id ='dataswiper'):
                    Image(pos=[0,0, 750, 310], src ='{item.pic}',onTap = moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}',tyepe='{item.type}'))# borderRadius='10px',
                       


            with Box(id='hidden_1',pos=[0,300]):
           
                Text( id='recommend', pos=[20,30], fontWeight='450',fontSize=37)
                
                # Box(size=[750,1],borderBottom='1px solid WhiteSmoke',pos=[0,500])  #横线
                with ScrollBox(pos=[0,40],size=[750, 300], scrollX=True):

                    with List(name='grid1', pos=['center', 10], whiteSpace='nowrap'):
                        with Box(size=[160,220],marginLeft=20,onTap = moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}',tyepe='{item.type}'), display='inline-block'):                   
                            Image(pos=['center', 50],size=[150, 150], src='{item.src}', mode='aspectFill',borderRadius= '5px')
                            Text(pos=['center',260],text='{item.people}',color='#808080',fontSize=25)
                            Text(pos=['center',220],text='{item.title}',color='#353535',fontSize=30,fontWeight='430')
                       
                Image(id='ad',pos=[0,370],size=[750,191],onTap=moui.request(ad_goto,name='ad'))


                
                with Box(id='hidden_ad',pos=[0,500]):
                   
                
                        
                    Text( id='all_play',pos=[20,80],fontWeight='450',fontSize=37)


                    with Box(pos=[0,140],width=750,background='#222222'):   #列表
                        

                        with List(name='dormitorylist'):
                            with Box(pos=[0,10],size=[750,180],borderRadius='0px',background='white',
                                borderBottom= '1px solid WhiteSmoke',marginBottom=15,onTap= moui.request(go_to,path='{item.path}',appid='{item.appid}',type='{item.type}',title='{item.title}')):
                                #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
                                Image(left=20,size=[150, 150], src='{item.cover}' , mode='aspectFill',borderRadius= '10px')
                                Text(pos=[190,0],text='{item.title}',color='#353535',fontSize=33)
                                Text(pos=[190,55],text='{item.people}',color='#808080',fontSize=28)
                                Text(pos=[190,110],text='{item.details}',fontSize=30,color='#808080')
                                Button(pos=[590,20],type='miniPrimary',text='{item.button_name}',size=[130,65],lineHeight='30px',padding=0,fontSize=35,
                                    fontWeight='400',color='#fbfafa',boxShadow ='1px 0px 1px 0px rgba(0,0,0,0.3)',
                                    background='#ee5b60')
                                Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',)

                    
                        
                        ShareButton(name='fenxiang',background='http://material.motimaster.com/shiyimin1533717166000/share.png',hidden=True,size = [210,70],position = 'fixed',lineHeight = 90,fontSize = 35,fontWeight = '900',
                            color = '#f7ca4e',border = 0,plain = True,effect=move(path=[(-40,950), (-10,950)], t=1.5, c=0,p=1))
                Image(id='ad_2',pos=[0,1030],size=[750,191],position = 'fixed',onTap=moui.request(ad_goto,name='ad_2'))
    def computeNameScore():
        mo.showAlert('好友名字契合度','你们名字契合度分数为%s分'% str(int(random.random()*100)))

    def onInit():   
        mo.setNavibarTitle('专业测试占卜')
        if page.options.channel != None:
            user.channel = page.options.channel
        page.neirong.hidden = False
        #page.auditing_box.hidden = False
        #mo.setNavibarTitle('名字匹配')
        if page.options.mpid:
            mo.stat('mpid_%s'%page.options.mpid)
        page.dormitorylist.data = dormitorydata  #获取列表信息
        page.grid1.data = griditems1
        page.share.title = "我发现了一个好玩的东西，快来看看吧！"
        page.share.imageUrl = 'http://material.motimaster.com/shiyimin1534156084000/box.png'
        page.fenxiang.hidden = False

        switch = False  #控制轮播器是否隐藏
        ad     = True #控制广告区域是否隐藏

        page.ad_2.hidden=True
        if switch == True:                
            page.dataswiper.hidden=True
            page.hidden_1.pos=[0,0]

        if ad == True:                  
            page.ad.hidden=True
            page.hidden_ad.pos=[0,310]


        page.recommend.text='热门测试'             #这里控制‘热门’的文字
        page.recommend.color='#d32f24'

        page.all_play.text='测试·占卜'      #这里控制‘大家都在玩’的文字
        page.all_play.color='#d32f24'

        page.dataswiper.data = dataswiper1


        page.swiper1.indicatorDots=True
        page.swiper1.indicatorActiveColor ='#FF8C69'

    def go_to():
        #mo.stat(params.appid)
        if params.type == 'protest' or params.tyepe == 'protest':
            if user.channel != None:
                mo.goto('webview', src=params.path + "?channel=%s"%user.channel )
            else:
                mo.goto('webview', src=params.path + "?channel=swlpdxcx")
            #mo.goto('webview', src=params.path)
        else:
            mo.stat(params.appid)
            mo.gotoMiniProgram(params.appid,params.path)
    def ad_goto():
        pass



class webview(Page):
    def UI():
        WebView(name='webview')
    def onInit():
        page.webview.src = page.options.src


class payment(Page):
    def UI():
        Text(text='支付中')
    def onInit():
        mo.wxpay.pay('专业测试', float(page.options.price), onPaySuccessed, onPayFailed)

    def onPaySuccessed():
        md5_value = hashlib.md5()
        mystr = (page.options.order_id+str(page.options.price)+'mozigu')
        mo.console(mystr)
        md5_value.update(mystr.encode('utf8'))
        params = {
            "order_id": page.options.order_id, 
            "money": page.options.price, 
            "sign": md5_value.hexdigest(),
            "channel": "swlpdxcx"
        }
        mo.console(params)
        r = requests.post("https://xcx2-zxcs.lingji666.com/api/v1/pay/lpd/notify.json", data=params)
        ret = r.text
        #mo.console(ret)
        mo.redirectTo('webview',src='https://xcx2-zxcs.lingji666.com/orders/v2/payreturn?order_id='+page.options.order_id)

    def onPayFailed(user, app, page, mo):
        mo.goBack()
