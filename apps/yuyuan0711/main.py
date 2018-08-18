import random
import time

question_num = 15 #设置答题数量

def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='2018直男考卷', navigationBarTitleText = '2018直男考卷', withLogin=True):
        with Page(name='mainPage', background='http://material.motimaster.com/appmaker/liuhongjie/2614.jpg', onReady=[moui.showLoading('加载中...'), indexReady,moui.hideLoading()], enableShare=True):
            ImageAvatar(name='avatar', size=[190,190], pos=['center',350], borderRadius='50%')
            Text(text='姓名：', fontWeight='bold', pos=[226,600,127,48], color='black', fontSize=40)
            TextNickName(pos=[350,600], size=[266,48], fontSize=40, color='black')
            Text(text='考号：', fontWeight='bold',pos=[226,712,127,48],color='black',fontSize=40)
            Text(name='num', text='2018023301', pos=[330,712], size=[386,48], fontSize=40, color='black')
            Button(text='开始答题', fontWeight='bold', boxShadow='-1px 15px 30px -12px black', fontSize=40, backgroundColor="#FFFFFF", borderRadius='20px', openType='getUserInfo', pos=['center',909], lineHeight=95, size=[369,95], onTap=onButtonClick)
        
        #问题页面
        with Page(name='questionPage', background='http://material.motimaster.com/appmaker/liuhongjie/2702.jpg', onReady = [moui.showLoading('加载中...'), questionPageReady,moui.hideLoading()], enableShare=True):
            with Box(width='90%', height='auto', position='relative'):
                Text(name='question', fontSize=38, fontWeight='bold',pos=[40, 50], width=670, lineHeight=50, position='relative')
            with Box(height='auto', position='relative'):
                Image(name='subquest', hidden=True, pos=[175, 120], size=[400, 400], position='relative')
            # 四个图片答案
                with Box(name='image_ans', hidden=True, position='relative', height='auto'):
                    Image(name='option1', pos=[55, 100], size=[300,300], mode='aspectFit', boxShadow='-1px 15px 30px -12px black', onTap=optionChange1)
                    Image(name='option2', pos=[395, 100], size=[300,300], mode='aspectFit', boxShadow='-1px 15px 30px -12px black', onTap=optionChange2)
                    Image(name='option3', pos=[55, 510], size=[300,300], mode='aspectFit', boxShadow='-1px 15px 30px -12px black', onTap=optionChange3)
                    Image(name='option4', pos=[395, 510], size=[300,300], mode='aspectFit', boxShadow='-1px 15px 30px -12px black', onTap=optionChange4)
                    Button(text='A', lineHeight=70, background='#fbc74a', pos=[180, 430], size=[70,70], border="1rpx solid #FFD886",boxShadow='-1px 15px 30px -12px black', onTap=optionChange1)
                    Button(text='B', lineHeight=70, background='#fbc74a', pos=[515, 430], size=[70,70], border="1rpx solid #FFD886",boxShadow='-1px 15px 30px -12px black', onTap=optionChange2)
                    Button(text='C', lineHeight=70, background='#fbc74a', pos=[180, 840], size=[70,70], border="1rpx solid #FFD886",boxShadow='-1px 15px 30px -12px black', onTap=optionChange3)
                    Button(text='D', lineHeight=70, background='#fbc74a', pos=[515, 840], size=[70,70], border="1rpx solid #FFD886",boxShadow='-1px 15px 30px -12px black', onTap=optionChange4)
            
            # 四个文字答案
                with Box(name='text_ans', hidden=True, position='relative', height='auto'):
                    Button(name='tans1', text='A', lineHeight=70, background='#fbc74a', border="1rpx solid #FFD886",pos=[60, 120], size=[70,70], boxShadow='-1px 15px 30px -12px black', onTap=optionChange1)
                    Text(name='answer1', pos=[140, 125], lineHeight=50, width='80%', onTap=optionChange1)
                    Button(name='tans2', text='B', lineHeight=70, background='#fbc74a', border="1rpx solid #FFD886",pos=[60, 250], size=[70,70], boxShadow='-1px 15px 30px -12px black', onTap=optionChange2)
                    Text(name='answer2', pos=[140, 255], lineHeight=50, width='80%', onTap=optionChange2)
                    Button(name='tans3', text='C', lineHeight=70, background='#fbc74a', border="1rpx solid #FFD886",pos=[60, 380], size=[70,70], boxShadow='-1px 15px 30px -12px black', onTap=optionChange3)
                    Text(name='answer3', pos=[140, 385], lineHeight=50, width='80%', onTap=optionChange3)
                    Button(name='tans4', text='D', lineHeight=70, background='#fbc74a', border="1rpx solid #FFD886",pos=[60, 510], size=[70,70], boxShadow='-1px 15px 30px -12px black', onTap=optionChange4)
                    Text(name='answer4', pos=[140, 515], lineHeight=50, width='80%', onTap=optionChange4)
                
            # 判断题答案
                with Box(name='judge_ans', hidden=True, position='relative', height='auto'):
                    Button(name='judge1', background='#fbc74a', lineHeight=80, size=[150, 80], pos=[150, 180], border="1rpx solid #FFD886", boxShadow='-1px 15px 30px -12px black', borderRadius='20px', onTap=optionChange1)
                    Button(name='judge2', background='#fbc74a', lineHeight=80, size=[150, 80], pos=[450, 180], border="1rpx solid #FFD886",  boxShadow='-1px 15px 30px -12px black', borderRadius='20px', onTap=optionChange2)
            
            
        #结果页面，显示头像、昵称及直男得分
        with Page(name='result', background='http://material.motimaster.com/appmaker/liuhongjie/3691.jpg',onShareSuccessed=afterShare, onReady = [moui.showLoading('正在生成成绩单'), resultPageReady, moui.hideLoading()], enableShare=True):
            with Box(pos=[0, 0], width=750, height=1020):
                Image(name='mopicImage', pos=[0, 0], size=[750, 1020])
            with Box(pos=[0, 0], width=750, height=750):
                ShareButton(text='分享给好友来PK', pos=[40, 935, 315, 85], lineHeight=85, fontWeight='bold', boxShadow='-1px 15px 30px -12px black', fontSize=40, backgroundColor="#FFFFFF", borderRadius='20px')
                Button(name='save', text='保存成绩单', fontSize=40, fontWeight='bold', pos=[395, 935, 315, 85], lineHeight=85, boxShadow='-1px 15px 30px -12px black', 
                       backgroundColor="#FFFFFF", borderRadius='20px', onTap = saveShareImage)
                Text(name='again', text='不服再战', fontWeight='bold', fontSize=40, lineHeight=42, borderBottom="3rpx solid #000000", pos=[410, 1055], onTap=onButtonClick)
                Text(name='showRes',text='查看答案', fontWeight='bold', fontSize=40, lineHeight=42, borderBottom="3rpx solid #000000", pos=[180, 1055], onTap=showShare)
            
            with Mask(name='allResult', hidden=True):
                with ScrollBox(background='rgba(17,17,17,0.8)',borderRadius='10px',border='1px solid #FFD886',
                size=[700,1000], pos=['center',100], scrollY=True):
                    with Box(position='relative',size=[550,50]):
                        Text(text='正确答案是：', color="#FFD886",fontSize=30,fontWeight='bold',pos=['center',0])
                    with List(name='resList', position='relative'):
                        with Box(hidden='{item.texthidden}',height=80,position='relative'):
                            Text(text='{item.textAns}', pos=['center',0], lineHeight=50,color='#FFFFFF')
                        with Box(hidden='{item.imagehidden}',height=350,position='relative'):
                            Image(src='{item.imageAns}',pos=['center',0], mode='aspectFit', boxShadow='-1px 15px 30px -12px black', size=[300, 300])
            with Mask(name='mask', hidden=True, locked=True):
                with Box(size=[600,300],pos=['center',400],backgroundColor='white',borderRadius=2):
                    Text(text='温馨提示',fontSize=32, pos=['center',25], fontWeight='bold')
                    Text(text='分享到群,立即查看答案',fontSize=30,color='#888888',pos=['center',100])
                    # Text(text='让其他好友也来测测吧!',fontSize=30,color='#888888',pos=['center',100])
                    Button(text='取消',onTap=cancel,textAlign='center',size=[300,100],lineHeight=100,pos=[0,200],
                        color='black',borderTop='1rpx solid #eeeeee',borderRight='1rpx solid #eeeeee',backgroundColor='white',borderRadius='0')
                    ShareButton(text='分享',textAlign='center',size=[300,100],lineHeight=100,pos=[300,200],
                        color='#09BB07',borderTop='1rpx solid #eeeeee',backgroundColor='white',borderRadius='0')
async def afterShare(user, app, page, mo):
    page.mask.hidden = True
    ResClick(user, app, page, mo)
async def cancel(user, app, page, mo):
    page.mask.hidden = True
                    
async def showShare(user, app, page, mo):
    #page.mask.hidden = False
    ResClick(user, app, page, mo)#审核的时候这个打开 审核完这个注释掉 上一个打开

async def ResClick(user, app, page, mo):
    page.allResult.hidden = False
    all_res = mo.db.ManTest.find({'openid':page.options.openid})[0]['result']
    mo.console(json.dumps(all_res, ensure_ascii=False))
    mo.console(json.dumps(len(all_res), ensure_ascii=False))
    mo.console(json.dumps(len(questionDict), ensure_ascii=False))
    res_data = []
    for i in range(len(questionDict)):
        res_dict = {}
        if questionDict[i]['subtype'] == 'text':
            res_dict['textAns'] = str(all_res[i])
            res_dict['imagehidden'] = True
            #res_dict['imageAns'] = ''
        else:
            #res_dict['textAns'] = ''
            res_dict['texthidden'] = True
            res_dict['imageAns'] = str(all_res[i])
        res_data.append(res_dict)
    page.resList.data = res_data
    
async def indexReady(user, app, page, mo):
    if page.options.openid and page.options.openid == user.openid:
        mo.goto('result', openid = user.openid)
        return
    page.num.text = 201802330000 + int(random.random()*9999)
    
async def onButtonClick(user,app,page,mo):
    mo.goto('questionPage') 

async def setType(page, quest, num):
    if quest['type'] == 'choice':
        if page.data.count == 14:
            page.question.text = '[附加题]'+ quest['question']
            page.subquest.pos = [50,60]
            page.subquest.size = [650,450]
        else:
            page.question.text = '[选择题]'+ str(num)+ '/10：'+ quest['question']
        if quest['subtype'] == 'image':
            page.subquest.hidden = True
            page.image_ans.hidden = False
            page.text_ans.hidden = True
            page.judge_ans.hidden = True
            page.option1.src = quest['answer'][0]
            page.option2.src = quest['answer'][1]
            page.option3.src = quest['answer'][2]
            page.option4.src = quest['answer'][3]
        else:
            if quest['subquest'] == '':
                page.subquest.hidden = True
            else:
                page.subquest.hidden = False
                page.subquest.src = quest['subquest']
            page.text_ans.hidden = False
            page.judge_ans.hidden = True
            page.image_ans.hidden = True
            page.answer1.text = quest['answer'][0]
            page.answer2.text = quest['answer'][1]
            page.answer3.text = quest['answer'][2]
            page.answer4.text = quest['answer'][3]
       
    elif quest['type'] == 'judge':
        # if quest['subquest']:
            # page.subquest.hidden = False
            # page.subquest.src = quest['subquest']
        # else:
            # page.subquest.hidden = True
        if quest['subquest'] == '':
            page.subquest.hidden = True
        else:
            page.subquest.hidden = False
            page.subquest.src = quest['subquest']
        page.question.text = '[判断题]'+ str(num)+ '/4：'+ quest['question']
        page.image_ans.hidden = True
        page.text_ans.hidden = True
        page.judge_ans.hidden = False
        page.judge1.text = quest['answer'][0]
        page.judge2.text = quest['answer'][1]

# 问题页面准备，给出第一题
async def questionPageReady(user, app, page, mo):
    count = 0
    total_score = 0
    allRes = []
    quest = questionDict[count]
    setType(page, quest, 1)
    page.data.count = count
    page.data.realAnswer = quest['realAnswer']
    real_index = int(quest['realAnswer'])-1
    allRes.append(questionDict[0]['answer'][real_index])
    page.data.allRes = allRes
    page.data.score = quest['score']
    page.data.total_score = total_score

async def update_db(user, app, page, mo):
    temp = mo.db.ManTest.find({'openid': user.openid})
    if temp:
        mo.db.ManTest.update(temp[0]['id'],{
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'total_score': page.data.total_score, #记录最近一次得分
            'result':page.data.allRes
            })
    else:
        mo.db.ManTest.insert({
                'name': user.nickName,# 答题者name
                'openid': user.openid,# 答题者openid
                'avatarUrl': user.avatarUrl,# 答题者头像
                'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                'total_score': page.data.total_score,
                'result':[]
                })
   
# 点击option1后，若答对则加分，并在最后将个人信息、得分加入数据库中
async def optionChange1(user, app, page, mo):
    count = int(page.data.count)+ 1
    page.data.count = count
    if int(page.data.realAnswer)==1:
        page.data.total_score += page.data.score
    if count==question_num:
        update_db(user, app, page, mo)
        mo.goto('result', openid=user.openid)
        return
    quest = questionDict[page.data.count]
    setType(page, quest, int(page.data.count)%10 + 1)
    page.data.realAnswer = quest['realAnswer']
    real_index = int(quest['realAnswer'])-1
    tmp = page.data.allRes
    tmp.append(questionDict[page.data.count]['answer'][real_index])
    page.data.allRes = tmp
    page.data.score = quest['score']
    
async def optionChange2(user, app, page, mo):
    count = int(page.data.count)+1
    page.data.count = count
    if int(page.data.realAnswer)==2:
        page.data.total_score += page.data.score
    if count==question_num:
        update_db(user, app, page, mo)
        mo.goto('result', openid=user.openid)
        return
    quest = questionDict[page.data.count]
    setType(page, quest, int(page.data.count)%10 + 1)
    page.data.realAnswer = quest['realAnswer']
    real_index = int(quest['realAnswer'])-1
    tmp = page.data.allRes
    tmp.append(questionDict[page.data.count]['answer'][real_index])
    page.data.allRes = tmp
    page.data.score = quest['score']
    
async def optionChange3(user, app, page, mo):
    count = int(page.data.count)+1
    page.data.count = count
    if int(page.data.realAnswer)==3:
        page.data.total_score += page.data.score
    if count==question_num:
        update_db(user, app, page, mo)
        mo.goto('result', openid=user.openid)
        return
    quest = questionDict[page.data.count]
    setType(page, quest, int(page.data.count)%10 + 1)
    page.data.realAnswer = quest['realAnswer']
    real_index = int(quest['realAnswer'])-1
    tmp = page.data.allRes
    tmp.append(questionDict[page.data.count]['answer'][real_index])
    page.data.allRes = tmp
    page.data.score = quest['score']
    
async def optionChange4(user, app, page, mo):
    count = int(page.data.count)+1
    page.data.count = count
    if int(page.data.realAnswer)==4:
        page.data.total_score += page.data.score
    if count==question_num:
        update_db(user, app, page, mo)
        mo.goto('result', openid=user.openid)
        return
    quest = questionDict[page.data.count]
    setType(page, quest, int(page.data.count)%10 + 1)
    page.data.realAnswer = quest['realAnswer']
    real_index = int(quest['realAnswer'])-1
    tmp = page.data.allRes
    tmp.append(questionDict[page.data.count]['answer'][real_index])
    page.data.allRes = tmp
    page.data.score = quest['score']
    
    
# 设置分享页面、title以及显示得分
async def resultPageReady(user, app, page, mo):
    if page.options.openid:
        tmp_score = mo.db.ManTest.find({'openid': page.options.openid})[0]['total_score']
    else:
        tmp_score = mo.db.ManTest.find({'openid': user.openid})[0]['total_score']

    image_dict={
                0:'http://material.motimaster.com/liuhongjie1531299273000/1-2.jpg',
                1:'http://material.motimaster.com/liuhongjie1531299273000/1-2.jpg',
                2:'http://material.motimaster.com/liuhongjie1531299296000/2-2.jpg',
                3:'http://material.motimaster.com/liuhongjie1531299296000/2-2.jpg',
                4:'http://material.motimaster.com/liuhongjie1531299312000/3-2.jpg',
                5:'http://material.motimaster.com/liuhongjie1531299330000/4-2.jpg',
                6:'http://material.motimaster.com/liuhongjie1531299330000/4-2.jpg',
                7:'http://material.motimaster.com/liuhongjie1531299347000/5-2.jpg',
                8:'http://material.motimaster.com/liuhongjie1531299347000/5-2.jpg',
                9:'http://material.motimaster.com/liuhongjie1531299363000/6-2.jpg',
                10:'http://material.motimaster.com/liuhongjie1531299375000/7-2.jpg'
    }
    
    # 创建最后展示页的画布
    canvas = mo.mopic.createCanvas(750, 1020, saveStrategy='permanent')
    # 在画布上加上背景图
    canvas.addImage('http://material.motimaster.com/appmaker/liuhongjie/3691.jpg', pos=[0, 0, 750, 1020])
    canvas.addImage(image_dict[int(int(tmp_score)/10)], pos=[0, 0, 750, 900])
    # 在画布上加上用户头像
    canvas.addImage(user.avatarUrl, pos=[290, 20, 170, 170], mask='circle')
    # 在画布上加上文字
    canvas.addText(user.nickName + '的得分为', fontSize=40, pos=[200, 245], color=(0, 0, 0))
    canvas.addText(str(tmp_score) + '分', fontSize=80, pos=[300, 295], color=(255, 0, 0))
    res = canvas.makeImage()

    canvas.addImage('http://material.motimaster.com/appmaker/liuhongjie/3732.jpg', pos=[0, 900, 750, 140])
    canvas.addText('2018直男考题统一卷', fontSize=35, pos=[60, 930], color=(0, 0, 0))
   
    
    # 生成一个带参数的二维码
    erweima = None
    params = {
        'page': 'mainPage',
        'width': 150,
        'options': {
            'openid': user.openid
        }
    }
    retParams = mo.acode.getWxAcodeUrl(params)
    if retParams['ret'] == 0:
        erweima = retParams['url']

    # 把二维码添加到画布上
    canvas.addImage(erweima, pos=[635, 910, 100, 100])

    # 生成图片
    res_erweima = canvas.makeImage()

    # 判断生成图片是否成功
    if res['ret'] == 0:
        # 在页面上展示结果图
        page.mopicImage.src = res['url']
        # 生成“保存图片”按钮操作需要的图片链接
        page.data.set('url', res_erweima['url'])
    
    page.share.title = '我的直男得分是'+str(tmp_score) + '分！快来测测你的吧~'
    page.share.page = 'mainPage'
    page.share.options = {"openid": user.openid}
    
async def saveShareImage(user, app, page, mo):
    url = page.data.get('url')
    mo.saveImage(url)
    
questionDict = [
    {
        'id': 'q1',
        'type': 'choice',
        'subtype': 'image',
        'question': '下面哪张图是传说中的“空气刘海”？',
        'subquest': '',
        'answer':['http://material.motimaster.com/liuhongjie1530502826000/90bba19677f664f389e4385de06f5a09.png',
                  'http://material.motimaster.com/guest1530174270000/904e22d4024ad5c5dc36c9adee234b96.jpg',
                  'http://material.motimaster.com/guest1530174287000/adb841743fd2b500429e61d224aef3f3.jpg',
                  'http://material.motimaster.com/liuhongjie1530502860000/39f870bd253e6790bebb870406e51375.jpg'
                 ],
        'realAnswer': 2,
        'score': 6
    },
    {
        'id': 'q2',
        'type': 'choice',
        'subtype': 'image',
        'question': '下列物品哪一个价格最贵？',
        'subquest': '',
        'answer':['http://material.motimaster.com/yuyuan13hao1530253349000/微信图片_20180629141253.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2646.png',
                  'http://material.motimaster.com/guest1530513029000/微信图片_20180702142757.jpg',
                  'http://material.motimaster.com/appmaker/liuhongjie/2648.png'
                 ],
        'realAnswer': 1,
        'score': 7
    },
    {
        'id': 'q3',
        'type': 'choice',
        'subtype': 'image',
        'subquest': '',
        'question': '下面哪个是TF口红的logo？',
        'answer':['http://material.motimaster.com/appmaker/liuhongjie/2649.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2650.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2651.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2652.png'
                 ],
        'realAnswer': 3,
        'score': 7
    },
    {
        'id': 'q4',
        'type': 'choice',
        'subtype': 'image',
        'subquest': '',
        'question': '请在正确位置为你的女朋友化上腮红，让她变得美美哒~',
        'answer':['http://material.motimaster.com/appmaker/liuhongjie/2694.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2695.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2696.png',
                  'http://material.motimaster.com/appmaker/liuhongjie/2697.png'
                 ],
        'realAnswer': 4,
        'score': 6
    },
    {
        'id': 'q5',
        'type': 'choice',
        'subtype': 'text',
        'question': '正确的化妆步骤是？',
        'subquest': 'http://material.motimaster.com/liuhongjie1531289791000/未标题-1.jpg',
        'answer':['②③①④',
                  '②①④③',
                  '①③②④',
                  '③①②④'
                 ],
        'realAnswer': 3,
        'score': 7
    },
    {
        'id': 'q6',
        'type': 'choice',
        'subtype': 'text',
        'subquest': '',
        'question': '女朋友剥小龙虾，不小心把油滴到你刚买的AJ鞋上了，你应该怎么说？',
        'answer':['没事，我回去洗一下就行了。',
                  '没事，我这鞋是假的。',
                  '我有手的一天，绝不会让你亲自动手剥虾。',
                  '没事 ，我把你的鞋也弄脏就好了。'
                 ],
        'realAnswer': 3,
        'score': 6
    },
    {
        'id': 'q7',
        'type': 'choice',
        'subtype': 'image',
        'subquest': '',
        'question': '女朋友抱怨最近长痘了，要用遮瑕遮住，让你帮忙拿一下，以下你应该拿哪个？',
        'answer':['http://material.motimaster.com/yuyuan13hao1530256515000/微信图片_20180629151450.jpg',
                  'http://material.motimaster.com/yuyuan13hao1530255989000/timg (1).jpg',
                  'http://material.motimaster.com/yuyuan13hao1530255990000/timg (3).jpg',
                  'http://material.motimaster.com/yuyuan13hao1530256073000/timg (4).jpg'
                 ],
        'realAnswer': 2,
        'score': 7
    },
    {
        'id': 'q8',
        'type': 'choice',
        'subtype': 'text',
        'question': '这个物品是用来做什么的？    ',
        'subquest': 'http://material.motimaster.com/liuhongjie1530501628000/微信图片_20180702111731.jpg',
        'answer':['吹风机',
                  '检测皮肤',
                  '美容',
                  '脱毛'
                 ],
        'realAnswer': 4,
        'score': 7
    },
    {
        'id': 'q9',
        'type': 'choice',
        'subtype': 'image',
        'question': '以下哪个是姨妈色？',
        'subquest': '',
        'answer':['http://material.motimaster.com/guest1530512477000/微信图片_20180702114818.jpg',
                  'http://material.motimaster.com/guest1530512496000/微信图片_20180702114822.jpg',
                  'http://material.motimaster.com/guest1530513196000/微信图片_20180702114825.jpg',
                  'http://material.motimaster.com/guest1530512563000/微信图片_20180702114808.jpg'
                 ],
        'realAnswer': 1,
        'score': 7
    },
    {
        'id': 'q10',
        'type': 'choice',
        'subtype': 'image',
        'question': '下面哪款包包的价格与一辆Jeep牧马人的价格最接近？',
        'subquest': '',
        'answer':['http://material.motimaster.com/liuhongjie1530589934000/c0c2af7423941a608c31685b98e3705f.jpg',
                  'http://material.motimaster.com/liuhongjie1530589556000/1.png',
                  'http://material.motimaster.com/liuhongjie1530589360000/微信图片_20180703114217.jpg',
                  'http://material.motimaster.com/liuhongjie1530590198000/0e10b389939235bbb45d2b48cde06a83.jpeg'
                 ],
        'realAnswer': 3,
        'score': 7
    },
    {
        'id': 'q11',
        'type': 'judge',
        'subtype': 'text',
        'subquest': 'http://material.motimaster.com/appmaker/liuhongjie/3714.png',
        'question': '跟女朋友吵架，她说:“我困了，先睡了。”这时，你应该贴心地对她说:“晚安。”',
        'answer':['对',
                  '错'
                 ],
        'realAnswer': 2,
        'score': 6
    },
    {
        'id': 'q12',
        'type': 'judge',
        'subtype': 'text',
        'subquest': 'http://material.motimaster.com/appmaker/liuhongjie/3700.png',
        'question': '看电影的时候，女朋友嫌前排的情侣太过亲密，影响到别人了，你应该端正坐姿跟她保持距离。',
        'answer':['对',
                  '错'
                 ],
        'realAnswer': 2,
        'score': 6
    },
    {
        'id': 'q13',
        'type': 'judge',
        'subtype': 'text',
        'subquest': 'http://material.motimaster.com/guest1530520106000/845841a01ecb42318ba519d87a317e9d.png',
        'question': '女朋友说自己的指甲油快用完了，你可以买下面这款产品送给她。          ',
        'answer':['对',
                  '错'
                 ],
        'realAnswer': 2,
        'score': 6
    },
    {
        'id': 'q14',
        'type': 'judge',
        'subtype': 'text',
        'subquest': 'http://material.motimaster.com/liuhongjie1531280181000/Moschino香水.jpg',
        'question': '你心疼女朋友下厨太累了，于是饭后主动拿起下面这款产品帮忙清洁厨房。',
        'answer':['对',
                  '错'
                 ],
        'realAnswer': 2,
        'score': 6
    },
    
    {
        'id': 'q15',
        'type': 'choice',
        'subtype': 'text',
        'question': '请问下面这段话里，共有几个错误？',
        'subquest': 'http://material.motimaster.com/yuyuan/Duudle/create/5099119f4a305f95504fbf9eb93d62cc.jpg',
        'answer':['9个',
                  '10个',
                  '11个',
                  '12个'
                 ],
        'realAnswer': 3,
        'score': 9
    }
]