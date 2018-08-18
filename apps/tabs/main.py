def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='abcTabbar'):

        # tabbar栏的页面需要需要定义在Tabbar内部，页面至最少2个，最多5个。
        # 当设置 position 为 top 时，将不会显示 icon
        with Tabbar(position='bottom', textColor='#000000', textSelectedColor='#e03a58'):
            page1()
            page2()
            page3()
class page1(Page): 

    text='A'
    selectedIconPath='img/money1.png'
    iconPath='img/money.png'
    def UI():
        Text(text='这是A页面')
class page2(Page):

    text='B'
    selectedIconPath='img/money1.png'
    iconPath='img/money.png'
    def UI():
        Text(text='这是B页面',onTap=move)
    def move():
        mo.switchTab('page3')
class page3(Page):

    text='C'
    selectedIconPath='img/money1.png'
    iconPath='img/money.png'
    def UI():
        Text(text='这是C页面')