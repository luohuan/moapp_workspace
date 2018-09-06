// app.js

App({
  onLaunch: function (e) {
    this.globalData.cjz = e.scene
    var backgroundAudioManager = this.globalData.backgroundAudioManager
    backgroundAudioManager.title = 'Tina'
    backgroundAudioManager.epname = 'POTION~Relaxin’ with FINAL FANTASY'
    backgroundAudioManager.singer = '植松伸夫'
    backgroundAudioManager.coverImgUrl = 'http://p3.music.126.net/oe1DUofzbf_7ZD7HgeFldA==/649811372027765.jpg?param=177y177'
    backgroundAudioManager.src = 'https://jordoncat.oss-cn-shenzhen.aliyuncs.com/music/%E6%A4%8D%E6%9D%BE%E4%BC%B8%E5%A4%AB%20-%20Tina.mp3'
    
    wx.login({
      success: res => {
      }
    })
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          wx.getUserInfo({
            success: res => {
              this.globalData.userInfo = res.userInfo
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
              console.log('app:', this.globalData.userInfo)
            }
          })
        }
      }
    })
  },
  onShow:function(){
    this.globalData.backgroundAudioManager.play()
  },
  onHide:function(){
    console.log('到后台')
    this.globalData.backgroundAudioManager.pause()
  },
  globalData: {
    userInfo: null,
    topenId:'',
    wopenId: '',
    sleepList:[],
    cjz:0,
    backgroundAudioManager : wx.getBackgroundAudioManager(),
    isDelete: false,
    isTohoutai: false,
  },
})