
from goods_db import *

enter_right_icon = 'http://material.motimaster.com/appmaker/goupeng/6488.png'

class MySubOrderPage(Page):

    naviBarTitle='我的订单'
    naviBarColor='#f4bc33' 
    naviBarStyle='black'
    enableShare=False

    background = '#eeeeee'

    def UI():
        with ScrollBox(size=[750, '100%'], scrollY=True,pos=['center',0]):
            fontSize=30
            with List(name='order_list',marginTop=40):
                with Box(size=[750, 80],background='white', marginTop=20,borderBottom='1px solid #EEEEEE'):
                    Text(pos=[30,'center'],text='{item.title}', textAlign='center',fontSize=fontSize,fontWeight='bold')
                    Text(pos=[600,'center'],text='{item.condition}',textAlign='right',color='{item.color}',fontSize=26)
                with Box(size=[750, 250], background='white',onTap=moui.request(onCheckOrderDetail, id='{item.goods_id}')):
                    Image(pos=[10,10],size=[200,200],src='{item.cover}',mode='aspectFill')
                    with Box(marginLeft=240,background='white', size=[300,220],marginBottom=20):
                        Text(pos=[10,20],text='￥{item.price}',size=['inherit', 100], textAlign='left',color='red',fontSize=fontSize,fontWeight='bold')
                        # Text(pos=[10,80],text='{item.newness}新', fontSize=22, background='#f4bc33', color='white', width=100, textAlign='center',borderRadius='2px')
                        # Text(pos=[10,130],text='{item.deliver_type}',size=['inherit', 100], textAlign='left',fontSize=26)
                        Text(pos=[10,170],text='{item.update_time_str}',size=['inherit', 100], textAlign='left',fontSize=26)
                    Image(pos=[650,'center'],size=[50,75],src=enter_right_icon,onTap=moui.request(onCheckOrderDetail, id='{item.goods_id}'))
        pass

    def onInit():
        pass
    def onCheckOrderDetail():
        mo.console('the id is %s' % params.id)
        description = '商品信息描述商品信息描述商品信息描述商品信息描述商品信息描述商品信息描述'
        for item in page.order_list.data:
            if(item['goods_id'] == params.id):  # 查找用户点击的订单，跳转到订单详情页并跳出循环
                mo.console('find ')
                mo.goto('SubOrderConfirmPage',
                    id=item['goods_id'],
                    title=item['title'],
                    url=item['cover'],
                    description=item['description'],
                    publisher=item['publisher'],
                    price=item['price'])
                break
            else:
                pass
        pass
    def  onShow():
        goods = Goods_db(user.openid,mo.db)
        sub_data = goods.get_sub_orderlist()  # 调用接口获取我接收的订单数据
        sub_data.sort(key=lambda item: item['update_time'],reverse=True)  # 按时间降序排列
        mo.console(sub_data)
        # 将数据库中的商品订单信息，以人类可读友好的方式显示，顺便设置每一项订单的状态显示的颜色
        for item in sub_data :
            item['update_time_str'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item['update_time']))
            if(item['condition'] == '待接'):
                item['condition'] = '待购买'
                item['color'] = 'red'
            elif(item['condition'] == '被接受'):
                item['condition'] = '待确认'
                item['color'] = 'orange'
            elif(item['condition'] == '已完成'):
                #item['condition'] = '已完成'
                item['color'] = 'green'
            elif(item['condition'] == '取消'):
                item['condition'] = '已删除'
                item['color'] = 'grey'
            else:
                pass
            if len(item['description'])>50 :  # 商品描述信息过长，截取部分信息进行显示
                item['description'] = item['description'][:50]+'...'
        page.order_list.data = sub_data
        pass

class SubOrderConfirmPage(Page):  # 我接收的订单详情页面

    naviBarTitle='订单详情'
    naviBarColor='#f4bc33'
    naviBarStyle='black'
    enableShare=True

    background = '#eeeeee'

    def UI():
        fontSize = 32
        with Box(size=[750, 80], position='relative'):
            Text(pos=[30, 'center'], text='商品信息', textAlign='center', fontSize=32, lineHeight=80)
        with Box(position='relative',size=[750, 280],borderBottom='1px solid EEEEEE',borderTop='1px solid EEEEEE',background='white',onTap=goCheckGoods):
            Image(name='pic',pos=[30,30],size=[220,220])
            with Box(pos=[280,0],size=[470,280]):
                with Box(position='relative',size=[470,120],marginTop=36):
                    Text(name='title',pos=['center','center'],text='',width=450, textAlign='left',padding=10,fontSize=fontSize,fontWeight='bold')
                with Box(position='relative',size=[470,56],marginTop=15):
                     Text(name='price',pos=['center','center'],text='',width=450, textAlign='left',padding=10,fontSize=fontSize,fontWeight='bold',color='red')


        with Box(size=[750,80],position='relative'):
            Text(pos=[30,'center'],text='卖家信息', textAlign='center',fontSize=32,lineHeight=80)

        with Box(position='relative',size=[750, 300],  marginBottom=15,borderBottom='1px solid EEEEEE',borderTop='1px solid EEEEEE',background='white',onTap=goPublisher):    
            Image(name='user_pic',pos=[30,50],size=[220,220])
            with Box(pos=[280,0],size=[470,280]):
                with Box(position='relative',size=[470,120],marginTop=36):
                    Text(name='user_nickname',pos=[30, 'center'],text='', textAlign='left',padding=10,fontSize=fontSize,fontWeight='bold')
                #with Box(position='relative',size=[470,56],marginTop=15):
                    #Text(name='user_anthentic_state',pos=[30,'center'],text='已认证', textAlign='left',padding=10,fontSize=25)
                    #Image(name='user_anthentic_state_icon',pos=[130,'center'],size=[20,20])
                    #Text(name='user_anthentic_info',pos=[150,'center'],text='武汉大学2016级的研究生', textAlign='center',fontSize=25)

        with Box(position='relative',size=[750, 200],  marginBottom=15,borderBottom='1px solid EEEEEE',borderTop='1px solid EEEEEE',background='white'):
            Text(pos=[30,10],text='微信号：', textAlign='center',fontSize=fontSize,lineHeight=100)
            Text(name='user_wechat',pos=[150,10],text='', textAlign='center',fontSize=fontSize,lineHeight=100)
            Text(pos=[30,90],text='电话：', textAlign='center',fontSize=fontSize,lineHeight=100)
            with Box(pos=[130,90],size=[500,100]):
                Text(name='user_phone',pos=[0,'center'],text='', color='#FF9E53', borderBottom='1px solid #FF9E53',lineHeight=40,textAlign='center',fontSize=fontSize,onTap=make_call)
        fontSize=32
    def goCheckGoods():
        mo.goto('goods_info',goods_id=page.options.id)
    def goPublisher():
        mo.goto('pub_list', publisher_id=page.options.publisher)
    def make_call():
        # 获取该订单的发布者电话，并调用打电话接口
        openid = page.options.publisher
        user_info = user.getInfo(openid)
        phone_number = user_info.phone
        mo.console(phone_number)
        mo.makePhoneCall(phone_number)
        pass
    def onInit():
        # 从传入的参数设置页面显示信息，并获取订单发布者信息进行显示
        page.price.text = '￥'+page.options.price
        page.pic.src = page.options.url
        page.title.text = page.options.title
        openid = page.options.publisher
        mo.console(openid)
        user_info = user.getInfo(openid)
        # mo.console(user_info)
        mo.console(' user_info : ')
        mo.console(user_info.realname)
        mo.console(user_info.sex)
        mo.console(user_info.phone)
        mo.console(user_info.head_url)
        page.user_pic.src = user_info.head_url
        page.user_nickname.text = user_info.realname
        page.user_wechat.text = user_info.weixin_account
        page.user_phone.text = user_info.phone
        # 认证信息暂时使用假数据填充
      #  page.user_anthentic_state.text = '已认证'
        #page.user_anthentic_state_icon.src = 'http://material.motimaster.com/appmaker/goupeng/6376.jpg'
       # page.user_anthentic_info.text = '武汉大学2016级的研究生'
        pass