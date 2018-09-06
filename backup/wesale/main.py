from user_info import *
from publish import *
from myorder import *
from goods_info import *
from order_confirm import *
from order_finish import *
from my_sub_order import *
from pub_list import *
from goods_db import *



signs = ['全部','出售','求购','赠送']

sharepic = ['http://material.motimaster.com/appmaker/xiaodong/6521.png',
                     'http://material.motimaster.com/appmaker/xiaodong/6522.png',
                     'http://material.motimaster.com/appmaker/xiaodong/6523.png']

sharepictitle=['学姐要毕业，1000件商品免费领！',
       '武大同学自己的二手交易小站，是校友就送好东西~',
       '武大人的校园二手平台，学姐的东西先到先领',
       '武大人的二手交易平台，就差你不知道了！']

bannerpic = [
    {
    'index':1,
    'pic':'http://material.motimaster.com/suyu1996/hi/main/aab8cc5f4da054429c04b1058486470e.png'
    },

    {
    'index':2,
    'pic':'http://material.motimaster.com/suyu1996/hi/main/a62bf7adc3591995df5e7cef564267af.png'
    }
]               

managerID = ['oTGgQ5RLS5mzO_W9wb74lnbGXFxo']

def main():     
    with MoApp(appid='wx263b9c72fc87b39c', name='WeSale'):   
        with Tabbar(position='bottom', textColor='#000000', textSelectedColor='#FF9153'):
            index()
            PublishPage()
            mine()
        


class index(Page):

    naviBarTitle='首页'


    naviBarColor='#f4bc33'
    naviBarStyle='black'
    background = '#FEF6E1'

    text='逛逛'
    selectedIconPath='images/guangguang2.png'
    iconPath='images/guangguang1.png'
    background='#eeeeee'
    def UI():
        #Text(pos=[5,300], text='List sorted by:')

        #Box(pos=['center', 440], size=[300, 3], background='#757575')
        #Text(text='正在热销', pos=['center', 410], fontSize=30, width=200, color='#757575',textAlign='center', height=50, lineHeight=50,background='#EEEEEE')
        Image(src='http://material.motimaster.com/appmaker/xiaodong/6356.png',size=[17,17],pos=[448,323])

        Image(src='http://material.motimaster.com/suyu1535614417000/背景页2.jpg',size=[750,120],pos=[0,282])

        

        with Swiper(id='swiper3',size=[750,285],interval=6000,top=0,duration=1500, autoplay=True):
            with SwiperItem(id='imgUrls'):
                with Image( src = '{item.pic}',mode='widthFix',width=750):
                    this.onTap = moui.request(clickBanner, index='{item.index}')
        with Box(pos=[28, 400],position='relative'):
            with List(name='list1', overflowX='hidden') as e:
                e._add_styles(['columnFill', 'columnCount','columnGap'])
                this.columnFill = 'auto' 
                this.columnCount = 2 #横向几排
                this.columnGap = '5px'  #横向间距
                with Box(width=345, fontSize=20, border='10px solid #ffffff',borderRadius=5,marginTop=10,background='white') as ee:
                    ee._add_styles(['breakInside'])
                    this.breakInside = 'avoid-column'
                    Image(src='{e.cover}',mode='widthFix',position='relative',width=300,onTap=moui.goto('goods_info',goods_id='{e.goods_id}'))
                    Image(src='{e.img_type}',size=[200,200], pos=[-52,-48])
                    with Box(position='relative'):
                        with Text(text='{e.title}',fontSize=30,width=330,position='relative') as kk:
                            kk._add_styles(['fontWeight'])
                            this.fontWeight = 'bold' 
                        Text(text='¥{e.price}',fontSize=30,position='relative',color='#ff9e53',display='block')
                        Text(text='浏览量:{e.pv}',fontSize=24,bottom=6 ,right=25,color='#888888')

        with Box(pos=[0, 350, 150, 60], position='fixed'):
            with SinglePickerButton(id='picker2', text='商品属性', type='primary', textAlign='center', background='rgba(255,255,255,0.50)', pos=[0, 0], size=[150, 60],
                color='#F4bc33', fontSize=30, borderRadius='0 20px 20px 0',border='1px solid #F4bc33',
                                    lineHeight=60, range=signs):
                this.onChange = onSelectorPickerButtonChange
                this.position = 'fixed'


    def onInit():   
        goods = Goods_db(user.openid, mo.db)
        res = goods.all_goods()
        page.list1.data = res
        mo.console(res)  
        page.imgUrls.data = bannerpic
        page.swiper3.indicatorDots=True
        page.swiper3.indicatorActiveColor ='#FF8C69'

        page.share.title = random.choice(sharepictitle)

        page.share.imageUrl = random.choice(sharepic)
        page.share.page = 'index'

        mo.setTabBarBadge(0, '')
        #mo.removeTabBarBadge(0)
        #mo.showTabBarRedDot(1)

#C:\Users\123\Desktop\moapp-apps-worspace\backup\wesale
#C:\Users\123\Desktop\moapp-apps-worspace\miniprogram2\wesale


    def onShow():
        goods = Goods_db(user.openid, mo.db)
        #goods.del_all_goods()  #危险勿用
        res = goods.all_goods()
        page.list1.data = res
        mo.console(res)

    def onSelectorPickerButtonChange():
        page.picker2.text = signs[int(page.picker2.value)]
        goods_type = page.picker2.text[:2]
        goods_list = []
        goods = Goods_db(user.openid, mo.db)   
        res = goods.all_goods()
        for item in res:
            if goods_type == item['type'] or goods_type=='全部':
                goods_list.append(item)
        mo.console(goods_list)
        page.list1.data = goods_list

    def clickBanner():
        if params.index == 1:
            mo.openWeb('https://mp.weixin.qq.com/s/VySqjNl1LXvoAa-OH7DHmQ')
        elif params.index == 2:
            mo.openWeb('https://mp.weixin.qq.com/s/VySqjNl1LXvoAa-OH7DHmQ')
        else:
            pass

class mine(Page):



    naviBarTitle='我的'
    naviBarColor='#febc33'
    naviBarStyle='black'
 
    background = '#EEEEEE'
    enableShare=True

    text='我的'
    selectedIconPath='images/wode2.png'
    iconPath='images/wode1.png'
    def UI():
        with Box(pos=['center', 40], size=[750, 200], borderBottom=0, background='#ffffff'):
            Image(name='head_url', pos=[30, 'center'], size=[180, 180], borderRadius='50%',mode='aspectFill')
            #Text(text='修改', pos=[640, 'center'], fontSize=35, color='#898989',onTap=moui.goto('user_info'))
            #Button(pos=[715, 'center'], size=[30, 30],plain=True,openType='getUserInfo',onTap=moui.goto('user_info'))
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6581.png', pos=[705, 'center'], size=[20, 43])
            Button(pos=[0, 0], size=[750, 220],plain=True,openType='getUserInfo',onTap=moui.goto('user_info'),border=0)
            Text(name='nickname', pos=[230, 40], fontSize=40, color='black')
            Text(name='signature', pos=[230, 110], fontSize=28,width=470, color='#898989')

        with Box(pos=['center', 280], size=[750, 100], position='relative',borderBottom=0, background='#ffffff',onTap=moui.goto('MyOrderPage')):
                 #Text(text='修改', pos=[640, 'center'], fontSize=35, color='#898989',onTap=moui.goto('user_info'))
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6558.png', pos=[30, 'center'], size=[70, 70])
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6581.png', pos=[705, 'center'], size=[20, 43])
            Text(text='我发布的订单', pos=[120,'center'], fontSize=30, color='black')
        with Box(pos=['center', 381], size=[750, 100], borderBottom=0, background='#ffffff',onTap=moui.goto('MySubOrderPage')):
                #Text(text='修改', pos=[640, 'center'], fontSize=35, color='#898989',onTap=moui.goto('user_info'))
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6559.png', pos=[30, 'center'], size=[70, 70])
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6581.png', pos=[705, 'center'], size=[20, 43])
            Text(text='我接受的订单', pos=[120,'center'], fontSize=30, color='black')

        with Box(pos=['center', 520], size=[750, 100], borderBottom=0, background='#ffffff'):
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6557.png', pos=[30, 'center'], size=[70, 70])
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6581.png', pos=[705, 'center'], size=[20, 43])
            with Text(text='分享给朋友', pos=[120,'center'], fontSize=30, color='#f4bc33') as  xx:
                xx._add_styles(['fontWeight'])
                this.fontWeight = 'bold' 
            ShareButton(pos=[0, 0], size=[750, 220],plain=True,border=0)

        with Box(pos=['center', 621], size=[750, 100], borderBottom=0, background='#ffffff'):
            ContactButton(name='helpBtn', hidden=False, plain=True, border="None", pos=[25, 'center'], size=[80, 80], background='http://material.motimaster.com/appmaker/xiaodong/6580.png')
            Image(src='http://material.motimaster.com/appmaker/xiaodong/6581.png', pos=[705, 'center'], size=[20, 43])
            Text(text='意见反馈', pos=[120,'center'], fontSize=30, color='black')
            ContactButton(pos=[0, 0], size=[750, 90],plain=True,border=0)

        with Box(id='manage', pos=[600, 900, 100, 100], hidden=True, position='fixed'):
            with Button(pos=[0, 0, 100, 100], textAlign='center', backgroundColor='e64340', opacity=0.7, color='#fff', lineHeight=100, borderRadius='50%', border=0, formType='submit'):
                this.onTap = moui.goto('manage')


    def onInit():
        page.share.title = random.choice(sharepictitle)

        page.share.imageUrl = random.choice(sharepic)
        page.share.page = 'index'



    def onShow():
        page.head_url.src = user.get('head_url') or 'http://material.motimaster.com/xiaodong1534413213000/timg.jpg'
        page.nickname.text = user.get('realname') or '游客'
        page.signature.text = user.get('signature') or '请点击右侧按钮录入你的信息吧'

        if user.openid in managerID:
            page.manage.show()
        else:
            page.manage.hide()


class manage(Page):
    background = '#f4f4f4'
    def UI():
        with Box(pos=[0, 0, 750, 300]):
            Text(pos=[0, 40, 750, 50], textAlign='center', lineHeight=50, text='将页面分享给好友，别人点开就会成为管理员')
            ShareButton(pos=['center', 150], type='primary', text='邀请')
        Text(pos=[0, 350, 750, 50], textAlign='center', lineHeight=50, text='管理员列表')
        with List(id='list', pos=[0, 350]):
            with Box(size=[750, 100], backgroundColor='#ffffff'):
                Image(pos=[20, 10, 80, 80], borderRadius='5px', src='{item.headpic}')
                Text(pos=[120, 'center', 500, 50], textAlign='left', lineHeight=50, text='{item.nickname}')
                with Image(pos=[650, 'center', 50, 50], src='http://material.motimaster.com/ywjiang/ceshiyong/demo/abeceac75367512bae810400fd62cbba.png'):
                    this.onTap = moui.request(deletemanager, index='{item.id}')
            Box(size=[750, 20])
    def onShow():
        allmanager = mo.db.manager.find()
        page.list.data = allmanager
        
        page.share.title = '邀请成为管理员'
        page.share.page = 'acceptmanager'


    def deletemanager():
        mo.db.manager.delete(params.index)
        onShow()


# class acceptmanager(Page):
#     def UI():
#         with Button(pos=['center'])




















