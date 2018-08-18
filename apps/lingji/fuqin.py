
import json
Questions={'测试' :[

    {
        #问题
        'title': '1/6 你知道你父亲平均一天抽多少支烟吗？',
        #选项
        'options': [
        {'text': '他不抽烟', 'value': '3'},
        {'text': '他不在我面前抽烟', 'value': '4'},
        {'text': '大概知道', 'value': '2'},
        {'text': '并不清楚', 'value': '1'}
    ],
        #答案(是第几个)，不需要调用答案的值时，可以不用填
       #'answer': 4
    },
    {
        'title': '2/6 你想怎么样陪你父亲度过这个父亲节？',
        'options': [
        {'text' : '给父亲发个大红包' , 'value':'2'},
        {'text' : '给父亲打个电话，聊聊天' , 'value':'4'},
        {'text' : '送父亲一件精美的礼物' , 'value':'3'},
        {'text' : '不是我们家会过的节日' , 'value':'1'}
    ],
        #'answer': 2
    },
    {
        'title': '3/6 你多久会给父亲打一通电话（语音、视频聊天）？',
        'options':[
        {'text' : '每一周', 'value' : '4'},
        {'text' : '每个月' , 'value': '3'},
        {'text' : '有事情需要商量的时候' , 'value': '2'},
        {'text' : '微信消息为最常用' , 'value': '1'},

    ],
        #'answer': 2
    },
    {
        #问题
        'title': '4/6 你觉得自己对你父亲的了解程度是？',
        #选项
        'options': [
        {'text': '大于80%', 'value': '4'},
        {'text': '50% - 80%', 'value': '3'},
        {'text': '20% - 50%', 'value': '2'},
        {'text': '少于20%', 'value': '1'}
    ],
        #答案(是第几个)
        #'answer': 4
    },
     {
        #问题
        'title': '5/6 你记得你父亲的生日嘛？',
        #选项
        'options': [
        {'text': '脱口而出', 'value': '4'},
        {'text': '不敢确定', 'value': '2'},
        {'text': '记在备忘录中', 'value': '3'},
        {'text': '都来自老妈的提醒', 'value': '1'}
    ],
        #答案(是第几个)
        #'answer': 4
    },
     {
        #问题
        'title': '6/6 如果满分10分，你为父亲打几分？',
        #选项
        'options': [
        {'text': '10分', 'value': '4'},
        {'text': '9分', 'value': '3'},
        {'text': '8分', 'value': '2'},
        {'text': '低于8分', 'value': '1'}
    ],
        #答案(是第几个)
        #'answer': 4
    },

]}

img_int = [
# 测试
'http://material.motimaster.com/who_i_am/hi/main/7c4518ac2b3241dfcc5e83d5128d40bc.jpg',
'http://material.motimaster.com/who_i_am/hi/main/7c4518ac2b3241dfcc5e83d5128d40bc.jpg',
'http://material.motimaster.com/who_i_am/hi/main/9620c9347b6fe703e056ae4aaa77b3fd.jpg',
'http://material.motimaster.com/who_i_am/hi/main/6b67b10895faa6858d41651e1f422ab5.jpg',
'http://material.motimaster.com/who_i_am/hi/main/670a7dc1fadca2dfb7e971bc1043e6c3.jpg',
'http://material.motimaster.com/who_i_am/hi/main/b393dc76d1d6135eba739ed94f281b75.jpg',
'http://material.motimaster.com/who_i_am/hi/main/02714b426fa604ad1d4bd87b9ce1dee0.jpg',
'http://material.motimaster.com/who_i_am/hi/main/c1a1f425fe12e02573897cfe75a24f28.jpg',
'http://material.motimaster.com/who_i_am/hi/main/d8e4c5bf0e4cb3e22b1bc0b3e2b3025f.jpg',
'http://material.motimaster.com/who_i_am/hi/main/6f714bac3a52a56669878d59ad8335ae.jpg'

]


async def ontestPageReady(user,app,page,mo):#页面题目准备
    questions = Questions['测试']#获取字典的内容

    page.data.set('pagenum',0)#设置第几题
    page.data.set('curnum',0)#当前第几题
    user.set('ans',[])
    page.radiotext.text = questions[0]['title']
    page.radio3.data = questions[0]['options']


async def onNext(user,app,page,mo):#答题&计分&结果判断
    questions = Questions['测试']#定义问题
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
        for i in [6,8,10,13,15,17,19,21,23,24]:
            if ansint <= i:
                break
            k += 1 #判断下一个图片
        user.set('imgurl',img_int[k])
        mo.redirectTo('ResultPage') 
        return
    page.data.set('pagenum',pagenum)
    page.radiotext.text = questions[pagenum]['title']
    page.radio3.data = questions[pagenum]['options']

#生成成绩单&添加二维码&添加用户昵称&分享页面设置
async def onReadyPicPage(user,app,page,mo):
    # page.saveImg.hidden = False
    imgsrc = user.get('imgurl')

    #创建最后展示页的画布
    canvas = mo.mopic.createCanvas(750, 1300)
    #在画布上加上背景图
    canvas.addImage(imgsrc, pos=[0, 0, 750, 1300])
    #在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=[129,65,115,115],mask='circle')
    #在画布上加上文字
    # canvas.addText(user.nickName+'的心理年龄是：', pos=[223, 232], fontSize=32, color=(0, 0, 0))
    
    res = canvas.makeImage()

    #生成一个带参数的二维码（如果不要参数，可以直接用小程序的二维码）
    # erweima = None
    # params = {
    #     'page': 'homePage',
    #     'width': 150,
    #     'options':{'a':1,'b':user.nickName}
    # }
    # retParams = mo.acode.getWxAcodeUrl(params)    
    # if retParams['ret'] == 0:
    #     erweima = retParams['url']
    # else:
    #     mo.console(erweima)
    #     page.mopicImage.src = json.dumps(erweima)
    #把二维码添加到画布上
    # canvas.addImage(erweima, pos=[540,920,100, 100])

    #生成图片
    res_erweima = canvas.makeImage()

    #判断生成图片是否成功
    if res_erweima['ret'] == 0:
        #在页面上展示结果图
        page.mopicImage.src = res_erweima['url']
        #生成“保存图片”按钮操作需要的图片链接
        page.data.set('url',res_erweima['url'])
    else:
        #mo.console(res_erweima)
        page.mopicImage.src = json.dumps(res_erweima)

    #设置页面分享的标题、图片、用户进入页、传递的参数 
    page.share.title = "你们爷俩有多亲密？"
    page.share.imageUrl = 'http://material.motimaster.com/who_i_am/hi/main/f564f10c090a115aeabbf74b1a64c0d0.jpg'
    page.share.page = 'homePage'
    page.share.options = {'a':1,'b':user.nickName}

    page.bottomButton.hidden = False

#点击“保存图片”按钮的操作
async def onSaveImage(user, app, page, mo):
    url = page.data.get('url')#提取分享图片的地址
    mo.saveImage(url)