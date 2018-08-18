def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='上传测试'):
        index()


class index(Page):
    naviBarTitle = '入口页面'
    background = "http://material.motimaster.com/appmaker/keric/5662.jpg"
    def UI():
        Button(text="拿到templateId",size=[300,100],pos=[300,200],type="primary",
            openType='getUserInfo')

        Button(text="发送模版消息",size=[300,100],pos=[300,400],type="primary",
            onTap=sendT)
    def onInit():
        mo.console('不想干啥')
    
    def sendT():
        mo.notice.send('oeGwh0TSlpiyDkJK-5QhTDtv8Wgc','UtyfeYzXCEKQdS_mO6DHOSxGKSrrsXZ9PlCvGRBxVPg',
            'index',['爱情测试','七夕快乐'],emphasis_index=1)
    