from yinxiangfazhan import *
from xiaoshirenge import *
from urllib import parse
PROTESR_APPID = 'wxf7c6308b0e199d50'

dormitorydata=[
    {
        'id':1,
        'cover':'http://material.motimaster.com/chenwei1535363514000/suoluetu.jpg',
        'bigsrc': 'http://material.motimaster.com/chenwei1535535879000/小程序轮播图封面1_自定义px_2018.08.29.jpg',
        'title':'好友印象发展',
        'people':'129.5万人在测',
        'details':'测朋友们对你的真实了解程度',
        'url':'page6',
        'type':['全部','性格']
    },
    {
        'id':2,
        'cover':'http://material.motimaster.com/chenwei1535530034000/tim.jpg',
        'bigsrc': 'http://material.motimaster.com/chenwei1535532396000/223242px_2018.08.29.jpg',
        'title':'24小时人格',
        'people':'89万人在测',
        'details':'测你24小时中不同的真实人格',
        'url':'page9',
        'type':['全部','性格']
    }
]

dormitorydata2=[
    {
        'id':1,
        'cover':'http://material.motimaster.com/chenwei1535363514000/suoluetu.jpg',
        'bigsrc': 'http://material.motimaster.com/chenwei1535535879000/小程序轮播图封面1_自定义px_2018.08.29.jpg',
        'title':'好友印象发展',
        'people':'129.5万人在测',
        'details':'测朋友们对你的真实了解程度',
        'url':'page6',
        'type':['全部','性格'],
        'appid':'',
        'path':'',
    },
    {
        'id':2,
        'cover':'http://material.motimaster.com/chenwei1535530034000/tim.jpg',
        'bigsrc': 'http://material.motimaster.com/chenwei1535532396000/223242px_2018.08.29.jpg',
        'title':'24小时人格',
        'people':'89万人在测',
        'details':'测你24小时中不同的真实人格',
        'url':'page9',
        'type':['全部','性格'],
        'appid':'',
        'path':'',
    },
    {
        'id':3,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/92920857d821b82764dd7d6b51fe2bcb.jpg',
        'title':'深度个人占星',
        'people':'19.8万人在测',
        'details':'个人星盘分析，透彻解读你的命运！',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html',
    },
    {
        'id':4,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/312e5c10b62539a3bd5f6f9237b3d5a0.jpg',
        'title':'2018狗年运程',
        'people':'46.03万人在测',
        'details':'2018狗年运程解析，助您催旺桃花姻缘...',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/mllyuncheng/index.html'


    },
    {
        'id':5,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/e490c2f427c3fe96f8644e48f14d6622.jpg',
        'title':'你有多好命？',
        'people':'47.02万人在测',
        'details':'分析命中富贵格局，解读今生吉凶祸福...',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/liunianyuncheng/index.html'
    },
    {
        'id':6,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/cbe9068f79faeff1a6ab40d5f1df682b.jpg',
        'title':'感情支招',
        'people':'27.44万人在测',
        'details':'八字姻缘解析，看你何时恋爱结婚？',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/baziyinyuan/index.html'
    },
    {
        'id':7,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/a4c6ebdb29a93a0c96a395e5420176fd.jpg',
        'title':'爱情塔罗牌',
        'people':'47.3万人在测',
        'details':'三张塔罗牌，解决你的爱情烦恼！',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html'
    },
    {
        'id':8,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/4fba6a7a432b118a57e6e5d659c52738.jpg',
        'title':'你今生有着怎样的命运？',
        'people':'49.53万人在测',
        'details':'通晓八字，乐知天命，道尽你今生命中...',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/forecastbazijingpibundle/index.html'
    },
    {
        'id':9,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/e04ef01bcbbfe3e2ece047cdc7f3ffd5.jpg',
        'title':'前世今生',
        'people':'49.53万人在测',
        'details':'知晓前世姻缘，重结今生善果！',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html'
    },
    {
        'id':10,
        'cover':'http://material.motimaster.com/linda123jiang/hi/main/69f671568b6f20fee220bffaab711c6b.jpg',
        'title':'前世姻缘',
        'people':'49.53万人在测',
        'details':'今生的相遇相知，是前世修来的何种缘...',
        'type': 'protest',
        'appid':PROTESR_APPID,
        'path': 'https://xcx2-zxcs.lingji666.com/qianshiyinyuan/index.html'
    }
]
        
       
def main():
    with MoApp(appid='',name='万事屋'):
        firstpage()
        yinxiangfazhan()
        xiaoshirenge()
        

class firstpage(Page):
    #background='http://material.motimaster.com/chenwei1535442280000/392c2c7fd3564ee24b14d7f232219d8d.jpg'
    """docstring for gridPage"""
    def UI():
        Box(size=[750,1],borderTop='6px solid #ecf0f3',pos=[0,0])  #横线
        #Image(pos=[0,0],size=[750,439],src='http://material.motimaster.com/chenwei1535437126000/副本_未命名_自定义px_2018.08.28.jpg')
        with Swiper(id='swiper1', size=[750,300], pos=[0,15,750,300], top=0,interval=3000,duration=500, autoplay=True, indicatorDots=True,indicatorActiveColor ='#FF8C69'):
            with SwiperItem(id ='dormitorydata'):
                with Image(pos=[0,0,750,300], src ='{item.bigsrc}'):
                    this.onTap = moui.goto('{item.url}', name='{item.name}')                  
       
        #分类
        #Text( pos=[20,449], text='分类',fontWeight='lighter',fontSize=34)
        #Box(size=[750,1],borderBottom='1px solid #ecf0f3',pos=[0,500])  #横线

       
        Box(size=[750,1],borderBottom='6px solid #ecf0f3',pos=[0,308])  #横线

        #Button(pos=[0,0],size=[750,439],plain=True,background='rgba(0,0,0,0)',border='3px solid red',onTap= moui.goto('page6'))
        Text( pos=[20,340], text='全部测试',fontWeight='lighter',fontSize=30)
        Box(size=[750,1],borderBottom='1px solid #ecf0f3',pos=[0,390])  #横线
        
        #测试列表展示
        #with Box(pos=[0,0],width=750,background='#222222'):   
        with List(name='dormitorylist',pos=[0,400]):
            with Box(pos=[0,0],size=[750,180],borderRadius='0px',background='white',
                borderBottom= '1px solid #ecf0f3',marginBottom=15,onTap=moui.request(go_mini, type='{item.type}', url='{item.url}', appid='{item.appid}', path='{item.path}')):
                #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
                Image(left=20,size=[150, 150], src='{item.cover}' , mode='aspectFill',borderRadius= '10px')
                Text(pos=[190,0],text='{item.title}',color='#353535',fontSize=33)
                Text(pos=[190,55],text='{item.people}',color='#808080',fontSize=28)
                Text(pos=[190,110],text='{item.details}',fontSize=30,color='#808080')
                Button(pos=[590,20],text='去测>',size=[100,50],lineHeight=50,fontSize=25,
                    color='#FF0000',background='#ffffff',border='1px solid red')
                Button(pos=[20,0],size=[710,200],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo')
    
        #顶部的轮播按钮图
        #Button(pos=[0,0],size=[750,439],plain=True,background='rgba(0,0,0,0)',border='0px solid red',openType='getUserInfo',onTap= moui.goto('page6'))
        
        #with Box(pos=[20,449],width=750,height=330):
        #    Button(name='quanbu',text='全部',pos=[20,90],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#f14203',openType='getUserInfo',onTap= moui.request(checkType,leixing='全部'))
        #    Button(name='qinggan',text='爱情',pos=[190,90],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#7d26cb',openType='getUserInfo',onTap= moui.request(checkType,leixing='爱情'))
        #    Button(name='xingge',text='性格',pos=[360,90],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#ff8151',openType='getUserInfo',onTap= moui.request(checkType,leixing='性格'))
        #    Button(name='zhishang',text='生肖',pos=[530,90],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#85cef7',openType='getUserInfo',onTap= moui.request(checkType,leixing='生肖'))
        #    Button(name='yingshi',text='影视',pos=[20,200],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#3bb26e',openType='getUserInfo',onTap= moui.request(checkType,leixing='影视'))
        #    Button(name='xingzhuo',text='星座',pos=[190,200],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#cf337a',openType='getUserInfo',onTap= moui.request(checkType,leixing='星座'))
        #    Button(name='egao',text='恶搞',pos=[360,200],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#f18180',openType='getUserInfo',onTap= moui.request(checkType,leixing='恶搞'))
        #    Button(name='qita',text='其他',pos=[530,200],size=[150,80],fontSize=33,color='#ffffff',lineHeight=80,background='#ff6b69',openType='getUserInfo',onTap= moui.request(checkType,leixing='其他'))


    #获取列表信息
    def onInit():   
        page.dormitorydata.data = dormitorydata
        page.dormitorylist.data = dormitorydata2

    #    page.imgUrls2.data = [
    #        'http://material.motimaster.com/jiangxiaoni1533094082000/bg2.jpg',
    #        'http://material.motimaster.com/jiangxiaoni1533094082000/bg2.jpg',
    #        'http://material.motimaster.com/jiangxiaoni1533094082000/bg2.jpg'
     #       ]

        #page.swiper.interval= 1000
        #page.swiper.duration = 500
        #page.swiper.autoplay = True
        #page.swiper.indicatorDots=True
        #page.swiper.indicatorActiveColor ='#FF8C69'

    #跳转逻辑
    def go_mini():
        if params.type == 'protest':
            params.path = params.path + "?channel=swlpdxcx3"
            param_m = parse.quote(params.path)
            mo.gotoMiniProgram(params.appid, 'pages/webview/webview?src='+ param_m )
        else:
            mo.goto(params.url)


    def checkType():
        mo.console('aaaaaaaaaaaaaaaaaaa')
        list_jump = []
        for item in dormitorydata:
            if params.leixing in item['type']:
                list_jump.append(item)
        page.dormitorylist.data = list_jump















         


