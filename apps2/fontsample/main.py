
# def main():
#     with MoApp(appid='wx263b9c72fc87b39c', name='字体示例'):
#         index()

# class index(Page):
#     def UI():
#         Text(text='Light,107', fontSize='40pt',pos=[20,20])
#         #Text(text='Light,107', fontSize=107, pos=[20,150])
#         Text(text='Medium,54', fontSize='20pt',pos=[20,320])
#         #Text(text='Medium,54', fontSize=54, pos=[20,450])

#         Text(text='Regular,46', fontSize='17pt',pos=[20,520])
#         #Text(text='Regular,46', fontSize=46, pos=[20,650])

#         Text(text='Regular,34', fontSize='13pt',pos=[20,720])
#         #Text(text='Regular,34', fontSize=34, pos=[20,850])

#     def onInit():

#         pass

#     def onShare():
#         page.share.page = 'share'
#         page.share.title = "请对我好一点，因为……"
#         page.share.options = {
#             "url":page.options.url,
#             "openid": page.options.openid,
#             "nickName": page.options.nickName,
#             "avatarUrl": page.options.avatarUrl
#         }

def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='mopicSample', navigationBarTitleText='mopic使用方法'):
        prepare()
        index()


class prepare(Page):

    def UI():
       # with Swiper(id ='swiper2', size=[750,240], onChange=OnChange,interval=2000,duration=500,  top=300):
       #      with SwiperItem(id='imgUrls'):
       #          Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')
        Button(name='test',type='primary', text='设置clipboad',pos=['center',200], openType='getUserInfo',
                onTap=setClipBoard)

        Button(name='test2',type='primary', text='取得clipboad',pos=['center',500], openType='getUserInfo',
                onTap=prepareUserinfo)
    def OnChange():
        mo.console('页面也换')
        mo.console(page.swiper2.value)
    def setClipBoard():
        mo.setClipboardData('hahahashdaslkasjdlkjaslkjd')
    def onInit():
        page.test.display = 'flex'
        page.test2.hidden =True
        #pass

    def prepareUserinfo():
        text = mo.getClipboardData()
        data = mo.getWxRunData()

        mo.wxpay.pay('xxx', 1.99, onPaySuccss, onPayFail)

        i=10
        if mo.wxpay.pay(1.99):
            pass
            i = 100
        else:
            pass #失败
            i= -1.99

        i


    def onPaySuccess():
        pass


    def getSuccess():
        mo.console('getSuccess')
        mo.console(params.data)

class index(Page):
    def UI():
        with Box(pos=[0, 0], width=750, height=750):
            Image(name='mopicImage',pos=[0,0],size=[750,750])

    def onInit():
        canvas = mo.mopic.createCanvas(776, 900,bg='#BA55D3')
        #canvas.addImage('http://material.motimaster.com/five/yinxiang/main/48ea6c541c2c942323f36458476a7b03.jpg', pos=[0, 0, 776, 900])
        canvas.addImage(page.options.avatarUrl, pos=[78, 90, 117, 117], mask='circle')
        canvas.addText('--来自'+page.options.nickName, pos=[245, 820], fontSize=25, color=(0, 0, 0))
        res = canvas.makeImage()

        if res['ret'] == 0:
            page.mopicImage.src=res['url']