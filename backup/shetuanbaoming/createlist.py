import time
from entrylist import *
from tools import *

placeholdervalue = ['社团报名表', '姓名', '性别', '学号', '院系', '联系方式', '', '', '', '', '']

option_choosed_color = '#F5F5F5'


class prelist(Page):
    background = '#fff'
    def UI():
        Text(pos=[20, 40, 20, 30], textAlign='left', lineHeight=30, text='*', color='#e64340')
        Text(pos=[40, 40, 600, 30], textAlign='left', lineHeight=30, fontSize=28, color='#888', text='活动名称')
        # with Box(pos=[0, 90, 750, 100], backgroundColor='#ffffff'):
        Input(id='title', pos=[20, 90, 710, 80], textAlign='left', lineHeight=100, paddingLeft=20, paddingRight=20, border='1px solid #256DF2', placeholder='请输入标题')
        # Text(pos=[50, 150, 600, 50], textAlign='left', lineHeight=50, text='表单名称')
        Text(pos=[40, 210, 710, 30], textAlign='left', lineHeight=30, fontSize=28, color='#888', text='活动简介')
        # with Box(pos=[0, 340, 750, 240], backgroundColor='#ffffff'):
        Textarea(id='intro', pos=[20, 260, 670, 240], padding=20, border='1px solid #256DF2', placeholder='简单介绍这个活动吧', lineHeight=50)

        with Button(pos=[20, 600, 710, 94], textAlign='center', lineHeight=94, color='#fff', text='下一步', backgroundColor=navicolor, formType='submit'):
            this.onTap = createlist
        

    def onInit():
        if page.options.title or page.options.intro:
            page.title.value = page.options.title
            page.intro.value = page.options.intro
        else:    
            page.title.value = ''
            page.intro.value = ''

    def createlist():
        if page.title.value:
            mo.redirectTo('addlist', title=page.title.value, intro=page.intro.value)
            app.data.option_choosed = []
        else:
            mo.showAlert('提示', '请输入活动名称哦')


class addlist(Page):
    background = greybackground
    def UI():
        with ScrollBox(id='scroll', pos=[0, 0], scrollY=True, width=750, height='90%'):
            with Box(pos=[0, 0, 750, 200], position='relative', backgroundColor='#ffffff', borderBottom='1px solid #888'):
                Text(id='title', pos=[0, 40, 750, 50], textAlign='center', lineHeight=50, fontWeight=700)
                Text(id='intro', pos=[20, 100, 710, 40], textAlign='left', lineHeight=40, fontSize=30)
            
            with List(id='list', position='relative'):
                with Box(size=[750, 190], position='relative'):
                    Box(pos=[0, 0, 750, 170], backgroundColor='#ffffff')
                    Text(pos=[20, 20, 400, 40], textAlign='left', lineHeight=40, text='{item.option}')
                    Box(pos=[20, 70, 710, 60], border='1px solid #256DF2')
                    with Image(pos=[650, 10, 50, 50], src='{item.delete}'):
                        this.onTap = moui.request(deleteoption, index='{item.index}')
                    
            with Box(pos=[0, 0, 750, 120], position='relative', marginTop=20):
                with Button(pos=['center', 'center', 550, 80], formType='submit', color=navicolor, plain=True, textAlign='center', border='1px dotted #256DF2', lineHeight=80, text='添加选项+'):
                    this.onTap = moui.goto('editoption')
            Box(size=[750, 200], position='relative')
        with Button(bottom=0, left=20, size=[710, 94], textAlign='center', lineHeight=94, color='#fff', backgroundColor=navicolor, text='创建报名', openType='getUserInfo'):
            this.onTap = createform
                    
    def onInit():
        page.title.text = page.options.title
        page.intro.text = page.options.intro
        
        option_choosed = []  #设置默认选项，按顺序显示
        app.data.option_choosed = option_choosed
        
        

        # for i in range(0, 15):
        #     if i < len(option_choosed):
        #         page.getElement(BOX[i]).show()
        #         page.getElement(INPUTID[i]).text = str(i+1)+'.'+option_choosed[i]
        #     else:
        #         page.getElement(BOX[i]).hide()
        #         page.getElement(INPUTID[i]).text = ''

    def onShow():
        option_choosed = app.data.option_choosed
        thisform = []
        i = 1
        for item in option_choosed:
            thisform.append({'option':str(i)+'.'+item, 'index':i, 'delete':'http://material.motimaster.com/ywjiang/ceshiyong/demo/abeceac75367512bae810400fd62cbba.png'})
            i += 1
        page.list.data = thisform
        page.scroll.scrollTop = 2000
        
    def clickoption():
        pass

        

    def deleteoption():
        option_choosed = app.data.option_choosed
        del option_choosed[params.index-1]
        
        app.data.option_choosed = option_choosed
        thisform = []
        i = 1
        for item in option_choosed:
            thisform.append({'option':str(i)+'.'+item, 'delete':'http://material.motimaster.com/ywjiang/ceshiyong/demo/abeceac75367512bae810400fd62cbba.png'})
            i += 1
        page.list.data = thisform
        

    def createform():
        option_choosed = app.data.option_choosed
        if option_choosed:
            formdetail = {}
            formdetail['label'] = []
            i = 0
            for item in option_choosed:
                formdetail[INPUTID[i]] = item
                x = 0
                for item1 in options_template:
                    if item1['option'] == item:
                        formdetail['label'].append({INPUTID[option_choosed.index(item)]:options_template[x]['label']})        
                        break
                    else:    
                        x += 1
                i += 1
            formdetail['openid'] = user.openid
            formdetail['title'] = page.options.title
            formdetail['intro'] = page.options.intro
            
            newform = form(user.openid, mo)
            newform.addform(formdetail)
            
            mo.redirectTo('createsuccess')
        else:
            mo.showAlert('提示', '还没添加内容')
            return

class editoption(Page):
    background = '#fff'
    def UI():
        
        Text(pos=[20, 40, 600, 30], textAlign='left', lineHeight=30, fontSize=28, text='请输入选项')
        
        Input(id='input', pos=[20, 90, 500, 80], textAlign='left', lineHeight=80, backgroundColor='#fff', border='1px solid #256DF2', 
            paddingLeft=20, paddingRight=20, placeholder='请输入选项')
        with Text(pos=[550, 90, 200, 80], textAlign='center', lineHeight=80, color=navicolor, text='确定'):
            this.onTap = submitoption
        
        Text(pos=[20, 300, 500, 50], textAlign='left', lineHeight=50, fontSize=28, text='常用模板')
        with Grid(id='grid', pos=['center', 390, 690, 170], column=4):
            with Box(pos=[0, 0, 170, 170], border='1px solid #888'):
                Image(pos=['center', 40, 60, 60], src='{item.icon}')
                Text(pos=['center', 100, 150, 40], textAlign='center', lineHeight=40, fontSize=30, text='{item.option}', color=navicolor)
                this.onTap = moui.request(choose_template, option='{item.option}')

    def onInit():
        page.input.value = ''
        page.grid.data = options_template


    def choose_template ():
        option_choosed = app.data.option_choosed
        option_choosed.append(params.option)
        app.data.option_choosed = option_choosed
        mo.goBack()
        

    def submitoption():
        if page.input.value:
            option_choosed = app.data.option_choosed
            option_choosed.append(page.input.value)
            app.data.option_choosed = option_choosed
        mo.goBack()
        



class createsuccess(Page):
    naviBarTitle = '创建成功'
    background = '#fff'
    disableScroll=True
    enableShare=False
    def UI():
        Image(pos=['center', 100, 200, 200], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/1fd7185308df38f0999c564cff79fdd7.png')
        Text(pos=['center', 300, 750, 50], textAlign='center', lineHeight=50, text='创建成功')
        Text(pos=['center', 350, 750, 50], textAlign='center', lineHeight=50, text='你可前往管理页面管理')
        with Button(pos=['center', 600], type='primary', color='#fff', text='前往管理', backgroundColor=navicolor, formType='submit'):
            this.onTap = moui.redirectTo('listmanage')

        
    def onInit():
        pass
    
    def gotoentry():
        mo.goto('entry', index=page.options.index, title=page.options.title)

    

class shareform(Page):
    background = greybackground
    def UI():
        with Box(pos=[0, 40, 750, 200], backgroundColor='#fff'):
            Text(id='title', pos=[40, 20, 650, 50], textAlign='left', lineHeight=50, fontWeight=700)
            Text(id='intro', pos=[40, 80, 650, 50], textAlign='left', lineHeight=50)
        with Button(pos=['center', 300], type='primary', backgroundColor=navicolor, textAlign='center', text='二维码下载', formType='submit'):
            this.onTap = createQrcode
        with ShareButton(pos=['center', 450], type='primary', backgroundColor=navicolor, textAlign='center', text='微信群邀请', formType='submit'):
            pass
    
    def onInit():
        page.options.index
        thisform = form(user.openid, mo)
        thisforminfo = thisform.get_formdata(page.options.index)
        page.title.text = thisforminfo[0]['title']
        page.intro.text = thisforminfo[0]['intro']

        mo.setNavibarTitle(thisforminfo[0]['title'])
        page.share.title = '邀请你参与'+thisforminfo[0]['title']
        page.share.page = 'entry'
        page.share.options = {'index':thisforminfo[0]['id']}


    def createQrcode():
        params = {
            'page': 'entry',
            'width': 200,
            'options': {
                'index': page.options.index
            }
        }
        
        qrcode = mo.acode.getWxAcodeUrl(params)
        mo.saveImage(qrcode['url'])













