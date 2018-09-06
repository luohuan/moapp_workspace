import re


enter_icon = 'http://material.motimaster.com/wangbing1534928192000/enter.png'
avatar = 'http://material.motimaster.com/wangbing1534311338000/avatar.png'


class user_info(Page):
    naviBarTitle = '个人信息详情'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = '#EEEEEE'
    enableShare = True

    def UI():

        with Box(pos=['center', 0], size=[750, 220], borderBottom=0, background='white', position='relative',onTap=fix_head_url):
            Image(name='head_url', pos=[30, 'center'], size=[180, 180], borderRadius='50%', mode='aspectFill')
            Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
            Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

        with Box(marginTop=40, size=[750, 400], background='white', position='relative'):
            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative', onTap=moui.goto('fix_name')):
                Text(text='昵称：', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='name', pos=[150 ,'center'], fontSize=30, height=100, lineHeight=100)
                #Input(name='input_name', pos=[150, 'center'], border='1px solid black', hidden=True, height=80)
                Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative',onTap=fix_gender):
                Text(text='性别：',pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='gender',  pos=[155,'center'], fontSize=30, height=100, lineHeight=100)
                Text(name='gender1', text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(name='gender2',src=enter_icon, pos=[695, 'center'], size=[30, 30])

            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative', onTap=moui.goto('fix_signature')):
                Text(text='个性签名：', pos=[0, 'center'], fontSize=30, height=100, lineHeight=100,padding=20, position='relative')
                Text(name='signature', pos=[155,'center'], fontSize=30, height=100, lineHeight=100)
                Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

            with Box(pos=['center', 0], size=[750, 100], position='relative', onTap=moui.goto('fix_location')):
                Text(text='宿舍区：', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='location',  pos=[155,'center'], fontSize=30, height=100, lineHeight=100)
                #Input(name='input_location', pos=[150, 'center'], border='1px solid black', hidden=True, height=80)
                Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

        with Box(left=0, width=750, height=80, position='relative'):
            Text(fontSize=26, textAlign='justify', color='#898989', width=710, left='center', top='center',text='下面的信息不被公开显示')

        with Box(marginTop=0, size=[750, 300], background='white', position='relative'):
            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative', onTap=fix_phone):
                Text(text='联系电话：', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='phone', pos=[155, 'center'], fontSize=30, height=100, lineHeight=100)
                #Input(name='input_phone', pos=[220, 'center'], border='1px solid black', hidden=True, height=80, type='number')
                Button(name='phone_but', text='绑定手机号', top='center',right=20, fontSize=26, openType='getphonenumber', hidden=True,
                    background='#f4bc33', color='black', width=150, height=40, lineHeight=40, onTap=get_phone_number)
                with Box(id='phonebox', pos=[640, 0, 100, 100], hidden=True):
                    Text(name='phone_fix',text='修改', pos=[0, 'center'], fontSize=26, color='#898989')
                    Image(name='phone_fix2', src=enter_icon, pos=[55, 'center'], size=[30, 30])

            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative', onTap=moui.goto('fix_weixin_account')):
                Text(text='微信号：', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='weixin_account', pos=[155, 'center'], fontSize=30, height=100, lineHeight=100)
                Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

            with Box(pos=['center', 0], size=[750, 100], position='relative', onTap=fix_authentication):
                Text(text='认证信息：', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100,padding=20)
                Text(name='authentication', pos=[0, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
                Text(text='修改', pos=[640, 'center'], fontSize=26, color='#898989')
                Image(src=enter_icon, pos=[695, 'center'], size=[30, 30])

        with Mask(name='mask01', opacity = 0.01):
            with Box(pos=[120, 330], background='white', size=[640, 90]):
                Radio(name='radio_gender', color='black',top=20, left=100, interval='100',onChange=onRadioChange, direction='x', fontSize=30)

    def onShow():
        if not user.get('isold'):
            user.set('realname', user.nickname)
            user.set('head_url',user.avatarUrl)
            user.set('sex', user.gender)
            user.set('location', '')
            user.set('signature', '')
            user.set('authentication', '')
            user.set('phone', '')
            user.set('weixin_account', '')
            user.set('isold', True)
        user.set('', user.nickname)
        page.head_url.src = user.get('head_url')
        page.name.text = user.get('realname')
        page.gender.text = get_gender(int(user.get('sex')))
        signature = user.get('signature')
        signature = intercept_str(signature, 28)
        page.signature.text = signature
        location = user.get('location')
        location = intercept_str(location, 30)
        page.location.text = location
        phone_number = user.get('phone')
        # hidden_but 从来判断绑定手机号按钮是否被隐藏，被隐藏后才允许点击修改手机号
        if not phone_number:
            page.phone_but.hidden = False
            page.phonebox.hide()
            # page.phone_fix.hidden = True
            # page.phone_fix2.hidden = True
            page.data.set('hidden_but', False)
        else:
            page.phone_but.hidden = True
            page.phonebox.show()
            # page.phone_fix.hidden = False
            # page.phone_fix2.hidden = False
        page.phone.text = phone_number
        page.weixin_account.text = user.get('weixin_account')
        page.authentication.text = user.get('authentication')

    def fix_phone():
        if page.data.get('hidden_but') or user.get('phone'):
            mo.goto('fix_phone')
        else:
            pass

    def get_phone_number():
        phone_number = user.phoneNumber
        mo.console(phone_number)
        if phone_number:
            user.set('phone', phone_number)
            page.phone.text = phone_number
        else:
            pass
        page.data.set('hidden_but', True)
        page.phone_but.hidden = True
        page.phone_fix.hidden = False
        page.phone_fix2.hidden = False

    def fix_head_url():
        mo.uploadImage(1, uploadSuccess, uploadFail)

    def uploadFail():
        pass

    def uploadSuccess():
        img_url = params.urls[0]
        user.set('head_url', img_url)
        page.head_url.src = img_url

    def fix_gender():
        page.radio_gender.data = [
            {'text': '男', 'value': 1, 'checked' : False},
            {'text': '女', 'value': 2, 'checked' : False},
        ]
        page.mask01.hidden = False

    def fix_authentication():
        mo.showAlert('抱歉','暂不支持')

    def onRadioChange():
        #page.radio_gender.hidden = True
        gender_index = int(page.radio_gender.value)
        user.set('sex', gender_index)
        page.gender.text = get_gender(gender_index)
        page.gender.hidden = False
        page.gender1.hidden = False
        page.gender2.hidden = False
        page.radio_gender.data = []


class fix_signature(Page):
    naviBarTitle = '设置个性签名'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = 'white'

    def UI():
        with Box(top=50, size=[750, 150], border=0, background='#FDF5E3'):
            Text(text='确定', right=50, top='center', fontSize=30, color='#f4bc33', onTap=checkInput)
            Textarea(name='input', placeholder = ' 写写你主要卖什么，会有更多人关注你...', left=20, size=[580, 150], border=0,fontSize=30, lineHeight=50,paddingTop=20)
        
    def onInit():
        page.input.value = user.get('signature')

    def checkInput():
        if len_str(page.input.value) > 60:
            mo.showAlert('格式有误', '输入过长')
        else:
            user.set('signature', page.input.value)
            mo.goBack()


class fix_name(Page):
    naviBarTitle = '设置昵称'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = 'white'

    def UI():
        with Box(top=50, size=[750, 100], border=0, background='#FDF5E3'):
            Text(text='确定', right=50, top='center', fontSize=30, color='#f4bc33', onTap=checkInput)
            Input(name='input', left=20, size=[600, 100], border=0, fontSize=30)

    def onInit():
        page.input.value = user.get('realname')
        page.share.title = "这是我的二手交易小站，快来看看吧！"
        page.share.imageUrl = 'http://material.motimaster.com/wangbing1534903202000/pic.png'
        page.share.page = 'pub_list'
        page.share.options = {'publisher_id': page.options.openid}

    def checkInput():
        # 13个汉字或26个小写字母或20个大写字母
        if len_str(page.input.value) > 26:
            mo.showAlert('格式有误', '输入过长')
        else:
            user.set('realname', page.input.value)
            mo.goBack()


class fix_location(Page):
    naviBarTitle = '设置地区'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = 'white'

    def UI():
        with Box(top=50, size=[750, 150], border=0, background='#FDF5E3'):
            Text(text='确定', right=50, top='center', fontSize=30, color='#f4bc33', onTap=checkInput)
            Textarea(name='input', left=20, size=[580, 150], border=0,fontSize=30, lineHeight=50,paddingTop=20)

    def onInit():
        page.input.value = user.get('location')

    def checkInput():
        if len_str(page.input.value) > 60:
            mo.showAlert('格式有误', '输入过长')
        else:
            user.set('location', page.input.value)
            mo.goBack()


class fix_phone(Page):
    naviBarTitle = '设置电话号码'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = 'white'

    def UI():
        with Box(top=50, size=[750, 100], border=0, background='#FDF5E3'):
            Text(text='确定', right=50, top='center', fontSize=30, color='#f4bc33', onTap=checkInput)
            Input(name='input', left=20, size=[600, 100], border=0, fontSize=30)

    def onInit():
        page.input.value = user.get('phone')

    def checkInput():
        # 加上 page.input.value != '' 这句，用户可以清空手机号
        if page.input.value != '' and not is_phone_number(page.input.value):
            mo.showAlert('格式有误', '请输入合法的手机号')
        else:
            user.set('phone', page.input.value)
            mo.goBack()


class fix_weixin_account(Page):
    naviBarTitle = '填写微信号'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = 'white'

    def UI():
        with Box(top=50, size=[750, 100], border=0, background='#FDF5E3'):
            Text(text='确定', right=50, top='center', fontSize=30, color='#f4bc33', onTap=checkInput)
            Input(name='input', left=20, size=[600, 100], border=0, fontSize=30)

    def onInit():
        page.input.value = user.get('weixin_account')

    def checkInput():
        user.set('weixin_account', page.input.value)
        mo.goBack()


def is_phone_number(number):
    if re.match(r'^1[3,4,5,7,8]\d{9}$', number):
        return True
    else:
        return False


def get_gender(index):
    gender_list = ['', '男', '女']
    return gender_list[index]


def len_str(string):
    count = 0
    for i in string:
        if 65 <= ord(i) <=90:
            count += 26 / 20
        elif 97 <= ord(i) <=122 or i == ' ':
            count += 1
        else:
            count += 26 / 13
    return count

def intercept_str(string, num):
    count = 0
    j = 0
    for i in string:
        count += word_width(i)
        j += 1
        if count >= num:
            return string[0: j] + '...'
    return string

def word_width(word):
    if 65 <= ord(word) <=90:
        return 26 / 20
    elif 97 <= ord(word) <=122 or word == ' ':
        return 1
    else:
        return 26 / 13