const moapp=require("./utils/moapp.js");App({onLaunch:function(t){this.globalData.scene=t.scene||0;moapp.appBgmAllInOne(this);console.log(`launch moapp, appid:wx9066c083d563977e, env:${this.globalData.env}, signature:${this.globalData.signature}`);var a=this;const o=wx.getUpdateManager();o.onUpdateReady(function(){wx.showModal({title:"更新提示",content:"新版本已经准备好，是否重启应用？",success:function(t){if(t.confirm){o.applyUpdate()}},fail:function(t){o.applyUpdate()}})})},globalData:{uiBaseAttr4Server:["hidden","color","width","height","background","backgroundColor","left","top","right","bottom","fontSize","fontWeight","opacity","text"],env:"release",signature:"CA9154E25BC3FDDF2B83A21922417AC260FC85FE",domain:"https://api.moapp.motimaster.com"}});