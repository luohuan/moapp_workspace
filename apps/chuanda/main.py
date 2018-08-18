

def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='穿搭', navigationBarTitleText='我的穿搭怎么样？'):
        index()
        analy()
# http://material.motimaster.com/harvey/5455/myrose/9c0c61f7b978297aa5d3809cf758a974.png
# http://material.motimaster.com/harvey/5455/myrose/149bf71ed95144a1fa166ea902ee44c5.png
class index(Page):
    def UI():
        Image(src='http://material.motimaster.com/harvey/5455/myrose/2d60d1acfdc7a626968bbf1055afc90f.png', size=[720, 106], pos=['center', 50])
        Text(text='“每一套美丽的穿搭，', fontSize=45, pos=[70, 250], color='#e87d67')
        Text(text='都值得被欣赏。”', fontSize=45, pos=[350, 310], color='#e87d67')
        Image(src='http://material.motimaster.com/liuhongjie1532394290000/首页小皇冠.png', size=[150, 150], pos=[535, 215])

        ImageAvatar(pos=['center', 500], size=[200, 200], borderRadius='50%')
        TextNickName(pos=['center', 705], size=[600, 100], textAlign='center')

        Button(text='开始分析我的穿搭', pos=['center', 950], size=[400, 90], lineHeight=90, fontSize=40, borderRadius=15,
            background='#e87d67', boxShadow='-1px 15px 30px -12px black', openType='getUserInfo', onTap=startAnalysis)

    def onInit():
        pass

    def startAnalysis():
        mo.goto('analy')

class analy(Page):
    background = 'http://material.motimaster.com/liuhongjie1532495170000/518a1c386e87c9309520f44ca7a3a9ba.jpeg'
    enableShare = True

    def UI():
        with Box(size=[700, 1010], pos=['center', 10], background='#ffffff', border='2rpx solid black', borderRadius=15, boxShadow='-1px 15px 30px -12px black'):
            Text(name='date', pos=[25, 5], fontSize=35)
            with Box(size=[670, 750], pos=['center', 60], background='#f2f2f2',
                border='1rpx solid black', borderRadius=15, onTap=[moui.chooseImage(), moui.uploadImage(), uploadImage]):
                Image(src='http://material.motimaster.com/harvey/5455/myrose/30bae249fb93c0d1ceff3918308f8d50.png', size=[300, 300], pos=['center', 150])
                Text(text='点击上传你的今日穿搭照，\n系统可以给你评价打分哦~', fontSize=40, pos=['center', 430])
  
            Image(name='photo', hidden=True, size=[670, 750], pos=['center', 60], background='#eeeeee', border='1rpx solid black', borderRadius=15)
            Image(name='kuang', hidden=True, size=[696, 772], pos=['center', 50])
            Image(name='xian', hidden=True, size=[696, 100], pos=['center', 60], effect=move(path=[(0,30),(0,740),(0,30),(0,740),(0,30)], t=7, c=0))
            Image(name='wenzi', src='http://material.motimaster.com/liuhongjie1532426719000/未标题-1.png', size=[180, 55], pos=[450, 5], hidden=True)
            Image(name='score', size=[235, 55], pos=[445, 65], hidden=True)
            #Text(name='score', pos=[440, 65], hidden=True)
            Text(name='result', hidden=True, size=[650, 200], pos=[25, 830], fontSize=35, lineHeight=42)

        Button(name='start', text='开始分析', pos=['center', 1050], size=[250, 90], 
            lineHeight=90, fontSize=40, borderRadius=15, background='#e87d67', boxShadow='-1px 15px 30px -12px black', onTap=startAnaly)

        Button(name='savebtn', text='保存我的穿搭成绩单', hidden=True, pos=['center', 1050], size=[450, 80], lineHeight=80,
            fontSize=40, background='#e87d67', borderRadius=15, boxShadow='-1px 15px 30px -12px black', onTap=saveFuc)
        ShareButton(name='sharebtn', text='分享给好友一起用', hidden=True, pos=['center', 1150], size=[450, 80], lineHeight=80,
            fontSize=40, background='#e87d67', borderRadius=15, boxShadow='-1px 15px 30px -12px black')
        with NumCounter(name='counter', color='#ffffff'):
                this.onFinish = analyFuc
    
    def onInit():
        date = time.localtime(time.time())
        week = ['一','二','三','四','五','六','日']
        dateText = '%s月%s日 星期%s' % (date.tm_mon, date.tm_mday, week[date.tm_wday])
        page.date.text = dateText

        page.share.title = "好友"+ str(user.nickName)+ "邀请您来进行穿搭评价~😍"
        page.share.page = 'index'
        page.share.options = {"openid": user.openid}

    def uploadImage():
        imageUrl = params.imageURL
        mo.console(imageUrl)
        mo.console(mo.mopic.getBodyAttr(imageUrl))
        page.data.imageUrl = imageUrl

        page.photo.src = imageUrl
        page.photo.hidden = False

        
    def startAnaly():
        page.counter.config = {
            'type': 'dec',
            'number': 3,
            'interval': 100,
        }
        page.kuang.hidden = False
        page.kuang.src = 'http://material.motimaster.com/liuhongjie1532423777000/扫描框.png'

        page.xian.hidden = False
        page.xian.src = 'http://material.motimaster.com/liuhongjie1532424401000/扫描线.png'

    def analyFuc():
        page.kuang.hidden = True
        page.xian.hidden = True
        if page.data.imageUrl == None:
            mo.showAlert('💡Tips','请先上传一张美美的照片~')
            return
        imageUrl = page.data.imageUrl
        attr = mo.mopic.getBodyAttr(imageUrl)
        
        if attr['upper_color']['name'] == '红':
            if attr['lower_color']['name'] == '黄':
                page.result.text = '点评：'+ random.choice(['撞色是表达自我内在个性的一个视觉宣告，像是你身上纯正的红、明亮的黄...美的张扬而具侵略性。',
                                                            ])
            elif attr['lower_color']['name'] == '蓝':
                page.result.text = '点评：'+ random.choice(['像麻将桌上的骰子一样的红蓝撞色，充满了街头的潮流趣味feel~而且自古红蓝出CP，穿上它的你真是潮到飞起来！',
                                                            '年轻感爆棚的红蓝撞色，充满了街头的潮流趣味feel~而且自古红蓝出CP，穿上它的你真是潮到飞起来！'])
            elif attr['lower_color']['name'] == '粉':
                page.result.text = '点评：'+ random.choice(['温暖红色，可爱橘粉色，少女味道在空气中蔓延~再加上绿色/蓝色/白色的清新感觉，妥妥的直男杀手嘿！',
                                                            ])
            elif attr['lower_color']['name'] == '黑':
                page.result.text = '点评：'+ random.choice(['习惯了工作日穿黑白灰，偶尔给生活加点色彩，来个红黑大撞色！不仅能成功夺取众人眼球，你自己是不是也同样会感受到这股热情呢？',
                                                            '红色一直是很醒目的颜色，有一种宣誓主权的效果；但加上黑色后带来了一些中和，也防止了从头红到脚的效果哟。'])
        elif attr['upper_color']['name'] == '黄':
            if attr['lower_color']['name'] == '红':
                page.result.text = '点评：'+ random.choice(['撞色是表达自我内在个性的一个视觉宣告，像是你身上纯正的红、明亮的黄...美的张扬而具侵略性。',
                                                            '夏季T恤真是一抓一大把，但我们可以在颜色上取胜啊！黄色T恤可以说是非常清凉了，穿上它你就是这条街最靓的仔！'])
            else:
                page.result.text = '点评：'+ random.choice(['夏季T恤真是一抓一大把，但我们可以在颜色上取胜啊！黄色T恤可以说是非常清凉了，穿上它你就是这条街最靓的仔！',
                                                            '鹅黄色T恤搭配浅色高腰裤，略带复古质感，十分有感觉，并且十足显身材呢~'])
        elif attr['upper_color']['name'] == '蓝':
            if attr['lower_color']['name'] == '蓝':
                page.result.text = '点评：'+ random.choice(['蓝色搭配蓝色真是最显瘦又清凉的穿搭了，不知道搭配什么的时候就用蓝色搭配蓝色，既简单好用又不会单调~',
                                                            ])
            elif attr['lower_color']['name'] == '粉':
                page.result.text = '点评：'+ random.choice(['穿上少女粉，变身直男斩！( •̀ ω •́ )✧给人带来丝丝清凉又不挑肤色的蓝色，也绝对是夏日首选！粉色搭配蓝色，两个都很青春减龄的颜色搭起来很是清新哟~',
                                                            ])
        elif attr['upper_color']['name'] == '粉':
            if attr['lower_color']['name'] == '红':
                page.result.text = '点评：'+ random.choice(['温暖红色，可爱橘粉色，少女味道在空气中蔓延~再加上绿色/蓝色/白色/的清新感觉，妥妥的直男杀手嘿！',
                                                            ])
            elif attr['lower_color']['name'] == '蓝':
                page.result.text = '点评：'+ random.choice(['穿上少女粉，变身直男斩！( •̀ ω •́ )✧给人带来丝丝清凉又不挑肤色的蓝色，也绝对是夏日首选！粉色搭配蓝色，两个都很青春减龄的颜色搭起来很是清新哟~',
                                                            '女人味十足的裸粉色看上去高级感也十足！视觉上营造出了简洁清爽的感觉，不仅自己穿着凉快，别人看在眼里也犹如给眼睛吃了冰淇淋一般！'])
            else:
                page.result.text = '点评：女人味十足的裸粉色看上去高级感也十足！视觉上营造出了简洁清爽的感觉，不仅自己穿着凉快，别人看在眼里也犹如给眼睛吃了冰淇淋一般！'
        elif attr['upper_color']['name'] == '黑':
            if attr['lower_color']['name'] == '红':
                page.result.text = '点评：'+ random.choice(['习惯了工作日穿黑白灰，偶尔给生活加点色彩，来个红黑大撞色！不仅能成功夺取众人眼球，你自己是不是也同样会感受到这股热情呢？',
                                                            '红色一直是很醒目的颜色，有一种宣誓主权的效果；但加上黑色后带来了一些中和，也防止了从头红到脚的效果哟。'])
        elif attr['upper_color']['name'] == '白':
            page.result.text = '点评：'+ random.choice(['基础款的白色T恤永不过时，百搭一切~坐地铁的时候在外面套上一件格子衬衣，最潮最in的韩国小姐姐就是你！',
                                                        '白T可是检验真女神的标准之一，能将一件普通的白T穿出自己风格的你，称得上是高级时髦精啦！',
                                                        '白色T恤绝对是夏日的经典装扮，个性帅气的中性欧美风，简约而不失强大气场，轻轻松松就能穿出明星范儿！'])
        else:
            page.result.text = '随意并不意味着随便，你的这身夏日穿搭就穿出了一种率性自由的美~简约经典版型，增添气质，大方迷人。'
        page.result.hidden = False
        page.wenzi.hidden = False
        page.score.src = random.choice(['http://material.motimaster.com/liuhongjie1532428428000/五星.png',
                                        'http://material.motimaster.com/liuhongjie1532428385000/四星半.png',
                                        'http://material.motimaster.com/liuhongjie1532428409000/四星.png'])
        page.score.hidden = False

        page.start.hidden = True
        page.savebtn.hidden = False
        page.sharebtn.hidden = False

        page.data.resultText = page.result.text
        page.data.score = page.score.src

    def saveFuc():
        canvas = mo.mopic.createCanvas(700, 1040)
        canvas.addImage('http://material.motimaster.com/liuhongjie1532508855000/结果页.jpg', pos=[0, 0], size=[700, 1040])
        canvas.addImage(page.data.imageUrl, pos=[28, 65, 650, 750])
        #canvas.addText(str(page.data.date), pos=[25, 5], fontSize=35)
        canvas.addImage('http://material.motimaster.com/liuhongjie1532426719000/未标题-1.png', size=[180, 55], pos=[450, 5])
        canvas.addImage(page.data.score, size=[235, 55], pos=[445, 65])
        canvas.addText(str(page.data.resultText), pos=[25, 820, 600], textAlign='center',width=600,color='#000000')

        params = {
            'page':'index',
            'width': 150,
        }
        retParams = mo.acode.getWxAcodeUrl(params)
        erweima = None
        if retParams['ret'] == 0:
            erweima = retParams['url']
        canvas.addImage(erweima, pos=[600, 950, 60, 60])
        res = canvas.makeImage()

        if res['ret'] == 0:
            mo.saveImage(res['url'])
            mo.console(res['url'])