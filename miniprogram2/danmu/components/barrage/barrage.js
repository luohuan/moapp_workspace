// components/danmu.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    data:{
      type: Object,
      value: {},
      observer:function(newVal, oldVal){
        if(!newVal){
          return 
        }
        var datas = newVal;

        if(!this.datas||this.datas.length==0){
          this.datas = datas;
          this.lastThreeTop = []
          this.ids = new Set()
          for(const item of datas){
            this.ids.add(item.id)
          }
          this.runDanmu()
        }else{
          for(const item of datas){
            if(!this.ids.has(item.id)){
                this.ids.add(item.id)
                this.sendNewDanmu(item)
              }
            }
        }
        
      }
    },
    danmuStyle: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'danmuStyle':newVal
        })
      }
    },

    danmuTailImage: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'tailImage':newVal
        })
      }
    },
    danmuTailImageStyle: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'tailImageStyle':newVal
        })
      }
    },
    danmuAvatarStyle: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'avatarStyle': newVal
        })
      }
    }
    ,
    danmuHeadImage: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'headImage':newVal
        })
      }
    },
    danmuHeadImageStyle: {
      type: String,
      value: '',
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'headImageStyle':newVal
        })
      }
    },
    danmuHeight: {
      type: Number,
      value: 35,
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        this.setData({
          'danmuHeight':newVal
        })
      }
    },
    danmuMargin: {
      type: Number,
      value: 20,
      observer: function(newVal, oldVal){
        if(!newVal){
          return
        }
        // this.setData({
        //   'danmuMargin':newVal
        // })
        //this.danmuMargin = newVal
      }
    },
    danmuRowNumber: {
      type: Number,
      value: 8,
      observer: function(newVal, oldVal){
        console.log('observerDanmuRowNumber')
        console.log(newVal)
        if(!newVal){
          return
        }
        this.danmuRowNumber = newVal
        
        // this.setData({
        //   'danmuRowNumber':newVal
        // })
      }
    },
    danmuFontSize:{
      type:Number,
      value: 25,
      observer:function(newVal, oldVal){
        console.log('fontSize'+ newVal)
      }
    },
    danmuLineHeight: {
      type:Number,
      value: 35,
      observer:function(newVal, oldVal){
        console.log('lineHeight'+ newVal)
      }
    },
    danmuBackground:{
      type: String,
      value: 'white',
      observer:function(newVal, oldVal){
        console.log('background'+ newVal)
      }
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    "danmuStyle":'',
    "tailImageStyle":'',
    "tailImage":'',
    "headImageStyle":'',
    'headImage':'',
    
  },
  lastThreeTop: [],
  // 'danmuRowNumber': 5,
  // 'danmuMargin': 20,
  //'danmuHeight': 60,
  /**
   * 组件的方法列表
   */
  methods: {
    runDanmu: function () {
      let current_time = new Date().getTime()
      var datas = this.datas
      const danmus = []
      var timeout = 0
      var index = 0
      const that = this;
      console.log(datas)
      for (var item of datas) {
        var danmu = {};
        danmu.index = index
        danmu.suoyin = Math.random()
        danmu.text = item.text;
        danmu.avatarUrl = item.avatarUrl;
        danmu.show = true;
        danmu.delay = 4 * Math.random() + parseInt(index / 4) * 8

        danmu.top = that.getCurrentTop()
        danmus.push(danmu)
        index = index + 1
        var cosume_time = (danmu.delay + 10) * 1000
        if (cosume_time > timeout) {
          timeout = cosume_time
        }
      }
      that.setData({
        danmus: danmus
      })
      this.endTime = current_time + timeout
      this.timeOutHandler = setTimeout(function () {
        that.runDanmu()
      }, timeout)
    },
    getCurrentTop: function () {
      // var allTops = [20, 120, 220, 320, 420, 520]
      console.log('getCurrentTop')
      console.log(this.data.danmuRowNumber)
      console.log(this.data.danmuHeight)
      console.log(this.data.danmuMargin)
      var allTops = []
      for(var index=0; index<this.data.danmuRowNumber; index++){
        allTops.push(index*(this.data.danmuHeight+this.data.danmuMargin))
      }
      while (true) {

        var randomTopindex = parseInt(allTops.length * Math.random())
        var randomTop = allTops[randomTopindex]
        var flag = false
        for (var top of this.lastThreeTop) {
          if (top == randomTop) {
            flag = true
          }
        }
        if (!flag) {
          this.lastThreeTop.push(randomTop)
          if (this.lastThreeTop.length > 3) {
            this.lastThreeTop.shift()
          }
          return randomTop;
        }

      }
    },
    bindinput: function (e) {
      this.currentInput = e.detail.value
      console.log(this.currentInput)
    },
    sendNewDanmu: function (newVal) {
        var newDanMu = newVal
        this.datas.push(newVal)
        const that = this
        var danmus = this.data.danmus
        var danmu = {}
        danmu.suoyin = Math.random()
        danmu.text = newVal.text
      danmu.avatarUrl = newVal.avatarUrl
        danmu.show = true
        danmu.delay = 0
        danmu.top = that.getCurrentTop()
        danmus.push(danmu)
        that.setData({
          danmus: danmus
        })
        var current_time = new Date().getTime()
        var this_danmu_end_time = current_time + 10 * 1000

        if (this_danmu_end_time > this.endTime) {
          clearTimeout(this.timeOutHandler)
          this.timeOutHandler = setTimeout(function () {
            that.runDanmu()
          }, 10 * 1000)
        }
    }
  }
  
})
