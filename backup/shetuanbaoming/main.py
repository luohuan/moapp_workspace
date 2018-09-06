import time
from createlist import *
from entrylist import *
from listmanage import *
from tools import *



def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='社团助手', withLogin=True, naviBarColor=navicolor, naviBarStyle='white'):
        with Tabbar(position='bottom', textColor='#000000', textSelectedColor=navicolor):
            # choosed()
            index()  #首页
            mine()                            
        createsuccess()
        entry()
        listresult()
        listmanage()
        template()
        managepage()
        mylist()
        mylistdetail()

        invitemanager()  #邀请好友为管理员
        acceptmanager()
        entryresult()
        prelist()
        addlist()

        shareform()  #分享报名表
        editoption()  #编辑选项
        entrydetail()
class index(Page):
    enableShare=True
    background='#F5F5F5'
    text='首页'
    selectedIconPath='image/shouye_choosed.png'
    iconPath='image/shouye_choose.png'
    def UI():
        with Swiper(id='swiper', pos=[0, 0, 750, 285], interval=6000, duration=1500, autoplay=True, indicatorDots=True, indicatorActiveColor=navicolor):
            with SwiperItem(id='banner'):
                Image(src='{item.pic}', mode='widthFix', width=750)
        with Box(pos=[0, 285, 750, 100], backgroundColor='#ffffff'):
            Box(pos=['center', 'center', 500, 2], backgroundColor='#b2b2b2')
            Text(pos=['center', 0, 200, 100], textAlign='center', lineHeight=100, text='正在报名', backgroundColor='#ffffff')
        with List(id='list',pos=[0, 385]):
            with Button(size=[750, 200], formType='submit', border='0px solid #ffffff', plain=True):
                Box(pos=[0, 0, 750, 180], backgroundColor='#ffffff', borderRadius='3px')
                Image(pos=[20, 20, 140, 140], src='{item.pic}')
                Text(pos=[200, 20, 530, 50], textAlign='left', lineHeight=50, fontWeight=700, text='{item.title}')
                Text(pos=[200, 80, 530, 50], textAlign='left', lineHeight=50, fontSize=28, color='#888', text='{item.intro}')
                Image(pos=[650, 'center', 50, 50], src='{item.right}')
                this.onTap = moui.goto('entry', index='{item.id}', title='{item.title}')
            
    def onInit():
        page.banner.data = banner_image
        
        #正在招新
        thisform = form(user.openid, mo)
        alldata = thisform.get_pass_formdata()
        for item in alldata:
            item['pic'] = 'http://material.motimaster.com/ywjiang/ceshiyong/demo/0b97bf6ca3802f2c5d998e43b7cd6cea.png'
            item['right'] = right_arrow
        page.list.data = alldata

    def onShow():
        onInit()

class mine(Page):
    enableShare=True
    background = greybackground
    text = '我的'
    selectedIconPath='image/person_choosed.png'
    iconPath='image/person_choose.png'
    def UI():
        with Box(pos=[0, 40, 750, 150], backgroundColor='#ffffff'):
            Image(id='headpic', pos=[20, 20, 110, 110], borderRadius='5px', border='1px solid #f4f4f4')
            Text(id='nickname', pos=[150, 'center', 500, 50], textAlign='left', lineHeight=50)
            Image(pos=[650, 'center', 50, 50], src=right_arrow)
        with Box(pos=[0, 230, 750, 200], backgroundColor='#ffffff'):
            with Box(pos=[0, 0, 750, 100]):
                Image(pos=[20, 20, 60, 60])
                Text(pos=[20, 0, 650, 100], textAlign='left', lineHeight=100, text='我参与的报名')
                Image(pos=[650, 'center', 50, 50], src=right_arrow)
                Box(pos=[20, 0, 730, 100], borderBottom='1rpx solid #f4f4f4')
                with Button(pos=[0, 0, 750, 100], plain=True, border='0px solid #ffffff', formType='submit'):
                    this.onTap = moui.goto('mylist')
            with Box(pos=[0, 100, 750, 100]):
                Image(pos=[20, 20, 60, 60])
                Text(pos=[20, 0, 650, 100], textAlign='left', lineHeight=100, text='我创建的报名')
                Image(pos=[650, 'center', 50, 50], src=right_arrow)
                with Button(pos=[0, 0, 750, 100], plain=True, border='0px solid #ffffff', formType='submit'):
                    this.onTap = moui.goto('listmanage')
        with Box(pos=[0, 500, 750, 200], backgroundColor='#ffffff'):
            with Box(pos=[0, 0, 750, 100]):
                Image(pos=[20, 20, 60, 60])
                Text(pos=[20, 0, 650, 100], textAlign='left', lineHeight=100, text='意见反馈')
                Image(pos=[650, 'center', 50, 50], src=right_arrow)
                Box(pos=[20, 0, 730, 100], borderBottom='1rpx solid #f4f4f4')
                with ContactButton(pos=[0, 0, 750, 100], plain=True, border='0px solid #ffffff', formType='submit'):
                    pass
            with Box(pos=[0, 100, 750, 100]):
                Image(pos=[20, 20, 60, 60])
                Text(pos=[20, 0, 650, 100], textAlign='left', lineHeight=100, text='加入我们')
                Image(pos=[650, 'center', 50, 50], src=right_arrow)
                with Button(pos=[0, 0, 750, 100], plain=True, border='0px solid #ffffff', formType='submit'):
                    pass
        with Button(id='manage', pos=[520, 900, 150, 150],  borderRadius='50%', backgroundColor='#ffffff', textAlign='center', lineHeight=150, formType='submit',
            borderBottom='1px solid #F5F5F5', text='管理', hidden=True):
            this.onTap = moui.goto('managepage')
    
    def onInit():
        personinfo = mo.db.person.find({'openid':user.openid})
        
        if personinfo:
            page.headpic.src = personinfo[0]['headpic'] 
            page.nickname.text = personinfo[0]['nickname']
        else:
            page.headpic.src = 'http://material.motimaster.com/ywjiang/ceshiyong/demo/39ff0e2ad85ccfec359a88b2d4f74756.png'
            page.nickname.text = '未知昵称'

        if user.openid in MANAGEID:
            page.manage.show()

        


