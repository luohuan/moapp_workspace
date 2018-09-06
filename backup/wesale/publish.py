import re
import time
from goods_db import *
from permission import *
from tools import *

kind_data =['出售','求购','赠送']
newness_data = ['10','9','8','7','6','5','4','3','2','1']
fetch_method_data = ['自提','送货上门']

sharepic = ['http://material.motimaster.com/appmaker/xiaodong/6521.png',
                     'http://material.motimaster.com/appmaker/xiaodong/6522.png',
                     'http://material.motimaster.com/appmaker/xiaodong/6523.png']

sharepictitle=['学姐要毕业，1000件商品免费领！',
       '武大同学自己的二手交易小站，是校友就送好东西~',
       '武大人的校园二手平台，学姐的东西先到先领',
       '武大人的二手交易平台，就差你不知道了！']

upload_pic_add_icon = 'http://material.motimaster.com/appmaker/goupeng/6342.png'
delete_icon = 'http://material.motimaster.com/appmaker/goupeng/4531.png'

class PublishPage(Page):

    naviBarTitle='发布商品'
    naviBarColor='#f4bc33'
    naviBarStyle='black'

    background = '#eeeeee'
    enableShare=True

    text='发布'
    selectedIconPath='images/fabu2.png'
    iconPath='images/fabu1.png'

    def UI():
        top = 0
        height = 70
        height_box = 60
        width_box = 750
        padding1 = 10
        padding2 = 10

        with Box(pos=[0,30],size=[750,100],background='white'):
            SinglePickerButton(id='picker_type',text='商品属性',pos=[30,0],size=[720,100],color='#f4bc33',background='white',textAlign='left',fontSize=32,lineHeight=100,range=kind_data,fontWeight='bold',onChange = onSelectorPickerTextKindChange)
            Image(src='http://material.motimaster.com/wangbing1534928192000/enter.png', pos=[660, 'center'], size=[40, 40])
            with Button(id='pickermask', pos=[0, 0, 750, 100], border=0, plain=True, openType='getUserInfo', hidden=True):
                this.onTap = clickpickermask
        with Box(pos=['center', 140], size=[750, 174],background='white'):
            Input(name='title_input',pos=[0,10], size=[720,80],placeholder = ' 输入标题，如凤凰牌自行车，20字以内',background='white',fontWeight='bold',lineHeight=30,fontSize=32,padding=20,onConfirm=titleInputEnd)
            Input(name='price_input',pos=[0,92], size=[720,80], placeholder=' 输入价格，便宜才是竞争力哟！',type='digit',background='white',lineHeight=30,fontSize=32,padding=20,onConfirm=priceInputEnd)
            Box(pos=['center', 90], size=[750, '1px'], background='#eeeeee')
            Box(pos=['center', 173], size=[750, '1px'], background='#eeeeee')

        with Box(pos=['center',314],background='white',size=[750,460]):
            Textarea(name='description',pos=[20,40],size=[710,100], placeholder=' 输入描述，品牌、规格、几成新、取货方式、购买渠道、转手原因等信息，建议150字以内哟~',fontSize=30,lineHeight=30)
            # Box(pos=[20,200],background='#F4F4F4',size=[200,200])
            # Box(pos=[230,200],background='#F4F4F4',size=[200,200])
            # Box(pos=[440,200],background='#F4F4F4',size=[200,200])

            with ScrollBox(size=[750, 250], scrollY=True,pos=['center',170]):
                with Grid(name='grid_pic', pos=['center', 20], size=[700, 210], column=3):
                    with Box(size=[200,200]):
                        Image(pos=['center','center'], size=[150,150], src='{item.src}', mode='aspectFill',onTap=moui.request(onUploadImg,src='{item.src}',pos='{item.pos}'))
                        Image(pos=[150,20], size=[40,40], src='{item.delete_icon}', mode='aspectFill',onTap=moui.request(onDeleteImg,src='{item.src}',pos='{item.pos}'))
            pass

       #此处是原有的新旧程度的修改

        # with Box(pos=['center',785],background='white',size=[750,200]):
        #     SinglePickerButton(id='picker_newness',text='新旧程度',textAlign='left',pos=[30,0],size=[720,100],color='black',background='white',fontSize=30,lineHeight=100, range=newness_data,onChange = onSelectorPickerTextNewsnessChange)
        #     SinglePickerButton(id='picker_fetch_method',text='取货方式',textAlign='left',pos=[30,100],size=[720,100],color='black',background='white',fontSize=30,lineHeight=100, range=fetch_method_data,onChange = onSelectorPickerTextFetchmethodChange)

        #     Image(src='http://material.motimaster.com/wangbing1534928192000/enter.png', pos=[660, 28], size=[40, 40])
        #     Image(src='http://material.motimaster.com/wangbing1534928192000/enter.png', pos=[660, 128], size=[40, 40])
        #     Box(pos=['center', 100], size=[750, '1px'], background='#eeeeee')




        #with Box(pos=['center', 850], size=[750, 100], background='white', position='relative',onTap=moui.goto('fix_picker_newness')):
           # Text(text='崭新程度：', pos=[20, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
            #Text(name='picker_newness', pos=[160, 'center'], fontSize=30, height=100, lineHeight=100)
            #Image(src='http://material.motimaster.com/wangbing1534928192000/enter.png', pos=[620, 'center'], size=[40, 40])
            #Box(pos=['center', 100], size=[680, '1px'],position='relative', background='#eeeeee')

        #with Box(pos=['center', 850], size=[750, 100], background='white', position='relative',onTap=moui.goto('fix_picker_newness')):
            #Text(text='取货方式：', pos=[20, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
            #Text(name='picker_fetch_method', pos=[160, 'center'], fontSize=30, height=100, lineHeight=100)
            #Image(src='http://material.motimaster.com/wangbing1534928192000/enter.png', pos=[620, 'center'], size=[40, 40])

        with Box(id='switchbox', pos=[0,785],size=[750,140]):
            with Box(pos=[30,10],size=[700,60]):
                Text(pos=[70,'center'],text='我同意',fontSize=30,color='black',lineHeight=60,width=100,textAlign='left')
                with Box(pos=[160,0],size=[430,60]):
                    Text(pos=[0,'center'],text='《二手交易服务用户协议》',fontSize=30,color='#FF9153',lineHeight=40,textAlign='left',onTap=onMask01Clicked)
            with Box(pos=[30,72],size=[700,60]):
                Text(pos=[70,'center'],text='我同意',fontSize=30,color='black',lineHeight=60,width=100,textAlign='left')
                with Box(pos=[160,0],size=[430,60]):
                    Text(pos=[0,'center'],text='《二手交易用户分享计划1.0》',fontSize=30,color='#FF9153',lineHeight=40,textAlign='left',onTap=onMask02Clicked)


            Switch(id='switch_agreement', pos=[30, 6], size=[40, 40], type='checkbox')
            Switch(id='switch_activity', pos=[30, 70], size=[40, 40],type='checkbox')

        # Box(pos=[0, 885], size=[750, 400], color='eeeeee')

        Button(pos=['center',970], size=[400, 94], text='发布',background='#f4bc33',lineHeight=94,color='white',borderradius=10,fontSize=36,onTap=onButtonPublishClicked)

        #Button(pos=[615, 15], size=[120, 60], text='保存', background='#eeeeee', lineHeight=60, color='#757575',fontSize=32)

        with Mask(name='mask', locked=True, opacity=0.7):
            with Box(pos=['center',230],background='white',size=[600,460],borderRadius='5px 5px 0 0 '):
                Text(pos=['center',50],text='发布失败!',fontSize=35,color='#000',lineHeight=40,width=400,textAlign='center')
                Text(pos=['center',150],text='为了保证他人能够联系到您，需要获取您的手机号信息\n\n是否绑定？',fontSize=35,color='black',lineHeight=40,width=450,textAlign='center')
            # Text(pos=['center',150],size=[520, 500],text='未认证用户没有发布权限!是否要立即认证？',background='white',fontSize=35,color='black',lineHeight=40,width=400,textAlign='left')
            with Box(pos=['center',690],background='white',size=[600,100],borderRadius='0 0 5px 5px'):

                Button(text='我再等等', pos=[0, 0],size=[300,100],fontSize=35, color='black',background='white',border = '1px solid #eeeee', onTap=hideMask)
                Button(text='立即绑定', pos=[300, 0],size=[300,100],fontSize=35, color='white',background='#f4bc33',border = '1px solid #eeeee', openType='getphonenumber', onTap=getphonenumber)

        with Mask(name='mask02', locked=True, opacity=0.7):
            with ScrollBox(size=[700, 700], scrollY=True,pos=['center',200],background='white',borderRadius='5px 5px 0 0' ):
                Image(pos=['center',20],src='http://material.motimaster.com/goupeng1534761967000/微信图片_20180820184430.jpg', mode='widthFix',width=600,borderRadius='5px')
                pass
            Button(text='我知道了', pos=['center', 900],size=[700,100],fontSize=35, color='white',background='#E64340',borderRadius='0 0 5px 5px', onTap=onMask01HiddenClicked)

        with Mask(name='mask03', locked=True, opacity=0.7):
            with ScrollBox(size=[700, 700], scrollY=True,pos=['center',200],background='white',borderRadius='5px 5px 0 0 '):
                Image(pos=['center',20],src='http://material.motimaster.com/goupeng1534768968000/微信图片_20180820204202.jpg', mode='widthFix',width=600,borderRadius='5px')
                pass
            Button(text='我知道了', pos=['center', 880],size=[700,94],fontSize=36, color='white',background='#E64340',borderRadius='0 0 5px 5px',onTap=onMask02HiddenClicked)

    #class fix_picker_newness(Page):
     #   naviBarTitle = '选择崭新程度'
      #  naviBarColor = '#f4bc33'
       # naviBarStyle = 'black'
        #background = '#eeeeee'

        #def UI():
         #   with Box(top=50, size=[750, 100], border=0, background='white'):
          #      Text(text='1成新’, left=50, top='center', fontSize=30, color='#E64340',onTap=onButtonClick)
           # with Box(top=150, size=[750, 100], border=0, background='white'):Text(text='1成新’, left=50, top='center', fontSize=30, color='white', onTap=onButtonClick)

        #def onButtonClick():
         #   user.set('picker_newness.text', page.picker_newness.value)
         #   mo.goBack()

    def onInit():
        mo.console('onInit')
        mo.removeTabBarBadge(0)
        page.picker_type.value = 0 
        page.grid_pic.data = [{'src':upload_pic_add_icon,'delete_icon':'','pos':0}]
        page.share.title = random.choice(sharepictitle)

        page.share.imageUrl = random.choice(sharepic)
        page.share.page = 'index'

    def onShow():
        mo.console('onshow')
        mo.removeTabBarBadge(0)
        isnew = is_newuser(user)
        mo.console(isnew)
        if isnew:
            page.pickermask.show()
        else:
            page.pickermask.hide()

        #user.set('isold', False)

        #page.mask.hidden = False
        #page.mask.hidden = True
    
    def clickpickermask():
        user.set('realname', user.nickname)
        user.set('head_url',user.avatarUrl)
        user.set('sex', user.gender)
        user.set('location', '')
        user.set('signature', '')
        user.set('authentication', '')
        user.set('phone', '')
        user.set('weixin_account', '')
        user.set('isold', True)    
        page.pickermask.hide()
        page.picker_type.text = '出售'
        page.picker_type.value = '0'

    def onMask01Clicked():
        page.description.hidden =True
        page.mask02.hidden = False

        # page.agreement_title.text = content_of_agreement['title']
        # page.agreement_content1.text = content_of_agreement['preface']
        pass
    def onMask02Clicked():
        page.description.hidden = True
        page.mask03.hidden = False
        pass
    def onMask01HiddenClicked():
        page.description.hidden = False
        page.mask02.hidden = True
        pass
    def onMask02HiddenClicked():
        page.description.hidden = False
        page.mask03.hidden = True
        pass
    def onDeleteImg():
        src = params.src
        pos = int(params.pos)
        mo.console("删除前：{}".format(pos))
        for data in page.grid_pic.data :
            mo.console(data)
        del page.grid_pic.data[pos]
        for data in page.grid_pic.data :
            mo.console(data)
        mo.console("删除hou：")
        for i in range(pos,len(page.grid_pic.data)):
            page.grid_pic.data[i]['pos'] = page.grid_pic.data[i]['pos'] -1
            mo.console("删除中：")
            for data in page.grid_pic.data :
                mo.console(data)
        mo.console("删除后：")
        for data in page.grid_pic.data :
            mo.console(data)
        pass
    def onUploadImg():
        src = params.src
        pos = int(params.pos)
        if(src == upload_pic_add_icon):
            mo.uploadImage( 9, uploadSuccess, uploadFail)
        else :
            # 更换图片

            # 滑动预览多张图片
            # temp = []
            # data_t  = page.grid_pic.data[:-1]
            # for img in page.grid_pic.data:
            #     temp.append(img['src'])
            # mo.previewImage(temp)

            # 预览单张图片
            mo.previewImage([src])
            
            pass

    def uploadFail():
        mo.console('失败了不可能的')

    def uploadSuccess():
        urls = params.urls
        pos = len(page.grid_pic.data)-1
        for url in urls:
            data = {
                'src': url,
                'delete_icon':delete_icon,
                'pos':pos
                }
            mo.console(data)
            page.grid_pic.data.insert(-1,data)
            pos = pos + 1
        page.grid_pic.data[-1]['pos'] = page.grid_pic.data[-1]['pos']+len(urls)
        app.data.grid_pic = page.grid_pic.data

    def onButtonClickedAuthentic():
        page.mask.hidden = True
        page.description.show()
        # mo.goto('index')
        # mo.goBack()
        mo.switchTab('mine')
    def hideMask():
        page.mask.hidden = True
        page.description.show()
    
    def publishgoods():
        type_ = kind_data[int(page.picker_type.value)]
        title = page.title_input.value
        price = float(page.price_input.value)
        description = page.description.value
        label = []
        # pic_list = ['http://material.motimaster.com/appmaker/goupeng/4834.jpg','http://material.motimaster.com/appmaker/goupeng/4835.jpg']
        pic_list = []
        if (len(page.grid_pic.data) == 1 and page.grid_pic.data[0]['src'] == upload_pic_add_icon):
            if page.picker_type.value == '1':
                pic_list = ['http://material.motimaster.com/yuweijiang1535974901000/WechatIMG1958.png']
            else:
                pic_list = ['http://material.motimaster.com/yuweijiang1535974901000/WechatIMG1960.png']
        else:
            temp = []
            for img in page.grid_pic.data:
                temp.append(img['src'])
            pic_list = temp[:-1]
            pass
        
        
        # newness = int(newness_data[int(page.picker_newness.value)])
        # pic_list = ['http://material.motimaster.com/appmaker/goupeng/4834.jpg','http://material.motimaster.com/appmaker/goupeng/4835.jpg']

        # deliver_type =  fetch_method_data[int(page.picker_fetch_method.value)]
        publisher = user.openid

        activity_take = page.switch_activity.value
        if activity_take != True:
            mo.console('activity_take is None')
            activity_take = False



        details = {
            'title': title,
            'price': price,
            'pic_list': pic_list,
            'description': description,
            'type': type_,
            'newness': 9,  # 默认9成新
            'deliver_type': '自提',  # 默认自提
            'publisher': publisher,
            'label': label,
            'activity_take': activity_take
        }

        mo.console(details)

        # 调用接口发布商品
        goods = Goods_db(user.openid, mo.db)
        res = goods.pub_goods(details)
        mo.console(res)
        # 将页面置位
        page.title_input.value = ''
        page.price_input.value = ''
        # page.picker_newness.value = ''
        page.picker_type.value = ''
        # page.picker_fetch_method.value = ''
        page.description.value = ''
        # page.picker_newness.text = '崭新程度'
        # page.picker_fetch_method.text = '取货方式'
        page.picker_type.value = 0
        page.picker_type.text = kind_data[int(page.picker_type.value)]
        page.grid_pic.data = [{'src': upload_pic_add_icon, 'delete_icon': '', 'pos': 0}]
        page.switch_activity.value = False
        page.switch_agreement.value = False
        page.switch_activity.checked = False
        page.switch_agreement.checked = False
        mo.goto('PublishSuccessPage', goods_id=res, title=details['title'], type=details['type'])
    
    def onButtonPublishClicked():

        canpublish = can_publish(user)  # 获取发布权限
        # mo.console(res)
        # # if res :
        # mo.console('res is true')
        # 检查用户输入
        # 价格检查
        pattern = '^([0-9]{1,6})([.][0-9]{1,2}){0,1}$'
        string = page.price_input.value
        res = re.match(pattern,string)
        if page.picker_type.value == '':
            #判断商品属性
            mo.showAlert('提示', '请选择商品属性')
            return
        elif (page.title_input.value == ''):
            # 标题检查
            mo.showAlert('输入错误', '标题为空，请输入标题')
            mo.console(page.title_input.value)
            return 
        elif(len(page.title_input.value)>15):
            # 标题检查
            mo.showAlert('输入错误', '标题长度不得超过15个字符！')
            mo.console(page.title_input.value)
            return 
        
        elif (string == '') :
            # 价格检查
            mo.showAlert('输入错误', '价格为空，请输入价格')
            mo.console(page.price_input.value)
            return
        elif(res is None) :
            # 价格检查
            mo.showAlert('输入错误', '价格输入格式错误,只能含有数字和小数点,小数点后数字不得超过2位，小数点前数字不得多于6位')
            mo.console(page.price_input.value)
            return
        # elif(page.picker_type.value == '') :
        #     # 品类检查
        #     # 默认为 ‘售出’
        #     mo.showAlert('输入错误', '请选择商品类别')
        #     mo.console('page.picker_type.value  is ')
        #     mo.console(page.picker_type.value )
        #     return
        #     pass
        # elif(page.picker_newness.value == '') :
        #     mo.showAlert('输入错误', '请选择崭新程度')
        #     return

        # elif(page.picker_fetch_method.value == '') :
        #     取货方式检查
        #     mo.showAlert('输入错误', '请选择取货方式')
        #     return

        elif(len(app.data.grid_pic) == 1 and app.data.grid_pic[0]['src'] == upload_pic_add_icon):
            mo.showAlert('', '请至少上传一张图片')
            return
        
        elif page.switch_agreement.value != True:
            mo.showAlert('', '请同意用户协议')
            return

        elif not canpublish:
            page.mask.show()
            page.description.hide()
            return
        else :
            publishgoods()


            
            # pass
        # else :
        #     page.mask.hidden = False
        #     mo.console('res is false')
    
    def getphonenumber():
        phone_number = user.phoneNumber
        if phone_number:
            user.set('phone', phone_number)
            
            publishgoods()
        else:
            mo.showTips('绑定失败')
        page.mask.hide()
        page.description.show()

    def onSelectorPickerTextKindChange():
        page.picker_type.text = kind_data[int(page.picker_type.value)]
        if page.picker_type.value == '0':
            page.switchbox.show()
        elif page.picker_type.value == '1':
            page.switchbox.hide()
            page.switch_agreement.value = True
            app.data.grid_pic = [
                {
                'pos': 0, 
                'delete_icon':'http://material.motimaster.com/appmaker/goupeng/4531.png',
                'src':'http://material.motimaster.com/yuweijiang1535974901000/WechatIMG1958.png'
                }, 
                {
                'pos': 1,
                'delete_icon':'', 
                'src':'http://material.motimaster.com/appmaker/goupeng/6342.png'
                }
            ]
        else:
            page.switchbox.hide()
            page.switch_agreement.value = True
            app.data.grid_pic = [
                {
                'pos': 0, 
                'delete_icon':'http://material.motimaster.com/appmaker/goupeng/4531.png',
                'src':'http://material.motimaster.com/yuweijiang1535974901000/WechatIMG1960.png'
                }, 
                {
                'pos': 1,
                'delete_icon':'', 
                'src':'http://material.motimaster.com/appmaker/goupeng/6342.png'
                }
            ]

    # def onSelectorPickerTextNewsnessChange():
    #     page.picker_newness.text = newness_data[int(page.picker_newness.value)]+'成新'

    # def onSelectorPickerTextFetchmethodChange():
    #     page.picker_fetch_method.text = fetch_method_data[int(page.picker_fetch_method.value)]

    def titleInputEnd():
        if(len(page.title_input.value)>15):
            mo.showAlert('', '标题长度不得超过15个字符！')
            mo.console(page.title_input.value)
        pass
    def priceInputEnd():
        pass

    def onShow():
        mo.console('发送消息')

icon_confirm = 'http://material.motimaster.com/suyu1535624138000/对号.png'
class PublishSuccessPage(Page):

    naviBarTitle='发布成功'
    naviBarColor='#f4bc33'
    naviBarStyle='black'

    background = '#eeeeee'
    enableShare=True

    def UI():
        with Box(pos=['center',100],size=[600, 700],background='#eeeeee',borderRadius='5px'):
            # Icon(marginTop =200,marginLeft =280,type = 'success', color = 'green', iconSize= 100) 
            Image(pos=['center',100],src=icon_confirm,size=[270,250]) 
            Text(pos=['center',400],text='订单发布成功',fontSize=50,color='black',lineHeight=50,width=400,textAlign='center')
            Text(pos=['center',500],text='您的订单已投入商品池',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
        
        with Button(text='分享给朋友', pos=['center', 800],size=[600,100],lineHeight=100,fontSize=36, color='black',background='#f4bc33'):
            this.onTap = gotoShareGood
        Button(text='查看详情', pos=['center', 950],size=[600,100],fontSize=36,lineHeight=100, color='black',background='white',onTap=toCheckDetail)
    
    def onInit():
        page.share.title = "我发布了一件商品:{},快来看看吧".format(page.options.title)
        page.share.imageUrl = 'http://material.motimaster.com/appmaker/goupeng/6455.png'
        page.share.page = 'goods_info'
        page.share.options = {'goods_id':page.options.goods_id}
        mo.console(page.options.type)
        if page.options.type == '求购':

            soldgoods = Goods_db(user.openid, mo.db)
            is_match = soldgoods.match(page.options.title)
            mo.console(is_match)
            if is_match:
                mo.notice.send(user.openid,'Y9gOp8Xh_GE7NI5Gc8eWSjRqyrHO9kSahyaITlVbWeI','index',[is_match[0]['title'], is_match[0]['description'], '正在出售的商品','点击查看'],emphasis_index=1)
        else:   
            pass

    def toCheckDetail():
        mo.redirectTo('goods_info',goods_id=page.options.goods_id)
        pass

    def gotoShareGood():
        thisgood = Goods_db(user.openid, mo.db)
        gooddetail = thisgood.get_goodsinfo(page.options.goods_id)
        mo.console(gooddetail)
        userinfo = get_publisher_info(gooddetail['id'], user, mo)
        
        mo.console(userinfo)
        params = {
            'page': 'goods_info',
            'width': 150,
            'options': 
                {
                'goods_id':page.options.goods_id
                }
                }
        retParams = mo.acode.getWxAcodeUrl(params)
        pic = retParams['url']
        # mo.console(retParams)
        # mo.console(pic)
        qrcode = None
        if retParams['ret'] == 0:
            qrcode = retParams['url']

        canvas = mo.mopic.createCanvas(776, 900,saveStrategy='permanent')
        canvas.addImage('http://material.motimaster.com/yuweijiang1535980752000/WechatIMG1961.jpeg', pos=[0, 0, 776, 900])
        canvas.addText(gooddetail['title'], pos=[50, 50], fontSize=25, color=(0, 0, 0))
        canvas.addText(gooddetail['description'], pos=[50, 100], fontSize=25, color=(0, 0, 0))
        canvas.addImage(gooddetail['pic_list'][0], pos=[78, 90, 500, 500], mask='crop')
        canvas.addText('扫我，查看物品详情', pos=[245, 820], fontSize=25, color=(0, 0, 0))
        canvas.addImage(qrcode, pos=[78, 90, 117, 117])
        canvas.addText('联系电话:'+userinfo.phone, pos=[245, 820], fontSize=25, color=(0, 0, 0))
        res = canvas.makeImage()
        mo.console(res)
        if res['ret'] == 0:
            sharepic = res['url']
        mo.goto('sharegood', sharepic=sharepic)

class sharegood(Page):
    naviBarTitle='发布成功'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    def UI():
        Image(id='picdetail', pos=['center', 50])
        ShareButton(pos=[50, 1000, 300, 80], textAlign='center', lineHeight=80, text='分享到群')
        with Button(pos=[425, 1000, 300, 80], textAlign='center', lineHeight=80, text='保存到朋友圈'):
            this.onTap = saveImage

    def onInit():
        page.picdetail.src = page.options.sharepic

    def saveImage():
        mo.saveImage(page.options.sharepic)












