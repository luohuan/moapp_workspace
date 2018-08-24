def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='上传测试'):
        index()


class index(Page):  
    naviBarTitle = '入口页面'
    def UI():
        with Grid(name='grid1', pos=['center', 20], size=[710, 210], column=3):     
            with Box(size=[220,400], border='1rpx solid black'):
                Image(pos=['center',30], size=[200,300], src='{item.src}', mode='aspectFill')
        Button(text="上传图片", size=[300,100], bottom=50,left=200, position='fixed', type="primary",
            onTap=test)

    def onInit():
        mo.console('初始化页面')
    
    def test():
        mo.uploadImage( 9, uploadSuccess, uploadFail)


    def uploadFail():
        mo.console('失败了不可能的')

    def uploadSuccess():
        urls = params.urls
        mo.console(urls)
        mo.console(params.imagesInfo)
        page.grid1.data = []
        for url in urls:
            page.grid1.data.append({
                'src': url
                })
    