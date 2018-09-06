from tools import *


weixin_img = 'http://material.motimaster.com/wangbing1534510112000/weixin.png'
phone_img = 'http://material.motimaster.com/wangbing1534509404000/phone.png'


class order_finish(Page):
    naviBarTitle = '订单完成'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = '#EEEEEE'
    enableShare = True

    def UI():
        with Box(size=[750, 600], background='white', position='relative'):
            Text(text='订单已生成', pos=['center', 120], fontSize=40,)
            Text(name='activity', marginTop=260, fontSize=26, color='#757575', width=690, textAlign='center',left='center')

            Text(text='发布者联系方式', pos=[30,340], fontSize=30,color='#757575')
            with Box(pos=[0, 400], size=[750, 100], borderBottom='1px #EEEEEE'):
                Image(src=phone_img, pos=[30, 'center'], size=[50, 50], opacity=0.5)
                Text(name="phone", left=110, top='center', fontSize=32, color='#FF9E53', borderBottom='1px solid #FF9E53', height=40, lineHeight=40, onTap=make_call)

            with Box(pos=[0, 501], size=[750, 100]):
                Image(src=weixin_img, pos=[30, 'center'], size=[50, 50], opacity=0.5)
                Text(name="weixin_account", left=110, top='center', fontSize=32, color='#FF9E53', borderBottom='1px solid #FF9E53', height=40, lineHeight=40, selectable=True)



        ShareButton(text='分享给好友', marginTop=80, pos=['center', 40], background='#f4bc33', width=400,fontSize=36, position='relative',
            color='white',lineHeight=90, height=90, boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)')
        Button(text='回首页再逛逛', marginTop=80, pos=['center', 40], background='white', width=400,fontSize=36, position='relative',
            color='black',lineHeight=90, height=90, boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)', onTap=moui.switchTab('index'))
        Box(marginTop=100, size=[750, 10], position='relative')

    def onInit():
        publisher_info = get_publisher_info(page.options.goods_id, user, mo)
        page.phone.text = publisher_info.phone or ''
        page.weixin_account.text = publisher_info.weixin_account or ''
        page.activity.text = '该商品已加入weisale用户分享计划，分享可与卖家协商砍价'
        page.share.title = "{}的商品清单".format(publisher_info.realname)
        page.share.imageUrl = 'http://material.motimaster.com/wangbing1534903202000/pic.png'
        page.share.page = 'pub_list'
        page.share.options = {'publisher_id':page.options.openid}

    def make_call():
        publisher_info = get_publisher_info(page.options.goods_id, user, mo)
        phone_number = publisher_info.phone
        mo.makePhoneCall(phone_number)
