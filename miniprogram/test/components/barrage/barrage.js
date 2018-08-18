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
    tailImage: {
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
    tailImageStyle: {
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
    headImage: {
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
    headImageStyle: {
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
    newDanmu:{
      type: String,
      value: {},
      observer:function(newVal, oldVal){
       
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
      var allTops = [20, 120, 220, 320, 420, 520]
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
        danmu.avatar = newVal.avatarUrl
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
