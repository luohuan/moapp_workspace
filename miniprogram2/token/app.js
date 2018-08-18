const moapp = require("./utils/moapp.js");

App({
    onLaunch: function(options) {
            this.globalData.scene = options.scene || 0;
            moapp.appBgmAllInOne(this);
            console.log(`launch moapp, appid:wx263b9c72fc87b39c, env:${this.globalData.env}, signature:${this.globalData.signature}`);
            var self = this;
            /*wx.getSystemInfo({
              success: function(res) {
                if (self.globalData.env != 'release' && res.platform == 'devtools') {
                  moapp.showAlert('提示', '这是测试版本，千万别上传提交审核哦');
               }
              }
            });*/
            const updateManager = wx.getUpdateManager()

            updateManager.onUpdateReady(function () {
              wx.showModal({
                title: '更新提示',
                content: '新版本已经准备好，是否重启应用？',
                success: function (res) {
                  if (res.confirm) {
                    // 新的版本已经下载好，调用 applyUpdate 应用新版本并重启
                    updateManager.applyUpdate()
                  }
                },fail: function(res){
                    updateManager.applyUpdate()
                }
              })
            });
        },
    globalData: {
            uiBaseAttr4Server: ['hidden', 'color', 'width', 'height', 'background', 'backgroundColor', 'left', 'top', 'right', 'bottom', 'fontSize', 'fontWeight', 'opacity', 'text'],
            env: 'test',
            signature: 'DEA358B116CA55B6C6A058DC4268AE87BB082896',
            domain: 'https://api.moapp.mogoboom.com'
        },
})