def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='上传测试'):
        index()
        second()

class index(Page):
    naviBarTitle = 'token例子小程序'
    background = "http://material.motimaster.com/appmaker/keric/5662.jpg"
    def UI():
        Button(name='btn',text="进入匹配",size=[300,100],pos=[300,900],type="primary")
    def onInit():
        if mo.token.isHost():
            mo.console('主态进入小程序')
            #if mo.token.get()
            if user.get('token1') == None:
                mo.console('主态用户第一次进入小程序')
                if mo.token._isTemporary():
                    mo.console('临时分配的token')
                else:
                    mo.console('不是临时token')

                #不能直接getHostInfo,需要先设置过数据
                mo.token.set('height',172)

                # 可以通过getHostInfo接口获取该token令牌主人的信息 包括 openid nickName avatarUrl gender等内容
                host = mo.token.getHostInfo()
                mo.console(host['openid'])
                mo.console(host['nickName'])
                mo.console(host['avatarUrl'])

                # 可以通过set  和get 在该Token令牌中设置值获取值
                height = mo.token.get('height')
                mo.console(height)
                #设置了信息之后就不再是临时token啦
                if mo.token._isTemporary():
                    mo.console('是临时token2')
                else:
                    mo.console('不是临时token2')

                
                tokenid = mo.token.id  #当前的tokenid 如果用户没有带token进来那么这个token是自动分配的一个id
                mo.console(tokenid)

                #正常操作是主态用户第一次进入之后把当前token保存起来一般放到user里面
                user.set('token1',tokenid)

            else:
                mo.console('主态用户进入小程序已经有token啦--第二次访问')
                tokenid = user.get('token1')  #此时只是拿到了Token
                token = mo.getToken(tokenid)  #此时拿到了真的token令牌

                #可以在令牌中取得信息
                height = token.get('height') # 这个时候不是用mo.token 而是用Token 此时页面存在的是临时token 上一步操作拿到的是有数据的Token
                mo.console(height)#从token中取得信息

                #可以用token去做跳转
                #例如
                token.goto('second')#带着token取到第二页  第二页的Token就是该值
        else:
            mo.console('客态进入小程序')
            #客态进入小程序 一定是带着主态的token进来的
            #客态一进来就可以获取主态的各种信息
            
            host = mo.token.getHostInfo()
            mo.console(host['openid'])
            mo.console(host['nickName'])
            mo.console(host['avatarUrl'])
            if mo.token.getGuestInfo(user.openid)==None:#如果该访客之前没有访问过匹配过有记录 

                #客人进来后可以通过markAsGuest在token中记录信息
                mo.token.markAsGuest({
                    'score': random.randint(1,100)
                })
            mo.token.goto('second')
            


class second(Page):
    naviBarTitle = '页面二'
    background = "http://material.motimaster.com/appmaker/keric/5662.jpg"
    def UI():
        #Button(text="没什么用的按钮",size=[500,100],pos=['center',100],type="primary")
        with List(name='matchList',pos=[25,20]):
            with Box(size=[700,200], border='1rpx solid black', borderRadius=20):
                Image(src='{item.hostAvatarUrl}', size=[100,100], borderRadius='50%', pos=[20,0])
                Image(src='{item.guestAvatarUrl}', size=[100,100], borderRadius='50%', pos=[400,0])
                Text(text='{item.hostNickName}', pos=[20,100])
                Text(text='{item.guestNickName}', pos=[400,100])
                Text(text='{item.score}', pos=[500,80], color='red')

    def onInit():
        #因为是
        if mo.token.isHost():
            mo.console('主人进来看到的')

        else:
            mo.console('客人进来看到的')
        host = mo.token.getHostInfo()
        guests = mo.token.getGuestList()
        page.matchList.data=[]
        if len(guests)>0:
            for i in range(len(guests)):
                page.matchList.data.append({
                    'hostAvatarUrl': host['avatarUrl'],
                    'guestAvatarUrl': guests[i]['avatarUrl'],
                    'hostNickName': host['nickName'],
                    'guestNickName': guests[i]['nickName'],
                    'score':guests[i]['score'],
                    })