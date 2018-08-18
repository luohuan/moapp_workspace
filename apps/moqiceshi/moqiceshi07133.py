
AUDITING = True
def main():
    with MoApp(appid='wx87dcda9739af9cb1',name='好友脑回路匹配'):
      ##############开始界面###############
        with Page(name='entrance',background='http://material.motimaster.com/appmaker/menlu/3645.jpg',
            onReady=[moui.showLoading('加载中'),entranceReady, moui.hideLoading()]):
            Image(src='http://material.motimaster.com/appmaker/menlu/3649.png',size=[700,700],pos=['center',125])

            pass

            # with Box(name='head',size=[750,800],pos=[0,0]):
            #     Button(text='我的主页', size=[456, 88], pos=['center', 825], type='plainDefault',plain=True, openType='getUserInfo',onTap=gotoStart,backgroundColor='#c64342',color='#FFFFFF',fontSize='15px',borderRadius='3px',boxShadow='3px 3px 5px #888888',border='0px')
        with Page(name='start',background='http://material.motimaster.com/appmaker/menlu/3645.jpg'):
            Image(src='http://material.motimaster.com/appmaker/menlu/3649.png',size=[700,700],pos=['center',125])
            with Box(name='head',pos=['center',0]):
                Button(effect=pulse(t=1,c=0),text='开   始', size=[400, 90], pos=['center', 825], 
                    type='plainDefault',plain=True, fontWeight='bold',
                  openType='getUserInfo',onTap=gotoSecondPage,backgroundColor='#c64342',color='#FFFFFF',
                  fontSize='28px',lineHeight=90,borderRadius='15px',boxShadow='3px 3px 5px #888888',border='0px')

            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86')
            
      ###############出题界面###################
        with Page(name='choose',background='http://material.motimaster.com/appmaker/menlu/2408.jpg'):
            this.onReady = answerQuestionReady
            with Box(pos=['center',58],size=[660,170],background='#FAED9E',borderRadius='10px'):
                Text(name='quenumber',size=[30,30],pos=[30,30],fontSize='17px',fontWeight='normal')
                Text(name='questionBox',size=[510,200],pos=[130,30],color='#000D2F',fontSize='17px')
                Image(name='queimage',size=[600,350],pos=['center',210])
            with MoRadio(name = 'qa',pos=['center',650,600,160],fontSize = 30):
                this.onChange = afterAnswer

            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86')
            # Image(src='http://material.motimaster.com/appmaker/menlu/3650.png',size=[500,357],pos=['center',800])
            
            # with Box(name='alert',size=[700,100],pos=[0,790]):
            #     Text(text='温馨提示：',size=[600,30],pos=[80,0],fontSize='15px',color='#3D3D3D')
            #     Text(text='用你的第一反应选择答案哦~',size=[600,60],pos=[80,60],fontSize='15px',color='#3D3D3d')
  
    ###################生成二维码##################
        with Page(name='matrixcode',navigationBarTitleText='我们脑回路一样吗?', enableShare=True,
         background='http://material.motimaster.com/appmaker/menlu/2983.jpg', 
         onReady=[moui.showLoading('加载中'),CreatMatrixCode, moui.hideLoading()]): 
            Image(id='mopicImage',pos=[50,50],size=[650,650])
            Image(id='defaultImage',pos=[50,50],size=[650,650])
            Button(id='savebtnbefore',effect=shake(t=2.5,c=0),text='保存海报', plain=True, pos=['center', 810], size=[456, 88],lineHeight=88,
            fontSize='15px',onTap=save,borderRadius='20px',color='#c64342',fontWeight='bold',border= '1px solid #c64342',
            backgroundColor='#ffffff'
            )
            # Button(id='savebtnafter',effect=pulse(t=1,c=0),text='脑回路匹配', plain=True, pos=['center', 810], size=[376, 88],lineHeight=88,
            #   fontSize='15px',border='0px',borderRadius='20px',color='#c64342',fontWeight='bold',
            #   backgroundColor='#FFFFFF'
            #   )

            ShareButton(text='分享到好友群', plain=True, pos=['center', 930], size=[456, 88],lineHeight=88,
            fontSize='15px',borderRadius='20px',color='#ffffff',fontWeight='bold',border= '1px solid #c64342',
            backgroundColor='#c64342')
            #fontSize='15px',border='0px',borderRadius='20px',color='#FFFFFF',fontWeight='bold',
            #background='http://material.motimaster.com/appmaker/menlu/2993.png')
            with Box(id='ad', bottom=0, size=[750, 175]):
                AD(unitId='adunit-2a2855a7ea705e86')
            with Box(name='ljad',hidden=True,width=750,height='91px',top=1030):
                Image(onTap=onMoreFunTap,size=[750,175],src='http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg')

     ##################答题界面#####################   
        with Page(name='guestchoose',background='http://material.motimaster.com/appmaker/menlu/2408.jpg'):
            this.onReady = guestanswerQuestionReady
            with Box(pos=['center',58],size=[660,170],background='#FAED9E',borderRadius='10px'):
                Text(name='quenumber',size=[30,30],pos=[30,30],fontSize='17px',fontWeight='normal')
                Text(name='questionBox',size=[510,200],pos=[130,30],color='#000D2F',fontSize='17px')
                Image(name='queimage',size=[600,350],pos=['center',210])
            with MoRadio(name = 'qa',pos=['center',650,600,160],fontSize = 30):
                this.onChange = guestafterAnswer  
            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86') 
      
########################主人的题目和答案#################
        with Page(name='hostAnswer', onReady=onGetListData):
            this.onReady=findHostData
            with List(id='hostAnswerlist', pos=[0,0]):
                with Box(size=[750,200]):
                    Image(src='{item.avatarUrl}',pos=[20,20],size=[120,120],borderRadius='50%')
                    Text(text='{item.name}',pos=[0,30],color='red')
                    Text(text='{item.questions}',pos=[0,60],color='red')
                    Text(text='{item.selected}',pos=[0,90],color='blue')
                 #   with Button(text='删除', pos=['right', 75], type='miniWarn'):
                     #   this.onTap = moui.request(deleteHostItemData, id='{item.id}')
            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86')
######################客人的题目和答案#####################                      
        with Page(name='showoneguestanswer'):
            this.onReady=findGuestData
            with List(id='list', pos=[0,0]):
                with Box(size=[750,200]):
                    Image(src='{item.avatarUrl}',pos=[20,20],size=[120,120],borderRadius='50%')
                    Text(text='{item.name}',pos=[0,30],color='red')
                    Text(text='{item.question_id}',pos=[0,60],color='red')
                    Text(text='{item.selected}',pos=[0,90],color='blue')
                  #  with Button(text='删除', pos=['right', 75], type='miniWarn'):
                 #       this.onTap = moui.request(deleteItemData1, id='{item.id}')
            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86')

######################答题结果###############################
        with Page(name='relationshipresult',background='http://material.motimaster.com/appmaker/menlu/2671.jpg'):
             this.onReady=onCompareAnswer
             # with ScrollBox(name='friendlist',scrollY=True,size=[700,1000],pos=[0,0]):
             with Box(size=[750,600]):
                 Text(id='resulename',fontSize='20px',color='#000000',pos=['center',30],fontWeight='bold')
                 ContactButton(name='helpBtn',plain=True, border="None", pos=[600,535], size=[70, 70],
                  background='http://material.motimaster.com/appmaker/zhaoyuanxue/2357.png')
                 Image(id='scoreimage',size=[500,500],pos=['center',10],
                    src='http://material.motimaster.com/appmaker/menlu/3861.png')
                 Image(id='scoreimage2',size=[85,85],pos=[200,162],effect=bouncein(t=2,c=0),
                    src='http://material.motimaster.com/appmaker/menlu/3745.png')
                 Text(id='score',fontSize='20px',color='#b4205e',pos=[200,285])
                 Text(id='solgn',fontSize='15px',color='#000000',pos=['center',400])
                 Image(src='http://material.motimaster.com/appmaker/menlu/3451.png',size=[600,75],pos=[75,610])
                 with ScrollBox(name='friendlist',scrollY=True,size=[623,550],pos=[76,690]):
                    with List(name='friends'):
                        with Box(size=[609,280],background='http://material.motimaster.com/appmaker/menlu/3438.png',borderRadius='50rpx',marginBottom= 20):
                            Image(src='{item.host_avatarUrl}',pos=[60,50],size=[92,92],borderRadius='50%')
                            Text(text='{item.host_name}',pos=[60,150],fontSize='13px')
                            Image(src='{item.answer_avatarUrl}',pos=[445,50],size=[92,92],borderRadius='50%')
                            Text(text='{item.answer_name}',pos=[445,150],color='#1b272e',fontSize='13px')
                            Text(text='{item.score}'+'%',pos=[285,22],color='#1b272e',fontSize='15px',fontWeight='bold')
                            Image(src='http://material.motimaster.com/appmaker/menlu/3096.png',pos=['center',70],
                                size=[200,80])
                            Text(text='{item.solgn}',pos=['center',210],color='#1b272e',fontSize='11px')
                            # Image(src='http://material.motimaster.com/appmaker/menlu/2508.png',pos=[45,124],size=[550,10])
                    # with Button(text='查看答案',pos=[400,50],size=[200,80],type='primary',openType='getUserInfo'):
                    #     this.onTap = moui.goto('showoneguestanswer')
                 with Button(name='metoo',effect=pulse(t=1,c=0),text='我也要出题',size=[363,90],pos=[188,495],
                    type='primary',openType='getUserInfo',lineHeight='45px',fontSize='15px',border='0px',
                    backgroundColor='#c64342',borderRadius='20px',color='#FFFFFF'):
                     this.onTap=entranceReady
             # with Box(id='ad', bottom=0, size=[750, 175]):
             #     AD(unitId='adunit-2a2855a7ea705e86')
#####################答题的朋友列表######################
        with Page(name='friendsanswerlist',enableShare=True,
            background='http://material.motimaster.com/appmaker/menlu/3645.jpg'):
            this.onReady=GuestInfoLists
            Image(src='http://material.motimaster.com/appmaker/menlu/3719.png',pos=['center',10],size=[700,400])
            Image(id='scoreimage',size=[300,300],pos=[345,40],
                    src='http://material.motimaster.com/appmaker/menlu/3725.png')
            Image(id='scoreimage2',size=[160,166],pos=[280,70],effect=bouncein(t=2,c=0),
                    src='http://material.motimaster.com/appmaker/menlu/3745.png')
            ContactButton(name='helpBtn',plain=True, border="None", pos=[15,15], size=[70, 70],
                  background='http://material.motimaster.com/appmaker/zhaoyuanxue/2357.png')
            with Box(size=[613,654],pos=['center',330],backgroundColor='#f0d668'):
                Text(text='好友测试结果',fontSize='16px',pos=['center',40],color='#1b272e',fontWeight='bold')
                with ScrollBox(name='friendlist',scrollY=True,size=[623,500],pos=['center',150]):
                    Text(id='Alert',text='快邀请好友来回答，测测你们脑回路的相似度吧！！',size=[500,280],fontSize='13px',
                      pos=['center',85],color='#1b272e')
                    with List(name='friends'):
                        with Box(size=[609,140]):
                            Image(src='{item.answer_avatarUrl}',pos=[45,12],size=[92,92],borderRadius='50%')
                            Text(text='{item.answer_name}',pos=[178,9],color='#1b272e',fontSize='15px')
                            Text(text='{item.score}'+'%',pos=[490,9],color='#1b272e',fontSize='15px')
                            Text(text='{item.solgn}',pos=[178,67],color='#1b272e',fontSize='11px')
                            Image(src='http://material.motimaster.com/appmaker/menlu/2508.png',pos=[45,124],size=[550,10])
                    # with Button(text='查看答案',pos=[400,50],size=[200,80],type='primary',openType='getUserInfo'):
                    #     this.onTap = moui.goto('showoneguestanswer')
                          #  with Button(size=[40,40],pos=[500, 67],background='http://material.motimaster.com/appmaker/menlu/3731.png'):
                           #     this.onTap = moui.request(deleteItemData, id='{item.id}')
                with Box(size=[600,90],pos=['center',674]):
                    with Button(name='btn',effect=shake(t=2.5,c=0),text='邀请好友来回答', hidden=True, plain=True, pos=['center', 0], size=[360, 88],lineHeight=88,
                       fontSize='18px',border='0px',borderRadius='5px',color='#FFFFFF',fontWeight='bold',backgroundColor='#c64342',
                       boxShadow='3px 3px 5px #888888'):
                       this.onTap=findNewData
                    ShareButton(name='shareBtn',effect=shake(t=2.5,c=0),text='邀请好友来回答', hidden=True, plain=True, pos=['center', 0], size=[360, 88],lineHeight=88,
                       fontSize='18px',border='0px',borderRadius='5px',color='#FFFFFF',fontWeight='bold',backgroundColor='#c64342',
                       boxShadow='3px 3px 5px #888888')
           # with Button(text='清空数据', size=[255, 88], pos=['left', 0], type='plainDefault',plain=True, 
            #            openType='getUserInfo',backgroundColor='#c64342',color='#FFFFFF',fontWeight='bold',fontSize='15px',lineHeight=88,
             #           borderRadius='5px',boxShadow='3px 3px 5px #888888',border='0px'):
              #         this.onTap=Delete
            # with Box(id='ad', bottom=0, size=[750, 175]):
            #        AD(unitId='adunit-2a2855a7ea705e86')
async def onMoreFunTap(user, app, page, mo):
    #mo.gotoMiniProgram('')
    mo.console('morefun')
    mo.gotoMiniProgram('wx9066c083d563977e','pages/pageentrance/pageentrance?channel=swlpdxcx5')
async def entranceReady(user, app, page, mo):
    mo.console('调用了entranceReady这个函数')
    # mo.setNavibarColor('#000000', '#f0d668')
    for item in normal_test_question:
      #mo.console(len(item['answer']))
      if len(item['answer']) != 4:
        mo.console(item)
    result=mo.db.hostAnswerData11.find({
      'hostid': user.id,
      })
    if len(result) >= 1:
      mo.console('找到了')
      mo.redirectTo('friendsanswerlist')
    else:
      mo.console('还没出过题')
      mo.redirectTo('start')

async def Delete(user, app, page, mo):
    items = mo.db.hostAnswerData11.find({ 
        'hostid': user.id,
        })
    mo.console(str(items))
  
    if  len(items) != 0:
      for item in items:
        mo.console(item['id'])
        mo.db.hostAnswerData11.delete(item['id'])

    items = mo.db.guestAnswerData11.find({ 
        'host_id': user.id,
        })
    mo.console(str(items))
  
    if  len(items) != 0:
      for item in items:
        mo.console(item['id'])
        mo.db.guestAnswerData11.delete(item['id'])

async def gotoshowGuestData(user,app,page,mo):
    mo.goto('showguestdata')

async def onGetListData(user, app, page, mo):  
    page.num.data = normal_test_question

async def GuestInfoLists(user,app,page,mo):
    # mo.setNavibarColor('#000000', '#f0d668')
    question=mo.db.hostAnswerData11.find({
      'hostid': user.id
      })
    host_id=question[0]['hostid']
    host_name=question[0]['name']
    host_avatarUrl=question[0]['hostAvatar']
    page.share.page = 'guestchoose'
    page.share.imageUrl='http://material.motimaster.com/appmaker/menlu/3638.jpg'
    page.share.title = random.choice(share_solgn)
    page.share.options = {
        # 'question_id': newquestion_id,
        'hostuser_id':host_id,
        'hostuser_name':host_name,
        'hostuser_avatarUrl':host_avatarUrl
    }
    # 'hostuser_id':page.options.hostuser_id,
    #     'hostuser_name':page.options.hostuser_name,
    #     'hostuser_avatarUrl':page.options.hostuser_avatarUrl
     #######改#####此处应该针对出题的题目id去获取用户的答案列表啊 
    page.friends.data=mo.db.guestAnswerData11.find({
      'host_id':user.id
      })
    if len(page.friends.data)==0:
        page.Alert.hidden=False
    else:
        page.Alert.hidden=True


    #page.btn.hidden = False ### 审核的时候这一行注释掉 显示name=shareBtn 直接分享
    page.shareBtn.hidden = False ## 审核完的时候这一行注释掉 显示name="Btn" 

async def findNewData(user,app,page,mo):
    mo.console('调用了findNewData这个函数')
    mo.console('用户ID：'+user.id)
    question=mo.db.hostAnswerData11.find({
      'hostid': user.id
      })
    # newquestion=questionID[0]
    # newquestion_id=newquestion['question_id']
    # mo.console('最新的题目ID：'+newquestion_id)
    host_id=question[0]['hostid']
    host_name=question[0]['name']
    host_avatarUrl=question[0]['hostAvatar']
    mo.console(str(question))
    mo.goto('matrixcode',hostuser_id=host_id,
            hostuser_name=host_name,hostuser_avatarUrl=host_avatarUrl)

async def gotoSecondPage(user, app, page, mo):    
    mo.goto('choose')

async def gotoStart(user, app, page, mo):    
    mo.goto('start')


import random
   
#######################出题########################## 
async def answerQuestionReady(user, app, page, mo):
    mo.setNavibarColor('#000000', '#f0d668')
    mo.console(user.nickName)
    page.quenumber.text="1/5:"
    page.questionBox.text=" %s" % normal_test_question[0]["question"]
    page.queimage.src=normal_test_question[0]["imageUrl"]
    answers = []
    for i in range(4):
        answers.append({'value':i,'text':normal_test_question[0]["answer"][i]})    
    page.qa.data = answers
    page.qa.color = "#3D3D3D"
    page.data.index = 0
    page.data.selected = []

async def afterAnswer(user, app, page, mo):
    mo.console(user.nickName)
    selected = page.data.selected
    selected.append(int(page.qa.value))
    page.data.selected = selected
    mo.console(selected)
    # questions_index = page.data.get('questions_index')
    index = int(page.data.index)+1
    mo.console(user.openid)
    if index == 5:
        mo.showTips('出完了',1000)
        mo.console(page.data.selected)
        question_id = mo.db.hostAnswerData11.insert({
            'hostopen_id':user.openid,
            'hostid': user.id,
            'hostAvatar':user.avatarUrl,
            'name': user.nickName,
            # 'questions': questions,
            'selected': page.data.selected
        })
        if AUDITING == False:
            mo.goto('matrixcode',hostuser_id=user.id,
                hostuser_name=user.nickName,hostuser_avatarUrl=user.avatarUrl)
        else:
            mo.redirectTo('friendsanswerlist', hostuser_id=page.options.hostuser_id,
             hostuser_name=page.options.hostuser_name,hostuser_avatarUrl=page.options.hostuser_avatarUrl)
        return
    page.quenumber.text="%s/5:"%(index+1)
    page.questionBox.text=" %s" % (normal_test_question[index]["question"])
    page.queimage.src=normal_test_question[index]["imageUrl"]
    # page.qa.question = "%s/10: %s" % (index+1,normal_test_question[b]["question"])
    mo.console(normal_test_question[index])
    answers = []
    for i in range(4):
        answers.append({'value':i,'text':normal_test_question[index]["answer"][i],'checked':False})
    page.qa.data = answers
    page.qa.color = "#3D3D3D"
    page.data.index = index

async def CreatMatrixCode(user,app,page,mo):
    page.defaultImage.src='http://material.motimaster.com/appmaker/menlu/3862.jpg'
    page.defaultImage.hidden=True  #审核时注释，上线放出
    #page.savebtnbefore.hidden=True  #审核时放出，上线注释
    #page.mopicImage.hidden=True  #审核时放出，上线注释
    

    mo.console('这里是二维码页面')
    mo.setNavibarColor('#000000', '#f0d668')
    # mo.console('问题ID：'+page.options.question_id)
    mo.console('主人ID：'+page.options.hostuser_id)
    mo.console('主人名字：'+page.options.hostuser_name)
    # host=mo.db.hostAnswerData.find({
    #   'id': page.options.question_id
    #   })
    # user_name=host[0]['name']
    # page.options.user_name=user_name

    page.share.page = 'guestchoose'
    page.share.imageUrl='http://material.motimaster.com/appmaker/menlu/3638.jpg'
    page.share.title = random.choice(share_solgn)
    page.share.options = {
        # 'question_id': page.options.question_id, 
        'hostuser_id':page.options.hostuser_id,
        'hostuser_name':page.options.hostuser_name,
        'hostuser_avatarUrl':page.options.hostuser_avatarUrl
    }

    params = {
        'page': 'guestchoose',
        'width': 150,
        'options': {
            # 'question_id': page.options.question_id,
            'hostuser_id':page.options.hostuser_id,
            'hostuser_name':page.options.hostuser_name,
            'hostuser_avatarUrl':page.options.hostuser_avatarUrl
        }
    }
    retParams = mo.acode.getWxAcodeUrl(params)
    erweima = None
    if retParams['ret'] == 0:
        erweima = retParams['data']['wxacode_url']
    Image=mo.mopic.createImage(650, 650,saveStrategy='permanent')
    Image.addImage('http://material.motimaster.com/appmaker/menlu/3635.jpg',pos=[0,0])
    Image.addImage(erweima, pos=[300, 250, 300, 300], mask='circle')
    Image.addImage(page.options.hostuser_avatarUrl, pos=[385, 335, 130, 130], mask='circle')

    res = Image.makeImage()
    if res['ret'] == 0:
        page.mopicImage.src=res['url']
        page.data.url=page.mopicImage.src

async def save(user, app, page, mo):
    mo.console(page.data.url)
    mo.saveImage(page.data.url)


##############################答题部分######################
async def guestanswerQuestionReady(user, app, page, mo):
    # page.cmt.hidden=True
    mo.setNavibarColor('#000000', '#f0d668')
    # mo.console('用户的昵称：'+user.nickName)
    mo.console('用户的ID：'+user.id)
    mo.console('（传）主人的ID：'+page.options.hostuser_id)
    mo.console('（传）主人的昵称:'+page.options.hostuser_name)
    mo.console('（传）主人的头像:'+page.options.hostuser_avatarUrl)
    result = mo.db.hostAnswerData11.find({
      'hostid': page.options.hostuser_id,
      })
    mo.console(('result',result))
    if len(result) >0:
      mo.console('找到了')
      questionInfo = result[0]
      mo.console(questionInfo)
      host_name=questionInfo['name']
      host_avatarUrl=questionInfo['hostAvatar']
      host_selected=questionInfo['selected']
      mo.console('(取)主人的昵称:'+host_name)
      mo.console('（取）主人的头像:'+host_avatarUrl)
      mo.console(host_selected)
      if questionInfo['hostid'] == user.id:
        mo.console('主人态')
        # mo.redirectTo('friendsanswerlist', hostuser_id=user.id,
        #     hostuser_name=user.nickName,hostuser_avatarUrl=user.avatarUrl)
        mo.redirectTo('friendsanswerlist', hostuser_id=page.options.hostuser_id,
             hostuser_name=page.options.hostuser_name,hostuser_avatarUrl=page.options.hostuser_avatarUrl)
      else:
        mo.console('客人态')
        theguest=mo.db.guestAnswerData11.find({
                'host_id':page.options.hostuser_id,
                'answer_id':user.id
                })
        #  ##########上线把这段注释掉##########
        # items = mo.db.guestAnswerData1.find({
        #   'host_id':page.options.hostuser_id,
        #   'answer_id':user.id
        # })
        # mo.console(str(items))
        # if  len(items) != 0:
        #   for item in items:
        #     mo.console(item['id'])
        #     mo.db.guestAnswerData1.delete(item['id'])
        #########以上注释掉#################
    #客人答过题了
        if len(theguest)>=1:
            mo.console('他答过这道题了')
            theguestInfo=theguest[0]
            mo.console(theguestInfo)
            mo.redirectTo('relationshipresult',hostuser_id=page.options.hostuser_id,
              hostuser_name=page.options.hostuser_name,hostuser_avatarUrl=page.options.hostuser_avatarUrl)
    
        else:
            mo.console('他没答过题')
            page.quenumber.text="1/5:"
            page.questionBox.text=" %s" % normal_test_question[0]["question"]
            page.queimage.src=normal_test_question[0]["imageUrl"]
            answers = []
            for i in range(4):
                answers.append({'value':i,'text':normal_test_question[0]["answer"][i]})    
            page.qa.data = answers
            page.qa.color = "#3D3D3D"
            page.data.index = 0
            page.data.selected = []
    else:
        mo.showAlert('提示', '问卷不存在')
    # page.quenumber.text="1/10:"
    # page.questionBox.text=" %s" % normal_test_question[0]["question"]
    # page.queimage.src=normal_test_question[0]["imageUrl"]
    # answers = []
    # for i in range(4):
    #     answers.append({'value':i,'text':normal_test_question[0]["answer"][i]})    
    # page.qa.data = answers
    # page.qa.color = "#3D3D3D"
    # page.data.index = 0
    # page.data.selected = []

async def guestafterAnswer(user, app, page, mo):
    # mo.console('客人的昵称：'+user.nickName)
    selected = page.data.selected
    selected.append(int(page.qa.value))
    page.data.selected = selected
    mo.console(selected)
    index = int(page.data.index)+1
    # questions_index = page.data.get('questions_index')
    if index == 5:
        mo.showTips('答完了',1000)
        mo.console(page.data.selected)
        guestAnswer_id=mo.db.guestAnswerData11.insert({

        'host_id':page.options.hostuser_id,
        'host_name':page.options.hostuser_name,
        'host_avatarUrl':page.options.hostuser_avatarUrl,
        # 'question_id': page.options.question_id,
        'answer_id': user.id,
        'answer_name': user.nickName,
        'answer_avatarUrl': user.avatarUrl,
        'selected': page.data.selected,
        'score':'',
        'solgn':'',
        'whetherAns':0
        })
        mo.redirectTo('relationshipresult',hostuser_id=page.options.hostuser_id,
              hostuser_name=page.options.hostuser_name,hostuser_avatarUrl=page.options.hostuser_avatarUrl)
        return
    page.quenumber.text="%s/5:"%(index+1)
    page.questionBox.text=" %s" % (normal_test_question[index]["question"])
    page.queimage.src=normal_test_question[index]["imageUrl"]
    # page.qa.question = "%s/10: %s" % (index+1,normal_test_question[b]["question"])
    mo.console(normal_test_question[index])
    answers = []
    for i in range(4):
        answers.append({'value':i,'text':normal_test_question[index]["answer"][i],'checked':False})
    page.qa.data = answers
    page.qa.color = "#3D3D3D"
    page.data.index = index

async def onCompareAnswer(user,app,page,mo):
    mo.setNavibarColor('#000000', '#f0d668')
    # mo.console(page.options.guestAnswer_id)

    guestInfo = mo.db.guestAnswerData11.find({
      # 'id': page.options.guestAnswer_id
      # 'question_id': page.options.question_id,
      'host_id':page.options.hostuser_id,
      'answer_id':user.id
      })
    guestselected = guestInfo[0]['selected']
    guestInfoID=guestInfo[0]['id']
    # question_id=guestInfo[0]['question_id']
    # host_id=guestInfo[0]['host_id']
    # host_name=guestInfo[0]['host_name']
    mo.console(guestselected)
    # mo.console(host_id)
    # mo.console(host_name)
    hostInfo = mo.db.hostAnswerData11.find({
      'hostid': page.options.hostuser_id
      })
    hostselected=hostInfo[0]['selected']
    host_id=hostInfo[0]['hostid']
    host_name=hostInfo[0]['name']
    mo.console(host_id)
    mo.console(host_name)
    mo.console(hostselected)
    score=100
    for i in range(0, len(hostselected)):
        if int(hostselected[i]) ==int(guestselected[i]):
            mo.console("在第" + str(i) + "个位置上数组host等于数组guest.")
            score=score

        elif int(hostselected[i]) !=int(guestselected[i]):
            mo.console("在第" + str(i) + "个位置上host不等于guest.")
            score=score-20
    mo.console(score)
    if 80<=score<=100:
        page.solgn.text=str(resulet_solgn[0])
    elif 60<=score<80:
        page.solgn.text=str(resulet_solgn[1])
    elif 40<=score<60:
        page.solgn.text=str(resulet_solgn[2])
    elif 0<=score<40:
        page.solgn.text=str(resulet_solgn[3])
    mo.db.guestAnswerData11.update(guestInfoID,{
        'score':score,
        'solgn':page.solgn.text,
        'whetherAns':1
        
    })
    page.resulename.text='你与%s的脑回路匹配度为'%(host_name)
    page.score.text = '%d%%' %(score)
    page.friends.data=mo.db.guestAnswerData11.find({
       'host_id':page.options.hostuser_id
      # 'answer_id': user.id
      })


#################分享#########################
async def gotoShare(user, app, page, mo):
    mo.redirectTo('matrixcode', question_id=page.options.question_id,hostuser_id=user.id,
            hostuser_name=user.nickName,hostuser_avatarUrl=user.avatarUrl)

async def findHostData(user,app,page,mo):
    # result = mo.db.hostAnswerData.find({
    #   'id': page.options.question_id
    #   })
    # questionInfo = result[0]
    page.hostAnswerlist.data =  mo.db.hostAnswerData11.find({
      'id': page.options.question_id
      })  #  

async def deleteHostItemData(user, app, page, mo, params):
    # 删除
    mo.db.hostAnswerData11.delete(params.id)
    page.hostAnswerlist.data = mo.db.hostAnswerData11.find()

async def insertGuestData(user, app, page, mo, selected):
    answer = page.data.get('selected')
    if not answer:
      answer = []

    answer.append(selected)
    page.data.set('selected', answer)
    mo.console(answer)
    return
    '''mo.db.guestAnswerData.insert({
        'name': user.nickName,
        'que':page.dialogtest.newQuestion,
        'ans': page.dialogtest.newAnswer
        })'''

async def findGuestData(user,app,page,mo):
    page.list.data = mo.db.guestAnswerData11.find()  # 获取数据库xxx的数据

async def GuestInfoList(user,app,page,mo):
    page.friends.data = mo.db.guestAnswerData11.find()  

async def deleteItemData(user, app, page, mo, params):
    # 删除
    mo.db.guestAnswerData11.delete(params.id)
    page.friends.data = mo.db.guestAnswerData11.find()

async def deleteItemData1(user, app, page, mo, params):
    # 删除
    mo.db.guestAnswerData11.delete(params.id)
    page.list.data = mo.db.guestAnswerData11.find()
normal_test_question = [
        { 
           "question": "如果把这幅图做成表情包，你会配什么文字？",
           "imageUrl":"http://material.motimaster.com/appmaker/menlu/3829.jpg",
           "answer":['真让人头大','两眼无神','发际线令人担忧','他们怎么还不走']
        },{
           "question": "今天38度，猫跑着去干什么？",
           "imageUrl":"http://material.motimaster.com/appmaker/menlu/3830.jpg",
           "answer":[ '见主人','见美女喵','吃西瓜','看世界杯']
        },{
           "question": "两个“你就等着吧”表达的是一个意思吗？",
           "imageUrl":"http://material.motimaster.com/appmaker/menlu/3842.jpg",
           "answer":[ '是，都是让蛙蛙等一下','是，都是蛙蛙会有严重的后果','不是，前者是等一下，后者会被打','不是，前者是等一下，后者会被亲']
        },{
           "question": "你和朋友去看电影，看到如图的选座情况，你会选择哪个座位？",
           "imageUrl":"http://material.motimaster.com/appmaker/menlu/3837.jpg",
           "answer":[ '1，正后方，视奸最佳视角','2，拒绝狗粮，从我做起','3，双面夹击，扫黄打非','4，旁边，斜眼一瞟，啥都知道']
        },{
           "question": "这张图你第一眼看到的是什么？",
           "imageUrl":"http://material.motimaster.com/appmaker/menlu/3828.jpg",
           "answer":[ '自学','白尝','自觉','白学']
        }
        ]


resulet_solgn=['确认过脑仁儿，你就是对的人儿','这么复杂的脑回路上都能遇到你','再靠近一点点我就跟你走','这位仁兄脑回路很清奇啊！']
share_solgn=['听说脑回路相反的人最能炸出友情的火花哦！','决定我们关系的，居然是脑回路！快来测测~','是朋友就一起来测测脑回路！','你是对的人吗？看看我们的脑回路相似度！']
