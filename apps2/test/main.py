def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='swiper'):
        index()
signs = ['水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天枰座','天蝎座','射手座','摩羯座']
class index(Page):
    title = 'swiper展示'
    def UI():        
        with SinglePickerText(name='picker1',text='点击选择', opacity=0.8,pos=['center', 88], size=[200,200],color='black',fontSize=26,range=signs):
            this.onChange = onSelectorPickerTextChange
        # with Swiper(id='swiper1', size=[750,240],interval=3000, duration=2000, autoplay=True):
        #     with SwiperItem(id ='dataswiper'):
        #         with Image(pos=[20,20, 710, 200], borderRadius='10px', src ='{item.pic}'):
        #             this.onTap = moui.goto('second', name='{item.name}')
        # # 滑块视图容器  可以自动滑动 interval 定义切换的间隔时间 
        # with Swiper(id ='swiper2', size=[750,240], top=300,interval=3000, duration=2000, autoplay=True):
        #     with SwiperItem(id='imgUrls'):
        #         Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')
        # # 滑块视图容器  选中以后指示点的颜色 indicatorActiveColor
        # with Swiper(id='swiper3', size=[750,240], top=600,interval=3000, duration=2000, autoplay=True):
        #     with SwiperItem(id='imgUrls2'):
        #         Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')


    def onInit():
        mo.console('测试')

    def onSelectorPickerTextChange():
        page.picker1.text = signs[int(page.picker1.value)]