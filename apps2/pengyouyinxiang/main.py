import time
import random
import uuid
from im_operator import imOperator
from global_data import AVATAR_URL
from global_data import IS_AUDIT_VERSION

# 看一条答案支付的价格
PAY_ONE_PRICE = 4.99
# 看所有答案支付的价格
PAY_ALL_PRICE = 9.99

# TestUser ={
#     'nickname': '机器人4301',
#     'share': '/pages/indexPage/indexPage?__token__=5b978066393e347a9c77f0e7&_openid=oeGwh0TSlpiyDkJK-5QhTDtv8Wgc'
# }

# 答题的标签文本
selectedTags = [
    {
        'text1':'地主家的傻儿子',
        'text2':'当然选择原谅你啦',
        'text3':'美颜盛世',
        'text4':'烂梗の王'
    },
    {
        'text1':'生活永远粉红色',
        'text2':'曾经小清新，现在重口味',
        'text3':'没有一天不花痴',
        'text4':'口亨，幼稚鬼'
    },
    {
        'text1':'外表想不到的毒舌',
        'text2':'从未见过如此厚颜无耻之人',
        'text3':'卖萌10级学者',
        'text4':'太粗枝大叶了吧'
    },
    {
        'text1':'除了可爱没优点',
        'text2':'呆若木鸡的理科生物',
        'text3':'腹黑程度报表',
        'text4':'充满恋爱的酸臭气'
    },
    {
        'text1':'骨灰级腐女',
        'text2':'硬盘里的私货总比别人多',
        'text3':'中央空调',
        'text4':'外壳坚硬内里柔软'
    }
]
inputtags = [
    'text1=#说说你眼中的我#'
    'text2=#我在你眼里变样了吗#'
    'text3=#吐槽一下'
    'text4=#悄悄表个白吧#'
]

def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='印象弹幕', naviBarColor='black', naviBarStyle='white'):
        indexPage()
        sharePage()

class indexPage(Page):
    disableScroll = True #页面整体不能上下滚动
    enableShare = True # 该页面可以分享
    background = '#000000'

    def UI():
        # 页面背景图
        Image(name='img', pos=[0, 0], size=[750, 1300], src='http://material.motimaster.com/suyu1536458821000/星空2.png')
        # 主态进入显示的内容
        with Box(name='host_box', pos=[0, 0], size=['100%', '100%']):
            # 找好友作答按钮
            Button(name='go_share_btn', hidden=False, pos=['center', 800],fontSize=32, lineHeight=90,
                   size=[402, 90], background = 'http://material.motimaster.com/suyu1536632002000/开启我的印象弹幕.png',
                   onTap=[moui.showLoading('请稍微等一下下...'), gotoSharePage, moui.hideLoading()], borderRadius=38,
                   openType='getUserInfo')
            # 没有好友留言显示的内容
            with Box(name='no_result_box', pos = [0, 0], width=750):
                ImageAvatar(pos=['center', 60], size=[160, 160], borderRadius='50%')
                TextNickName(pos=['center', 220], textAlign='center', color='white', fontWeight=500, fontSize=40)
                Image(pos=['center', 400], size=[600, 300], effect=pulse(t=2,c=0),src='http://material.motimaster.com/suyu1536406716000/朋友心中会怎样.png')
                with Box(name='text_shareGuide', pos=[150, 800],background = 'rgba(255, 255, 255,0.3)', size=[450, 100], borderRadius=10, hidden = True):
                    Text(pos=[0, 10], text='暂时还没有人作答哦 ，点下面的按钮，分享给朋友吧', fontSize=30, color='white', size = [450, 100], lineHeight=40,padding=10,
                        textAlign='left')
            # 有好友留言显示的内容
            with Box(name='result_box', pos=[0, 0], width=750, hidden=True):
                # 头像和文字
                with Box(name='result_box', pos=[0, 0], width=750):
                    ImageAvatar(pos=['center', 60], size=[160, 160], borderRadius='50%')
                    TextNickName(pos=['center', 220], textAlign='center', color='white', fontWeight=500, fontSize=40)
                    Image(pos=['center', 300], size=[600, 180],effect=pulse(t=1,c=0),src='http://material.motimaster.com/suyu1536632464000/说说你对我的印象.png')
                # 留言的内容
                with ScrollBox(name='resultText', hidden=True, pos=['center', 400], size=[724, 620], scrollY=True):
                    with Grid(name='result_text_list', pos=['center', 0], width=724, column=1):
                        # grid控件兼容全面屏手机的写法，加一层下面这样的box 子box 必须设置 position='relative'
                        with Box(width='100%', display='flex', justifyContent='center'):
                            with Box(size=[600, 120], borderRadius=0, marginBottom=30, position='relative',
                                     background='http://material.motimaster.com/suyu1536544156000/流星2.png',effect=shake(t=10,c=0),onTap=moui.request(onShowMask, item_id='{item.id}', item_text='{item.text}')):
                                Image(src='{item.url}', pos=[20, 34], size=[50, 50], borderRadius='50%')
                                with Box(pos=[90, 0], size=[500, 120]):
                                    Text(pos=[30,40],position='relative', text='{item.text}', fontSize=32, textAlign='left',color='white')
                                    with Box(position='relative',display='inline',size=[90,120]):
                                        Image(size=[60, 60],pos=[50,30],src='http://material.motimaster.com/suyu1536647462000/xingxing.png')

                with Box(pos=['center', 300], hidden=False,size=[724, 620]):
                    Barrage(name='danmu',fontSize=32, itemtap=barrageItemTap,avatarStyle='width:50rpx;height:50rpx;left:0;',lineHeight=120, height=120,
                        margin=20,rowNumber=4,danmuTailImage='http://material.motimaster.com/suyu1536647462000/xingxing.png')
            # 邀请好友回答按钮
            Button(name='btn_result_box', hidden=True, pos=['center', 'bottom'],background='http://material.motimaster.com/suyu1536631146000/邀请好友继续填充233.png',size=[750, 100],
                   onTap=[moui.showLoading('请稍微等一下...'), gotoSharePage, moui.hideLoading()])

        # 从客态进入页面显示的内容
        with Box(name='guest_box', pos=[0, 0], width=750, height='100%', hidden=True):
            # 头像和文字
            with Box(name='avatar_box', pos=[0, 0], width=750):
                with Box(name='avatar_box', pos=[0, 0], width=750):
                    Image(name='host_avatar', pos=['center', 60], size=[160, 160], borderRadius='50%')
                    Image(pos=['center', 400], size=[600,180],src='http://material.motimaster.com/suyu1536632464000/说说你对我的印象.png',effect=pulse(t=1,c=0))

            # 别人或者自己匿名给好友的留言内容
            with Box(name='showText', pos=['center', 160], size=[724, 630]):
                Text(name='empty', pos=['center', 400], size=[280, 100], fontSize=30, text='其他人还没有回答哦 你来做第一个吧',color='white',
                     hidden=False, textAlign='center')
                with ScrollBox(name='im_list', pos=['center', 40], size=[724, 630], scrollY=True, hidden=True):
                    with Grid(name='showboxes', pos=['center', 0], width=724, column=1):
                         # grid控件兼容全面屏手机的写法，加一层下面这样的box 子box 必须设置 position='relative'
                        with Box(width='100%', display='flex', justifyContent='center'):
                            with Box(size=[600, 120], borderRadius=0, marginBottom=30, position='relative',effect=shake(t=10,c=0),
                                      background='http://material.motimaster.com/suyu1536544156000/流星2.png'):
                                Image(src='{item.url}', pos=[20, 24], size=[50, 50], borderRadius='50%')
                                with Box(pos=[90, 0], size=[500, 120]):
                                    Text(pos=[30,20], position='relative', text='{item.text}', fontSize=32,
                                          textAlign='left', color='white')
                                    with Box(position='relative', display='inline', size=[90, 120]):
                                        Image(size=[60, 60], pos=[50, 30],
                                               src='http://material.motimaster.com/suyu1536647462000/xingxing.png')
                with Box(pos=['center', -50], hidden=False,size=[724, 620]):
                    Barrage(name='danmu',fontSize=32, itemtap=barrageItemTap,avatarStyle='width:50rpx;height:50rpx;left:0;top:30rpx',lineHeight=120, height=120,
                        margin=20,rowNumber=4,danmuTailImage='http://material.motimaster.com/suyu1536647462000/xingxing.png',danmuTailImageStyle='width:60rpx;height:60rpx;right:0;top:30rpx')
            # 输入区域 和 标签显示区域
            with Box(name='input_box', pos=[20, 850], size=[700, 240]):
                # 输入框
                Input(pos=[20, 0], size=[529, 50], name='input2', placeholder='请选择或在这里输入你的答案',color='white',fontsize=30,
                     borderBottom='1px solid white')
                  # 确定按钮
                Button(name='btn_ok', pos=[600, 0], size=[120, 50], background='#ec866e', borderRadius=10,
                     border='1px solid #00000', text='发射💗', textAlign='center', fontSize=30, lineHeight=50, openType='getUserInfo',
                     onTap=onAnswerSubmit)
                 # 标签显示

                with Box(pos=[20, 70], size=[530, 160]):
                     # 短标签
                    Text(name='selected_text1', pos=[0, 0], size=[296, 60], fontSize=26,color='white',
                         textAlign='center', lineHeight=60, borderRadius=10, border='1px dashed white',
                         onTap=moui.request(onSelectTag, select_id='text1'))
                     # 长标签

                    Text(name='selected_text2', pos=[320, 0], size=[330, 60], fontSize=26,color='white',
                         textAlign='center', lineHeight=60, borderRadius=10, border='1px dashed white',
                         onTap=moui.request(onSelectTag, select_id='text2'))
                     # 短标签
                    Text(name='selected_text3', pos=[0, 80], size=[220, 60], fontSize=26,color='white',
                         textAlign='center', lineHeight=60, borderRadius=10, border='1px dashed white',
                         onTap=moui.request(onSelectTag, select_id='text3'))
                     # 长标签
                    Text(name='selected_text4', pos=[244, 80], size=[280, 60], fontSize=26, color='white',
                          textAlign='center', lineHeight=60, borderRadius=10, border='1px dashed white',
                          onTap=moui.request(onSelectTag, select_id='text4'))
                 # 换一换按钮
                Button(name='btn_change', pos=[650, 150], size=[50, 50], background='http://material.motimaster.com/suyu1536410649000/换一换.png',onTap=onChangeTags)
            # 创建自己的留言墙按钮
            Button(name='btn_create_im', pos=['center', 'bottom'],background='http://material.motimaster.com/suyu1536631297000/创建我的印象弹幕233.png',
                    size=[750, 100], onTap=onGoToPlay)

        # 遮罩层 正常情况下不显示
        with Mask(name='mask'):
            # 显示放大的留言墙
            with Box(name='bigger_box', pos=['center', 300], size=[600, 600], borderRadius=10,background='http://material.motimaster.com/suyu1536559902000/xingqiu2.png'):
                Image(pos=[20, 24],size=[150, 150],borderRadius='50%', src='images/avatar.png')
                 #Image(pos=[530, 20], size=[45, 48], src='images/dot_icon.png')
                Button(pos=[240, 70], size=[200, 70], text='看看是谁', color='#494a76',fontSize=40, lineHeight=70, background='white', onTap=onShowPay)
                with Box(pos=[20, 200], size=[550, 200], borderTop='1px solid #fff'):
                     Text(name='bigger_text', pos=[0, 10], size=[550, 200], text='谁在评价你一看就知道', fontSize=40, textAlign='left',color='white')
            # 支付框
            with Box(name='pay_box', pos=['center', 360], size=[670, 400], background='#ffffff', borderRadius=20, hidden=True):
                Text(text='花点小钱购买透视镜吧 谁在评价你一看就知道', fontSize=30, color='#000000', size=[310, 100], pos=['center', 100])
                Button(name='pay_one', text='¥4.99偷看一下', background='#ec866e', pos=[70, 300], size=[214, 74], lineHeight=74,
                    fontSize=30, border='1px solid #000000', borderRadius=10,
                    color='#000000', onTap=[moui.showLoading('请稍微等一下下...'), onPayOne, moui.hideLoading()])
                Button(name='pay_all', text='¥9.9查看全部', background='#7dcdad', border='1px solid #000000',
                    pos=[386, 300], size=[214, 74], lineHeight=74, fontSize=30, borderRadius=10,
                    color='#000000', onTap=[moui.showLoading('请稍微等一下下...'), onPayAll, moui.hideLoading()])
    def barrageItemTap():
        mo.console('在测试')

    def onInit():

        # page.danmu.data = [
        #     {'id':1,'text':'我喜欢你萨达达大厦萨就是垃圾焚烧收到反馈数据反馈时间到发生了大空间','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':2,'text':'弹幕一','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},
        #     {'id':3,'text':'弹幕二','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':4,'text':'弹幕三','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':5,'text':'弹幕四','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':6,'text':'弹幕五','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':7,'text':'弹幕六','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':8,'text':'弹幕七 ','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"}, 
        #     {'id':9,'text':'弹幕八','avatarUrl':"http://material.motimaster.com/appmaker/lijiong/2315.png"},  
        # ]
        page.danmu.danmuStyle='color:white;background:url(http://material.motimaster.com/suyu1536544156000/流星2.png) no-repeat;background-size:100% 100%;'
        # 保证从模版消息进入页面导航栏颜色一致
        mo.setNavibarColor('#ffffff', '#000000')
        mo.playBGM('http://material.motimaster.com/suyu1536457844000/yese.mp3',True, "black")

        # 后台统计是哪一个二维码入口
        imOperator.statQrcode()
        #mo.console(mo.token.getHostInfo()['openid'])

        if imOperator.isHost():
            mo.console('主态进入小程序')
            page.guest_box.hidden = True
            page.host_box.hidden = False

            if imOperator.isFirstTimeToTheApp() == False:
                mo.console('主态用户进入小程序--第二次访问')
                if imOperator.isNeedReloadPage() == True:
                    imOperator.reloadPage()
                else:
                    guestList = imOperator.getAnswerData()
                    mo.console('好友留言的数据:')
                    mo.console(guestList)

                    if len(guestList) == 0: # 没人留言
                        page.text_shareGuide.hidden = False
                    else:
                        page.result_box.hidden = False
                        page.no_result_box.hidden = True

                        #page.result_text_list.data = imOperator.getImListData(guestList)
                        page.danmu.data = imOperator.getImListData(guestList)
                        page
                    page.go_share_btn.hidden = True
                    page.btn_result_box.hidden = False
            else:
                mo.console('主态用户第一次进入小程序')
        else:
            mo.console('从客态进入')
            page.guest_box.hidden = False
            page.host_box.hidden = True

            setRandomTags()
            page.host_avatar.src = imOperator.getHostAvatarUrl()
            guests = imOperator.getAnswerData()

            if len(guests) > 0: # 有留言
                hideArr = imOperator.formatAnswerList(guests)
                mo.console(hideArr)
                page.danmu.data = hideArr
                page.showboxes.data = hideArr
                page.empty.hidden = True
                page.im_list.hidden = True
            else:
                page.empty.hidden = False
                page.im_list.hidden = True

    def onShowMask():
        if IS_AUDIT_VERSION == False:   # 不是审核版本
            imOperator.setPayId(params.item_id)

            page.bigger_text.text = params.item_text
            page.mask.hidden = False
            page.bigger_box.hidden = False
            page.pay_box.hidden = True
        else:
            # 提交审核需要改的代码
            pass

    def onShowPay():
        page.bigger_box.hidden = True
        page.pay_box.hidden = False

    def onPayOne():
        mo.wxpay.pay('查看详情', PAY_ONE_PRICE, onPayOneSuccess, onPayOneFail)

    def onPayAll():
        mo.wxpay.pay('查看详情', PAY_ALL_PRICE, onPayAllSuccess, onPayAllFail)

    def onPayOneSuccess():
        payList = imOperator.getUpdatedPayOneList()
        # 更新数据显示
        page.result_text_list.data = imOperator.getList()
        page.mask.hidden = True

    def onPayOneFail():
        mo.showAlert('提示','支付失败！')
        mo.console('支付失败')

    def onPayAllSuccess():
        payAllList = imOperator.getUpdatedPayAllList()
        page.result_text_list.data = payAllList
        page.mask.hidden = True

    def onPayAllFail():
        mo.showAlert('提示','支付失败！')
        mo.console('支付失败')

    def onShare():
        setShareInfo()

    def onShareSuccessed():
        imOperator.setAppData()

    # 跳转到海报页面
    def gotoSharePage():
        imOperator.setAppData()
        imOperator.setAvatarUrl()

        makeShareImage()
        imOperator.gotoSharePage()

    # 制作海报
    def makeShareImage():
        headimg = imOperator.getAvatarUrl()
        ret = mo.acode.make('indexPage',{'from_erweima':"erweima1"}, logo=headimg)

        canvas = mo.mopic.createCanvas(750, 750, 'http://material.motimaster.com/suyu1536460472000/弹幕3.png')
        canvas.addImage(ret.url, pos=[420, 720], size=[400, 400])
        res = canvas.makeImage()

        if res.ret == 0:
            imOperator.saveImageUrl(res.url)
        else:
            mo.showAlert('提示','作图失败！')

    def onGoToPlay():
        mo.redirectTo('indexPage')

    def onSelectTag():
        clearTextBackground()

        selectId = params.select_id

        # 改变文字标签的背景色
        if selectId == 'text1':
            page.selected_text1.background = '#ec866e'
        elif selectId == 'text2':
            page.selected_text2.background = '#ec866e'
        elif selectId == 'text4':
            page.selected_text4.background = '#ec866e'
        else:
            page.selected_text3.background = '#ec866e'

        textList = page.data.selectedList
        page.input2.value = textList[0][selectId]

    # 清空标签文本的背景色
    def clearTextBackground():
        page.selected_text1.background = ''
        page.selected_text2.background = ''
        page.selected_text3.background = ''
        page.selected_text4.background = ''

    # 随机给标签设置文本
    def setRandomTags():
        selectedList = random.sample(selectedTags, 1)

        page.selected_text1.text = selectedList[0]['text1']
        page.selected_text2.text = selectedList[0]['text2']
        page.selected_text3.text = selectedList[0]['text3']
        page.selected_text4.text = selectedList[0]['text4']

        page.data.selectedList = selectedList

    def onChangeTags():
        clearTextBackground()
        setRandomTags()


    def onAnswerSubmit():
        clearTextBackground()

        if page.input2.value == '':
            mo.showAlert('提示','请输入或者选择你的答案！')
        else:
            text = page.input2.value
            arr = imOperator.getShowAnswerList(text)

            page.showboxes.data = arr
            page.empty.hidden = True
            #page.im_list.hidden = False

            record = imOperator.saveAnswerData(text)

            page.danmu.data.append(record)
            # 回答完毕清空输入框数据
            page.input2.value = ''

            # 发送模版消息
            imOperator.sendTemplateMessage()

# 分享给好友的设置
def setShareInfo():
    if user.nickName == None:
        page.share.title = "你被点名啦，快来回答TA为你设置的问题吧"
    else:
        page.share.title = "你被%s点名啦，快来回答TA为你设置的问题吧"%(user.nickName)

    page.share.imageUrl = 'http://material.motimaster.com/suyu1536633820000/你说我变了.png'
    page.share.page = 'indexPage'

class sharePage(Page):
    background = 'http://material.motimaster.com/suyu1536458821000/星空2.png'#设置页面背景色
    naviBarColor = '#000000'
    def UI(self):
        # 用于提交审核显示的内容
       with Box(name='no_result_box', pos=[0, 0], width=750):
            #Image(pos=['center', 300], size=[484, 153], src='http://material.motimaster.com/suyu1536403227000/分享背景图.png')
            with Box(name='text1', pos=['center', 550], size=[370, 140], background='#ffffff', borderRadius=20, hidden=True):
                Text(pos=['center', 'center'], text='暂时还没有人发消息哦 快分享给好友吧', fontSize=30, color='#000000', size=[280, 70], lineHeight=35,
                    textAlign='center')
        # 页面背景
       Image(name='shareImage', pos=[0, 0], size=[750, 750])
       # 保存海报的按钮 和 分享给别人的按钮
       with Box(name='btn_box', pos=['center', 930], width=750):
           Button(name='send', background='http://material.motimaster.com/suyu1536413663000/保存朋友圈海报.png', borderRadius=48,
               pos=['center', 0], size=[402, 90], openType='getUserInfo', onTap=onSaveImage)
           ShareButton(name='share', background='http://material.motimaster.com/suyu1536413686000/转发群聊.png',
               pos=['center', 134], size=[402, 90], borderRadius=40)


    def onInit():
        if IS_AUDIT_VERSION == False:
            page.send.hidden = False
            page.shareImage.hidden = False
            page.shareImage.src = imOperator.getImageUrl()
        else:# 提交审核需要改的代码
            page.send.hidden = True
            page.shareImage.hidden = True

    def onShare():
        setShareInfo()

    # 保存图片到相册
    def onSaveImage():

        url = imOperator.getImageUrl()
        mo.saveImage(url)
