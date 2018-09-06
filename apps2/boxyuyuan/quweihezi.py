def main():
    with MoApp(appid='wx3d29f3f59fee8a87', name='趣玩盒子', navigationBarTitleText='趣玩盒子', withLogin=True):
        MainPage()


LING_APPID = 'wx9066c083d563977e'
class MainPage(Page):
    naviBarTitle='趣玩盒子'
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
        with Box(name='AD2', hidden=False, size=[750, 200],bottom=0,position='fixed',background='white'):
                AD(unitId='adunit-e8887b2fdfd4c695',bottom=0)
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
        if(params.appid == LING_APPID):
            params.path = params.path + "?channel=swlpdxcx6"
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
        #page.AD2.hidden = False
        page.AD1.hidden = True
        page.ad.size=[700,200]
        page.ad.src='http://material.motimaster.com/appmaker/goupeng/4820.jpg'
        page.morefun.hidden = False
        #page.morefun2.text='更多精彩'
        #page.morefun2.color='black'
        page.share.title = random.choice(['快看，我发现了什么！超嗨的游戏，越玩越上瘾！','@所有人，最火的小游戏全在这里了，错过别哭！','Skr! Skr! 这个盒子有点好玩，不点后悔！'])
        page.share.imageUrl = 'http://material.motimaster.com/shiyimin1534156084000/box.png'
        # page.share.page = 'index'
        # page.share.options = {'a':1,'b':user.opendid}
        page.grid1.data = griditems1
        page.imgUrls.data = dataswiper1
        page.swiper.indicatorDots=True
        page.swiper.indicatorActiveColor ='#FF8C69'
        page.recommend.text='热门推荐'             #这里控制‘热门’的文字
        page.recommend.color='d32f24'

dataswiper1=[
            {
                'id': 1,
                'pic':'http://material.motimaster.com/shiyimin1535447842000/qianshi1.jpg',
                'title':'前世姻缘',
                'people':'89.53万人在测',
                'details':'知晓前世姻缘，重结今生善果！',
                "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
                'appid':LING_APPID,
                'button_name':'测试',
                'type': 'picker'
            },
            {
                'id': 6,
                'pic':'http://material.motimaster.com/shiyimin1535443364000/peidui.jpg',
                'title':'恋爱配对',
                'people':'123.1万人在测',
                'details':'TA是你的真爱吗？你和TA会有结果吗？',
                "path":"https://xcx2-zxcs.lingji666.com/lianaipeidui/index.html",
                'appid':LING_APPID,
                'button_name':'测试',
                'type': 'picker'
            },
            {
                'id': 5,
                'pic':'http://material.motimaster.com/shiyimin1535443842000/bazi.jpg',
                'title':'八字合婚',
                'people':'109.8万人在测',
                'details':'夫妻情缘的深浅，看八字日柱便知！',
                "path":"https://xcx2-zxcs.lingji666.com/newhehun/index.html",
                'appid':LING_APPID,
                'button_name':'测试',
                'type': 'picker'
            },
            {
                'id': 2,
                'pic':'http://material.motimaster.com/shiyimin1535109449000/tlp.png',
                'title':'爱情塔罗牌',
                'people':'97.3万人在测',
                'details':'三张塔罗牌，解决你的爱情烦恼！',
                "path":"https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html",
                "type":'protest',
                'appid':LING_APPID,
                'button_name':'测试',
                'type': 'picker'                
            },
            {
                'id': 4,
                'pic':'http://material.motimaster.com/shiyimin1535109463000/zx.png',
                'title':'深度个人占星',
                'people':'19.8万人在测',
                'details':'个人星盘分析，透彻解读你的命运！',
                "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
                'appid':LING_APPID,
                'button_name':'测试',
                'type': 'picker'
            },
            # {
            #     'id':4,
            #     'pic': 'http://material.motimaster.com/liuhongjie1535641808000/默契.png',
            #     'title': '好友默契挑战',
            #     'people':'101万人在玩',
            #     'slogan':'看看谁是你最默契的好友！' ,
            #     'path':'pages/mainpage/mainpage',
            #     'appid':'wx18610e0755615e2f'

            # },

            ]

griditems1 = [
    {
        'id': 1,
        'src':'http://material.motimaster.com/liuhongjie1535681138000/恋爱配对.png',
        'title':'恋爱配对',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'people':'183.1万人在测',
        'slogan':'TA会喜欢你吗？你和TA会有结果吗？',
        "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
        'appid':LING_APPID,

    },
    {
        'id': 2,
        'src':'http://material.motimaster.com/liuhongjie1535645788000/运势.png',
        'title':'个人运势',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'people':'246万人在测',
        'slogan':'事业爱情健康，为你全面解析2018运程！',
        "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
        'appid':LING_APPID,

    },
    {
        'id':3,
        'src':'http://material.motimaster.com/liuhongjie1535643898000/前世姻缘.png',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title':'前世姻缘',
        'slogan':'揭秘前尘往事，缔结今生情缘。' ,
        'people':'149万人在测',
        'path':'https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html',
        'appid':LING_APPID,

    },
    {
        'id':4,
        'src': 'http://material.motimaster.com/liuhongjie1535641808000/默契.png',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title': '好友默契挑战',
        'people':'131万人在玩',
        'slogan':'看看谁是你最默契的好友！' ,
        'path':'pages/mainpage/mainpage',
        'appid':'wx18610e0755615e2f'

    },
    {
        'id':5,
        'src': 'http://material.motimaster.com/liuhongjie1535626541000/1.png',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title':'好友回忆墙',
        'people':'198万人在玩',
        'slogan':'收集一波与好友的回忆吧！',
        'path':'pages/begin/begin',
        'appid':'wxaa8fe119f5c62d23'

    },
    {
        'id':6,
        'src':'http://material.motimaster.com/liuhongjie1535626508000/3.png',
        'text1_color':'#010101',
        'text2_color':'#ee5b60',
        'title':'看动图猜影视',
        'people':'185万人在玩',
        'slogan':'阅片老司机来战，看看你闯到第几关！',
        'path':'pages/mainPage/mainPage',
        'appid':'wx91f13354f5356b6c'
    },

]

# dormitorydata=[
#     {
#         'id':2,
#         'cover':'http://material.motimaster.com/shiyimin1535369612000/huiyi.jpg',
#         'details':'那些年，我们的回忆',
#         'people':'30万人在测',
#         'title': '好友回忆墙',
#         'path':'pages/begin/begin',
#         'appid':'wx468ad783f165eea0',
#         'text3_color':'#010101',
#         'text4_color':'#ee5b60'


#     },
#     {
#         'id':6,
#         'cover': 'http://material.motimaster.com/shiyimin1535368458000/kanni.jpg',
#         'title':'看你怎么说',
#         'people':'129万人在测',
#         'details':'说说你对我的印象吧！',
#         'path':'pages/page1/page1',
#         'appid':'wxc1a59dd1befff332',
#         'text3_color':'#010101',
#         'text4_color':'#ee5b60'
#     },

# ]