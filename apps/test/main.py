def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='上传测试'):
        index()


class index(Page):
    naviBarTitle = '入口页面'
    background = "http://material.motimaster.com/appmaker/keric/5662.jpg"
    def UI():
        Button(text="上传图片",size=[300,100],pos=[300,900],type="primary",
            onTap=test)
    def onInit():
        mo.console('不想干啥')
    
    def test():
        mo.uploadImage( 9, uploadSuccess, uploadFail)


    def uploadFail():
        mo.console('失败了不可能的')

    def uploadSuccess():
        mo.console('urls')

        mo.console(params.urls)
    def test2():
        mo.console('一个测试')
        mo.console(params.haha)