const moapp=require("./utils/moapp.js");App({onLaunch:function(t){this.globalData.scene=t.scene||0;moapp.appBgmAllInOne(this);console.log(`launch moapp, appid:wxa9b01a93c80e98e9, env:${this.globalData.env}, signature:${this.globalData.signature}`);var a=this;const e=wx.getUpdateManager();e.onUpdateReady(function(){wx.showModal({title:"更新提示",content:"新版本已经准备好，是否重启应用？",success:function(t){if(t.confirm){e.applyUpdate()}},fail:function(t){e.applyUpdate()}})})},globalData:{uiBaseAttr4Server:["hidden","color","width","height","background","backgroundColor","left","top","right","bottom","fontSize","fontWeight","opacity","text"],env:"release",signature:"53E48ECD6340B7A9B5EE1353D82C36BAB1B39795",domain:"https://api.moapp.motimaster.com"}});