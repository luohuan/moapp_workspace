def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='二维码示例', withLogin=True):
        share()
templateID = ['232','2323']
class share(Page):
    def UI():
        with SinglePickerButton(name='templatetitle', background='#256df3',border='1px solid #256df3', width=600, textAlign='center', borderRadius='5px', pos=['center', 65, 600, 90], text='面试邀请通知', fontSize=40, color='white', lineHeight=90, range=templateID):
            this.onChange = choose_template

    def choose_template():
        pass
        # params = {
        #     'page': 'entrance',
        #     'width': 150,
        #     'logo':user.avatarUrl,
        #     'options': {
        #         'openid': user.openid,
        #         'avatarUrl': user.avatarUrl,
        #         'nickName': user.nickName,
        #     }
        # }
        # retParams = mo.acode.getWxAcodeUrl(params)
        # erweima = None
        # if retParams['ret'] == 0:
        #     erweima = retParams['url']
        # page.shareImage.src = erweima
        # page.s.hidden=True

    def onShare():
        page.share.page = 'share'
        page.share.title = "请对我好一点，因为……"
        page.share.options = {
            "url":page.options.url,
            "openid": page.options.openid,
            "nickName": page.options.nickName,
            "avatarUrl": page.options.avatarUrl
        }