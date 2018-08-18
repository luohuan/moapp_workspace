import json
all_data= [
{
'who':'爱人',
'detail':['你们有着崇高的理想和追求，甘愿为共同热爱的事业而奋斗终生。正是因为如此，你跟TA最终结为连理。在你的内心，TA就是你的灵魂伴侣。每当疲惫、困惑时，你总能从TA那里得到灵魂上的安抚。','你们有着崇高的理想和追求，甘愿为共同热爱的事业而奋斗终生。正是因为如此，Ta跟你最终结为连理。在Ta的内心，你就是Ta的灵魂伴侣。每当疲惫、困惑时，Ta总能从你那里得到灵魂上的安抚。'],
'gender':'5'
},
{
'who':'恋人',
'detail':['情投意合的你们来世会成为一对忠诚的恋人。没有猜疑、没有苛求，只需一个眼神，你们就能通晓对方的心意。生活也许并不能尽如人意，但TA的陪伴却给你带来了直面挫折的勇气和力量。','情投意合的你们来世会成为一对忠诚的恋人。没有猜疑、没有苛求，只需一个眼神，你们就能通晓对方的心意。生活也许并不能尽如人意，但你的陪伴却给Ta带来了直面挫折的勇气和力量。'],
'gender':'5'
},
{
'who':'闺蜜',
'detail':['你会在最美的年华，遇见一个陪你笑、陪你疯的人。来世的TA不漂亮，也不温柔，但对你却掏心掏肺，真情付出。恋人吵架会分手，但好闺蜜一牵手就是一辈子。','Ta会在最美的年华，遇见一个陪Ta笑、陪Ta疯的人。来世的你不漂亮，也不温柔，但对Ta却掏心掏肺，真情付出。恋人吵架会分手，但好闺蜜一牵手就是一辈子。'],
'gender':'4'
},
{
'who':'姐姐',
'detail':['来世的TA是你的长姐，不仅生得一副好皮囊，更有一颗温柔聪慧的心。无数个阳光明媚的下午，TA牵着你的手， 嬉戏在放学回家的小路上。重重的书包全压在TA一个人的肩膀上，一压就是一整个童年。','来世的你是Ta的长姐，不仅生得一副好皮囊，更有一颗温柔聪慧的心。无数个阳光明媚的下午，你牵着Ta的手， 嬉戏在放学回家的小路上。重重的书包全压在你一个人的肩膀上，一压就是一整个童年。'],
'gender':'2'
},
{
'who':'妹妹',
'detail':['TA胆子不大，却总爱捉弄人。爱吃棒棒糖，爱穿粉色裙子。在你眼里，TA永远是一个长不大的小孩。生气时，你就是TA的出气筒。失落时，你就是TA的抱抱熊。','你胆子不大，却总爱捉弄人。爱吃棒棒糖，爱穿粉色裙子。在Ta眼里，你永远是一个长不大的小孩。生气时，Ta就是你的出气筒。失落时，Ta就是你的抱抱熊。'],
'gender':'2'
},
{
'who':'弟弟',
'detail':['从小TA就是你最忠实的粉丝，总爱跟在你身后。你做什么，TA也学着做什么。慢慢的，你教会了TA唱歌、游泳、打球、下象棋……下一世，你们会陪伴着彼此度过生命的大部分时光，相亲相爱。','从小你就是Ta最忠实的粉丝，总爱跟在Ta身后。Ta做什么，你也学着做什么。慢慢的，Ta教会了你唱歌、游泳、打球、下象棋……下一世，你们会陪伴着彼此度过生命的大部分时光，相亲相爱。'],
'gender':'1'
},
{
'who':'哥哥',
'detail':['来世的TA是你的哥哥，在家一副吊儿郎当的样子，总爱占你便宜。在外却化身正义使者，时刻保护着你的安全。你们互相嫌弃，拌起嘴来丝毫不给对方情面。即便如此，TA在你生活中仍旧是不可或缺的存在。','来世的你是Ta的哥哥，在家一副吊儿郎当的样子，总爱占Ta便宜。在外却化身正义使者，时刻保护着Ta的安全。你们互相嫌弃，拌起嘴来丝毫不给对方情面。即便如此，你在Ta生活中仍旧是不可或缺的存在。'],
'gender':'1'
},
{
'who':'死党',
'detail':['与我们交往最多的人被称为朋友，而与我们交往最密切的朋友则被称为死党。来世的TA作为你的死党，会在你阴郁孤独时，像一根线似的牵引着你走向光明。这根线，柔韧无比，除非你亲自剪断它。别人的剪刀是剪不断的。','朋友易得，死党难求。来世的你作为Ta的死党，会在Ta阴郁孤独时，像一根线似的牵引着Ta走向光明。这根线，柔韧无比，除非Ta亲自剪断它。别人的剪刀是剪不断的。'],
'gender':'0'
},
{
'who':'知己',
'detail':['人之相知，贵相知心。正所谓，“万两黄金容易得，知心一个也难求”。来世的TA是最了解你，也最信赖你的那个人。在他面前你可以放下一切伪装和顾虑，完全展露自己最真实的灵魂。','人之相知，贵相知心。正所谓，“万两黄金容易得，知心一个也难求”。来世的你是最了解Ta，也最信赖Ta的那个人。在你面前Ta可以放下一切伪装和顾虑，完全展露自己最真实的灵魂。 '],
'gender':'0'
},
{
'who':'发小',
'detail':['你们一个冷静如水，一个热烈似火。水火不相容的你们，相处过程中常常会碰撞出火药味。即便如此，你们的感情历经时间的淬炼，却越来越坚不可摧。那份小打闹到大的情谊，是造物主给予你下一世生命的最美好的礼物。','你们一个冷静如水，一个热烈似火。水火不相容的你们，相处过程中常常会碰撞出火药味。即便如此，你们的感情历经时间的淬炼，却越来越坚不可摧。那份小打闹到大的情谊，是造物主给予你们下一世生命的最美好的礼物。'],
'gender':'0'
},
{
'who':'表妹',
'detail':['小时候的你，最喜欢黏的人就是TA。TA讲起故事来绘声绘色，还会画各种卡通动物。TA出嫁的那天，你哭了一天，眼睛哭得又红又肿。但值得高兴的是，从此世上又多了一个好妻子、好妈妈。','巧笑倩兮，美目盼兮！ 来世的你，人见人爱，颜值高，智商也高。每到放假，你们便会玩在一起。人小鬼大的你是玩游戏的一流高手，每次和你比赛打赌，Ta都会输掉自己的压箱底宝贝。'],
'gender':'2'
},
{
'who':'表姐',
'detail':['小时候的你，最喜欢黏的人就是TA。TA讲起故事来绘声绘色，还会画各种卡通动物。TA出嫁的那天，你哭了一天，眼睛哭得又红又肿。但值得高兴的是，从此世上又多了一个好妻子、好妈妈。','小时候的Ta，最喜欢黏的人就是你。你讲起故事来绘声绘色，还会画各种卡通动物。你出嫁的那天，Ta哭了一天，眼睛哭得又红又肿。但值得高兴的是，从此世上又多了一个好妻子、好妈妈。'],
'gender':'2'
},
{
'who':'室友',
'detail':['学生时代，你们同住一个屋檐下，彼此产生了非常深厚的感情。休息日，TA会陪你一起逛街、看电影。生病时，TA会放下手中的一切来照顾你。面对生活中的小烦恼，你第一时间想到的是跟TA倾诉。 在你看来，TA不只是你的朋友，更是家人。','学生时代，你们同住一个屋檐下，彼此产生了非常深厚的感情。休息日，你会陪Ta一起逛街、看电影。Ta生病时，你会放下手中的一切来照顾Ta。面对生活中的小烦恼，Ta第一时间想到的是跟你倾诉。 在Ta看来，你不只是Ta的朋友，更是家人。'],
'gender':'6'
},
{
'who':'同学',
'detail':['来世的你与TA同窗数年，你们一起排队打饭、一起操场跑圈、一起闷头做题……颓废时相互打气，考试时又相互较劲。青春散场，同学各奔东西，但那份纯粹的美好却会被保存心间，像美酒一般，愈发醇香。','来世的Ta与你同窗数年，你们一起排队打饭、一起操场跑圈、一起闷头做题……颓废时相互打气，考试时又相互较劲。青春散场，同学各奔东西，但那份纯粹的美好却会被保存心间，像美酒一般，愈发醇香。'],
'gender':'0'
},
{
'who':'同桌',
'detail':['课堂笔记没记？TA会把自己的笔记借给你。作业有几道题没算出？TA会耐心把解题思路讲给你。下一世，能够遇上这样的同桌，算你走运了。不知不觉中，你就被TA从学渣修炼成了学霸。','课堂笔记没记？你会把自己的笔记借给Ta。作业有几道题没算出？你会耐心把解题思路讲给Ta。下一世，能够遇上你这样的同桌，算Ta走运了。不知不觉中，Ta就被你从学渣修炼成了学霸。'],
'gender':'0'
},
{
'who':'偶像',
'detail':['下一世，TA是一位实力超群的偶像。第一次见到TA，你就沦为TA的铁杆粉丝。TA高高在上，非常人所能接近。但在目之所及的地方，TA就像是专属于你的一道圣光，能够照亮生活中的所有迷茫。','下一世，你是一位实力超群的偶像。第一次见到你，Ta就沦为你的铁杆粉丝。你高高在上，非常人所能接近。但在目之所及的地方，你就像是专属于Ta的一道圣光，能够照亮生活中的所有迷茫。'],
'gender':'0'
},
{
'who':'爱豆',
'detail':['来世的TA是一个唱跳俱佳，在舞台上散发着耀眼光芒的爱豆，而你在TA眼里只是一个普通人。不过，距离并不会阻止你对TA的爱。正是因为你的默默支持，TA才能更加闪耀，给更多人带来希望和力量。','来世的你是一个唱跳俱佳，在舞台上散发着耀眼光芒的爱豆，而Ta在你眼里只是一个普通人。不过，距离并不会阻止Ta对你的爱。正是因为Ta的默默支持，你才能更加闪耀，给更多人带来希望和力量。'],
'gender':'0'
},
{
'who':'邻居',
'detail':['“远亲不如近邻”。热心的邻居总是可遇而不可求，来世的TA为人非常坦率，且乐于助人。烹饪、茶道、修理、种植、带孩子等手艺样样精通。很多搞不定的家务事，你只需呼唤一下TA，就能很快得到解决。','“远亲不如近邻”。热心的邻居总是可遇而不可求，来世的你为人非常坦率，且乐于助人。烹饪、茶道、修理、种植、带孩子等手艺样样精通。很多搞不定的家务事，Ta只需呼唤一下你，就能很快得到解决。'],
'gender':'0'
},
{
'who':'情敌',
'detail':['你们的品味很接近，都喜欢看同一类型的电影，穿同一个牌子的衣服。更巧的是，你和TA都喜欢过同一个人。来世的你们因为争风吃醋，很遗憾不能成为朋友。','你们的品味很接近，都喜欢看同一类型的电影，穿同一个牌子的衣服。更巧的是，Ta和你都喜欢过同一个人。来世的你们因为争风吃醋，很遗憾不能成为朋友。'],
'gender':'6'
},
{
'who':'体育老师',
'detail':['TA是你来世最不想打交道的一个人，每次动作没做标准，都会被TA罚跑圈。孩童时期的你，每天都盼望着早点摆脱 TA的摧残。不过好在 TA不教你语文，不用担心被调侃“语文是体育老师教的”。','你是Ta来世最不想打交道的一个人，每次动作没做标准，都会被你罚跑圈。孩童时期的Ta，每天都盼望着早点摆脱你的摧残。不过好在你不教语文，不然Ta可能会被调侃“语文是体育老师教的”。'],
'gender':'0'
},
{
'who':'班长',
'detail':['下一世，TA是班级里最优秀的学生，读书刻苦，成绩优秀。身为班长，为了树立足够的威信，TA不得不表现出超乎年龄的成熟老练。这让包括你在内的很多同学对其产生了距离感。但只要你肯走进TA，就会发现TA身上有着像钻石一般的优秀品质。','下一世，你是班级里最优秀的学生，读书刻苦，成绩优秀。身为班长，为了树立足够的威信，你不得不表现出超乎年龄的成熟老练。这让包括Ta在内的很多同学对你产生了距离感。但只要Ta肯走进你，就会发现你身上有着像钻石一般的优秀品质。'],
'gender':'0'
},
{
'who':'家教老师',
'detail':['来世的TA是你的家教老师，毕业于名校，博学多识且举止优雅。TA的课堂生动有趣，道理讲得浅显易懂，令你如沐春风。有这样一位尽心负责的老师，你会收获很多学校学不到的东西。','来世的你是Ta的家教老师，毕业于名校，博学多识且举止优雅。你的课堂生动有趣，道理讲得浅显易懂，令Ta如沐春风。有你这样一位尽心负责的老师，Ta会收获很多学校学不到的东西。'],
'gender':'0'
},
]
gates=[
{'name':'天福门','luck':'擅长交际，因缘极佳'},
{'name':'存禄门','luck':'事业平顺，福禄丰盈'},
{'name':'华盖门','luck':'家族兴旺 ，富贵绵长'},
{'name':'玉锦门','luck':'出身高贵，锦衣玉食'},
{'name':'文曲门','luck':'天生聪慧，少年成名'},
{'name':'聚德门','luck':'慧根深厚，德高望重 '},
{'name':'慈会门','luck':'和善仁慈，享誉八方'},
{'name':'静安门','luck':'心静体勤，一世安康'},
{'name':'临贵门','luck':'与人为善，多遇贵人'},
{'name':'碧瑶门','luck':'姿色出众，桃花兴旺 '},
{'name':'天官门','luck':'官运亨通，福泽常伴'},
{'name':'文彬门','luck':'文质彬彬，事事遂心'},

]
l1=['邻居','姐姐','妹妹','弟弟','哥哥','闺蜜','发小' ,'知己','恋人','爱人']
l2=['室友','表妹','表姐','同桌','同学','死党','知己','闺蜜','发小','恋人','爱人']
l3=['情敌','爱豆','体育老师','家教老师','偶像','同学','室友','表妹','表姐','同桌' ]
def main(): # 定义一个函数
    # 声明MoApp（注，一个小程序只能有一个MoApp）
    with MoApp(appid='wx628e03240351132c', name='下一世',naviBarTitle='下一世',naviBarColor='#2f172d',naviBarStyle='white'):
        page_analyze()
        # 定义一个小程序页面
        page1()#首页动画页
        page_gate()#选门页

        page_sign()
        page_detail()#展示页
        page4()#分享页
        page_check()
        page_test()
class page_analyze(Page):
    def UI():
        pass 

    def onInit():
        # dele=mo.db.yiyi716.find({'user_id':user.id})
        # for i in dele:
        #     mo.db.yiyi716.delete(i['id'])
        # dele=mo.db.yiyi716.find({'user_id':user.id})
        # mo.console(('database',dele))

        # mo.redirectTo('page1',status='host',host_id=user.id)
        # return
     

        is_host=mo.db.yiyi716.find({'user_id':user.id})       
        if page.options.user_id:       
            if page.options.user_id != user.id:
                host_info=mo.db.yiyi716.find({'user_id':page.options.user_id})[0]
                friends=host_info['friends']
                mo.console(('frid',user.id,friends))
                for friend in friends:
                    if friend['friends_id']==user.id:
                        mo.redirectTo('page_detail',status='guest',host_id=page.options.user_id)
                        return
                mo.redirectTo('page_gate',status='guest',host_id=page.options.user_id)
            else:
                mo.redirectTo('page_detail',status='host',host_id=page.options.user_id)
       
        elif is_host:
            mo.redirectTo('page_detail',status='host',host_id=user.id)
        else:
            mo.redirectTo('page1',status='host',host_id=user.id)

class page1(Page):
    
    def UI():
        
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        with Box(name='animabox1',pos=[0,0],size=[750,1334],hidden=True):
            with Box(pos=[0,0],size=[750,1334],effect = fadein(size=(0,1),d=0,t=2,c=1,s=0)):#载入动画
                Image(src='http://material.motimaster.com/shiyimin1531886202000/guangxian.png',pos=['center',100],size=[452,685],effect = fadein(size=(0,1),d=1,t=2,c=1,s=0,w="*-*"))
                Image(src='http://material.motimaster.com/shiyimin1531886198000/banzi.png',pos=['center',80],size=[235,150],effect = zoomin(d=0,t=2,c=1,p=0,s=0))
                Image(src='http://material.motimaster.com/shiyimin1531886209000/xiankuang.png',pos=['center',50],size=[400,200],effect = zoomin(d=0,t=2,c=1,p=0,s=0))
                Image(src='http://material.motimaster.com/shiyimin1531895669000/xiaoren.png',pos=['center',420],size=[110,144],effect = [fadein(size=(0,1),d=2,t=2,c=1,s=0,w="*-*"),move(path=[(25,420), (25,418)], d=2,t=1.2, c=0,p=0)])
                Text(text='生命轮回不休',pos=['center',680],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=2.5,t=2,c=1,s=0))
                Text(text='下一世，你的运势',pos=['center',760],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=3,t=2,c=1,s=0,w="*-*"))
                Text(text='又会是怎样的呢？',pos=['center',830],color='#FFFFFF',fontSize=38,fontWeight=500,effect = fadein(size=(0,1),d=3.5,t=2,c=1,s=0,w="*-*"))
                #Image(src='http://material.motimaster.com/shiyimin1531473477000/lazhude.png',pos=['center',270],size=[464,613],effect = fadein(size=(0,1),d=3,t=2,c=1,s=0,w="*-*"))#蜡烛
                #Button(text = '开启来世之旅 ',fontWeight = 'bolder',borderRadius = '4px',background = '#5e5ca5',color = '#FFFFFF',effect = fadein(size=(0,1),d=4,t=2,c=1,s=0,w="*-*"),boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',fontSize=32,lineHeight=60,pos =['center',950],size=[220,60], onTap=moui.goto('page2'))
            
                Button(text = '开启来世之旅 ',openType='getUserInfo',fontWeight = 'bolder',borderRadius = '4px',background = '#5e5ca5',color = '#FFFFFF',effect = fadein(size=(0,1),d=4,t=2,c=1,s=0,w="*-*"),boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',fontSize=32,lineHeight=70,pos =['center',950],size=[220,70], onTap=gotopage)
    def onInit():
        page.animabox1.hidden = False
    def gotopage():
        mo.redirectTo('page_gate',status='host',host_id=user.id)#上线后开启
    
    # def gotopage():
    #      mo.redirectTo('page_check',status='host',host_id=user.id)
class page_gate(Page):
   
    def UI():        
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        with Box(name='animabox',pos=[0,0],size=[750,1334],hidden=True):#选门动画
            
            Text(text='佛说，欲通往下一段缘，必先开启一扇门',pos=['center',10],color='#FFFFFF',fontSize=30,effect = fadein(size=(0,1),d=0.5,t=2,c=1,p=1,s=0))
            Image(pos=['center',70],size=[40,33],src='http://material.motimaster.com/shiyimin1531473851000/jiantou.png',effect =[fadein(size=(0,1),d=1,t=2,c=1,p=1,s=0),move(path=[(10,70),(10,80)], t=1.2, c=0,p=1)]) # 小箭头
            Text(text='请选择下一世，你最想开启的门',pos=['center',130],color='#FFFFFF',fontSize=30,fontWeight=600,effect = fadein(size=(0,1),d=1.5,t=2,c=1,p=1,s=0)) 
            
            with Box(pos=[0,-60],size=[750,1000],effect = fadein(size=(0,1),d=2,t=2,c=1,p=1,s=0)):
                with Box(pos=[0,0],size=[750,700],effect=move(path=[(30,320), (30,360)], t=3, c=0,p=1)):
                # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                    Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[670,760],pos=[0,0])#大门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[30,37],pos=[440,80],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#1左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[60,57],pos=[245,175],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#2左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,35],pos=[110,240],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,47],pos=[5,530],effect = fadein(d=0,t=1,c=0,p=1,s=0))#4左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,25],pos=[230,470],effect = fadein(d=0,t=1.2,c=0,p=1,s=0))#5左向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,27],pos=[600,275],effect = fadein(d=0,t=1.1,c=0,p=1,s=0))#1右向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[405,420],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#2右向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,35],pos=[625,550],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3右向光
                    Button(pos=[440,0],openType='getUserInfo',size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='440,0',No=4,gate_name='俱舍门'))#1按钮
                    Button(pos=[225,95],openType='getUserInfo',size=[130,226],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='215,75',No=3,gate_name='禅门'))#2按钮
                    Button(pos=[120,235],openType='getUserInfo',size=[80,116],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='120,200',No=2,gate_name='天台门'))#3按钮
                    Button(pos=[15,380],openType='getUserInfo',size=[150,196],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='15,380',No=7,gate_name='法相门'))#4按钮
                    Button(pos=[240,410],openType='getUserInfo',size=[75,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='240,410',No=8,gate_name='律门'))#5按钮
                    Button(pos=[550,185],openType='getUserInfo',size=[80,166],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='550,185',No=5,gate_name='真言门'))#1按钮
                    Button(pos=[365,350],openType='getUserInfo',size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='365,350',No=9,gate_name='华严门'))#2按钮
                    Button(pos=[540,375],openType='getUserInfo',size=[120,186],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='540,375',No=10,gate_name='净土门'))#3按钮

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(40,310), (40,350)], t=2, c=0,p=1)):#左上角门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                    Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[80,176],pos=[0,0])#门
                    Button(pos=[0,0],size=[80,176],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='85,330',No=1,gate_name='成实门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,330), (640,330)], t=3, c=0,p=1)):#右上角门
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                    Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[60,132],pos=[0,0])#门
                    Button(pos=[0,0],size=[60,132],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='600,330',No=6,gate_name='三论门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(175,930), (195,930)], t=3.5, c=0,p=1)):#左下角门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                    Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[90,198],pos=[0,0])#门
                    Button(pos=[0,0],size=[90,198],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='175,930',No=11,gate_name='涅槃门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,940), (600,970)], t=3, c=0,p=1)):#右下角门
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                    Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[80,176],pos=[0,0])#门
                    Button(pos=[0,0],size=[80,176],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='600,940',No=12,gate_name='地论门'))
    def onInit():
        page.animabox.hidden = False
    def save_record():

        mo.console(params.p)
        
        if page.options.status=='host':  
            if page.options.repick: 
                info=mo.db.yiyi716.find({'user_id':user.id})[0]
                mo.db.yiyi716.update(info['id'],{'pos':params.p,'gate_name':params.gate_name,'No':params.No,})
                mo.redirectTo('page_detail',status='host',host_id=user.id)
            else:        
                mo.db.yiyi716.insert({'gender':user.gender,'user_id':user.id,'user_avatar':user.avatarUrl,'pos':params.p,'gate_name':params.gate_name,'No':params.No,'user_name':user.nickName,'payinfo':0,'friends':[]})
                #mo.goto('page_detail',status='host',host_id=user.id)
                mo.redirectTo('page_sign',status='host',host_id=page.options.host_id,choose=params.gate_name)
        else:
            if page.options.repick: 
                info=mo.db.yiyi716.find({'user_id':page.options.host_id})[0]
                friends=info['friends']
                for friend in friends:
                    if friend['friends_id']==user.id:
                        friend['friends_pos']=params.p
                        friend['gate_name']=params.gate_name
                        friend['No']=params.No
                        break
                mo.db.yiyi716.update(info['id'],{'friends':friends})
                mo.redirectTo('page_detail',status='guest',host_id=page.options.host_id)
            else:    
                info=mo.db.yiyi716.find({'user_id':page.options.host_id})
                friends=info[0]['friends']
                friends.append({'gender':user.gender,'friends_name':user.nickName,'payinfo':0,'friends_avatar':user.avatarUrl,'friends_id':user.id,'friends_pos':params.p,'gate_name':params.gate_name,'No':params.No,})
                mo.db.yiyi716.update(info[0]['id'],{'friends':friends})
                mo.redirectTo('page_detail',status='guest',host_id=page.options.host_id)
class page_sign(Page):
    def UI():       
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        
        Image(pos=[120,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='我的好友缘分部落图',pos=['center',20],fontSize=32,color='#FFFFFF')
        Image(pos=[540,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
            
        with Box(pos=[0,-60],size=[750,450]):
            with Box(pos=[0,0],size=[750,450],effect=move(path=[(170,130), (170,140)], t=1.8, c=0,p=1)):
            # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[370,420],pos=[0,0])#大门
               
                #Image(id='3_1',borderRadius='50%',pos=[130,90],size=[45,45]) 
                with Box(size=[162, 162],pos=[130,90]):
                    Image(id='3_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='3_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='2_1',borderRadius='50%',pos=[70,30],size=[45,45])
                with Box(size=[162, 162],pos=[70,30]):
                    Image(id='2_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='2_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='4_1',borderRadius='50%',pos=[240,40],size=[45,45])
                with Box(size=[162, 162],pos=[240,40]):
                    Image(id='4_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='4_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='5_1',borderRadius='50%',pos=[300,45],size=[45,45])
                with Box(size=[162, 162],pos=[300,45]):
                    Image(id='5_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='5_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='10_1',borderRadius='50%',pos=[300,225],size=[45,45])
                with Box(size=[162, 162],pos=[300,225]):
                    Image(id='10_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='10_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
              
                #Image(id='7_1',borderRadius='50%',pos=[50,200],size=[45,45])
                with Box(size=[162, 162],pos=[50,200]):
                    Image(id='7_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='7_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               
                #Image(id='8_1',borderRadius='50%',pos=[130,210],size=[45,45])
                with Box(size=[162, 162],pos=[130,210]):
                    Image(id='8_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='8_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='9_1',borderRadius='50%',pos=[205,130],size=[45,45])
                with Box(size=[162, 162],pos=[205,130]):
                    Image(id='9_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='9_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(155,135), (155,140)], t=1.5, c=0,p=1)):#左上角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[50,110],pos=[0,0])#门
              
                #Image(id='1_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='1_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='1_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(530,145), (535,145)], t=1.6, c=0,p=1)):#右上角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[40,88],pos=[0,0])#门
               
                #Image(id='6_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='6_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='6_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(215,440), (225,440)], t=1.8, c=0,p=1)):#左下角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[60,132],pos=[0,0])#门
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='6_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='6_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
              
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(550,440), (550,450)], t=1.2, c=0,p=1)):#右下角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[50,110],pos=[0,0])#门
                
                #Image(id='12_1',borderRadius='50%',pos=[3,40],size=[45,45])
                with Box(size=[162, 162],pos=[3,40]):
                    Image(id='12_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='12_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
        Text(id='choose',text='',color='#FFFFFF',fontSize=30,pos=['center',600])
        Text(text='选择不同的门，缘分不同',color='#FFFFFF',fontSize=30,pos=['center',680])
        Text(text='分享好友，测测你们的缘分有多近',color='#FFFFFF',fontSize=30,pos=['center',760])
        Text(text='↓ ↓ ↓',color='#FFFFFF',fontSize=30,pos=['center',840])
        #Image(src='',pos=['center',800],size=[])
        Button(name='fenxiang',text='邀请好友来测', lineHeight= 80,size=[300,80],pos=['center',900],fontSize=30,background = '#5e5ca5',color = '#FFFFFF',boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',border = 0,onTap=moui.goto('page4'))
    def onInit():
        page.choose.text='你选择的是'+page.options.choose
        data=mo.db.yiyi716.find({'user_id':user.id})[0]
        avatar=data['user_avatar']
        No=data['No']
        if No==11:
            page.getElement('7_1').src=avatar
            page.getElement('7_1h').src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png'
            page.getElement('7_1').size=[70,70]
            page.getElement('7_1').top=200
            page.getElement('7_1h').top=163
        else:  
            page.getElement(str(No)+'_1').src=avatar
            page.getElement(str(No)+'_1h').src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png'
            page.getElement(str(No)+'_1').size=[70,70]

class page_detail(Page):
    
    def UI():       
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        
        Image(pos=[120,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='我的好友缘分部落图',pos=['center',20],fontSize=32,color='#FFFFFF')
        Image(pos=[540,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
            
        with Box(pos=[0,-60],size=[750,450]):
            with Box(pos=[0,0],size=[750,450],effect=move(path=[(170,130), (170,140)], t=1.8, c=0,p=1)):
            # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[370,420],pos=[0,0])#大门
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[30,37],pos=[440,80],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#1左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[60,57],pos=[245,175],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#2左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,35],pos=[110,240],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,47],pos=[5,530],effect = fadein(d=0,t=1,c=0,p=1,s=0))#4左向光
                # Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,25],pos=[230,470],effect = fadein(d=0,t=1.2,c=0,p=1,s=0))#5左向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,27],pos=[600,275],effect = fadein(d=0,t=1.1,c=0,p=1,s=0))#1右向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[405,420],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#2右向光
                # Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,35],pos=[625,550],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3右向光
                # 
                # 
                #Image(id='3',borderRadius='50%',pos=[130,50],size=[45,45])#主人头像
                with Box(size=[162, 162],pos=[130,50]):
                    Image(id='3',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='3_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='3_1',borderRadius='50%',pos=[130,90],size=[45,45]) 
                with Box(size=[162, 162],pos=[130,90]):
                    Image(id='3_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='3_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='3_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='2',borderRadius='50%',pos=[70,70],size=[45,45])
                with Box(size=[162, 162],pos=[70,70]):
                    Image(id='2',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='2_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='2_1',borderRadius='50%',pos=[70,30],size=[45,45])
                with Box(size=[162, 162],pos=[70,30]):
                    Image(id='2_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='2_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='2_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               # Image(id='4',borderRadius='50%',pos=[240,0],size=[45,45])
                with Box(size=[162, 162],pos=[240,0]):
                    Image(id='4',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='4_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                with Box(size=[162, 162],pos=[240,40]):
                    Image(id='4_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='4_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='4_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='5',borderRadius='50%',pos=[300,85],size=[45,45])
                with Box(size=[162, 162],pos=[300,85]):
                    Image(id='5',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='5_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               # Image(id='5_1',borderRadius='50%',pos=[300,45],size=[45,45])
                with Box(size=[162, 162],pos=[300,45]):
                    Image(id='5_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='5_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='5_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               # Image(id='10',borderRadius='50%',pos=[300,185],size=[45,45])
                with Box(size=[162, 162],pos=[300,185]):
                    Image(id='10',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='10_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='10_1',borderRadius='50%',pos=[300,225],size=[45,45])
                with Box(size=[162, 162],pos=[300,225]):
                    Image(id='10_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='10_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='10_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

                #Image(id='7',borderRadius='50%',pos=[10,230],size=[45,45])
                with Box(size=[162, 162],pos=[10,230]):
                    Image(id='7',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='7_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

                #Image(id='7_1',borderRadius='50%',pos=[50,200],size=[45,45])
                with Box(size=[162, 162],pos=[50,200]):
                    Image(id='7_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='7_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='7_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='8',borderRadius='50%',pos=[130,250],size=[45,45])
                with Box(size=[162, 162],pos=[130,250]):
                    Image(id='8',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='8_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='8_1',borderRadius='50%',pos=[130,210],size=[45,45])
                with Box(size=[162, 162],pos=[130,210]):
                    Image(id='8_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='8_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='8_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='9',borderRadius='50%',pos=[205,170],size=[45,45])
                with Box(size=[162, 162],pos=[205,170]):
                    Image(id='9',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='9_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='9_1',borderRadius='50%',pos=[205,130],size=[45,45])
                with Box(size=[162, 162],pos=[205,130]):
                    Image(id='9_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='9_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='9_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(155,135), (155,140)], t=1.5, c=0,p=1)):#左上角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[50,110],pos=[0,0])#门
                #Image(id='1',borderRadius='50%',pos=[0,0],size=[45,45]) #客人头像
                with Box(size=[162, 162],pos=[0,0]):
                    Image(id='1',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='1_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='1_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='1_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='1_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='1_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(530,145), (535,145)], t=1.6, c=0,p=1)):#右上角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[40,88],pos=[0,0])#门
                #Image(id='6',borderRadius='50%',pos=[0,0],size=[45,45]) #客人头像
                with Box(size=[162, 162],pos=[0,0]):
                    Image(id='6',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='6_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='6_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='6_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='6_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='6_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(215,440), (225,440)], t=1.8, c=0,p=1)):#左下角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[60,132],pos=[0,0])#门
                #Image(id='11',borderRadius='50%',pos=[5,0],size=[45,45]) #客人头像
                with Box(size=[162, 162],pos=[5,0]):
                    Image(id='11',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='11_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='11_1',borderRadius='50%',pos=[5,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='11_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='11_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='11_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(550,440), (550,450)], t=1.2, c=0,p=1)):#右下角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[50,110],pos=[0,0])#门
                #Image(id='12',borderRadius='50%',pos=[3,0],size=[45,45]) #客人头像
                with Box(size=[162, 162],pos=[3,0]):
                    Image(id='12',borderRadius='50%',pos=[0,0],size=[45,45])
                    #Image(id='4_h',borderRadius='50%',src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='12_g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='12_1',borderRadius='50%',pos=[3,40],size=[45,45])
                with Box(size=[162, 162],pos=[3,40]):
                    Image(id='12_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='12_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                    Image(id='12_1g',borderRadius='50%',pos=[-50,-49],size=[147,147],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
        
        Image(pos=[140,520],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='来世缘分详解',pos=['center',500],fontSize=32,color='#FFFFFF')
        Image(pos=[510,520],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        with ScrollBox(scrollY=True,size=[750,460],pos=['center',540]):
            with List(name='list1'):

                with Box(pos=[20,0],size=[720,500],background='rgba(37, 22, 63,0.6)'):
                    
                    Image(src='{item.host_avatar}',borderRadius='50%',pos=[155,20],size=[75,75]) #主人头像

                    Text(text='缘份值{item.score}分',fontSize=28,color='#FFFFFF',pos=['center',8])
                    Box(background='#4aaac0',size=[170,4],pos=['center',50])
                    Text(text='相距{item.distance}公里',fontSize=28,color='#FFFFFF',pos=['center',58])

                    Image(src='{item.friends_avatar}',borderRadius='50%',pos=[460,20],size=[75,75]) #客人头像

                    with Box(pos=[170,100],size=[20,30]):
                        Text(text='{item.host_name}',color='#FFFFFF',pos=['center',0],fontSize=25,textAlign='center') #主人昵称
                        Text(text='({item.host_gatename})',color='#FFFFFF',pos=[-5,30],fontSize=25) #主人选择的门的名字
                    with Box(pos=[475,100],size=[20,30]):
                        Text(text='{item.friends_name}',color='#FFFFFF',pos=['center',0],fontSize=25,textAlign='center') #客人昵称
                        Text(text='({item.friends_gatename})',color='#FFFFFF',pos=[-5,30],fontSize=25) #客人选择的门的名字
         
                    Text(text='{item.pre_who}',color='#c8f9ff',fontSize=28,pos=[10,180])
                    Text(text='{item.who}',color='#FFFFFF',fontSize=28,pos=[190,180])
                    Text(text='来世缘分详解',color='#c8f9ff',fontSize=28,pos=[10,240])
                    Text(text='{item.detail}',color='#FFFFFF',fontSize=24,size=[500,300],pos=[190,240])
        Button(id='repick',text='我要重选', size=[100,50],pos=[650,450],fontSize=21,background = '#5e5ca5',color='#FFFFFF',border =1,onTap=repick)         
        Button(id='share_b',text='邀请好友来测',hidden=True, lineHeight= 80,size=[300,80],pos=['center',1050],fontSize=30,background = '#5e5ca5',color = '#FFFFFF',boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',border = 0,onTap=moui.goto('page4'))
        Button(id='build_b',text='创建我的好友缘分图',hidden=True, lineHeight= 80,size=[300,80],pos=['center',1050],fontSize=30,background = '#5e5ca5',color = '#FFFFFF',boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',border = 0,onTap=moui.goto('page_analyze'))   
    def onInit():
        friends_data=[]
        data=mo.db.yiyi716.find({'user_id':page.options.host_id})[0]
        host_gatename=data['gate_name']
        host_pos=data['pos'].split(',')
        host_avatar=data['user_avatar']
        host_id=page.options.host_id
        host_name=data['user_name']
        friends=data['friends']
        host_No=data['No']
        host_gender=data['gender']
        random.seed(int(host_pos[0])+int(host_pos[1]))
        mo.console(('friends',friends))
        for friend in friends:
            num=random.randint(0,21) 
            friend_No=int(friend['No'])
            friend_pos= friend ['friends_pos'].split(',')
            distance=abs(int(friend_pos[1])-int(host_pos[1]))+abs(int(friend_pos[0])-int(host_pos[0]))+random.randint(0,100)
            friend_gender=friend['gender']
            a=abs(int(friend['No'])-int(host_No))
            b=abs(int(friend['No'])+12-int(host_No))
            c=abs(int(friend['No'])-12-int(host_No))
            s=min(a,b,c)
           
            mo.console(('host_gender',str(type(host_gender)),host_gender))
            mo.console(('friend_gender',str(type(friend['gender'])),friend['gender']))
            while True:
                # if host_gender==1:
                #     mo.console('qwer')
                #     break
                if s==0:
                    who=random.choice(l1)
                    index=l1.index(who)
                    score=1.5*index+85
                elif s<6:
                    who=random.choice(l2)
                    index=l2.index(who)
                    score=2*index+75
                else:
                    who=random.choice(l3)
                    index=l3.index(who)
                    score=2.5*index+50

                for i in all_data :
                    if i['who']==who:
                        ge=int(i['gender'])
                if friend_gender==0:
                    if ge==0:
                        break
                    else:
                        pass
                elif friend_gender==1:
                    if ge==0 or ge ==1:
                        break
                    
                    elif( ge==3 or ge==6)and(host_gender==1):
                        break
                    elif (ge==5) and (host_gender==2):
                        break
                    else:
                        pass
                else:
                    if ge==0 or ge ==2:
                        break
                    
                    elif( ge==4 or ge==6)and(host_gender==2):
                        break
                    elif (ge==5) and (host_gender==1):
                        break
                    else:
                        pass
            if who=='恋人':
                for i in l1 :
                        if i=='恋人':
                            l1.pop(l1.index('恋人'))
                for i in l2 :
                        if i=='恋人':
                            l2.pop(l2.index('恋人'))
            if who=='爱人'  :
                for i in l1 :
                        if i=='爱人':
                            l1.pop(l1.index('爱人'))
                for i in l2 :
                        if i=='爱人':
                            l2.pop(l2.index('爱人'))
            for i in all_data:
                if i['who']==who:
                    detail=i['detail']        
                
            mo.console(('who',who))
            friends_data.append({'score':score,'No':friend['No'],'hidden':True,'friends_pos':friend['friends_pos'],'friends_id':friend['friends_id'],'friends_name':friend['friends_name'],'distance':distance,'host_gatename':host_gatename,'friends_gatename':friend['gate_name'],'host_name':host_name,'host_avatar':host_avatar,'friends_avatar':friend['friends_avatar'],'who':who})

      
        if page.options.status=='host':
            for i in friends_data:
                i['pre_who']='来世Ta是你的'
                for j in all_data:
                    if j['who']==i['who']:
                        i['detail']=j['detail'][0]
            payinfo=data['payinfo']
        else:
            for friend in friends:
                if friend['friends_id']==user.id:
                    payinfo=friend['payinfo']
            c=0
            for i in friends_data:
                i['pre_who']='来世你是Ta的'
                for j in all_data:
                    if j['who']==i['who']:
                        i['detail']=j['detail'][1]
                if i['friends_id']==user.id:
                    friends_data.insert(0,friends_data[c])
                    friends_data.pop(c+1)
                c+=1
        img_list=[]
        for i in range(12):
            img_list.append([])
        if  friends_data:      
            for i in range(len(friends_data)):

                try:
                    #friends_data[i]['hidden']=False
                    N=int(friends_data[i]['No'])
                    img_list[N-1].append(friends_data[i]['friends_avatar'])
                except:
                    pass
        else:
            pass
        mo.console(('ssss',img_list))




        for i in range(1,13):
           # page.getElement(str(i+1)).src=host_avatar
            try:
                page.getElement(str(i)).src=img_list[i-1][0]
                page.getElement(str(i)+'_g').src='http://material.motimaster.com/shiyimin1532072101000/kerentouxiangguanghuan.png'
                page.getElement(str(i)+'_1').src=img_list[i-1][1]
                page.getElement(str(i)+'_1g').src='http://material.motimaster.com/shiyimin1532072101000/kerentouxiangguanghuan.png'
            except:
                pass
            if i==host_No:
                page.getElement(str(i)+'_1').size=[70,70]
                page.getElement(str(i)+'_1').src=host_avatar
                page.getElement(str(i)+'_1h').src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png'
            else:
                pass
        page.list1.data=friends_data
        
        mo.console(('f',data))


        if page.options.status=='host':
            page.share_b.hidden=False
            page.share.title = "下一世，你是我的谁？"
            page.share.page = 'page_analyze'
            page.share.options = {'user_id':user.id}
        else:
            page.build_b.hidden=False

    def onPullDownRefresh():
        onInit()

    def repick():
        mo.redirectTo('page_gate',status=page.options.status,repick=True,host_id=page.options.host_id)
    def go_pay():
        data=mo.db.yiyi716.find({'user_id':page.options.host_id})[0]
        if page.options.status=='host':
            
            mo.db.yiyi716.update(data['id'],{'payinfo':data['payinfo']+1})
            mo.goto('page_detail',status='host',host_id=user.id)
        else:
            friends=data['friends']
            for i in friends:
                if i['friends_id']==user.id:
                    mo.console(('fffff',i))
                    i['payinfo']+=1
                    mo.console(('fffff',i))
                    mo.db.yiyi716.update(data['id'],{'friends':friends})
                    mo.redirectTo('page_detail',status='guest',host_id=page.options.host_id)
                    return 



class page4(Page):
    
    def UI():
        Image(pos=[0,0],size=[750,296],src='http://material.motimaster.com/shiyimin1531820626000/share.jpg') # 背景图
        #Text(text='下一世',pos=['center',50],color='#FFFFFF',fontSize=30,fontWeight=600)
        #Text(text='你是我的谁？',pos=['center',100],color='#FFFFFF',fontSize=30,fontWeight=600)
        Image(id='img',borderRadius='50%',size=[300,300],pos=['center',330]) #二维码
        Text(name='shibie',hidden = True,pos=['center',650],color='#000000',fontSize=25)
        ShareButton(text='分享给朋友',size=[320,80],pos=['center',750],fontSize=33,background = '#5e5ca5',color = '#FFFFFF',border = 0,boxShadow ='3px 4px 3px 1px rgba(0,0,0,0.3)',)
        Button(name='pyq',hidden=True,size=[320,80],pos=['center',870],fontSize = 33,onTap=save_img,color = '#5e5ca5',border = '1px solid #5e5ca5',plain=True)

    def onInit():
        page.pyq.hidden = False
        page.pyq.text = '保存朋友圈海报'

        page.shibie.hidden = False
        page.shibie.text ='长按识别二维码'

        page.share.title = "下一世，你是我的谁？"
        page.share.imageUrl = 'http://material.motimaster.com/huxiaofeng1531997047000/80719175912.png'
        page.share.page = 'page_analyze'
        page.share.options = {'user_id':user.id}
        params = {
            'page': 'page_analyze',
            'width': 150,
            'options': {
                'user_id':user.id
            }
        }
        retParams = mo.acode.getWxAcodeUrl(params)
        erweima = None
        if retParams['ret'] == 0:
            erweima = retParams['url']
        canvas = mo.mopic.createCanvas(300, 300)   
        canvas.addImage(erweima, pos=[0, 0,300,300])
        canvas.addImage(user.avatarUrl, pos=[82,82,135,135],mask='circle')
        res=canvas.makeImage()
        if res['ret'] == 0:
            page.img.src=res['url']
            page.data.img=res['url']
        else:
            mo.console('制图未完成！')
    def onShareSuccessed():
        mo.goto('page_detail',status='host',host_id=user.id)

    def save_img():
        mo.console(('img',page.data.img))
        canvas = mo.mopic.createCanvas(776, 700)
        canvas.addImage('http://material.motimaster.com/wangzhen1531989467000/white.png', pos=[0, 0, 776, 900])
        canvas.addImage('http://material.motimaster.com/shiyimin1531820626000/share.jpg', pos=[0, 0, 776, 296])
        canvas.addImage(page.data.img, pos=[228, 320, 310,310])
        res = canvas.makeImage()

        if res['ret'] == 0:
            
            mo.saveImage(res['url'])
        else:
            mo.console('制作图片出错！！')

class page_check(Page):
    def UI():        
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        with Box(name='animabox',pos=[0,0],size=[750,1334],hidden=True):#选门动画
            
            Text(text='佛说，欲通往下一段缘，必先开启一扇门',pos=['center',10],color='#FFFFFF',fontSize=30,effect = fadein(size=(0,1),d=0.5,t=2,c=1,p=1,s=0))
            Image(pos=['center',70],size=[40,33],src='http://material.motimaster.com/shiyimin1531473851000/jiantou.png',effect =[fadein(size=(0,1),d=1,t=2,c=1,p=1,s=0),move(path=[(10,70),(10,80)], t=1.2, c=0,p=1)]) # 小箭头
            Text(text='请选择下一世，你最想开启的门',pos=['center',130],color='#FFFFFF',fontSize=30,fontWeight=600,effect = fadein(size=(0,1),d=1.5,t=2,c=1,p=1,s=0)) 
            
            with Box(pos=[0,-60],size=[750,1000],effect = fadein(size=(0,1),d=2,t=2,c=1,p=1,s=0)):
                with Box(pos=[0,0],size=[750,700],effect=move(path=[(30,320), (30,360)], t=3, c=0,p=1)):
                # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                    Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[670,760],pos=[0,0])#大门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[30,37],pos=[440,80],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#1左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[60,57],pos=[245,175],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#2左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,35],pos=[110,240],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,47],pos=[5,530],effect = fadein(d=0,t=1,c=0,p=1,s=0))#4左向光
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,25],pos=[230,470],effect = fadein(d=0,t=1.2,c=0,p=1,s=0))#5左向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,27],pos=[600,275],effect = fadein(d=0,t=1.1,c=0,p=1,s=0))#1右向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[405,420],effect = fadein(d=0,t=0.9,c=0,p=1,s=0))#2右向光
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[35,35],pos=[625,550],effect = fadein(d=0,t=0.7,c=0,p=1,s=0))#3右向光
                    Button(pos=[440,0],openType='getUserInfo',size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='440,0',No=4,gate_name='俱舍门'))#1按钮
                    Button(pos=[225,95],openType='getUserInfo',size=[130,226],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='215,75',No=3,gate_name='禅门'))#2按钮
                    Button(pos=[120,235],openType='getUserInfo',size=[80,116],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='120,200',No=2,gate_name='天台门'))#3按钮
                    Button(pos=[15,380],openType='getUserInfo',size=[150,196],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='15,380',No=7,gate_name='法相门'))#4按钮
                    Button(pos=[240,410],openType='getUserInfo',size=[75,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='240,410',No=8,gate_name='律门'))#5按钮
                    Button(pos=[550,185],openType='getUserInfo',size=[80,166],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='550,185',No=5,gate_name='真言门'))#1按钮
                    Button(pos=[365,350],openType='getUserInfo',size=[80,146],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='365,350',No=9,gate_name='华严门'))#2按钮
                    Button(pos=[540,375],openType='getUserInfo',size=[120,186],border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='540,375',No=10,gate_name='净土门'))#3按钮

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(40,310), (40,350)], t=2, c=0,p=1)):#左上角门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                    Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[80,176],pos=[0,0])#门
                    Button(pos=[0,0],size=[80,176],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='85,330',No=1,gate_name='成实门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,330), (640,330)], t=3, c=0,p=1)):#右上角门
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                    Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[60,132],pos=[0,0])#门
                    Button(pos=[0,0],size=[60,132],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='600,330',No=6,gate_name='三论门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(175,930), (195,930)], t=3.5, c=0,p=1)):#左下角门
                    Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                    Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[90,198],pos=[0,0])#门
                    Button(pos=[0,0],size=[90,198],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='175,930',No=11,gate_name='涅槃门'))

                with Box(pos=[0,0],size=[150,330],effect=move(path=[(600,940), (600,970)], t=3, c=0,p=1)):#右下角门
                    Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                    Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[80,176],pos=[0,0])#门
                    Button(pos=[0,0],size=[80,176],openType='getUserInfo',border=0,background = 'rgba(150,150,150,0)',onTap=moui.request(save_record,p='600,940',No=12,gate_name='地论门'))
    def onInit():
        page.animabox.hidden = False
    def save_record():
        mo.redirectTo('page_test',No=params.No)
class page_test(Page):
    def UI():
           
        Image(pos=[0,0],size=[750,1334],src='http://material.motimaster.com/shiyimin1531798710000/zs.jpg',position = 'fixed') # 背景图
        
        Image(pos=[120,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
        Text(text='我的运势说明',pos=['center',20],fontSize=32,color='#FFFFFF')
        Image(pos=[540,40],size=[91,3],src='http://material.motimaster.com/shiyimin1531731473000/dian-1.png')#点点
            
        with Box(pos=[0,-60],size=[750,450]):
            with Box(pos=[0,0],size=[750,450],effect=move(path=[(170,130), (170,140)], t=1.8, c=0,p=1)):
            # with Box(pos=[0,0],size=[750,700],effect=move(path=[(375,500), (390,490), (375,480), (360,490)], t=4, c=0)):
                Image(src='http://material.motimaster.com/shiyimin1531477142000/center.png',size=[370,420],pos=[0,0])#大门
               
                #Image(id='3_1',borderRadius='50%',pos=[130,90],size=[45,45]) 
                with Box(size=[162, 162],pos=[130,90]):
                    Image(id='3_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='3_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='2_1',borderRadius='50%',pos=[70,30],size=[45,45])
                with Box(size=[162, 162],pos=[70,30]):
                    Image(id='2_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='2_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='4_1',borderRadius='50%',pos=[240,40],size=[45,45])
                with Box(size=[162, 162],pos=[240,40]):
                    Image(id='4_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='4_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='5_1',borderRadius='50%',pos=[300,45],size=[45,45])
                with Box(size=[162, 162],pos=[300,45]):
                    Image(id='5_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='5_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='10_1',borderRadius='50%',pos=[300,225],size=[45,45])
                with Box(size=[162, 162],pos=[300,225]):
                    Image(id='10_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='10_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
              
                #Image(id='7_1',borderRadius='50%',pos=[50,200],size=[45,45])
                with Box(size=[162, 162],pos=[50,200]):
                    Image(id='7_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='7_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               
                #Image(id='8_1',borderRadius='50%',pos=[130,210],size=[45,45])
                with Box(size=[162, 162],pos=[130,210]):
                    Image(id='8_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='8_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
                #Image(id='9_1',borderRadius='50%',pos=[205,130],size=[45,45])
                with Box(size=[162, 162],pos=[205,130]):
                    Image(id='9_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='9_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
               
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(155,135), (155,140)], t=1.5, c=0,p=1)):#左上角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[40,42],pos=[-15,110],effect = fadein(size=(1,0.5),d=0.9,t=0.4,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[50,110],pos=[0,0])#门
              
                #Image(id='1_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='1_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='1_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))

            with Box(pos=[0,0],size=[150,330],effect=move(path=[(530,145), (535,145)], t=1.6, c=0,p=1)):#右上角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[30,25],pos=[50,80],effect = fadein(d=0.1,t=0.6,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[40,88],pos=[0,0])#门
               
                #Image(id='6_1',borderRadius='50%',pos=[0,40],size=[45,45])
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='6_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='6_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(215,440), (225,440)], t=1.8, c=0,p=1)):#左下角门
                #Image(src='http://material.motimaster.com/shiyimin1531743808000/zuoxiangguang1.png',size=[50,52],pos=[-15,120],effect = fadein(d=0.6,t=0.7,c=0,p=1,s=0))#左向光
                Image(src='http://material.motimaster.com/shiyimin1531476968000/zuoshangjiao.png',size=[60,132],pos=[0,0])#门
                with Box(size=[162, 162],pos=[0,40]):
                    Image(id='6_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='6_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
              
            with Box(pos=[0,0],size=[150,330],effect=move(path=[(550,440), (550,450)], t=1.2, c=0,p=1)):#右下角门
                #Image(src='http://material.motimaster.com/shiyimin1531477304000/youxiangguang.png',size=[40,37],pos=[60,110],effect = fadein(d=0,t=0.8,c=0,p=1,s=0))#右向光
                Image(src='http://material.motimaster.com/shiyimin1531476717000/youshangjiao.png',size=[50,110],pos=[0,0])#门
                
                #Image(id='12_1',borderRadius='50%',pos=[3,40],size=[45,45])
                with Box(size=[162, 162],pos=[3,40]):
                    Image(id='12_1',borderRadius='50%',pos=[0,0],size=[45,45])
                    Image(id='12_1h',borderRadius='50%',pos=[-43,-36],size=[162,162],effect = fadein(size=(1,0),d=0,t=2,c=0,p=1,s=0))
        Text(id='choose',text='',color='#FFFFFF',fontSize=30,pos=['center',600])

        #Text(text='选择不同的门，缘分不同',color='#FFFFFF',fontSize=30,pos=['center',680])
        #Text(text='分享好友，测测你们的缘分有多近',color='#FFFFFF',fontSize=30,pos=['center',760])
        Text(text='↓ ↓ ↓',color='#FFFFFF',fontSize=30,pos=['center',840])
        Text(id='luck',text='',color='#FFFFFF',fontSize=30,pos=['center',900])
        #Image(src='',pos=['center',800],size=[])
        #Button(name='fenxiang',text='邀请好友来测', lineHeight= 80,size=[300,80],pos=['center',900],fontSize=30,background = '#5e5ca5',color = '#FFFFFF',boxShadow ='3px 4px 3px 1px rgba(200,200,200,0.3)',border = 0,onTap=moui.goto('page4'))
    def onInit():
        No=int(page.options.No)
        for i in range(1,13):
            if i == No:
                page.choose.text='你选择的是'+gates[i-1]['name']
                page.luck.text='你的运势：'+gates[i-1]['luck']
                page.getElement(str(No)+'_1').src=user.avatarUrl
                page.getElement(str(No)+'_1h').src='http://material.motimaster.com/shiyimin1532066648000/touxiangguanghuan.png'
                page.getElement(str(No)+'_1').size=[70,70]