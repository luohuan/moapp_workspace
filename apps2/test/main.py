def main():
    with MoApp(appid='wx08fe2b1ff0c169f2', name='二维码示例', withLogin=True):
        share()

class share(Page):
    def UI():
        with Box(size=[750,750], pos=[0,0],textAlign='center'):
            Image(id ='shareImage', size=[750, 750], pos=[0,0])
        Button(name='s',text='获取信息', openType='getUserInfo',onTap=test)

    def test():
        params = {
            'page': 'entrance',
            'width': 150,
            'logo':user.avatarUrl,
            'options': {
                'openid': user.openid,
                'avatarUrl': user.avatarUrl,
                'nickName': user.nickName,
            }
        }
        retParams = mo.acode.getWxAcodeUrl(params)
        erweima = None
        if retParams['ret'] == 0:
            erweima = retParams['url']
        page.shareImage.src = erweima
        page.s.hidden=True

    def onShare():
        page.share.page = 'share'
        page.share.title = "请对我好一点，因为……"
        page.share.options = {
            "url":page.options.url,
            "openid": page.options.openid,
            "nickName": page.options.nickName,
            "avatarUrl": page.options.avatarUrl
        }