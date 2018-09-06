
from goods_db import *
import time

enter_right_icon = 'http://material.motimaster.com/wangbing1534928192000/enter.png'  # 我发布的订单列表中每个订单中引导用户点击查看详情的图标
limit_description = 35
class MyOrderPage(Page):

    naviBarTitle='我的订单'
    naviBarColor='#f4bc33' 
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        with ScrollBox(size=[750, '100%'], scrollY=True,pos=['center',0]):
            fontSize=30
            with List(name='order_list',marginTop=40):
                with Box(size=[750, 80],background='white', marginTop=20,borderBottom='1px solid #EEEEEE'):
                    Text(pos=[30,'center'],text='{item.title}', textAlign='center',fontSize=fontSize)
                    Text(pos=[600,'center'],text='{item.condition}',textAlign='right',color='{item.color}',fontSize=26)
                with Box(size=[750, 250], background='white',onTap=moui.request(onCheckOrderDetail, id='{item.goods_id}')):
                    Image(pos=[10,10],size=[200,200],src='{item.cover}',mode='aspectFill')
                    with Box(marginLeft=240,background='white', size=[300,220],marginBottom=20):
                        Text(pos=[10,20],text='￥{item.price}',size=['inherit', 100], textAlign='left',color='red',fontSize=32,fontWeight='bold')
                        # Text(pos=[10, 80], text='{item.newness}新', fontSize=22, background='#f4bc33', color='white',
                        #      width=100, textAlign='center', borderRadius='2px')
                        # Text(pos=[10,130],text='{item.deliver_type}',size=['inherit', 100], textAlign='left',fontSize=26)
                        Text(pos=[10,180],text='{item.update_time_str}',size=['inherit', 100], textAlign='left',fontSize=26)
                    Image(pos=[650,'center'],size=[75,75],src=enter_right_icon,onTap=moui.request(onCheckOrderDetail, id='{item.goods_id}'))
        pass

    def onInit():
        goods = Goods_db(user.openid,mo.db)
        pub_data = goods.get_pub_orderlist()  # 调用接口获取我发布的订单数据
        pub_data.sort(key=lambda item: item['update_time'],reverse=True)  # 按时间降序排列
        # 将数据库中的商品订单信息，以人类可读友好的方式显示，顺便设置每一项订单的状态显示的颜色
        for item in pub_data :
            item['update_time_str'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item['update_time']))
            if(item['condition'] == '待接'):
                item['condition'] = '待购买'
                item['color'] = 'red'
            elif(item['condition'] == '被接受'):
                item['condition'] = '待确认'
                item['color'] = 'orange'
            elif(item['condition'] == '已完成'):
                #item['condition'] = '购买'
                item['color'] = 'green'
            elif(item['condition'] == '取消'):
                item['condition'] = '已删除'
                item['color'] = 'grey'
            if len(item['description'])>limit_description :
                item['description'] = item['description'][:limit_description]+'...'
        page.order_list.data = pub_data

    def onCheckOrderDetail():
        mo.console('the id is %s' % params.id)
        # 根据用户点击订单项传入的订单号 查询订单信息,并跳转到详情页
        for item in page.order_list.data:
            if(item['goods_id'] == params.id):
                if(item['condition'] == '待确认'):
                    mo.goto('OrderConfirmPage',
                        id=item['goods_id'],
                        title=item['title'],
                        price=item['price'],
                        url=item['cover'],
                        description=item['description'],
                        subcriber=item['subcriber'],
                        publisher=item['publisher'],
                        type=item["type"]
                        )
                elif (item['condition'] == '待购买'):
                    mo.goto('OrderNobuyerConfirmPage',
                        id=item['goods_id'],
                        title=item['title'],
                        price=item['price'],
                        url=item['cover'],
                        description=item['description'],
                        subcriber=item['subcriber'],
                        publisher=item['publisher'])
                elif (item['condition'] == '已完成'):
                    mo.goto('OrderCompleteConfirmPage',
                        id=item['goods_id'],
                        title=item['title'],
                        price=item['price'],
                        url=item['cover'],
                        description=item['description'],
                        subcriber=item['subcriber'],
                        publisher=item['publisher'])
                elif (item['condition'] == '已删除'):
                    mo.goto('OrderDeletedConfirmPage',
                        id=item['goods_id'],
                        title=item['title'],
                        price=item['price'],
                        url=item['cover'],
                        description=item['description'],
                        subcriber=item['subcriber'],
                        publisher=item['publisher'])
                else:
                    pass
                break
            else:
                pass
        pass
    def  onShow():
        goods = Goods_db(user.openid,mo.db)
        pub_data = goods.get_pub_orderlist()
        pub_data.sort(key=lambda item: item['update_time'],reverse=True)
        # pub_data = []
        mo.console(pub_data)
        for item in pub_data :
            item['update_time_str'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item['update_time']))
            if(item['condition'] == '待接'):
                item['condition'] = '待购买'
                item['color'] = 'red'
            elif(item['condition'] == '被接受'):
                item['condition'] = '待确认'
                item['color'] = 'orange'
            elif(item['condition'] == '已完成'):
                #item['condition'] = '购买'
                item['color'] = 'green'
            elif(item['condition'] == '取消'):
                item['condition'] = '已删除'
                item['color'] = 'grey'
            if len(item['description'])>limit_description :
                item['description'] = item['description'][:limit_description]+'...'
        page.order_list.data = pub_data
        pass

    def onInit():
        page.share.title = '我的二手交易小站，还不来看一看！'

        page.share.imageUrl =' http://material.motimaster.com/suyu1535619155000/微信图片_20180830161516.jpg'
        page.share.page = 'pub_list'
        page.share.options = {'publisher_id': page.options.openid}

class OrderConfirmPage(Page):

    naviBarTitle='订单确认'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        fontSize = 32
        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='商品信息', textAlign='center', fontSize=32, lineHeight=80)
        with Box(position='relative', size=[750, 120], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            with Box(pos=[0, 0], size=[750, 100]):
                with Box(pos=[30, 0], size=[600, 80]):
                    Text(name='title', pos=[0, 'center'], text='', width=570, textAlign='left', fontSize=fontSize,
                         fontWeight='bold')
                with Box(pos=[600, 0], size=[130, 80]):
                    Text(name='price', pos=[0, 'center'], text='', width=100, textAlign='left', fontSize=fontSize,
                         fontWeight='bold', color='red')
            Box(pos=['center', 80], size=[750, '1px'], background='#eeeeee')
            # Box(pos=['center', 160], size=[750, '1px'], background='#eeeeee')
        with Box(position='relative', size=[750, 160], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Text(name="description", pos=[30, 0], fontSize=30, width=690, textAlign='left', lineHeight=40)
        with Box(position='relative', size=[750, 280], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Image(name='pic', pos=[30, 0], size=[250, 250], position="relative")

        with Box(size=[750,80],position='relative'):
            Text(pos=[30,'center'],text='买家信息', textAlign='center',fontSize=32,lineHeight=80)

        with Box(position='relative',size=[750, 200],  marginBottom=15,borderBottom='1px solid EEEEEE',borderTop='1px solid EEEEEE',background='white'):
            Text(pos=[30,10],text='姓名：', textAlign='center',fontSize=30,lineHeight=100)
            Text(name='user_name',pos=[130,10],text='', textAlign='center',fontSize=30,lineHeight=100)
            Text(pos=[30,90],text='电话：', textAlign='center',fontSize=fontSize,lineHeight=100)
            with Box(pos=[130,90],size=[500,100]):
                Text(name='user_phone',pos=[0,'center'],text='', color='#FF9E53', borderBottom='1px solid #FF9E53',lineHeight=40,textAlign='center',fontSize=fontSize,onTap=make_call)
        fontSize=35
        marginTop=1050
        Button(text='确认订单', size=[477,80],pos=['center', marginTop],lineHeight=80,fontSize=fontSize, onTap=onButtonConfirm,background='#f4bc33',openType='getUserInfo')#,type='plainPrimary' background='green'
        Button(text='取消订单', size=[477,80],pos=['center', marginTop+60+80],lineHeight=80,fontSize=fontSize, onTap=onButtonCancel,background='white')#,type='plainPrimary' background='green'
        #Button(text='删除订单', size=[477,80],pos=['center', marginTop+(60+80)*2],lineHeight=80,fontSize=fontSize, onTap=onButtonDelete,background='white')#,type='plainPrimary' background='green'
        pass

        with Mask(name='mask_delete', locked=True, opacity=0.7):
            with Box(pos=['center',230],background='white',size=[600,460],borderRadius='3px'):
                Text(pos=['center',120],text='删除订单以后，订单将会移出商品池',fontSize=35,color='black',lineHeight=60,width=450,textAlign='left')
                Text(pos=['center',300],text='确认删除？',fontSize=35,color='black',lineHeight=60,width=450,textAlign='left')
            # Text(pos=['center',150],size=[520, 500],text='未认证用户没有发布权限!是否要立即认证？',background='white',fontSize=35,color='black',lineHeight=40,width=400,textAlign='left')
            with Box(pos=['center', 690],size=[600,60]):
                Button(text='确认', pos=[0, 'center'],size=[300,80],fontSize=32, lineHeight=80,color='black',background='white',borderRadius='0 0 0 5px',onTap=onButtonClickedSureDelete)
                Button(text='放弃', pos=[300, 'center'],size=[300,80],fontSize=32, lineHeight=80,color='black',background='#f4bc33', borderRadius='0 0 5px 0',onTap=onMaskDeleteHidden)

        with Mask(name='mask_cancel', locked=True, opacity=0.7):
            with Box(pos=['center',230],background='white',size=[600,460],borderRadius='3px'):
                Text(pos=['center', 120], text='取消订单以后，这次交易将会失效，订单将会放回商品池\n\n确认取消？', fontSize=35, color='black', lineHeight=60, width=450,
                 textAlign='left')
            # Text(pos=['center',150],size=[520, 500],text='未认证用户没有发布权限!是否要立即认证？',background='white',fontSize=35,color='black',lineHeight=40,width=400,textAlign='left')
            with Box(pos=['center', 690], size=[600, 60]):
                Button(text='确认', pos=[0, 'center'], size=[300, 80], fontSize=32, lineHeight=80, color='black',
                   background='white', borderRadius='0 0 0 5px', onTap=onButtonClickedSureDelete)
                Button(text='放弃', pos=[300, 'center'], size=[300, 80], fontSize=32, lineHeight=80, color='black',
                   background='#f4bc33', borderRadius='0 0 5px 0', onTap=onMaskDeleteHidden)


    def goCheckGoods():
        mo.goto('goods_info',goods_id=page.options.id)
    def make_call():
        openid = page.options.subcriber
        user_info = user.getInfo(openid)
        phone_number = user_info.phone
        mo.console(phone_number)
        mo.makePhoneCall(phone_number)
        pass
    def onInit():

        goods = Goods_db(user.openid, mo.db)

        page.pic.src = page.options.url
        page.title.text = page.options.title
        page.price.text = '￥'+page.options.price
        openid = page.options.subcriber
        user_info = user.getInfo(openid)
        #page.description.text=page.options.description
        page.description.text = page.options.description
        items = goods.get_goodsinfo(page.options.id)

        # mo.console(user_info)
        mo.console(' user_info : ')
        mo.console(user_info.realname)
        mo.console(user_info.sex)
        mo.console(user_info.phone)
        mo.console(user_info.head_url)
        page.user_name.text = user_info.realname
        page.user_phone.text = user_info.phone

        page.mask_cancel.hidden = True
        page.mask_delete.hidden = True

        pass
    
    def onButtonClickedSureCancel():
        page.mask_cancel.hidden = True
        goods_id = page.options.id 
        mo.console(goods_id)
        goods = Goods_db(user.openid,mo.db)
        res = goods.cancel_order(goods_id)
        mo.console(res)

        title =page.options.title
        price = page.options.price
        cancel_time =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        
        publisher = page.options.publisher
        user_info = user.getInfo(publisher)
        seller_phone = user_info.phone

        subcriber = page.options.subcriber
        mo.console(subcriber)
        # 商品名称、订单金额、取消时间、联系电话、备注
        #mo.notice.send(publisher,'SQAieR-biof9MtibOcFdsZGSHLcEZX-L5y0VzXbOsOM','index',[title,price,cancel_time,seller_phone,'无'],emphasis_index=1)
        mo.notice.send(subcriber,'-x6bp3l8VaNs9SoAeYlPbWiWQptTG_ABDbe4B6kLJZM','index',[title,price,cancel_time,seller_phone,'无'],emphasis_index=1)

        mo.redirectTo('CancelSuccessPage')
        pass

    def onButtonClickedSureDelete():
        # page.mask_delete.hidden = True
        # goods_id = page.options.id 
        # mo.console(goods_id)
        # goods = Goods_db(user.openid,mo.db)
        # res = goods.delete_order(goods_id)
        # mo.console(res)

        # title =page.options.title
        # publisher = page.options.publisher
        # subcriber = page.options.subcriber
        # delete_time =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # # 删除内容、删除时间、提示
        # #mo.notice.send(publisher,'P49fsOvBhUz6Z2E37d72eZQSxTNU9KTxvrjQHq1OxjQ','index',[title,delete_time,'无'],emphasis_index=1)

        # # mo.notice.send(subcriber,'bojGcDeU_Suo2HzKrBhsZ2VtMMTAjx6EdZ_APJkQhjM','index',[title,delete_time,'无'],emphasis_index=1)


        # mo.redirectTo('DeleteSuccessPage')
        # pass
        page.mask_cancel.hidden = True
        goods_id = page.options.id 
        mo.console(goods_id)
        goods = Goods_db(user.openid,mo.db)
        res = goods.cancel_order(goods_id)
        mo.console(res)

        title =page.options.title
        price = page.options.price
        cancel_time =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        
        publisher = page.options.publisher
        user_info = user.getInfo(publisher)
        seller_phone = user_info.phone

        subcriber = page.options.subcriber
        mo.console(subcriber)
        # 商品名称、订单金额、取消时间、联系电话、备注
        #mo.notice.send(publisher,'SQAieR-biof9MtibOcFdsZGSHLcEZX-L5y0VzXbOsOM','index',[title,price,cancel_time,seller_phone,'无'],emphasis_index=1)
        mo.notice.send(subcriber,'-x6bp3l8VaNs9SoAeYlPbWiWQptTG_ABDbe4B6kLJZM','index',[title,price,cancel_time,seller_phone,'无'],emphasis_index=1)

        mo.redirectTo('CancelSuccessPage')
        pass

        
    def onButtonConfirm():
        goods_id = page.options.id 
        mo.console(goods_id)
        goods = Goods_db(user.openid,mo.db)
        res = goods.confirm_order(goods_id)
        mo.console(res)
        #发送模板消息
        publisher=page.options.publisher
        subcriber=page.options.subcriber
        title =page.options.title
        price = page.options.price
        
        publisher = page.options.publisher
        user_info = user.getInfo(publisher)
        seller_name = user_info.realname
        seller_phone = user_info.phone

        subcriber = page.options.subcriber
        user_info = user.getInfo(subcriber)
        buyer_name = user_info.realname
        buyer_phone = user_info.phone
        # 商品名称、订单金额、联系人、联系电话、订单状态
        #mo.notice.send(publisher,'BMjIUhW3gex93mAMtidYk_7jHD18CpB6Bh7gnBxjilw','index',[title,price,buyer_name,buyer_phone,'已完成'],emphasis_index=1)

        mo.notice.send(subcriber,'JFLKwH1yURm4Fwq2DU5FDMg3Nmf_ocs1h1MJ4HVd2iM','index',[title,price,seller_name,seller_phone,'已完成'],emphasis_index=1)


        mo.redirectTo('ConfirmSuccessPage')
        pass
    def onButtonCancel():
        page.mask_cancel.hidden = False
        pass
    def onMaskCancelHidden():
        page.mask_cancel.hidden = True
    def onButtonDelete():
        page.mask_delete.hidden = False
        pass
    def onMaskDeleteHidden():
        page.mask_delete.hidden = True
    

class OrderNobuyerConfirmPage(Page):

    naviBarTitle='订单确认'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        fontSize = 32
        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='商品信息', textAlign='center', fontSize=32, lineHeight=80)
        with Box(position='relative', size=[750, 120], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            with Box(pos=[0, 0], size=[750, 100]):
                with Box(pos=[30, 0], size=[600, 80]):
                    Text(name='title', pos=[0, 'center'], text='', width=570, textAlign='left', fontSize=fontSize,
                         fontWeight='bold')
                with Box(pos=[600, 0], size=[130, 80]):
                    Text(name='price', pos=[0, 'center'], text='', width=100, textAlign='left', fontSize=fontSize,
                         fontWeight='bold', color='red')
            Box(pos=['center', 80], size=[750, '1px'], background='#eeeeee')
            # Box(pos=['center', 160], size=[750, '1px'], background='#eeeeee')
        with Box(position='relative', size=[750, 160], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Text(name="description", pos=[30, 0], fontSize=30, width=690, textAlign='left', lineHeight=40)
        with Box(position='relative', size=[750, 280], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Image(name='pic', pos=[30, 0], size=[250, 250], position="relative")

        with Box(position='relative',size=[720, 300],  marginBottom=15,borderBottom='1px solid #EEEEEE',borderTop='1px solid #EEEEEE',background='#eeeeee'):
            Text(pos=['center',76],text='还没有人购买，请耐心等待买家出现', textAlign='center',fontSize=24)
            Text(pos=['center',150],text='你可以重新编辑信息，调整价格会有更多人购买哦~', textAlign='center',fontSize=24)
            
        fontSize=32
        Button(text='删除订单', size=[477,80],pos=['center', 1050],fontSize=fontSize, lineHeight=80,onTap=onButtonDelete,background='#febc43')

        with Mask(name='mask_delete', locked=True, opacity=0.7):
            with Box(pos=['center',230],background='white',size=[600,460],borderRadius='3px'):
                Text(pos=['center',120],text='删除订单以后，订单将会移出商品池',fontSize=35,color='black',lineHeight=60,width=450,textAlign='left')
                Text(pos=['center',300],text='确认删除？',fontSize=35,color='black',lineHeight=60,width=450,textAlign='left')
            # Text(pos=['center',150],size=[520, 500],text='未认证用户没有发布权限!是否要立即认证？',background='white',fontSize=35,color='black',lineHeight=40,width=400,textAlign='left')
            with Box(pos=['center', 690],size=[600,60]):
                Button(text='确认', pos=[0, 'center'],size=[300,80],fontSize=32, lineHeight=80,color='black',background='white',borderRadius='0 0 0 5px',onTap=onButtonClickedSureDelete)
                Button(text='放弃', pos=[300, 'center'],size=[300,80],fontSize=32, lineHeight=80,color='black',background='#f4bc33', borderRadius='0 0 5px 0',onTap=onMaskDeleteHidden)
        pass
    def goCheckGoods():
        mo.goto('goods_info',goods_id=page.options.id)
    def onInit():
        page.pic.src = page.options.url
        page.title.text = page.options.title
        page.price.text = '￥'+page.options.price
        page.description.text = page.options.description

        page.mask_delete.hidden = True
        pass

    def onButtonDelete():
        page.mask_delete.hidden = False
        pass
    def onMaskDeleteHidden():
        page.mask_delete.hidden = True
        pass
    def onButtonClickedSureDelete():
        page.mask_delete.hidden = True
        goods_id = page.options.id 
        mo.console(goods_id)
        goods = Goods_db(user.openid,mo.db)
        res = goods.delete_order(goods_id)
        mo.console(res)

        title =page.options.title
        publisher = page.options.publisher
        subcriber = page.options.subcriber
        delete_time =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # 删除内容、删除时间、提示
        #mo.notice.send(publisher,'P49fsOvBhUz6Z2E37d72eZQSxTNU9KTxvrjQHq1OxjQ','index',[title,delete_time,'无'],emphasis_index=1)

        mo.notice.send(publisher,'bojGcDeU_Suo2HzKrBhsZ2VtMMTAjx6EdZ_APJkQhjM','index',[title,delete_time,'无'],emphasis_index=1)

        
        mo.redirectTo('DeleteSuccessPage')
        pass

class OrderCompleteConfirmPage(Page):

    naviBarTitle='已完成订单'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        fontSize = 32
        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='商品信息', textAlign='center', fontSize=32, lineHeight=80)
        with Box(position='relative', size=[750, 120], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            with Box(pos=[0, 0], size=[750, 100]):
                with Box(pos=[30, 0], size=[600, 80]):
                    Text(name='title', pos=[0, 'center'], text='', width=570, textAlign='left', fontSize=fontSize,
                         fontWeight='bold')
                with Box(pos=[600, 0], size=[130, 80]):
                    Text(name='price', pos=[0, 'center'], text='', width=100, textAlign='left', fontSize=fontSize,
                         fontWeight='bold', color='red')
            Box(pos=['center', 80], size=[750, '1px'], background='#eeeeee')
            # Box(pos=['center', 160], size=[750, '1px'], background='#eeeeee')
        with Box(position='relative', size=[750, 160], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Text(name="description", pos=[30, 0], fontSize=30, width=690, textAlign='left', lineHeight=40)
        with Box(position='relative', size=[750, 280], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Image(name='pic', pos=[30, 0], size=[250, 250], position="relative")

        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='买家信息', textAlign='center', fontSize=32, lineHeight=80)

        with Box(position='relative', size=[750, 200], marginBottom=15, borderBottom='1px solid EEEEEE',
                 borderTop='1px solid EEEEEE', background='white'):
            Text(pos=[30, 10], text='姓名：', textAlign='center', fontSize=fontSize, lineHeight=100)
            Text(name='user_name', pos=[130, 10], text='', textAlign='center', fontSize=fontSize, lineHeight=100)
            Text(pos=[30, 90], text='电话：', textAlign='center', fontSize=fontSize, lineHeight=100)
            with Box(pos=[130, 90], size=[500, 100]):
                Text(name='user_phone', pos=[0, 'center'], text='', color='#FF9E53', borderBottom='1px solid #FF9E53',
                     lineHeight=40, textAlign='center', fontSize=fontSize, onTap=make_call)
        fontSize = 35
    def goCheckGoods():
        mo.goto('goods_info',goods_id=page.options.id)
    def make_call():
        openid = page.options.subcriber
        user_info = user.getInfo(openid)
        phone_number = user_info.phone
        mo.console(phone_number)
        mo.makePhoneCall(phone_number)
        pass
    def onInit():
        page.pic.src = page.options.url
        page.title.text = page.options.title
        page.price.text = '￥'+page.options.price
        openid = page.options.subcriber
        user_info = user.getInfo(openid)
        #page.description.text = "hhhhhhhhhhhhhhhh"
        page.description.text = page.options.description
        # mo.console(user_info)
        mo.console(' user_info : ')
        mo.console(user_info.realname)
        mo.console(user_info.sex)
        mo.console(user_info.phone)
        mo.console(user_info.head_url)
        page.user_name.text = user_info.realname
        page.user_phone.text = user_info.phone
        pass

class OrderDeletedConfirmPage(Page):

    naviBarTitle='已删除的订单'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        fontSize = 32
        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='商品信息', textAlign='center', fontSize=32, lineHeight=80)
        with Box(position='relative', size=[750, 120], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            with Box(pos=[0, 0], size=[750, 100]):
                with Box(pos=[30, 0], size=[600, 80]):
                    Text(name='title', pos=[0, 'center'], text='', width=570, textAlign='left', fontSize=fontSize,
                         fontWeight='bold')
                with Box(pos=[600, 0], size=[130, 80]):
                    Text(name='price', pos=[0, 'center'], text='', width=100, textAlign='left', fontSize=fontSize,
                         fontWeight='bold', color='red')
            Box(pos=['center', 80], size=[750, '1px'], background='#eeeeee')
            # Box(pos=['center', 160], size=[750, '1px'], background='#eeeeee')
        with Box(position='relative', size=[750, 160], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Text(name="description", pos=[30, 0], fontSize=30, width=690, textAlign='left', lineHeight=40)
        with Box(position='relative', size=[750, 280], borderBottom='1px solid EEEEEE', borderTop='1px solid EEEEEE',
                 background='white', onTap=goCheckGoods):
            Image(name='pic', pos=[30, 0], size=[250, 250], position="relative")

    def goCheckGoods():
        mo.goto('goods_info',goods_id=page.options.id)
    def onInit():
        page.pic.src = page.options.url
        page.title.text = page.options.title
        page.price.text = '￥'+page.options.price
        #page.description.text = "hhhhhhhhhhhhhhhh"
        page.description.text = page.options.description
        pass
icon_confirm = 'http://material.motimaster.com/suyu1535624138000/对号.png'
class ConfirmSuccessPage(Page):

    naviBarTitle='确认成功'
    naviBarColor='#f4bc33'
    naviBarStyle='black'

    background = '#eeeeee'
    enableShare=True

    def UI():
        with Box(pos=['center',100],size=[600, 700],background='#eeeeee',borderRadius='5px'):
            # Icon(marginTop =200,marginLeft =280,type = 'success', color = 'green', iconSize= 100) 
            Image(pos=['center',100],src=icon_confirm,size=[270,250]) 
            Text(pos=['center',400],text='订单已确认',fontSize=50,color='black',lineHeight=40,width=400,textAlign='center')
            Text(pos=['center',500],text='恭喜您又完成了一单~',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
            Text(pos=['center',550],text='共享让校园生活更美好！',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
        
        Button(text='处理下一单', pos=['center', 900],size=[600,100],fontSize=40, lineHeight=100,color='black',background='white',onTap=moui.redirectTo("MyOrderPage"))
        Button(text='返回首页', pos=['center', 1050],size=[600,100],fontSize=40, lineHeight=100,color='black',background='#f4bc33',onTap=moui.switchTab('index'))

icon_delete_cancel = 'http://material.motimaster.com/suyu1535624330000/取消.png'
class CancelSuccessPage(Page):

    naviBarTitle='取消成功'
    naviBarColor='#f4bc33f4bc33'
    naviBarStyle='black'

    background = '#eeeeee'
    enableShare=True

    def UI():
        with Box(pos=['center',100],size=[600, 700],background='#eeeeee',borderRadius='5px'):
            # Icon(marginTop =200,marginLeft =280,type = 'success', color = 'green', iconSize= 100) 
            Image(pos=['center',100],src=icon_delete_cancel,size=[270,250]) 
            Text(pos=['center',400],text='订单已取消',fontSize=50,color='black',lineHeight=40,width=400,textAlign='center')
            Text(pos=['center',500],text='您的订单已放回商品池',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
            Text(pos=['center',550],text='请耐心等待下一位卖家出现~',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
        
        Button(text='处理下一单', pos=['center', 900],size=[600,100],fontSize=40, lineHeight=100,color='black',background='white',onTap=moui.redirectTo("MyOrderPage"))
        Button(text='返回首页', pos=['center', 1050],size=[600,100],fontSize=40, lineHeight=100,color='black',background='#f4bc33',onTap=moui.switchTab('index'))


class DeleteSuccessPage(Page):

    naviBarTitle='删除成功'
    naviBarColor='#f4bc33'
    naviBarStyle='black'

    background = '#eeeeee'
    enableShare=True

    def UI():
        with Box(pos=['center',100],size=[600, 700],background='#eeeeee',borderRadius='5px'):
            # Icon(marginTop =200,marginLeft =280,type = 'success', color = 'green', iconSize= 100) 
            Image(pos=['center',100],src=icon_delete_cancel,size=[270,250]) 
            Text(pos=['center',400],text='订单已删除',fontSize=50,color='black',lineHeight=40,width=400,textAlign='center')
            Text(pos=['center',500],text='您的订单已删除',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
            Text(pos=['center',550],text='您可以编辑之后重新发布商品',fontSize=35,color='black',lineHeight=40,width=500,textAlign='center')
        
        Button(text='处理下一单', pos=['center', 900],size=[600,100],fontSize=40, lineHeight=100,color='black',background='white',onTap=moui.redirectTo("MyOrderPage"))
        Button(text='返回首页', pos=['center', 1050],size=[600,100],fontSize=40, lineHeight=100,color='black',background='#f4bc33',onTap=moui.switchTab('index'))
        pass