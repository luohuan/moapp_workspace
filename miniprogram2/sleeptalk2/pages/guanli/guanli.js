// pages/guanli/guanli.js
const app = getApp()
var sentenceChoiceList = []
Page({

  data: {
    sentenceList:[],
    isLongPress:false,
    isQuanXuan:false,
    isClickSuo:true,
    isFirstOpenGuanli:true,
    isXiaoshi:true,
    isOpenFukuanxuzhi:false,
    isOpenFukuanxuzhi:false,
    isXuzhixiaoshi:true,
    isTongyi: false,
    wyid: 'a',
  },

  onLoad: function (options) {
  },
  onShow: function () {
    app.globalData.isTohoutai = false
    wx.request({
      url: 'https://www.yangshuxian.xyz:80/sleep/guanLi/',
      data: {
        'wopenId': app.globalData.wopenId,
      },
      method: 'POST',
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      success: res => {
        console.log('guanliOnshow',res.data)
        var tmp = res.data
        for(var i in tmp){
          tmp[i].push(false)
        }
        this.setData({
          sentenceList: tmp
        })
        sentenceChoiceList = tmp
      }
    })
  },

  onShareAppMessage: function () {
  
  },
  back:function(){
    wx.navigateBack({
      delta:'1',
    })
  },
  fenxiang:function(){
    wx.navigateTo({
      url: '../fenxiang/fenxiang',
    })
  },
  openDelete:function(){
    this.setData({
      isLongPress: !this.data.isLongPress
    })
  },
  choiceOne:function(e){
    var index = e.currentTarget.dataset.index
    sentenceChoiceList[index][7] = !sentenceChoiceList[index][7]
    this.setData({
      sentenceList:sentenceChoiceList
    })
  },
  quxiao:function(){
    this.setData({
      isLongPress:false
    })
  },
  quanxuan:function(){
    if(!this.data.isQuanXuan){
      for (var i in sentenceChoiceList) {
        sentenceChoiceList[i][7] = true
      }
      this.setData({
        isQuanXuan : !this.data.isQuanXuan,
        sentenceList: sentenceChoiceList
      })
    }else{
      for (var i in sentenceChoiceList) {
        sentenceChoiceList[i][7] = false
      }
      this.setData({
        isQuanXuan: !this.data.isQuanXuan,
        sentenceList: sentenceChoiceList,
      })
    }
  },
  shanchu:function(){
    var tmp = []
    for (var i in sentenceChoiceList){
      if(sentenceChoiceList[i][7]){
        tmp.push(sentenceChoiceList[i][5])
      }
    }
    console.log(tmp)
    wx.request({
      url: 'https://www.yangshuxian.xyz:80/sleep/delete/',
      data: {
        'wopenId': app.globalData.wopenId,
        'lists': tmp,
      },
      method: 'GET',
      dataType: JSON,
      header: { 'content-type': 'application/json' },
      success: res => {
        wx.showToast({
          title: '删除成功',
          icon:'success',
          duration: 2000,
        })
        this.onShow()
        app.globalData.isTohoutai = true
        this.setData({
          isLongPress: false,
        })
      }
    })
  },
  pay:function(e){
    this.setData({
      isClickSuo: true,
      isFirstOpenGuanli: false,
      isXiaoshi:false,
      wyid: e.currentTarget.dataset.id,
    })
    
  },
  xiaoshi:function(){
    var that = this
    this.setData({
      isClickSuo: false,
    })
    setTimeout(function () {
      that.setData({
        isXiaoshi:true,
      })
    }, 200)
  },
  openXuzhi:function(){
    this.setData({
      isOpenFukuanxuzhi:true,
      isXuzhixiaoshi:false,
    })
  },
  querenxuzhi:function(){
    var that = this
    this.setData({
      isOpenFukuanxuzhi:false,
    })
    setTimeout(function () {
      that.setData({
        isXuzhixiaoshi: true,
      })
    }, 300)
  },
  xuanzetontyi:function(){
    this.setData({
      isTongyi:!this.data.isTongyi
    })
  },
  querenpay:function(e){
    wx.request({
      url: 'https://www.yangshuxian.xyz:80/sleep/pay/',
      data: {
        'wopenId': app.globalData.wopenId,
        'wyid': e.currentTarget.dataset.id,
      },
      method: 'POST',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      success: res => {
        var responsoe = JSON.parse(res.data)
        wx.requestPayment({
          'timeStamp': responsoe.timeStamp,
          'nonceStr': responsoe.nonceStr,
          'package': responsoe.package,
          'signType': responsoe.signType,
          'paySign': responsoe.paySign,
          'success': res=> {
            wx.request({
              url: 'https://www.yangshuxian.xyz:80/sleep/finishPay/',
              data: {
                'wopenId': app.globalData.wopenId,
                'wyid': this.data.wyid,
              },
              method: 'POST',
              header: {
                "Content-Type": "application/x-www-form-urlencoded"
              },
              success: res => {
                wx.showToast({
                  title: '解锁成功！',
                  icon: 'success',
                  duration: 1000,
                })
                this.setData({
                  isXiaoshi:true,
                })
              }
            })
          },
          'fail': function (res) {
            console.log(res)
          }
        })
      }
    })
  }
})
