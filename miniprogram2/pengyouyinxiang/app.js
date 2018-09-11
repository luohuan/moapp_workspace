const moapp = require("./utils/moapp.js");

App({
    globalData: {
            uiBaseAttr4Server: ['hidden', 'color', 'width', 'display', 'height', 'background', 'backgroundColor', 'left', 'top', 'right', 'bottom', 'fontSize', 'fontWeight', 'opacity', 'text'],
            env: 'test',
            signature: 'A8785C09F6B5C18BC3D824BC8B69237FC5301594',
            domain: 'https://api.moapp.mogoboom.com',
            upload: 'https://upload.motimaster.com/upload/image',
        },
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
})