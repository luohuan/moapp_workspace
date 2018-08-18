// pages/index/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
  
  },
  chooseImagePromise:function(){
    return new Promise((resolve, reject)=>{
      wx.chooseImage({
        success: function(res) {
          resolve(res)
        },
        fail:function(res){
          reject(res)
        }
      })
    })
  },
  uploadImage:function(){
    chooseImagePromise().then((res)=> {
      let flag = 0;
      var tempFilePaths = res.tempFIlePaths;
      const urls = [];
      
    })
    // wx.chooseImage({
    //   success: function(res) {
    //     var tempFilePaths = res.tempFilePaths;
    //     const urls = [];
    //     for(const tempFilePath of tempFilePaths){
    //       console.log(tempFilePath)
    //       wx.uploadFile({
    //         url: 'http://dev.mozigu.net/upload',
    //         filePath: tempFilePath,
    //         name: 'file',
    //         formData: {
    //           'user': 'test'
    //         },
    //         success: function (res) {
    //           var data = res.data
    //           console.log(data)
    //           urls.push(data.url)
    //         }
    //       })
    //     }

    //     console.log('urls hahahaha')
    //     console.log(urls)
        
    //   },
    // })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})