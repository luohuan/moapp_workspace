from tools import *
# placeholderkey = ['title', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7', 'input8', 'input9', 'input10', 'input11']



class entry(Page):
    background = '#ffffff'
    disableScroll=True
    enableShare=True
    def UI():
        with ScrollBox(id='scroll', pos=[0, 0], scrollY=True, width=750, height='90%'):
            with Box(pos=[0, 0, 750, 200], position='relative', borderBottom='1px solid #888'):
                Text(id='title', pos=[0, 40, 750, 50], textAlign='left', lineHeight=50, fontWeight=700)
                Text(id='intro', pos=[20, 100, 710, 40], textAlign='left', lineHeight=40, fontSize=30)
            for i in range(1, 16):
                with Box(id='box%s'%i, size=[750, 160], backgroundColor='#ffffff', position='relative', hidden=True):
                    Text(id='input%s'%i, pos=[20, 20, 680, 50], textAlign='left', lineHeight=50)
                    Input(id='input_%s'%i, pos=[20, 80, 710, 60], border='1px solid #F5F5F5', textAlign='left', paddingLeft=20, paddingRight=20, 
                        lineHeight=60)    
        with Box(id='submit', bottom=0, width=750, height=80, position='fixed', backgroundColor='#ffffff'):
            with Button(pos=[20, 0, 710, 80], lineHeight=80, textAlign='center', text='提交', backgroundColor=navicolor, color='#ffffff', openType='getUserInfo'):
                this.onTap = submit
        # with Box(id='edit', bottom=0, width=750, height='10%', position='fixed', backgroundColor='#ffffff', hidden=True):
        #     with Button(type='primary', pos=['center', 20, 450, 80], lineHeight=80, textAlign='center', text='重新编辑', formType='submit'):
        #         this.onTap = moui.setData(__mask_hidden=True, __submit_hidden=False, __edit_hidden=True)
    # def countkey(listid):
    #     #判断显示几个选项
    #     listdata = mo.db.createlist.find({'id':listid})
    #     if len(listdata) == 9:
    #         pass
    #     elif len(listdata) == 10:
    #         page.

    def onInit():
        
        

        # thisuser = formdata(user.openid, mo)
        # if thisuser.haveformdata(page.options.index):
        #     mo.redirectTo('mylistdetail', index=page.options.index)
        #     return
        # else:
        #     pass

        thisform = form(user.openid, mo)
        formdatainfo = thisform.get_formdata(page.options.index)
        
        mo.setNavibarTitle(formdatainfo[0]['title'])
        page.share.title = '邀请你参与'+formdatainfo[0]['title']
        page.share.page = 'entry'
        page.share.options = {'index':formdatainfo[0]['id'], 'title':formdatainfo[0]['title']}

        app.data.formdata = formdatainfo
        page.title.text = formdatainfo[0]['title']
        page.intro.text = formdatainfo[0]['intro']
        
        for k, v in formdatainfo[0].items():
            if k in INPUTID:
                page.getElement(BOX[INPUTID.index(k)]).show() 
                page.getElement(k).text = str(INPUTID.index(k)+1)+'.'+v
                
            else:
                pass

    def submit():
        #更新用户信息
        thisuser = person(user, mo)
        if thisuser.is_newuser():
            thisuser.addpersoninfo()
        else:
            pass
        thisdata = app.data.formdata
        
        formdict = {}
        for k in thisdata[0].keys():
            if k in INPUTID:
                formdict[k] = page.getElement(FORMDATAID[INPUTID.index(k)]).value
            else:
                pass

        
        formdict['formid'] = page.options.index
        

        newform = formdata(user.openid, mo)
        newform.addformdata(formdict)

        mo.notice.send(user.openid, entryid,'mine',[page.options.title, user.nickName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '后续报名状态通过本通知送达，点击进入了解'])        
        # mo.notice.send(app.data.createopenid, 'WN2KK_bl5lTluvPcHgBDkPnM4Qw8jHtpLWc79JP9kQ0','index',[page.options.title, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        mo.redirectTo('entryresult')

class entryresult(Page):
    enableShare = False
    def UI():
        Image(pos=['center', 100, 200, 200], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/1fd7185308df38f0999c564cff79fdd7.png')
        Text(pos=['center', 300, 750, 50], textAlign='center', lineHeight=50, text='报名成功', fontSize=28)
        Text(pos=['center', 500, 750, 50], textAlign='center', lineHeight=50, text='将以服务通知形式发送状态更新')
        with Button(pos=['center', 600], type='primary', color='#fff', text='查看状态', backgroundColor=navicolor, formType='submit'):
            this.onTap = moui.switchTab('mine')
    def onInit():
        pass






                


