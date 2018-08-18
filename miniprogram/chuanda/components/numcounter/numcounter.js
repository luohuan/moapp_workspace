// components/counter/counter.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    'config':{
      type: Object,
      value: {},
      observer: function(newVal, oldVal){
        const config = newVal;
        console.log(newVal)
        if(!config){return}

        if(this.inter){
          clearInterval(this.inter)
        }
        const that = this;
        const dir = config.type;
        const num = config.number;
        const style = config.style;
        let interval = config.interval;
        if(!interval){
          interval = 1000
        }
        let decimal = config.decimal
         if(!decimal){
          decimal = 0
        }
        if(!dir || dir=='dec'){
          that.setData({
            'number': num,
            'style': style
          })
          that.number = num
          that.inter = setInterval(function () {
            let current = that.number;
            
            current -= interval/1000;
            if (current <= 0) {
              that.setData({
                'number': 0,
              })
              clearInterval(that.inter)
              that.triggerEvent('onfinish')
              return
            }
            that.setData({
              'number': current.toFixed(decimal)
            })
            that.number = current
          }, interval)
        }else{
          that.setData({
            'number': 0,
            'style': style
          })
          that.number = 0;
          that.inter = setInterval(function () {
            let current = that.number;
            
            current += interval/1000;
            if (current >= num) {
              that.setData({
                'number': num,
              })
              clearInterval(that.inter)
              that.triggerEvent('onfinish')
              return
            }
            that.setData({
              'number': current.toFixed(decimal)
            })
            that.number = current
          }, interval)
        }
      }
    },
    'stop': {
      type: String,
      value: false,
      observer: function(newVal, oldVal){
        console.log(newVal);
        if(newVal) {
          clearInterval(this.inter)
        }
      }

    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    'style': '',
    'number': '',
  },

  /**
   * 组件的方法列表
   */
  methods: {

  }
})
