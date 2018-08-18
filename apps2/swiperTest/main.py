def main():
    with MoApp(appid='wx263b9c72fc87b39c', name='swiper'):
        index()

class index(Page):
    title = 'swiper展示'
    def UI():        
        with Swiper(id='swiper1', size=[750,240],interval=3000, duration=2000, autoplay=True):
            with SwiperItem(id ='dataswiper'):
                with Image(pos=[20,20, 710, 200], borderRadius='10px', src ='{item.pic}'):
                    this.onTap = moui.goto('second', name='{item.name}')
        # 滑块视图容器  可以自动滑动 interval 定义切换的间隔时间 
        with Swiper(id ='swiper2', size=[750,240], top=300,interval=3000, duration=2000, autoplay=True):
            with SwiperItem(id='imgUrls'):
                Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')
        # 滑块视图容器  选中以后指示点的颜色 indicatorActiveColor
        with Swiper(id='swiper3', size=[750,240], top=600,interval=3000, duration=2000, autoplay=True):
            with SwiperItem(id='imgUrls2'):
                Image(pos=[20,20, 710, 200], borderRadius='10px', src = '{item}')


    def onInit():
        page.dataswiper.data = [
            {
                'id': 2,
                'pic': 'http://material.motimaster.com/ywjiang/ceshiyong/demo/7c3b8b73d50778fc0cf6292de422c0fe.png',
                'name': '恋爱成绩单',
                'type': 'picker'
            },
            {
                'id': 3,
                'pic': 'http://material.motimaster.com/ywjiang/ceshiyong/demo/cb688325b2b5b1b5b2d707e4befb5057.png',
                'name': '可爱指数',
                'type': 'picker'
            },
            {
                'id': 1,
                'pic': 'http://material.motimaster.com/ywjiang/ceshiyong/demo/6a03511a59be38a1f3a6756009c7dc6e.png',
                'name': '印象成绩单',
                'type': 'input'
            }]

        page.imgUrls.data = [
            'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg',
            'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
            'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg'
                    ]

        # page.swiper2.interval=2000
        # page.swiper2.duration = 500
        # page.swiper2.autoplay = True

        page.imgUrls2.data = [
            'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg',
            'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
            'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg'
                    ]

        # page.swiper3.interval=2000
        # page.swiper3.duration = 500
        # page.swiper3.autoplay = True
        # page.swiper3.indicatorDots=True
        # page.swiper3.indicatorActiveColor ='#FF8C69'