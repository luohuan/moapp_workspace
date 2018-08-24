def main():
    with MoApp(appid='wx2374ed010f4bd862', name='游戏盒子', navigationBarTitleText='游戏盒子', withLogin=True):
        MainPage()

class MainPage(Page):
    naviBarTitle='游戏盒子'
    naviBarColor='#0088de'
    naviBarStyle='white'
    background = '#0088de'
    enableShare=True

    def UI():
        with ScrollBox(size=[740, 1170], scrollY=True,position='relative'):
            with Box(size=[710,300],position='relative',background='white',borderRadius= '5px',marginLeft=20):
                with Swiper(id='swiper', size=[700,300],pos=[0,0],interval=2000,duration=500, autoplay=True):
                    with SwiperItem(id='imgUrls'):
                        Image(pos=[10,10, 720,280], borderRadius='5px', src = '{item.pic}',onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}'))
                pass
            with Grid(name='grid1', position='relative', size=[730, 720], column=2,marginTop=20,marginLeft=10):   
                with Box(size=[360,300],marginTop=20,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')):
                    with Box(pos=['center','center'],size=[350,340],background='white',borderRadius= '5px'):
                        Image(pos=['center',10],size=[330,240], borderRadius='5px', src = '{item.src}')     
                        Text(pos=[10, 260], text="{item.title}",fontSize=30,color='blue', textAlign='center')
                        Text(pos=[200, 270],text="{item.people}",fontSize=20,color='red', textAlign='center')
                        Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
                        Text(pos=[10, 300], text="{item.slogan}",fontSize=20,color='grey', textAlign='center') 

                    pass
            with Box(name='AD1', hidden=False, size=[700, 200], position='relative',background='white',marginLeft=20,marginTop=0,):
                AD(unitId='adunit-6f392758e231cb34')
            # with Grid(name='grid2', position='relative', width=730, column=2,marginTop=20,marginLeft=10):    
            #     with Box(size=[360,300],marginTop=40,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')): 
            #         with Box(pos=['center','center'],size=[350,340],background='white',marginTop=20,borderRadius= '5px'):  
            #             Image(pos=['center',10],size=[330,240], borderRadius='5px', src = '{item.cover}')     
            #             Text(pos=[10, 260], text="{item.title}",fontSize=30,color='blue', textAlign='center')
            #             Text(pos=[200, 270],text="{item.people}",fontSize=20,color='red', textAlign='center')
            #             Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
            #             Text(pos=[10, 300], text="{item.details}",fontSize=20,color='grey', textAlign='center')                    
           
            with Grid(name='grid3', position='relative', width=730, column=2,marginTop=10,marginLeft=10):   
                with Box(size=[360,320],marginTop=40,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')):  
                    with Box(pos=['center','center'],size=[350,340],background='white',borderRadius= '5px',):  
                        Image(pos=['center',10],size=[330,240], borderRadius='5px', src = '{item.cover}')     
                        Text(pos=[10, 260], text="{item.title}",fontSize=30,color='blue', textAlign='center')
                        Text(pos=[200, 270],text="{item.people}",fontSize=20,color='red', textAlign='center')
                        Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
                        Text(pos=[10, 300], text="{item.details}",fontSize=20,color='grey', textAlign='center')                     
                        pass
            with Box(name='AD3', hidden=False, size=[700, 240], position='relative',background='rgba(0,0,0,0)',marginLeft=20,marginTop=0,):
                pass

        with Image(pos=[630,850],size=[130, 60],src = 'http://material.motimaster.com/appmaker/goupeng/6756.png'):
            ShareButton(pos=[0,0],size=[130, 60],opacity=0)
        Image(pos=[100,-50],size=[130, 60],src = 'http://material.motimaster.com/appmaker/goupeng/6756.png')
        ContactButton(name='helpBtn',plain=True, border="None", pos=[600,100], size=[80, 80], background='http://material.motimaster.com/appmaker/zhaoyuanxue/2357.png')
        with Box(name='AD2', hidden=False, bottom=0,position='fixed',width=750,background='white'):
                AD(unitId='adunit-6f392758e231cb34',bottom=0)
    def gotoGame():
        mo.console("gotoGame")
        pass
    def gotoPocket():
        mo.console("gotoPocket")
        pass
    def go_to():
        if page.options.adtag:
            mo.stat('click_%s_%s'%(page.options.adtag,params.appid))
        
        mo.stat('click_all_%s'%(params.appid))
        if(params.appid == 'wx6acc1db2845590f6'):
            params.path = params.path + "?channel=swlpdxcx"
            param_m = parse.quote(params.path)
            mo.gotoMiniProgram(params.appid, 'pages/webview/webview?src='+ param_m )
        else:
            mo.gotoMiniProgram(params.appid,params.path)
    def onInit():
        page.share.title = "您的好友邀请您来玩"
        page.share.imageUrl = 'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=61f086829416fdfad86cc1e88cb4eb69/a08b87d6277f9e2fc11760a11630e924b899f37d.jpg'
        page.share.page = 'index'
        page.share.options = {'a':1,'b':user.opendid}
        page.grid1.data = griditems1
        # [
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     }
        # ]
        page.grid3.data = dormitorydata 
        # [
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     }
        # ]
        # page.grid3.data = [
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     },
        #     {
        #         'name':'打砖块王者',
        #         'src':'http://material.motimaster.com/appmaker/goupeng/4820.jpg',
        #         'count':68.7,
        #         'slogan':'最好玩的打砖块，球多到爆炸！'
        #     }
        # ]
        page.imgUrls.data = dataswiper1
        page.swiper.indicatorDots=True
        page.swiper.indicatorActiveColor ='#FF8C69'



dataswiper1=[
            {
                'id':3,
                'pic':'http://material.motimaster.com/shiyimin1534501968000/258321859288967773.gif',
                'title':'御天传奇',
                'people':'378.45万人在玩',
                'details':'腾讯正版授权游戏',
                'path':'?hdposition=20914',
                'appid':'wx895e6463811fd7ca',              
                'button_name':'可用',
                'type': 'picker'
           
            }]

griditems1 = [
    {
        'id':1,
        'src': 'http://material.motimaster.com/shiyimin1534153129000/xingzuoxiaowo.png',
        'people':'1200万人在测',
        'title': '星座小屋',
        'path':'pages/pageentrance/pageentrance',
        'appid':'wx01434b3ed0010d28',
        'slogan':'最好玩的打砖块，球多到爆炸！',
    },
   
    {
        'id':3,
        'src': 'http://material.motimaster.com/shiyimin1534153552000/huiyiqiang.png',
        'people':'30万人在测',
        'title': '好友回忆墙',
        'path':'pages/begin/begin',
        'appid':'wx468ad783f165eea0',
        'slogan':'最好玩的打砖块，球多到爆炸！'

    },
    {
        'id':4,
        'src': 'http://material.motimaster.com/shiyimin1534154048000/quce.png',
        'people':'87万人在测',
        'title': '趣测小窝',
        'path':'pages/mainPage/mainPage',
        'appid':'wx91f13354f5356b6c',
        'slogan':'最好玩的打砖块，球多到爆炸！'

    },
    {
        'id':5,
        'src':'http://material.motimaster.com/shiyimin1534500732000/小程序头像.png',
        'title':'平行世界',
        'people':'98万人在测',
        'path':'pages/page1/page1',
        'appid':'wx628e03240351132c',
        'slogan':'最好玩的打砖块，球多到爆炸！'
    },
    

]

dormitorydata=[

    {
        'id':7,
        'cover':'http://material.motimaster.com/shiyimin1534211266000/haoyouhuawo.jpg',
        'title':'好友画我',
        'people':'98.04万人在测',
        'details':'好友眼中的你是什么样子的？',
        'path':'pages/index/index',
        'appid':'wx02207e6022e44158',
        'button_name':'开玩'
    },



    {
        'id':6,
        'cover':'http://material.motimaster.com/shiyimin1534489600000/434059160321695634.png',
        'title':'御天传奇',
        'people':'378.45万人在玩',
        'details':'腾讯正版授权游戏，等你来玩!',
        'path':'?hdposition=20914',
        'appid':'wx895e6463811fd7ca',
        'button_name':'开玩'
    },

    {
        'id':1,
        'cover':'http://material.motimaster.com/jiangxiaoni1533089743000/6.jpg',
        'title':'看你怎么说',
        'people':'129.35万人在测',
        'details':'说说你对我的印象吧！',
        'path':'pages/page1/page1',
        'appid':'wxc1a59dd1befff332',
        'button_name':'开玩'
    },
    {
        'id':3,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/417a21294755bea737cefda07585213a.jpg',
        'title':'名字价值',
        'people':'89.08万人在测',
        'details':'测你名字都包含哪些特性？' ,
        'path':'pages/page9/page9',
        'appid':'wx9f918c171334a22a', 
        'button_name':'开玩'

    },

    {
        'id':9,
        'cover':'http://material.motimaster.com/jiangxiaoni1533094978000/123.jpg',
        'title':'八月关键词',
        'people':'21.09万人在测',
        'details':'愿你有人爱，有事做，也有所期待。',
        'path':'pages/page13/page13',
        'appid':'wx9f918c171334a22a', 
        'button_name':'开玩'

    },
    {
        'id':10,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/e04ef01bcbbfe3e2ece047cdc7f3ffd5.jpg',
        'title':'前世今生',
        'people':'49.53万人在测',
        'details':'知晓前世姻缘，重结今生善果！',
        "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
        'appid':'wx6acc1db2845590f6',
        'button_name':'测试'
    },
    {
        'id':11,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/a4c6ebdb29a93a0c96a395e5420176fd.jpg',
        'title':'爱情塔罗牌',
        'people':'47.3万人在测',
        'details':'三张塔罗牌，解决你的爱情烦恼！',
        "path":"https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html",
        "type":'protest',
        'appid':'wx6acc1db2845590f6',
        'button_name':'测试'
        
    },
    {
        'id':12,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/cbe9068f79faeff1a6ab40d5f1df682b.jpg',
        'title':'感情支招',
        'people':'27.44万人在测',
        'details':'八字姻缘解析，看你何时恋爱结婚？',
        "path":"https://xcx2-zxcs.lingji666.com/baziyinyuan/index.html",
        'appid':'wx6acc1db2845590f6',
        'button_name':'测试'
    },
    # {
    #     'id':13,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/92920857d821b82764dd7d6b51fe2bcb.jpg',
    #     'title':'深度个人占星',
    #     'people':'19.8万人在测',
    #     'details':'个人星盘分析，透彻解读你的命运！',
    #     "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
    #     'appid':'wx6acc1db2845590f6',
    #     'button_name':'测试'
        
    # },
]