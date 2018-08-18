
from test import *
from fuqin import *
def main():

    with MoApp(appid='wxf7c6308b0e199d50', name='小猜心'):
        with Page(name='pageentrance',naviBarTitle='小猜心',onReady = [
                moui.showLoading('加载中...'),
                onReadyIndexPage,
                moui.hideLoading()
                ]):
            with Swiper(name ='swiperGuangGao',hidden=False, size=[750, 270],top=0,position='absolute'):
                with SwiperItem(name='imgUrls',top=0):
                    Image(pos=[0,0, 750, 270], src = '{item.src}',onTap=moui.request(onBannerTap, id='{item.id}', type='{item.type}', path='{item.path}'))
            Text(pos=[20,280], text='测评·占卜',fontWeight='lighter',fontSize=34)
            Box(size=[750,1],borderBottom='1px solid WhiteSmoke',pos=[0,340])
            with List(name='dormitorylist',pos=[0,350],width=750):
                with Box(size=[750,180],borderRadius='0px',background='white',
                    borderBottom= '1px solid WhiteSmoke',marginBottom=15,
                    onTap=moui.request(toTest, path='{item.path}', type='{item.type}')):
                    #Text(pos=[55,55],text='{item.id}',color='#353535',fontSize=35)
                    Image(left=20,size=[150, 150], src='{item.cover}' , mode='aspectFill',borderRadius= '10px')
                    Text(pos=[190,0],text='{item.title}',color='#353535',fontSize=33)
                    Text(pos=[190,55],text='{item.people}',color='#808080',fontSize=28)
                    Text(pos=[190,110],text='{item.details}',fontSize=30,color='#808080')
                    Button(pos=[590,20],type='miniPrimary',text='去测>',size=[100,50],lineHeight=50,
                        padding=0,fontSize=25,fontWeight='lighter',color='#FF0000',background='#ffffff',border='1px solid red')
        
        with Page(name='webview'):
            this.onReady = webviewReady
            WebView(name='webview')
        with Page(name='payment',onReady=paymentReady):
            Text(text='支付中')


        with Page(name='homePage',naviBarTitle='亲密测试',background='#ece9e5',naviBarColor = '#ece9e5'): 
            Image(pos=[0,0],size=[750,1400],src="img/homePage.jpg",position = 'fixed')
            Button(text = '开始测试',
                right = 100,bottom = 220,
                size = [180,180],
                background = '#b1a79f',
                borderRadius = '18px',
                fontSize= 35,
                lineHeight = 180,
                fontWeight = '900',
                color = '#4d3825',
                boxShadow ='-2px 2px 4px rgba(157,150,144,0.5)',
                effect = bounceindown(t=1.5,c=1),
                onTap = moui.goto('testPage'),
                openType='getUserInfo'
                )

        with Page(name = 'testPage', naviBarTitle='亲密测试', background= '#ece9e5',naviBarColor = '#ece9e5'):
            this.onReady = [
                moui.showLoading('题目加载中…'),
                ontestPageReady,
                moui.hideLoading()
                ]
            Image(size = [3000,400],right = 0,bottom = 0,src= 'img/10.png',effect =move(path=[(0,850), (-2250,850)], t=24, c=0))
        
            with MoRadio(name = 'radio3',pos=[70,330, 620, 140],fontSize = 30,onChange = onNext):
                Text(name = 'radiotext',padding=30,pos=[0,-250],backgroundColor='#fbfdf7',fontSize = 30,borderRadius= '10px 10px 10px 10px',color = '#040404',width =600,lineHeight= 50)
    
        with Page(name = 'ResultPage', naviBarTitle='亲密测试',enableShare=True,backgroundColor='#ece9e5',naviBarColor = '#ece9e5'):
            this.onReady = [
                moui.showLoading('分析中…'),
                onReadyPicPage,
                moui.hideLoading()
                ]
            with Box(pos=[0, 0], width=750, height=750):#放置整个图片的box
                Image(id='mopicImage',pos=[0,0],size=[750,1300])#设置image的ID，通过云函数获取。

            with Box(name = 'bottomButton',hidden = True,left = 0,bottom = 0,size = [750,90],background = '#b1a79f',position = 'fixed'):
                ShareButton(
                    text = '分享给好友',
                    pos = [0,0],
                    size = [375,90],
                    lineHeight = 90,
                    fontSize = 35,
                    fontWeight = '900',
                    color = '#4d3825',
                    border = 0,
                    plain = True)
                # Box(pos = ['center',13],size = [4,64],background = '#f7ca4e')
                Box(pos=['center',10],size = [4,70],background  = '#4d3825',borderRadius = '50%')
                Button(name = 'saveImg',
                    text = '保存图片',
                    pos = [375,0],
                    size = [375,90],
                    lineHeight = 90,
                    fontSize = 35,
                    fontWeight = '900',
                    color = '#4d3825',
                    border = 0,plain = True,onTap=onSaveImage)
            

        