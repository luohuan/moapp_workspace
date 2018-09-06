


def ui():
    with MoApp(appid='', name='示例'):
        index()


class index (Page):
    title = '首页'
    shareTitle = 'abc'
    loadingText = '客官请稍候...'
    
    def UI():
      pass
    # 页面初始化，只会调用一次
    def onInit():
        mo.console('on index init')

    
    # 页面显示，每次显示都会调用
    def onShow():
        mo.console('on index show')

    # 下拉刷新
    def onPullDownRefresh():
        mo.console('onPullDownRefresh')

    def onReachBottom():
        mo.console('onReachBottom')

    def onShareSuccessed():
        mo.console('onShareSuccessed')

    def onShareFailed():
        mo.console('onShareFailed') 

    def onShare():
        page.share.page = 'home'
        page.share.title = '分享标题，定制'
        page.share.imageUrl = user.avatarUrl

        page.share.options = {
            "openid": user.id,
            "nickName": user.nickName,
            "avatarUrl": user.avatarUrl
        }


