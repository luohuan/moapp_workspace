
import requests
import hashlib
import json
dormitorydata=[
    
    {
        'id':1,
        'cover':'http://material.motimaster.com/harvey///2df5f1da858d6e6875bb0c3ab3c83d7f.jpeg',
        'title':'亲密测试',
        'people':'39.8万人在测',
        'details':'测测与老爸的亲密指数',
       # "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html?channel=swlpdxcx",
        "type":'homePage',
    },
    # {
    #     'id':0,
    #     'cover':'http://material.motimaster.com/harvey/5455/myrose/29c83079b0f9ffaa2b75c2ce0b90644d.png',
    #     'title':'八字合婚',
    #     'people':'429.533万人在测',
    #     'details':'夫妻情缘的深浅，看八字日柱便知...',
    #     "path":"https://xcx2-zxcs.lingji666.com/newhehun/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':1,
    #     'cover':'http://material.motimaster.com/harvey/5455/myrose/cdddb5693da5559e2d9964f494184b14.png',
    #     'title':'恋爱配对',
    #     'people':'824.23万人在测',
    #     'details':'十二星座配对幸福指数，看看你跟谁最配',
    #     "path":"https://xcx2-zxcs.lingji666.com/lianaipeidui/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':2,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/92920857d821b82764dd7d6b51fe2bcb.jpg',
    #     'title':'深度个人占星',
    #     'people':'19.8万人在测',
    #     'details':'个人星盘分析，透彻解读你的命运！',
    #     "path":"https://xcx2-zxcs.lingji666.com/gerenzhanxing/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':3,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/312e5c10b62539a3bd5f6f9237b3d5a0.jpg',
    #     'title':'2018狗年运程',
    #     'people':'46.03万人在测',
    #     'details':'2018狗年运程解析，助您催旺桃花姻缘...',
    #     "path":"https://xcx2-zxcs.lingji666.com/mllyuncheng/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':4,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/e490c2f427c3fe96f8644e48f14d6622.jpg',
    #     'title':'你有多好命？',
    #     'people':'47.02万人在测',
    #     'details':'分析命中富贵格局，解读今生吉凶祸福...',
    #     "path":"https://xcx2-zxcs.lingji666.com/liunianyuncheng/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':5,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/cbe9068f79faeff1a6ab40d5f1df682b.jpg',
    #     'title':'感情支招',
    #     'people':'27.44万人在测',
    #     'details':'八字姻缘解析，看你何时恋爱结婚？',
    #     "path":"https://xcx2-zxcs.lingji666.com/baziyinyuan/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':6,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/a4c6ebdb29a93a0c96a395e5420176fd.jpg',
    #     'title':'爱情塔罗牌',
    #     'people':'47.3万人在测',
    #     'details':'三张塔罗牌，解决你的爱情烦恼！',
    #     "path":"https://xcx2-zxcs.lingji666.com/forecasttaluobundle/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':6,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/4fba6a7a432b118a57e6e5d659c52738.jpg',
    #     'title':'你今生有着怎样的命运？',
    #     'people':'49.53万人在测',
    #     'details':'通晓八字，乐知天命，道尽你今生命中...',
    #     "path":"https://xcx2-zxcs.lingji666.com/forecastbazijingpibundle/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':7,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/e04ef01bcbbfe3e2ece047cdc7f3ffd5.jpg',
    #     'title':'前世今生',
    #     'people':'49.53万人在测',
    #     'details':'知晓前世姻缘，重结今生善果！',
    #     "path":"https://xcx2-zxcs.lingji666.com/forecastlunhuishubundle/index.html",
    #     "type":'protest',
    # },
    # {
    #     'id':8,
    #     'cover':'http://material.motimaster.com/linda123jiang/hi/main/69f671568b6f20fee220bffaab711c6b.jpg',
    #     'title':'前世姻缘',
    #     'people':'49.53万人在测',
    #     'details':'今生的相遇相知，是前世修来的何种缘...',
    #     "path":"https://xcx2-zxcs.lingji666.com/qianshiyinyuan/index.html",
    #     "type":'protest',
    # }
]

# 轮播图
topAdvertising = [ 
    # {   "id":1,
    #     "type": "wxf944c46118ad28a8", 
    #     "path": "pages/mainpage/mainpage",
    #     "src":"http://material.motimaster.com/yuyuan/Duudle/create/e3f467967b8c190befaf37862867c9c6.jpg"
    # },
    # {   "id":2,
    #     "type": "wx042aabd9b7e169a", 
    #     "path": "pages/first/first",
    #     "src":"http://material.motimaster.com/harvey/5455/myrose/9a61ab47bf701383989b815c27d9066e.jpg"
    # }
    ]


async def onReadyIndexPage(user,app,page,mo):
    if page.options.channel != None:
        user.channel = page.options.channel

    page.dormitorylist.data=dormitorydata
    page.imgUrls.data = topAdvertising
    #page.grid1.data = griditems
    page.swiperGuangGao.interval=3000
    page.swiperGuangGao.duration = 500
    page.swiperGuangGao.autoplay = True
    page.swiperGuangGao.indicatorDots=True
    page.swiperGuangGao.indicatorActiveColor ='#FF8C69'

async def onBannerTap(user, app, page, mo, params):
    mo.gotoMiniProgram(params.type, params.path)



async def getInputContent(user,app,page,mo):
    page.inputShow.text=page.myInput.value

async def toTest(user, app, page, mo, params):
    if params.type == 'protest':
        if user.channel != None:
            mo.goto('webview', src=params.path + "?channel=%s"%user.channel )
        else:
            mo.goto('webview', src=params.path + "?channel=swlpdxcx8")
    else:
        mo.goto(params.type)

async def webviewReady(user, app, page, mo):
    page.webview.src = page.options.src

async def paymentReady(user, app, page, mo):

    mo.wxpay.pay('专业测试',0.1, onPaySuccessed2, onPayFailed2)
async def onPaySuccessed2(user, app, page, mo):
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
async def onPayFailed2(user, app, page, mo):
    mo.goBack()