from goods_db import *
from tools import *
from permission import *


share_img = 'http://material.motimaster.com/suyu1996/hi/main/25437e5fdb27b2de0f22a1217ecc929d.png'
hang_img = 'http://material.motimaster.com/suyu1996/hi/main/936621f5336c1e025842f68d25b7c095.png'


class goods_info(Page):
    naviBarTitle = '商品详情'
    naviBarColor = '#f4bc33'
    naviBarStyle = 'black'
    background = '#EEEEEE'
    enableShare = True

    def UI():
        with Box(size=[750, 240], background='white', position='relative', onTap=go_pub):
            Image(name='head_url', pos=[30, 'center'], size=[180, 180], borderRadius='50%', mode='aspectFill')
            Text(name="nickname", pos=[250, 60], fontSize=30, fontWeight='bold')
            Text(name="signature", pos=[250, 140], fontSize=24, width=480, color='#898989')
            Text(name='authentication', pos=[240, 180], fontSize=24, background='#f4bc33', borderRadius='5px')

        with Box(marginTop=10, size=[750, 80], background='white', position='relative', borderBottom='1px solid #EEEEEE'):
                Text(name="type", pos=[30, 'center'], fontSize=30, background='#f4bc33', color='white', width=100, textAlign='center',borderRadius='1px')
                Text(name="title", pos=[150, 'center'], fontSize=30, fontWeight='bold')
                Text(name="price", right=30, top='center', fontSize=30, color='#FF6228')

        with Box(name="description_box", left=0, width=750, position='relative', background='white'):
            Text(name="description", fontSize=28, textAlign='justify', position='relative',
                display='block', width=690, left='center', lineHeight=40, paddingTop=40, paddingBottom=30)

        with Box(name='grid_box',marginTop=10, size=[750, 690], background='white', position='relative'):
            with Grid(name='grid', size=[690, 230], column=3, pos=['center', 'center']):
                with Box(size=[230,230]):
                    Image(pos=['center', 'center'],size=[220, 220], src='{item.src}', mode='aspectFill', onTap=moui.request(show_pic, id='{item.id}'))

        # with Box(marginTop=10, size=[750, 100], background='white', position='relative', borderBottom='1px solid #EEEEEE'):
        #     Text(text='取货方式：', pos=[30, 'center'], fontSize=30)
        #     Text(name='fetch_method', pos=[180, 'center'], fontSize=30)
        #     Text(text='新旧程度：', pos=[480, 'center'], fontSize=30)
        #     Text(name='newness', pos=[620, 'center'], fontSize=30, background='white', color='black', width=100, textAlign='center',borderRadius='2px')

        with Box(marginTop=0, size=[750, 80], background='white', position='relative'):
            Text(text='浏览量：', pos=[30, 'center'], fontSize=25)
            Text(name='pv', pos=[120, 'center'], fontSize=25)
            ContactButton(text='举报', pos=[630, 'center'], size=[100, 50],plain=True,border=0, fontSize=25, color='#FF9E53', lineHeight=50)

        Text(name='activity', marginTop=40, fontSize=25, color='#FF9E53', width=720, textAlign='left', left='center',padding=5,)
        #管理员删除按钮
        with Box(id='manage', pos=[600, 900, 100, 100], hidden=True, position='fixed'):
            with Button(pos=[0, 0, 100, 100], textAlign='center', backgroundColor='#e64340', opacity=0.7, color='#fff', text='删除', lineHeight=100, borderRadius='50%', border=0, formType='submit'):
                this.onTap = moui.confirm('温馨提示','确认删除此订单？', deleteorder)
                # this.onTap = moui.showTips('tips')
                

        # Box(marginTop=100, size=[750, 100], position='relative')
        with Box(size=[750, 120], background='white', bottom=0, position='fixed', borderTop='1px solid #EEEEEE'):
            with Box(size=[120, 120], left=60):
                Image(src=share_img, pos=['center', 30], size=[50, 50])
                Text(pos=['center', 75], fontSize=25, text='分享')
                ShareButton(pos=['center', 20], size=[40, 80], plain=True, border=0)
            with Box(size=[120, 120], left=250, onTap=moui.switchTab('index')):
                Image(src=hang_img, pos=['center', 30], size=[50, 50])
                Text(pos=['center', 75], fontSize=25, text='回首页')
            Button(name='buy_button', marginTop=80, top='center', right=50, width=180, color='white',
                lineHeight=60, height=60, boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)', onTap=buy, fontSize=30)

        with Mask(name='mask01', opacity = 0.9):
            with Swiper(name='swiperImage', width=750, height='100%', autoplay = False, indicatorActiveColor ='#FF8C69', duration=100):
                with SwiperItem(name='imgUrls', width=750, height='100%'):
                    Image(src='{item}', left='center', top='ceter', display='inline', width=750, mode='aspectFit')

        with Mask(name='tip', locked=True, opacity=0.7):
            with Box(name='tc', pos=['center', 375], size=[620, 328], borderRadius='5px', background='white'):
                Text(name='tip_title', pos=['center', 55], fontSize=40, text='提示')
                Text(name='content', pos=['center', 140], fontSize=28, text='您尚未填写个人信息，卖家无法联系到您', color='#838184')
                with Box(pos=['center', 230], size=[620, 98], fontSize=20, borderTop='1px solid #EEEEEE', onTap=moui.switchTab('mine')):
                    Text(pos=['center', 'center'], fontSize=40, text='去完善个人信息', color='#4DB23A')

    def onInit():
        goods = Goods_db(user.openid, mo.db)
        items = goods.get_goodsinfo(page.options.goods_id)
        publisher_id = items.get('publisher')
        publisher_info = user.getInfo(publisher_id)
        page.head_url.src = publisher_info.head_url
        page.nickname.text = publisher_info.realname
        page.signature.text = publisher_info.signature
        page.authentication.text = publisher_info.authentication

        mo.console(items.get('type'))
        page.type.text = items.get('type', '')
        page.title.text = items.get('title', '')
        page.price.text = '￥' + str(items.get('price', ''))
        page.description.text = items.get('description', '')
        if not page.description.text:
            page.description_box.hidden = True
        else:
            page.description_box.hidden = False
        # mo.console(items.get('pic_list'))
        imgs = items.get('pic_list', [])
        griditems = []
        index = 0
        for url in imgs:
            griditems.append({'src': url, 'id': index})
            index += 1
        page.grid.height = ((len(griditems) - 1) // 3 + 1) * 230
        page.grid_box.height = page.grid.height + 20
        page.grid.data = griditems

        # page.fetch_method.text = items.get('deliver_type', '')
        # page.newness.text = str(items.get('newness', '')) + '成新'
        page.pv.text = str(items.get('pv', ''))
        page.activity.text = '该商品已加入校园二手交易用户分享计划，分享可与卖家协商砍价'
        
        page.imgUrls.data = imgs
        if len(imgs) > 1:
            page.swiperImage.indicatorDots = True
        else:
            page.swiperImage.indicatorDots = False
        if items['condition'] == '待接':
            page.buy_button.text = '我要认领'
            page.buy_button.background = '#FF9153'
            page.buy_button.disabled = False
        else:
            page.buy_button.text = '已被认领'
            page.buy_button.background = 'grey'
            page.buy_button.disabled = True

        page.share.title = "这里有一件【{}】等你来认领".format(items.get('title', ''))
        
        page.share.page = 'goods_info'
        page.share.options = {'goods_id':page.options.goods_id}

        #判断是否显示删除按钮
        ismanager = mo.db.manager.find({'openid':user.openid})

        if ismanager:
            page.manage.show()
        else:
            page.manage.hide()

    def buy():
        goods = Goods_db(user.openid, mo.db)
        items = goods.get_goodsinfo(page.options.goods_id)
        publisher_id = items.get('publisher')
        if can_buy(user):
            if user.openid == publisher_id:
                mo.showAlert('提示','不可认领自己的商品')
            else:
                mo.goto('order_confirm', goods_id=page.options.goods_id)
        else:
            page.tip.hidden = False

    def show_pic(): 
        page.swiperImage.current = int(params.id)
        page.mask01.hidden = False

    def go_pub():
        goods = Goods_db(user.openid, mo.db)
        items = goods.get_goodsinfo(page.options.goods_id)
        publisher_id = items.get('publisher')
        mo.console(publisher_id)
        if page.options.pre_page == 'pub_list':
            mo.goBack()
        else:
            mo.goto('pub_list', publisher_id=publisher_id)

    def deleteorder():
        thisgood = Goods_db(user.openid, mo.db)
        thisgood.delete_order(page.options.goods_id)
        goodinfo = thisgood.get_goodsinfo(page.options.goods_id)
        delete_time =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        mo.notice.send(goodinfo['publisher'],'bojGcDeU_Suo2HzKrBhsZ2VtMMTAjx6EdZ_APJkQhjM','index',[goodinfo['title'],delete_time,'您的信息不合格，已被管理员删除'],emphasis_index=1)
        mo.showTips('删除成功')
        mo.goBack()
        


