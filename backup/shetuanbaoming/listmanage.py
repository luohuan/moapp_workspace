import time
from tools import *
from entrylist import *


chooseicon = 'http://material.motimaster.com/ywjiang/ceshiyong/demo/4590b1b395f50ad24d13f5e96b9118f4.png'

templateID = ['面试邀请通知', '面试结果通知']

class listmanage(Page):
    background = '#F5F5F5'
    def UI():
        with List(id='list', pos=[20, 40]):
            with Box(size=[710, 300], backgroundColor='#ffffff', borderRadius='5px', position='relative', marginBottom=20):
                Text(pos=[20, 40, 500, 50], textAlign='left', lineHeight=50, text='{item.title}', fontWeight=700)
                Text(pos=[20, 120, 500, 50], textAlign='left', lineHeight=50, text='已报名:{item.count}人', color='#888', fontSize=30)
                with Box(pos=[500, 200, 200, 80]):
                    Image(pos=[0, 'center', 50, 50], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/f50f98e1ad348a90c84389ab9ea9b3ef.png')
                    Text(pos=[70, 0, 150, 80], textAlign='left', lineHeight=80, text='管理', color=navicolor)
                    this.onTap = moui.request(showmask, title='{item.title}', formid='{item.id}')
        with Mask(id='managemask', pos=[0, 0, '100%', '100%'], hidden=True, opacity=0.6):
            
                
            with Box(bottom=0, size=[750, 500], backgroundColor='#f4f4f4', position='fixed'):
                Text(id='title', pos=[0, 0, 750, 60], textAlign='center', lineHeight=60, borderBottom='1px solid #888')
                with Grid(id='grid', pos=[10, 70, 720, 150], column=4):
                    with Box(pos=[0, 0, 180, 150]):
                        Box(pos=['center', 10, 90, 90], backgroundColor='#ffffff', borderRadius='5px')
                        Image(pos=['center', 25, 60, 60], src='{item.pic}')
                        Text(pos=['center', 100, 170, 50], textAlign='center', lineHeight=50, text='{item.function}', fontSize=28)
                        this.onTap = moui.request(clickfunction, function='{item.function}', formid='{item.formid}')
                with Box(bottom=0, size=[750, 100], backgroundColor='#ffffff'):
                    Text(pos=['center', 0, 750, 100], textAlign='center', lineHeight=100, text='关闭')
                    this.onTap = moui.setData(__managemask_hidden=True)
            this.onTap = moui.setData(__managemask_hidden='{!__managemask_hidden}')
                # Image(pos=[500, 20, 60, 60], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/5558ad0928b237a2aede8bb18eb8e23d.png')
                # with Button(pos=[500, 20, 60, 60], formType='submit', border='0px solid #ffffff', plain=True):
                #     this.onTap = moui.goto('createsuccess', index='{item.id}', title='{item.title}')
                # Image(pos=[500, 90, 60, 60], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/e00f5f28d78848116a889a812c4628ff.png')
                # with Button(pos=[500, 90, 60, 60], formType='submit', border='0px solid #ffffff', plain=True):
                #     this.onTap = moui.goto('invitemanager', index='{item.id}', title='{item.title}')
                # # with Button(pos=[350, 120, 150, 60], type='primary', textAlign='center', lineHeight=60, fontSize=30, formType='submit', text='查看结果'):
                # this.onTap = moui.goto('listresult', index='{item.id}', title='{item.title}')
        # with Button(pos=[520, 120, 150, 60], type='primary', textAlign='center', lineHeight=60, fontSize=30, formType='submit', text='群发'):
        #     this.onTap = [moui.setData(__maskbottom_hidden=False, __template_hidden=False), moui.request(clicksend, index='{item.id}', title='{item.title}')]
        

        # with Button(id='maskbottom', pos=[0, 0, '100%', '100%'], backgroundColor='#000000', opacity=0.7, hidden=True, formType='submit'):
        #     this.onTap = moui.setData(__maskbottom_hidden=True, __template_hidden=True)                        
        # with Box(id='template', bottom=0, size=[750, 400], position='fixed', backgroundColor='#ffffff', hidden=True):
        #     with Button(pos=['center', 50, 450, 80], type='primary', textAlign='center', lineHeight=80, formType='submit', text='面试邀请通知'):
        #         this.onTap = moui.request(gototemplate, template='invate')
        #     with Button(pos=['center', 150, 450, 80], type='primary', textAlign='center', lineHeight=80, formType='submit', text='面试结果通知'):
        #         this.onTap = moui.request(gototemplate, template='result')
        #     with Button(pos=['center', 300, 450, 80], type='primary', textAlign='center', lineHeight=80, formType='submit', text='关闭'):
        #         this.onTap = moui.setData(__maskbottom_hidden=True, __template_hidden=True)                        
        #                 # this.onTap = moui.goto('entry', index='{item.id}', title='{item.title}')
        # with Box(left=600, top='90%', size=[750, '10%'], position='fixed'):
        #     Image(pos=[0, 0, 100, 100], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/21593a4eba7d6f678af7dc1add3eff8b.png')
        #     with Button(pos=[0, 0, 100, 100], border='0px solid #ffffff', plain=True):
        #         this.onTap = moui.goto('prelist')

    def onInit():    
        formdata = get_my_all_createform(user, mo)
        
        for item in formdata:
            item['createtime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['createtime'])) 
        
        page.list.data = formdata

    def onShow():
        onInit()


    def showmask():
        page.managemask.show()
        page.title.text = params.title
        for item in functionlist:
            item['formid'] = params.formid
        page.grid.data = functionlist

    def clickfunction():
        if params.function == functionlist[0]['function']:  #查看报名
            mo.goto('entry', index=params.formid)
        elif params.function == functionlist[1]['function']:  #邀请报名
            mo.goto('shareform', index=params.formid)
        elif params.function == functionlist[2]['function']:  #查看报名结果
            mo.goto('listresult', index=params.formid)
        elif params.function == functionlist[3]['function']:  #权限管理
            pass
        elif params.function == functionlist[4]['function']:  #删除
            pass
        else:
            pass

    def onHide():
        page.managemask.hide()


class listresult(Page):
    background = greybackground
    def UI():
        with Box(id='allchoose', size=[750, 80], position='relative', hidden=True):
            with Button(pos=[600, 'center', 120, 60], textAlign='center', lineHeight=60, backgroundColor=navicolor, color='#ffffff', text='全选'):
                this.onTap = chooseAll
        with ScrollBox(size=[750, '90%'], position='relative'):
            with List(id='list', pos=[0, 0]):
                with Button(size=[750, 200], plain=True, border='0px solid #ffffff', formType='submit'):
                    Box(pos=[0, 0, 750, 180], backgroundColor='#ffffff')
                    Text(pos=[20, 0, 480, 40], textAlign='left', lineHeight=50, fontSize=30, text='{item.keyword1}')
                    Text(pos=[20, 40, 480, 40], textAlign='left', lineHeight=50, fontSize=30, text='{item.keyword2}')
                    Text(pos=[20, 80, 480, 40], textAlign='left', lineHeight=50, fontSize=30, text='{item.keyword3}')
                    this.onTap = moui.goto('entrydetail', index='{item.formid}', openid='{item.openid}')
            with List(id='list2', pos=[0, 0], hidden=True):
                with Box(size=[750, 200]):
                    Box(pos=[650, 'center', 40, 40], border='2px solid #F5F5F5', backgroundColor='{item.backgroundcolor}')
                    Image(pos=[650, 'center', 40, 40], src='{item.pic}')
                    this.onTap = moui.request(singleChoose, openid='{item.openid}')

        with Box(bottom=0, position='fixed', size=[750, '10%'], backgroundColor=greybackground):
            with Button(id='sendall', pos=[20, 20, 710, 94], textAlign='center', type='primary', lineHeight=94,  backgroundColor=navicolor, text='群发通知', openType='getUserInfo'):
                this.onTap = [moui.setData(__allchoose_hidden=False, __sendall_hidden=True, __choose_hidden=False, __list2_hidden=False), sendall]
            with Box(id='choose', pos=[0, 0, 750, '10%'], hidden=True):
                with Box(bottom=0, left=0, width=375, height='10%'):
                    with Button(pos=[0, 10, 360, 94], textAlign='center', lineHeight=94, backgroundColor=navicolor, text='确定', color='#ffffff', formType='submit'):
                        this.onTap = gototemplate
                with Box(bottom=0, left=375, width=375, height='10%'):
                    with Button(pos=[15, 10, 360, 94], textAlign='center', lineHeight=94, plain=True, border='1px solid #256DF2', color='#256DF2', text='取消', formType='submit'):
                        this.onTap = [moui.setData(__allchoose_hidden=True, __sendall_hidden=False, __choose_hidden=True, __list2_hidden=True), cancelsend]

    def onInit():
        formdata = showformdata(mo, page.options.index)
        # for item in formdata:
        #     item['keyword4'] = '提交时间:'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['keyword4']))
        
        page.list.data = formdata
        
        
        app.data.alldata = formdata
        
    def onHide():
        page.allchoose.hide()
        page.sendall.show()
        page.choose.hide()
        page.list2.hide()
        

    def singleChoose():
        choosed = app.data.choosed
        alldata = app.data.alldata

        if params.openid in choosed:
            choosed.remove(params.openid)
        else:
            choosed.append(params.openid)
        app.data.choosed = choosed
        
        choosedbox = []
        for i in range(0, len(alldata)):
            if alldata[i]['openid'] in choosed:
                choosedbox.append({'backgroundcolor':'', 'pic':chooseicon, 'openid':alldata[i]['openid']})
            else:
                choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':alldata[i]['openid']})
        page.list2.data = choosedbox

    def cancelsend():
        alldata = app.data.alldata
        app.data.choosed = []
        choosedbox = []
        for i in range(0, len(alldata)):
            choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':''})
        page.list2.data = choosedbox        
        

    def sendall():
        alldata = app.data.alldata
        app.data.choosed = []

        choosedbox = []
        allopenid = []
        for i in range(0, len(alldata)):
            choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':alldata[i]['openid']})
            allopenid.append(alldata[i]['openid'])
        app.data.allopenid = allopenid
        page.list2.data = choosedbox

    def gototemplate():
        choosed = app.data.choosed
        if choosed:
            mo.goto('template')
        else:
            mo.showAlert('提示', '请选择收件人')
    
    def chooseAll():
        pass
        # choosed = app.data.choosed
        # allopenid = app.data.allopenid
        # if choosed == allopenid:



class entrydetail(Page):
    def UI():
        Text(id='title', pos=[0, 0, 750, 100], textAlign='center', lineHeight=100)
        with ScrollBox(pos=[0, 100, 750, '90%'], scrollY=True):
            with List(id='list'):
                with Box(pos=[0, 0, 750, 120]):
                    Text(pos=[50, 0, 650, 50], textAlign='left', lineHeight=50, text='{item.keyword1}')
                    Text(pos=[70, 50, 650, 50], textAlign='left', lineHeight=50, text='{item.keyword2}')
        with Box(bottom=0, position='fixed', size=[750, '10%']):
            with Button(pos=[0, 20, 375, 80], textAlign='center', lineHeight=80, text='上一条', border='0px solid #ffffff', plain=True):
                this.onTap = upItem
            with Button(pos=[375, 20, 375, 80], textAlign='center', lineHeight=80, text='下一条', border='0px solid #ffffff', plain=True):
                this.onTap = downItem


    def onInit():
        thisform = showformdatadetail(mo, page.options.openid, page.options.index)
        page.title.text = thisform[0]
        page.list.data = thisform[1]
        
        thisformdata = formdata(user.openid, mo)
        allopenid = thisformdata.get_thisform_allopenid(page.options.index)
        app.data.allopenid = allopenid
        app.data.nowindex = allopenid.index(page.options.openid)

    def upItem():
        allopenid = app.data.allopenid
        nowindex = app.data.nowindex 
        if nowindex == 0:
            mo.showAlert('提示', '前面没有啦')
            return
        else:
            nowindex -= 1
            app.data.nowindex = nowindex
            thisform = showformdatadetail(mo, allopenid[nowindex], page.options.index)
            page.list.data = thisform[1]

    def downItem():
        allopenid = app.data.allopenid
        nowindex = app.data.nowindex 
        if nowindex == len(allopenid)-1:
            mo.showAlert('提示', '后面没有啦')
            return
        else:
            nowindex += 1
            app.data.nowindex = nowindex
            thisform = showformdatadetail(mo, allopenid[nowindex], page.options.index)
            page.list.data = thisform[1]


class mylist(Page):
    background = '#F5F5F5'
    def UI():
        with List(id='list'):
            with Button(pos=[0, 50, 750, 170], formType='submit', border='0px solid #ffffff', plain=True):
                Box(pos=[0, 0, 750, 150], backgroundColor='#ffffff')
                Text(pos=[20, 0, 480, 40], textAlign='left', lineHeight=50, fontSize=30, text='{item.title}')
                this.onTap = moui.goto('mylistdetail', index='{item.formid}')
        # with Box(bottom=0, position='fixed', size=['100%', '10%']):
        #     with Button(pos=['center', 20, 450, 80], textAlign='center', lineHeight=80, text='群发通知', openType='getUserInfo'):
        #         this.onTap = sendMessage

    def onInit():
        myformdata = get_my_formdata(user, mo)
        page.list.data = myformdata


class mylistdetail(Page):
    def UI():
        Text(id='title', pos=[0, 0, 750, 100], textAlign='center', lineHeight=100)
        with ScrollBox(pos=[0, 100, 750, '90%'], scrollY=True):
            with List(id='list'):
                with Box(pos=[0, 0, 750, 120]):
                    Text(pos=[50, 0, 650, 50], textAlign='left', lineHeight=50, text='{item.keyword1}')
                    Text(pos=[70, 50, 650, 50], textAlign='left', lineHeight=50, text='{item.keyword2}')
    def onInit():
        thisform = showformdatadetail(mo, user.openid, page.options.index)
        page.title.text = thisform[0]
        page.list.data = thisform[1]        

class template(Page):
    background = '#F5F5F5'
    def UI():
        # Text(id='acttitle', pos=['center', 20, 750, 50], textAlign='center', lineHeight=50, )
        with SinglePickerButton(id='picker', text='点击选择', type='primary', background='#ffffff', pos=['center', 0, 200, 80], color='#000', 
            fontSize=26, lineHeight=80, range=templateID):
            this.onChange = choose_template
        with Box(pos=[0, 100, 750, 400], backgroundColor='#ffffff'):
            Text(id='templatetitle', pos=['center', 0, 500, 50], textAlign='center', lineHeight=50)
            with List(id='list', pos=[0, 70]):
                with Box(size=[200, 70]):
                    Text(pos=[0, 0, 200, 50], textAlign='center', lineHeight=50, text='{item.txt}')
            Text(id='input1', pos=[230, 70, 450, 50], textAlign='center', lineHeight=50, borderBottom='1px solid #F5F5F5', color='#808080', text='自动填充昵称')
            Input(id='input2', pos=[230, 140, 450, 50], textAlign='center', lineHeight=50, borderBottom='1px solid #F5F5F5')
            Input(id='input3', pos=[230, 210, 450, 50], textAlign='center', lineHeight=50, borderBottom='1px solid #F5F5F5')
            Input(id='input4', pos=[230, 290, 450, 50], textAlign='center', lineHeight=50, borderBottom='1px solid #F5F5F5')
        
        with Box(bottom=0, size=[750, 100], position='fixed'):
            with Button(pos=['center', 10, 450, 80], textAlign='center', lineHeight=80, text='发送', type='primary', formType='submit'):
                this.onTap = sendMessage


    def onInit():
        mo.setNavibarTitle('群发消息')
        
        choosed = app.data.choosed
        mo.console(choosed)

        page.input2.value = ''
        page.input3.value = ''
        page.input4.value = ''

        
            
        page.templatetitle.text = '面试邀请通知'
        templatekey = invate
        templatedata = []
        for item in templatekey:
            templatedata.append({'txt':item})
        page.list.data = templatedata
        
        
    def choose_template():
        templatevalue = page.picker.value    
        mo.console(page.picker.value)
        if templateID[int(page.picker.value)] == '面试邀请通知':
            templatekey = invate
            page.templatetitle.text = '面试邀请通知'
        else:
            templatekey = result
            page.templatetitle.text = '面试结果通知'
        templatedata = []
        for item in templatekey:
            templatedata.append({'txt':item})
        page.list.data = templatedata

        page.input2.value = ''
        page.input3.value = ''
        page.input4.value = ''
        # thisformdata =showformdata(mo, page.options.index)
        # app.data.alldata = thisformdata
        # page.list1.data = thisformdata

        # choosedbox = []
        # allopenid = []
        # for i in range(0, len(thisformdata)):
        #     choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':thisformdata[i]['openid']})
        #     allopenid.append(thisformdata[i]['openid'])
        # app.data.allopenid = allopenid
        # page.list2.data = choosedbox
        


    # def chooseAll():
    #     choosed = app.data.choosed
    #     alldata = app.data.alldata
    #     allopenid = app.data.allopenid

    #     if choosed != allopenid:
    #         choosed = allopenid
    #     else:
    #         choosed = []
    #     app.data.choosed = choosed

    #     choosedbox = []
    #     for i in range(0, len(alldata)):
    #         if alldata[i]['openid'] in choosed:
    #             choosedbox.append({'backgroundcolor':'', 'pic':chooseicon, 'openid':alldata[i]['openid']})
    #         else:
    #             choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':alldata[i]['openid']})
    #     page.list2.data = choosedbox

    # def singleChoose():
    #     choosed = app.data.choosed
    #     alldata = app.data.alldata

    #     if params.openid in choosed:
    #         choosed.remove(params.openid)
    #     else:
    #         choosed.append(params.openid)
    #     app.data.choosed = choosed
        
    #     choosedbox = []
    #     for i in range(0, len(alldata)):
    #         if alldata[i]['openid'] in choosed:
    #             choosedbox.append({'backgroundcolor':'', 'pic':chooseicon, 'openid':alldata[i]['openid']})
    #         else:
    #             choosedbox.append({'backgroundcolor':'', 'pic':'', 'openid':alldata[i]['openid']})
    #     page.list2.data = choosedbox

    def sendMessage():
        choosed = app.data.choosed
        mo.console(choosed)
        if templateID[int(page.picker.value)] == '面试邀请通知':
            templateindex = invateid
            
        else:
            templateindex = resultid
        
        choosed = app.data.choosed
        if choosed:
            for item in choosed:
                thisdata = mo.db.person.find({'openid':item})
                mo.notice.send(item, templateindex,'index',[thisdata[0]['nickname'], page.input2.value, page.input3.value, page.input4.value])        
            mo.showAlert('提示', '发送成功！')
            
            onInit()
        else:
            mo.showAlert('提示', '还没选择收件人')
            return
        
    

class managepage(Page):
    background = '#F5F5F5'
    def UI():
        with List(id='list'):
            with Box(pos=[0, 20, 750, 220]):
                Box(pos=[0, 0, 750, 200], backgroundColor='#ffffff')
                Image(pos=[10, 10, 110, 110], borderRadius='50%', src='{item.headpic}')
                Text(pos=[150, 0, 750, 50], textAlign='left', lineHeight=50, text='{item.title}')
                Text(pos=[150, 50, 500, 50], textAlign='left', lineHeight=50, text='{item.nickname}')
                Text(pos=[150, 100, 500, 50], textAlign='left', lineHeight=50, fontSize=30, text='{item.createtime}')
                Text(pos=[600, 0, 150, 50], textAlign='center', lineHeight=50, fontSize=30, text='{item.state}')
                with Button(pos=[400, 150, 150, 50], textAlign='center', lineHeight=50, type='primary', text='查看'):
                    this.onTap = moui.goto('entry', index='{item.id}', title='{item.title}')
                with Button(pos=[580, 150, 150, 50], textAlign='center', lineHeight=50, type='primary', text='审核'):
                    this.onTap = moui.request(check, index='{item.id}')
                

    def onInit():
        formdata = form(user.openid, mo)
        alldata = formdata.get_all_formdata()
        for item in alldata:
            thisuser = person(user, mo)
            personinfo = thisuser.showpersoninfo()
            item['nickname'] = personinfo[0]['nickname']
            item['headpic'] = personinfo[0]['headpic']
            item['createtime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['createtime']))
            if item['state'] == 0:
                item['state'] = '待审核'
            else:
                item['state'] = '已审核'
        page.list.data = alldata

    def check():
        formdata = form(user.openid, mo)
        thisform = formdata.update_form_state(params.index)
        if thisform:
            mo.showAlert('提示', '审核通过')
        else:
            mo.showAlert('提示', '取消成功')
        onInit()
        
        

class invitemanager(Page):
    background = '#F5F5F5'
    enableShare=True
    def UI():
        with Box(pos=[0, 0, 750, 400], backgroundColor='#ffffff'):
            Text(id='title', pos=[0, 50, 750, 50], textAlign='center', lineHeight=50)
            Text(pos=[0, 100, 750, 50], textAlign='center', lineHeight=50, text='新增管理员请将本页分享给好友')
            with ShareButton(pos=['center', 200, 450, 80], textAlign='center', lineHeight=80, type='primary', text='转发', formType='submit'):
                pass
        Text(pos=[0, 400, 750, 50], textAlign='center', lineHeight=50, text='管理员')
        with List(id='list', pos=[0, 450]):
            with Box(size=[750, 150], backgroundColor='#ffffff'):
                Image(pos=[20, 20, 110, 110], borderRadius='50%', src='{item.headpic}')
                Text(pos=[150, 20, 500, 50], textAlign='left', lineHeight=50, text='{item.nickname}')
                with Button(pos=[400, 70, 150, 60], type='primary', textAlign='center', lineHeight=60, text='移除'):
                    this.onTap = moui.request(deleteManager, openid='{item.openid}')
    def onInit():
        thisform = form(user.openid, mo)
        thisform_data = thisform.get_formdata(page.options.index)

        thisperson = person(user, mo)
        thisperson_data = thisperson.get_person_info(thisform_data[0]['openid'])
        
        page.share.title = thisperson_data[0]['nickname']+'邀请你成为'+page.options.title+'管理员'
        page.share.options = {'index':page.options.index, 'title':page.options.title}
        page.share.page = 'acceptmanager'

        page.title.text = page.options.title
        
        thismanger = manager(user.openid, mo)
        thismanger_openid = thismanger.get_form_manager(page.options.index)
        
        managerinfo = []
        for item in thismanger_openid:
            thisperson_data = thisperson.get_person_info(item['managerid'])
            managerinfo.append({'openid':thisperson_data[0]['openid'], 'nickname':thisperson_data[0]['nickname'], 'headpic':thisperson_data[0]['headpic']})
        page.list.data = managerinfo
        


    def deleteManager():
        thisperson = manager(params.openid, mo)
        thisperson.deletemanager()
        mo.showTips('移除成功')
        onInit()

class acceptmanager(Page):
    def UI():
        with Box(pos=[0, 0, 750, 400], backgroundColor='#ffffff'):
            Text(id='content',pos=[0, 100, 750, 50], textAlign='center', lineHeight=50)
        with Button(pos=['center', 600, 400, 80], type='primary', openType='getUserInfo', textAlign='center', lineHeight=80, text='接受'):
            this.onTap = accept 
        with Button(pos=['center', 700, 400, 80], type='primary', formType='submit', textAlign='center', lineHeight=80, text='拒绝'):
            this.onTap = moui.switchTab('index')
    def onOnit():
        thismanger = manager(user.openid, mo)
        
        if thismanger.is_manager():
            mo.goto('index')
        else:
            thisform = form(user.openid, mo)
            thisform_data = thisform.get_formdata(page.options.index)

            thisperson = person(user, mo)
            thisperson_data = thisperson.get_person_info(thisform_data[0]['openid'])
            
            page.content.text = thisperson_data[0]['nickname']+'邀请你成为'+page.options.title+'管理员'

    def accept():
        #更新用户个人信息
        thismanger = manager(user.openid, mo)
        thismanger.addmanager(page.options.index)
        mo.switchTab('mine')




