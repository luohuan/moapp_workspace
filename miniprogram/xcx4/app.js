const moapp=require("./utils/moapp.js");App({onLaunch:function(t){this.globalData.scene=t.scene||0;moapp.appBgmAllInOne(this);console.log(`launch moapp, appid:wx9066c083d563977e, env:${this.globalData.env}, signature:${this.globalData.signature}`);var a=this;const o=wx.getUpdateManager();o.onUpdateReady(function(){wx.showModal({title:"更新提示",content:"新版本已经准备好，是否重启应用？",success:function(t){if(t.confirm){o.applyUpdate()}},fail:function(t){o.applyUpdate()}})})},globalData:{uiBaseAttr4Server:["hidden","color","width","height","background","backgroundColor","left","top","right","bottom","fontSize","fontWeight","opacity","text"],env:"release",signature:"8C63D10E9F996D1EC4151BEDA3E831A49396685D",domain:"https://api.moapp.motimaster.com",upload:"https://upload.motimaster.com/upload/image"}});