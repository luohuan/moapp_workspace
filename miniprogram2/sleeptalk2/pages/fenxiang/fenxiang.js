// pages/fenxiang/fenxiang.js
const app = getApp()
Page({
  data: {
    erweimaImage:'',
  },

  onLoad: function (options) {
    wx.showLoading({
      title: '图片加载中……',
    })
    wx.request({
      url: 'https://www.yangshuxian.xyz:80/sleep/geterweima/',
      data:{
        'wopenId': app.globalData.wopenId
      },
      method: 'POST',
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      success:res=>{
        wx.hideLoading()
        this.setData({
          erweimaImage: 'https://www.yangshuxian.xyz:80/img/liuxin_erweima/' + app.globalData.wopenId + '.png'
        })
      }
    })
  },

  onShow: function () {
    app.globalData.isTohoutai = false
  },
  baocun:function(){
    wx.showLoading({
      title: '下载中……',
    })
    wx.downloadFile({
      url: 'https://www.yangshuxian.xyz:80/static/liuxin_erweima/' + app.globalData.wopenId + '.png',
      header: { "Content-Type": "application/x-www-form-urlencoded" },
      success:res=>{
        console.log(res)
        wx.saveImageToPhotosAlbum({
          filePath: res.tempFilePath,
          success:res=>{
            wx.hideLoading()
            wx.showToast({
              title: '已保存',
              icon: 'success',
              duration: 800,
            })
          },
          fail:res=>{
            wx.hideLoading()
            wx.showToast({
              title: '保存失败!',
              icon: 'none',
              duration: 1300,
            })
          }
        })
      }
    })
  },
  back:function(){
    wx.navigateBack({
      delta:'3'
    })
  },
  onShareAppMessage: function () {
    return {
      title: '来这说出平时不敢对我说的话吧~',
      path: '/pages/index/index?user=' + app.globalData.wopenId,
    }
  }
})