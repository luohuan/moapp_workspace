def main():
    with MoApp(appid='wx267c13c76965a037', name='游戏盒子', navigationBarTitleText='游戏盒子', withLogin=True):
        MainPage()

class MainPage(Page):
    naviBarTitle='娱乐盒子'
    naviBarColor='#f2f2f2'
    naviBarStyle='black'
    background = '#f2f2f2'
    enableShare=True

    def UI():
        # with Swiper(id='swiper1',size=[750,310],interval=3000, duration=2000, autoplay=True) as a:
        #     a._add_attrs(['circular'])
        #     this.circular = True
        #     with SwiperItem(id ='dataswiper'):
                
        #         Image(pos=[20,0, 710, 300],borderRadius='10px', src ='{item.pic}',onTap = moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}'))# 
        #         Box(pos=[20,0],size=[710,310],color='#f1f5f8')


        with ScrollBox(size=[740, 1200], scrollY=True,position='relative'):
            with Box(size=[720,370],position='relative',borderRadius= '5px',marginLeft=20):
                Box(name='box',hidden=True,size=[720,300], position='relative', borderRadius= '5px',background='white')
                with Swiper(id='swiper', size=[710,300],pos=[0,0],interval=3000,duration=1000, autoplay=True)as a:
                    a._add_attrs(['circular'])
                    this.circular = True
                    with SwiperItem(id='imgUrls'):
                        Image(pos=[10,10, 700,280],borderRadius= '5px',src = '{item.pic}',onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}'))
                pass

                Text( id='recommend', pos=[20,310], fontWeight='450',fontSize=37)
                ContactButton(name='helpBtn',plain=True, border="None", pos=[640,310], hidden=True,size=[60, 60], background='http://material.motimaster.com/shiyimin1534742505000/contact1.png')
                
            with Grid(name='grid1', position='relative', size=[730, 950], column=2,marginTop=10,marginLeft=10):   
                with Box(size=[360,280],marginTop=10,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')):
                    with Box(pos=['center','center'],size=[350,300],background='white',borderRadius= '5px'):
                        Image(pos=['center',10],size=[330,200], borderRadius='5px', src = '{item.src}')     
                        Text(pos=[10, 220], text="{item.title}",fontSize=30,color='{item.text1_color}', textAlign='center')
                        Text(pos=[210, 230],text="{item.people}",fontSize=20,color='{item.text2_color}', textAlign='center')
                        # Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
                        Text(pos=[10, 260], text="{item.slogan}",fontSize=20,color='grey', textAlign='center') 

                    pass
            with Box(name='AD1', hidden=False, size=[700, 200], position='relative',marginLeft=20,marginTop=10,marginBottom=10):
                # AD(unitId='adunit-7232acaa49b50672')
                Image(id='ad',onTap=moui.request(ad_goto,name='ad'))
            # with Grid(name='grid2', position='relative', width=730, column=2,marginTop=20,marginLeft=10):    
            #     with Box(size=[360,300],marginTop=40,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')): 
            #         with Box(pos=['center','center'],size=[350,340],background='white',marginTop=20,borderRadius= '5px'):  
            #             Image(pos=['center',10],size=[330,240], borderRadius='5px', src = '{item.cover}')     
            #             Text(pos=[10, 260], text="{item.title}",fontSize=30,color='blue', textAlign='center')
            #             Text(pos=[200, 270],text="{item.people}",fontSize=20,color='red', textAlign='center')
            #             Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
            #             Text(pos=[10, 300], text="{item.details}",fontSize=20,color='grey', textAlign='center')                    
            with Box(name='morefun',size=[750,45],hidden=True,position='relative',marginLeft=10):
                Text(name='morefun2',fontWeight='450',fontSize=37,marginLeft=20)

            with Grid(name='grid3', position='relative', width=730, column=2,marginTop=0,marginLeft=0):   
                with Box(size=[360,280],marginTop=40,onTap=moui.request(go_to, path='{item.path}',appid='{item.appid}',title='{item.title}')):  
                    with Box(pos=['center','center'],size=[350,300],background='white',borderRadius= '5px',):  
                        Image(pos=['center',10],size=[330,200], borderRadius='5px', src = '{item.cover}')     
                        Text(pos=[10, 220], text="{item.title}",fontSize=30,color='{item.text3_color}', textAlign='center')
                        Text(pos=[210, 230],text="{item.people}",fontSize=20,color='{item.text4_color}', textAlign='center')
                        # Text(pos=[240, 270], text="万人在玩",fontSize=20,color='grey', textAlign='center')
                        Text(pos=[10, 260], text="{item.details}",fontSize=20,color='grey', textAlign='center')                     
                        pass
            with Box(name='AD3', hidden=False, size=[700, 200], position='relative',background='rgba(0,0,0,0)',marginLeft=20,marginTop=20,):
                pass



        # ContactButton(id='helpBtn',plain=True, border="None", hidden=True,pos=[660,330],size=[50, 50],background='http://material.motimaster.com/shiyimin1534742505000/contact1.png' )
        # with Image(pos=[630,850],size=[210, 70],src = 'http://material.motimaster.com/shiyimin1535340539000/share2.png'):
        #     ShareButton(pos=[0,0],size=[210,70],hidden=True,opacity=0)
        ShareButton(name='fenxiang',background='http://material.motimaster.com/shiyimin1535340539000/share2.png',hidden=True,size = [180,60],position = 'fixed',lineHeight = 90,fontSize = 35,fontWeight = '900',
               color = '#f7ca4e',border = 0,plain = True,effect=move(path=[(630,800), (580,800)], t=1.5, c=0,p=1))
        # Image(pos=[100,-50],size=[130, 60],src = 'http://material.motimaster.com/appmaker/goupeng/6756.png')
        # ContactButton(name='helpBtn',plain=True, border="None", pos=[660,330], size=[80, 80], background='http://material.motimaster.com/appmaker/zhaoyuanxue/2357.png')
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
        if(params.appid == 'wxf7c6308b0e199d50'):
            params.path = params.path + "?channel=swlpdxcx1"
            param_m = parse.quote(params.path)
            mo.gotoMiniProgram(params.appid, 'pages/webview/webview?src='+ param_m )
        else:
            mo.gotoMiniProgram(params.appid,params.path)
    def ad_goto(): 
        pass
    def onInit():
        page.fenxiang.hidden = False
        page.box.hidden = False
        page.helpBtn.hidden=False
        page.AD2.hidden = False
        page.AD1.hidden = True
        page.ad.size=[700,200]
        page.ad.src='http://material.motimaster.com/appmaker/goupeng/4820.jpg'
        page.morefun.hidden = False
        page.morefun2.text='更多精彩'
        page.morefun2.color='black'
        page.share.title = random.choice(['快看，我发现了什么！超嗨的游戏，越玩越上瘾！','@所有人，最火的小游戏全在这里了，错过别哭！','Skr! Skr! 这个盒子有点好玩，不点后悔！'])
        page.share.imageUrl = 'http://material.motimaster.com/shiyimin1534156084000/box.png'
        # page.share.page = 'index'
        # page.share.options = {'a':1,'b':user.opendid}
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
        page.recommend.text='热门推荐'             #这里控制‘热门’的文字
        page.recommend.color='d32f24'


dataswiper1=[
            {
                'id': 1,
                'pic':'http://material.motimaster.com/shiyimin1535447842000/qianshi1.jpg',
                'title':'前世今生',
                'people':'49.53万人在测',
                'details':'知晓前世姻缘，重结今生善果！',
                "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
                'appid':'wxf7c6308b0e199d50',
                'button_name':'测试',
                'type': 'picker'
            },

            # {
            #    'id':5,
            #    'pic':'http://material.motimaster.com/shiyimin1535084248000/封面2.gif',
            #    'title':'水波相册',
            #    'people':'245万人在测',
            #    'details':'让你的照片灵动起来！',
            #    'path':'pages/page_1/page_1',
            #    'appid':'wx3eff12058d4f74c6',
            #    'button_name':'开玩',
            #    'type': 'picker'
            # },
            {
                'id': 6,
                'pic':'http://material.motimaster.com/shiyimin1535443364000/peidui.jpg',
                'title':'恋爱配对',
                'people':'23.1万人在测',
                'details':'十二星座配对幸福指数，看看你跟谁最配!',
                "path":"https://xcx2-zxcs.lingji666.com/lianaipeidui/index.html",
                'appid':'wxf7c6308b0e199d50',
                'button_name':'测试',
                'type': 'picker'

           
            },
            {
                'id': 5,
                'pic':'http://material.motimaster.com/shiyimin1535443842000/bazi.jpg',
                'title':'八字合婚',
                'people':'39.8万人在测',
                'details':'夫妻情缘的深浅，看八字日柱便知！',
                "path":"https://xcx2-zxcs.lingji666.com/newhehun/index.html",
                'appid':'wxf7c6308b0e199d50',
                'button_name':'测试',
                'type': 'picker'

           
            },
            {
                'id': 2,
                'pic':'http://material.motimaster.com/shiyimin1535109449000/tlp.png',
                'title':'爱情塔罗牌',
                'people':'47.3万人在测',
                'details':'三张塔罗牌，解决你的爱情烦恼！',
                "path":"https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html",
                "type":'protest',
                'appid':'wxf7c6308b0e199d50',
                'button_name':'测试',
                'type': 'picker'                
            },
            # {
            #     'id': 3,
            #     'pic':'http://material.motimaster.com/shiyimin1535419191000/bazi.jpg',
            #     'title':'感情支招',
            #     'people':'27.44万人在测',
            #     'details':'八字姻缘解析，看你何时恋爱结婚？',
            #     "path":"https://xcx2-zxcs.lingji666.com/baziyinyuan/index.html",
            #     'appid':'wx6acc1db2845590f6',
            # #     'button_name':'测试',
            # #     'type': 'picker'
            # # },
            {
                'id': 4,
                'pic':'http://material.motimaster.com/shiyimin1535109463000/zx.png',
                'title':'深度个人占星',
                'people':'19.8万人在测',
                'details':'个人星盘分析，透彻解读你的命运！',
                "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
                'appid':'wxf7c6308b0e199d50',
                'button_name':'测试',
                'type': 'picker'

           
            }]

griditems1 = [

    {
        'id': 1,
        'src':'http://material.motimaster.com/shiyimin1535447842000/qianshi1.jpg',
        'title':'前世今生',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'people':'49.53万人在测',
        'slogan':'知晓前世姻缘，重结今生善果！',
        "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
        'appid':'wxf7c6308b0e199d50',

    },
   
    {
        'id':2,
        'src': 'http://material.motimaster.com/shiyimin1535366337000/xingyu2.jpg',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title': '流星之语',
        'people':'81万人在测',
        'slogan':'来这里，说出你平时不敢说的话吧！' ,
        'path':'pages/index/index',
        'appid':'wx1aa2b715d93c7058'

    },



    {
        'id':3,
        'src': 'http://material.motimaster.com/shiyimin1535366117000/xingming2.jpg',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title':'名字契合度',
        'people':'78万人在测',
        'slogan':'你们的名字有多匹配？',
        'path':'pages/entrance/entrance',
        'appid':'wx08fe2b1ff0c169f2'

    },
    {
        'id':4,
        'src':'http://material.motimaster.com/shiyimin1535366547000/fengmian2.gif',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title':'水波相册',
        'people':'245万人在测',
        'slogan':'让你的照片灵动起来！',
        'path':'pages/page_1/page_1',
        'appid':'wx3eff12058d4f74c6'
    },
    # {
    #     'id':5,
    #     'src': 'http://material.motimaster.com/shiyimin1535370848000/pingxing.jpg',
    #     'title':'平行世界',
    #     'people':'98万人在测',
    #     'path':'pages/page1/page1',
    #     'appid':'wx628e03240351132c',
    #     'slogan':'平行世界里，你会遇到哪些缘分？',
    #     'text1_color':'#010101',
    #     'text2_color':'#ee5b60'
    # },   

    # {
    #     'id':6,
    #     'src': 'http://material.motimaster.com/shiyimin1535368458000/kanni.jpg',
    #     'title':'看你怎么说',
    #     'people':'129万人在测',
    #     'slogan':'说说你对我的印象吧！',
    #     'path':'pages/page1/page1',
    #     'appid':'wxc1a59dd1befff332',
    #     'text1_color':'#010101',
    #     'text2_color':'#ee5b60'
    # },
    {
        'id':6,
        'src':'http://material.motimaster.com/shiyimin1535365590000/xingzuo2.jpg',
        'slogan':'你们的星座有多搭？' ,
        'people':'1200万人在测',
        'title': '星座小屋',
        'path':'pages/pageentrance/pageentrance',
        'appid':'wx01434b3ed0010d28',
        'text3_color':'#010101',
        'text4_color':'#ee5b60'
    },
    {
        'id':7,
        'src':'http://material.motimaster.com/shiyimin1535367977000/xingge.jpg',
        'title':'三系性格属性',
        'people':'21万人在测',
        'slogan':'你的佛系、道系和儒系性格比例是多少？',
        'path':'pages/page17/page17',
        'appid':'wx9f918c171334a22a', 
        'text1_color':'#010101',
        'text2_color':'#ee5b60'
    }    

]

dormitorydata=[

    # {
    #     'id':7,
    #     'cover':'http://material.motimaster.com/shiyimin1534211266000/haoyouhuawo.jpg',
    #     'title':'好友画我',
    #     'people':'98.04万人在测',
    #     'details':'好友眼中的你是什么样子的？',
    #     # 'path':'pages/index/index',
    #     # 'appid':'wx02207e6022e44158',
    #     'button_name':'开玩'
    # },

    # {
    #     'id':4,
    #     'cover':'http://material.motimaster.com/shiyimin1535084248000/封面2.gif',
    #     'title':'水波相册',
    #     'people':'245.57万人在测',
    #     'details':'让你的照片灵动起来！',
    #     # 'path':'pages/page_1/page_1',
    #     # 'appid':'wx3eff12058d4f74c6',
    #     'button_name':'开玩'
    # },
    {
        'id':2,
        'cover':'http://material.motimaster.com/shiyimin1535369612000/huiyi.jpg',
        'details':'那些年，我们的回忆',
        'people':'30万人在测',
        'title': '好友回忆墙',
        'path':'pages/begin/begin',
        'appid':'wx468ad783f165eea0',
        'text3_color':'#010101',
        'text4_color':'#ee5b60'


    },

    # {
    #     'id':6,
    #     'cover':'http://material.motimaster.com/shiyimin1535365590000/xingzuo2.jpg',
    #     'details':'你们的星座有多搭？' ,
    #     'people':'1200万人在测',
    #     'title': '星座小屋',
    #     'path':'pages/pageentrance/pageentrance',
    #     'appid':'wx01434b3ed0010d28',
    #     'text3_color':'#010101',
    #     'text4_color':'#ee5b60'
    # },
    {
        'id':6,
        'cover': 'http://material.motimaster.com/shiyimin1535368458000/kanni.jpg',
        'title':'看你怎么说',
        'people':'129万人在测',
        'details':'说说你对我的印象吧！',
        'path':'pages/page1/page1',
        'appid':'wxc1a59dd1befff332',
        'text3_color':'#010101',
        'text4_color':'#ee5b60'
    },
    # {
    #     'id':6,
    #     'cover':'http://material.motimaster.com/shiyimin1534489600000/434059160321695634.png',
    #     'title':'御天传奇',
    #     'people':'378.45万人在玩',
    #     'details':'腾讯正版授权游戏，等你来玩!',
    #     'path':'?hdposition=20914',
    #     'appid':'wx895e6463811fd7ca',
    #     'button_name':'开玩'
    # },

    # {
    #     'id':1,
    #     'cover':'http://material.motimaster.com/jiangxiaoni1533089743000/6.jpg',
    #     'title':'看你怎么说',
    #     'people':'129.35万人在测',
    #     'details':'说说你对我的印象吧！',
    #     # 'path':'pages/page1/page1',
    #     # 'appid':'wxc1a59dd1befff332',
    #     'button_name':'开玩'
    # },
    # {
    #     'id':3,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/417a21294755bea737cefda07585213a.jpg',
    #     'title':'名字价值',
    #     'people':'89.08万人在测',
    #     'details':'测你名字都包含哪些特性？' ,
    #     # 'path':'pages/page9/page9',
    #     # 'appid':'wx9f918c171334a22a', 
    #     'button_name':'开玩'

    # },

    # {
    #     'id':9,
    #     'cover':'http://material.motimaster.com/jiangxiaoni1533094978000/123.jpg',
    #     'title':'八月关键词',
    #     'people':'21.09万人在测',
    #     'details':'愿你有人爱，有事做，也有所期待。',
    #     # 'path':'pages/page13/page13',
    #     # 'appid':'wx9f918c171334a22a', 
    #     'button_name':'开玩'

    # },
    # {
    #     'id':7,
    #     'cover':'http://material.motimaster.com/shiyimin1534736235000/740930247887016559.jpg',
    #     'title':'三系性格属性',
    #     'people':'21.09万人在测',
    #     'details':'你的佛系、道系和儒系性格比例是多少？',
    #     # 'path':'pages/page17/page17',
    #     # 'appid':'wx9f918c171334a22a', 

    #     'button_name':'开玩'

    # }
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