def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='mopicSample', navigationBarTitleText='mopic使用方法'):
        prepare()
        index()


class prepare(Page):

    def UI():
        Button(type='primary', text='准备制作',pos=['center',200], openType='getUserInfo',
                onTap=prepareUserinfo)

    def prepareUserinfo():
        mo.goto('index', nickName=user.nickName, avatarUrl=user.avatarUrl)

class index(Page):
    def UI():
        with Box(pos=[0, 0], width=750, height=750):
            Image(name='mopicImage',pos=[0,0],size=[750,750])

    def onInit():
        canvas = mo.mopic.createCanvas(400, 400,quality=100)
        canvas.addImage('http://material.motimaster.com/zhaoyuanxue1531502036000/bk.jpg', pos=[0, 0, 400, 400])
        # canvas.addImage('http://material.motimaster.com/zhaoyuanxue1531495171000/timg.jpg', pos=[100, 50, 200], mask='circle')
        # canvas.addText('学习哥',textAlign='left',pos=[10,260], color=(250,250,250),fontSize=24, fontFace='xjl')
        canvas.addText('会和喜欢的人看一场电影',color=(250,250,250),pos=[10, 300], fontSize=24, fontFace='pangzhonghua')
        canvas.addText('人们往往用至诚的外表和虔敬的行动',color=(250,250,250),pos=[10, 200], fontSize=24, fontFace='pangzhonghua')
        #canvas.addText('掩饰一颗魔鬼般的心',color=(250,250,250),pos=[100, 340], fontSize=24, fontFace='xjl')
        res = canvas.makeImage()

        if res['ret'] == 0:
            page.mopicImage.src=res['url']
            mo.console(res['url'])
            #'gh_3208b9ed2563', 'wx086e518492a0fa2d', '3f602ab0aa146a0f0a961781749a5a5d', '3519614782@qq.com', '朱凯丰')
