from goods_db import *


class pub_list(Page):
    naviBarTitle='卖家列表'
    naviBarColor='#f4bc33' 
    naviBarStyle='black'
    background = '#EEEEEE'
    enableShare = True


    def UI():
        with Box(size=[750, 240], background='white', position='relative'):
            Image(name='head_url', pos=[30, 'center'], size=[180, 180], borderRadius='50%', mode='aspectFill')
            Text(name="nickname", pos=[240, 30], fontSize=30, fontWeight='bold')
            Text(name="signature", pos=[240, 100], fontSize=24, width=480, color='#898989')
            Text(name='authentication', pos=[240, 180], fontSize=24, background='#FF9E53', borderRadius='5px')
        Box(size=[600, 75], left='center', position='relative', borderBottom='1px solid black',)
        Text(text='TA的发布', pos=['center', 290], fontSize=30,width=200, textAlign='center', height=50, lineHeight=50, background='#EEEEEE')
        with Grid(name='grid', size=[750, 555], column=2, left='center', position='relative', marginTop=75):
            with Box(size=[375,555], onTap=moui.request(go_goods_info, id='{item.goods_id}')):
                with Box(size=[360,540], background='white', borderRadius='5px', pos=['center', 'center']):
                    Image(src='{item.cover}', size=[300, 370], top=30, left='center',  mode='aspectFill')
                    Text(text='{item.title}', left=20, top=430, fontSize=25, fontWeight='bold')
                    Text(text='￥{item.price}', right=20, top=430, fontSize=25, fontWeight='bold', color='#FF6228')
                    Text(text='浏览量：', left=20, bottom=25, fontSize=20)
                    Text(text='{item.pv}', left=100, bottom=25, fontSize=20)
                    # Text(text='{item.newness}新', right=20, bottom=25, fontSize=20, background='#FF6228',
                    #     color='white', width=60, textAlign='center',borderRadius='2px', height=25, lineHeight=25)
                    Image(src='{item.img_type}', size=[200, 200], pos=[-22, -22])

        Box(marginTop=10, size=[750, 100], position='relative')
                
                
    def onShow():
        mo.removeTabBarBadge(0)
        #page.grid.data=griditems
        openid=page.options.publisher_id
        goods = Goods_db(openid,mo.db)
        publisher_info = user.getInfo(openid)
        page.head_url.src = publisher_info.head_url
        page.nickname.text = publisher_info.realname
        page.signature.text = publisher_info.signature
        page.authentication.text = publisher_info.authentication
        pub_data = goods.get_pub_orderlist()
        list_data = []
        mo.console(pub_data)
        for item in pub_data:
            mo.console('--------------------------')
            mo.console(item)
            item['price'] = str(item['price'])
            item['pv'] = str(item['pv'])
            item['update_time_str'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item['update_time']))
            if item['condition'] == '待接':
                item['condition'] = '待认领'
                item['color'] = 'red'
                if item['type'] == '出售':
                    item['img_type'] = img_type['出售']
                elif item['type'] == '求购':
                    item['img_type'] = img_type['求购']
                elif item['type'] == '赠送':
                    item['img_type'] = img_type['赠送']
                else:
                    pass
                list_data.append(item)
            else:
                pass
        page.grid.data = list_data
        page.grid.height = ((len(list_data) - 1) // 2 + 1) * 555

    def go_goods_info():
        mo.console('the id is %s' % params.id)
        for item in page.grid.data:
            if(item['goods_id'] == params.id):
                mo.goto('goods_info',goods_id=item['goods_id'], pre_page='pub_list')

    def onInit():
        openid = page.options.publisher_id
        publisher_info = user.getInfo(openid)
        page.share.title = "{}的商品清单".format(publisher_info.realname)
        page.share.imageUrl = 'http://material.motimaster.com/wangbing1534903202000/pic.png'

