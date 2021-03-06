const moapp = require("./utils/moapp.js");

App({
    onLaunch: function(options) {            
            this.globalData.scene = options.scene || 0;
            moapp.appBgmAllInOne(this);
            console.log(`launch moapp, appid:wx263b9c72fc87b39c, env:${this.globalData.env}, signature:${this.globalData.signature}`);
            var self = this;            
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
            ;
        },
    globalData: {
            uiBaseAttr4Server: ['hidden', 'color', 'width', 'display', 'height', 'background', 'backgroundColor', 'left', 'top', 'right', 'bottom', 'fontSize', 'fontWeight', 'opacity', 'text'],
            env: 'dev',
            signature: 'C51879AC39BC56DFA2324BC82885E53A9EB5288E',
            domain: 'https://dev.mozigu.net/moapp',
            upload: 'https://dev.mozigu.net/upload/image',
        },
})