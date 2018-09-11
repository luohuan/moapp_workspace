#coding=utf-8

# 用于操作小程序数据的类

import time
import uuid
from global_data import AVATAR_URL
from global_data import IS_AUDIT_VERSION

class __imOperator():
    # 统计二维码入口数据
    def prepare(self):
        tokenid = user.get('token_datav2')  #此时只是拿到了Token
        token = mo.getToken(tokenid)  #此时拿到了真的token令牌
        if token:
            token.active()

        if page.options.from_erweima != None:
            mo.stat(page.options.from_erweima)
        else:
            pass
    # 统计二维码入口数据
    def statQrcode(self):
        if page.options.from_erweima != None:
            mo.stat(page.options.from_erweima)
        else:
            pass
            
    def isHost(self):
        return mo.token.isHost()

    def isFirstTimeToTheApp(self):
        if user.get('token_datav2') != None:
            return False
        else:
            return True

    def reloadPage(self):
        tokenid = user.get('token_datav2')  #此时只是拿到了Token
        token = mo.getToken(tokenid)  #此时拿到了真的token令牌
        token.redirectTo('indexPage')

    def isNeedReloadPage(self):
        tokenid = user.get('token_datav2')  #此时只是拿到了Token
        token = mo.getToken(tokenid)  #此时拿到了真的token令牌
        if tokenid != mo.token.id:
            return True
        else:
            return False

    def getAnswerData(self):
        return mo.token.getGuestList()

    def getHostAvatarUrl(self):
        host = mo.token.getHostInfo()
        return host['avatarUrl']

    def formatAnswerList(self, guests):
        hideArr = self.formatArrData(guests)
        for i in range(len(hideArr)):
            # 从客态进入头像一概都是匿名头像
            hideArr[i]['url'] = AVATAR_URL
            # if 'isPay' in hideArr[i] and hideArr[i]['isPay'] ==True:
            #     hideArr[i]['avatarUrl'] = hideArr[i]['real_avatar_url']
            # else:
            hideArr[i]['avatarUrl'] = AVATAR_URL
        return hideArr


    def setPayId(self, id):
        mo.token.set('answerId',id)

    def getUpdatedPayOneList(self):
        answerId = mo.token.get('answerId')
        guestList = mo.token.getGuestList()

        arr = self.formatArrData(guestList)
        payId = arr[answerId]['payId']
        mo.token.set('pay_key_%s'%(payId), True)

        return self.unLockGuestData(arr)

    def getUpdatedPayAllList(self):
        guestList = mo.token.getGuestList()
        arr = self.formatArrData(guestList)

        mo.token.set('pay_key_%s'%('pay_all'), True)
        return self.unLockGuestData(arr)

    # 获取客态的留言数据
    def getImListData(self, guestList):
        arr = self.formatArrData(guestList)
        arr = self.unLockGuestData(arr)
        for i in range(len(arr)):
            # 从客态进入头像一概都是匿名头像
            #arr[i]['url'] = AVATAR_URL
            if 'isPay' in arr[i] and arr[i]['isPay'] ==True:
                arr[i]['avatarUrl'] = arr[i]['real_avatar_url']
            else:
                arr[i]['avatarUrl'] = AVATAR_URL
        return self.unLockGuestData(arr)

    def setAppData(self):
        if user.get('token_datav2') == None:
            tokenid = mo.token.id
            mo.token.markAsHost()
            user.set('token_datav2',tokenid)
        else:
            pass

    def setAvatarUrl(self):
        avatarUrl = user.avatarUrl
        mo.token.set('host_headimg',avatarUrl)

    def gotoSharePage(self):
        mo.token.goto('sharePage')

    def getAvatarUrl(self):
        return mo.token.get('host_headimg')

    def saveImageUrl(self, url):
        mo.token.set('share_image', url)

    def getImageUrl(self):
        return mo.token.get('share_image')

    def getShowAnswerList(self, text):
        item = {
        'url':'',
        'text':text
        }

        guests = self.getAnswerData()

        arr = []
        if len(guests)>0:
            arr = self.formatArrData(guests)
        else:
            pass

        item['url'] = AVATAR_URL
        arr.insert(0, item)

        return arr

    def saveAnswerData(self, text):
        guests = self.getAnswerData()
        guestData = self.formatGuestData(guests, user.openid, text)
        #客人进来后可以通过markAsGuest在token中记录信息
        mo.token.markAsGuest({
            'guest_data':guestData
        })
        mo.console('guestData==============')
        mo.console(guestData)
        # hideArr[i]['url'] = AVATAR_URL
        # hideArr[i]['avatarUrl'] = AVATAR_URL
        guestData[-1]['url'] = AVATAR_URL
        guestData[-1]['avatarUrl'] = AVATAR_URL
        return guestData[-1]

    # 对保存到token的数据格式化
    def formatGuestData(self, guests, guestId, text):
        guestData = []
        if len(guests) == 0:
            guestData.append({'text':text,'payId':''})
        else:
            flag = False
            for i in range(len(guests)):
                if guests[i]['openid'] == guestId:
                    flag = True
                    arr = guests[i]['guest_data']
                    if arr != None:
                        arr.append({'text':text,'payId':''})
                        guestData = arr
                    else:
                        guestData.append({'text':text,'payId':''})

            if flag == False:
                guestData.append({'text':text,'payId':''})


        # 给每一项记录一个唯一的payid
        for i in range(len(guestData)):
            if guestData[i]['payId'] == '':
                id = self.createUid()
                guestData[i]['payId'] = id

        return guestData

    # 生成唯一的id字符串
    def createUid(self):
        return str(uuid.uuid1())

    def sendTemplateMessage(self):
        # 发送模版消息
        host = mo.token.getHostInfo()
        curTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # 配置模版消息文档链接 http://doc.mozigu.cn/chang-jian-wen-ti/ru-he-tian-jia-mo-ban-xiao-xi.html
        mo.notice.send(host['openid'], 'uRRU2OTAB3h5kRJvdOljZlh9C43qKuDG5pYqiu5N8yE',
        'indexPage', [curTime, '又有好友回答你的问题啦', '好友印象墙提醒你，又有好友对你做出了评价，快去看看吧'])

    # 格式化保存留言的数组数据
    def formatArrData(self, guests):
        arr = []
        for i in range(len(guests)):
            guestArr = guests[i]['guest_data']
            for j in range(len(guestArr)):
                arr.append({
                    'id':j, #留言墙id，按照数组顺序
                    'url': AVATAR_URL, # 匿名头像地址
                    'isPay':False, # 默认没有支付过
                    'real_avatar_url':guests[i]['avatarUrl'], # 真实的个人头像地址
                    'payId':guestArr[j]['payId'], #标记支付的payid
                    'text':guestArr[j]['text'] # 好友留言的文本
                    })

        return arr

    # 刷新支付过的数据
    def unLockGuestData(self, arr):
        if IS_AUDIT_VERSION == False:
            isToPayAll = mo.token.get('pay_key_%s'%('pay_all'))

            for i in range(len(arr)):
                isToPay = mo.token.get('pay_key_%s'%(arr[i]['payId']))

                if isToPay or isToPayAll == True:
                    arr[i]['isPay'] = True
                    arr[i]['url'] = arr[i]['real_avatar_url']
        else:
            for i in range(len(arr)):
                arr[i]['isPay'] = True
        return arr

# 实例化imOperator类，提供单例对象
imOperator = __imOperator()
