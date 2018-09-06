from goods_db import *


avatar = 'http://material.motimaster.com/wangbing1534311338000/avatar.png'


class order_confirm(Page):
    naviBarTitle = '订单确认'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = '#EEEEEE'
    disableShare =True
    def UI():

        with Box(size=[750,100],background='#eeeeee',position='relative'):
            Text(text='发布者详情', pos=[30, 30], fontSize=32)

        with Box(size=[750, 240], background='white', position='relative'):
            Image(name='head_url', pos=[30, 30], size=[180, 180], borderRadius='50%')
            Text(name="nickname", pos=[240, 30], fontSize=30, fontWeight='bold')
            Text(name="signature", pos=[240, 120], fontSize=25)
            Text(name='authentication', pos=[240, 180], fontSize=25, background='#FF9E53', borderRadius='5px')

        with Box(marginTop=40, size=[750, 300], background='white', position='relative'):
            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative'):
                Text(text='商品名称：', pos=[30, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
                Text(name="title", pos=[30, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)

            with Box(pos=['center', 0], size=[750, 100], borderBottom='1px solid #EEEEEE', position='relative'):
                Text(text='价格：', pos=[30, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
                Text(name="price", pos=[78, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)

            with Box(pos=['center', 0], size=[750, 100], position='relative'):
                Text(text='配送方式：', pos=[30, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)
                Text(name="fetch_method", pos=[30, 'center'], fontSize=30, position='relative', height=100, lineHeight=100)

      #  Text(name='activity', marginTop=40, fontSize=25, color='#FF9E53', width=720, textAlign='left', left='center',padding=10,)
        Button(text='确认订单', marginTop=80, pos=['center', 40], background='#f4bc33', width=400,fontSize=36, position='relative',
            color='white',lineHeight=94, height=94, boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)', onTap=confirm)
        Button(text='取消订单', marginTop=80, pos=['center', 40], background='white', width=400,fontSize=36, position='relative',
            color='f4bc33',lineHeight=94, height=94, boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)', onTap=moui.goBack())
        Box(marginTop=100, size=[750, 10], position='relative')

    def onInit():
        goods = Goods_db(user.openid, mo.db)
        items = goods.get_goodsinfo(page.options.goods_id)
        publisher_id = items.get('publisher')
        publisher_info = user.getInfo(publisher_id)
        page.nickname.text = publisher_info.realname
        page.head_url.src = publisher_info.head_url
        page.signature.text = publisher_info.signature
        page.authentication.text = publisher_info.authentication
        page.title.text = items.get('title', '')
        page.price.text = '￥' + str(items.get('price', ''))
        page.fetch_method.text = items.get('deliver_type', '')
       # page.activity.text = '该商品已加入校园二手交易用户分享计划，分享可与卖家协商砍价'

    def confirm():
        goods = Goods_db(user.openid, mo.db)
        items = goods.get_goodsinfo(page.options.goods_id)
        publisher_id = items.get('publisher')
        publisher_info = user.getInfo(publisher_id)
        res = goods.sub_goods(page.options.goods_id)
        if res:
            mo.notice.send(publisher_id,'UAGF15YmmL_8JI0k2FyxKj7sNareE5o-zILHo_ty87Y','index',
                [items.get('title', ''), '￥' + str(items.get('price', '')), user.get('realname', ''), '联系电话' + user.get('phone', '')], emphasis_index=1)
            mo.redirectTo('order_finish', goods_id=page.options.goods_id, openid=items['publisher'])
        else:
            mo.showAlert('提示', '物品被抢走了')
