const util=require("./util.js");module.exports={requestingSession:false,requestCloudFunction:function(e,a,t,o,s){var n=this;return new Promise((r,i)=>{const l=getApp();n.login(a).then(c=>{if(l.globalData.userInfo){s.app.userInfo=l.globalData.userInfo;delete l.globalData.userInfo}wx.request({url:`${l.globalData.domain}/cloud`,data:{session:c.sessionID,module:t,func_name:o,data:s},method:"POST",header:{"content-type":"application/json"},success:o=>{if("statusCode"in o&&o.statusCode!=200){wx.hideLoading();n.showAlert("错误提示",`糟糕,服务器出错了,错误码:${o.statusCode},请稍后重试...`);i({statusCode:o.statusCode,data:o.data})}else{if(o.data.ret==0){var c={};var g={};for(var d in o.data.data){var u=o.data.data[d];var f=u.cmd;var m=u.data;switch(f){case"setTitle":n.setTitle(m);break;case"setAttr":c[n.genObjectDataName(m.id,m.key)]=m.value;break;case"goto":let o=util.jsonToUrlParams(m.options||{});wx.navigateTo({url:`../${m.page_name}/${m.page_name}?${o}`});break;case"redirectTo":let r=util.jsonToUrlParams(m.options||{});wx.redirectTo({url:`../${m.page_name}/${m.page_name}?${r}`});break;case"switchTab":wx.switchTab({url:`../${m.page_name}/${m.page_name}`});case"goBack":wx.navigateBack({delta:1});break;case"setNavibarColor":wx.setNavigationBarColor({frontColor:m.frontColor=="#000000"?"#000000":"#ffffff",backgroundColor:m.backgroundColor||"#ffffff"});break;case"showAlert":n.showAlert(m.title,m.content);break;case"showTips":wx.showToast({title:m.text,icon:"success",image:m.image,duration:m.duration});break;case"playBGM":if(wx.createInnerAudioContext){l.bgm.src=m.src;l.bgm.control=false;l.bgm.controlStyle="bgm-"+m.controlStyle;l.bgm.title="bgm";l.bgm.autoplay=m.autoplay;l.bgm.loop=m.loop;e.setData({bgmcontrol:+l.bgm.control,bgmstate:[1,+!l.bgm.autoplay],controlStyle:l.bgm.controlStyle})}break;case"pauseBGM":if(e.data.bgmstate&&e.data.bgmstate[0]==1){l.bgm.pause();e.setData({bgmstate:[1,1]})}break;case"resumeBGM":if(e.data.bgmstate&&e.data.bgmstate[0]==1){l.bgm.play();e.setData({bgmstate:[1,0]})}break;case"closeBGM":if(e.data.bgmstate&&e.data.bgmstate[0]==1){l.bgm.stop();e.setData({bgmcontrol:0,bgmstate:[0,1]})}break;case"gotoMiniProgram":wx.navigateToMiniProgram({appId:m.appid,path:m.path,success:function(e){console.log("跳转小程序成功")},fail:function(e){console.log("跳转小程序失败，错误信息:");console.log(e)}});break;case"playAudio":if(wx.createInnerAudioContext){l.soundEffect.src=m.src;l.soundEffect.autoplay=true;e.setData({soundEffectState:[1,0]})}break;case"setData":g[m.key]=m.value;break;case"saveImage":n.saveImage(null,m).then().catch(()=>{});break;case"appendData":let i=n.genObjectDataName(m.id,"data");let d=e.data[i];d.push(m.value);c[i]=d;break;case"console":console.log(m.content);break;case"previewImage":console.log("previewImage");wx.previewImage({urls:m});break;case"wxpay":if(m.params){let o=m.params;wx.requestPayment({timeStamp:o.timeStamp,nonceStr:o.nonceStr,package:o.package,signType:o.signType,paySign:o.paySign,success:function(o){n.requestCloudFunction(e,a,t,m.success.function,s)},fail:function(o){console.log(o);let r=o.errMsg.indexOf("cancel")>-1;if(s.params){s.params.wxpayCancel=r}else{s.params={wxpayCancel:r}}n.requestCloudFunction(e,a,t,m.fail.function,s)}})}else{if(m.fail){n.requestCloudFunction(e,a,t,m.fail.function,s)}console.error("invalid wxpay params")}break;default:console.log("invalid server cmd:"+f);break}}if(JSON.stringify(g)!="{}"){var p=e.data.serverData||{};for(var b in g){p[b]=g[b]}c["serverData"]=p}if(JSON.stringify(c)!="{}"&&e){e.setData(c)}s.data=o.data.data;if("resolve"in o.data&&o.data.resolve===false){wx.hideLoading();i(s)}else{r(s)}}else{console.log(`Execute cloud function fail！error code:${o.data.ret}`);try{if(o&&o.data&&o.data.data&&"traceback"in o.data.data){console.log("---------error traceback---------:\n"+o.data.data.traceback)}if(o&&o.data&&o.data.data&&"error_message"in o.data.data){console.log("---------error message---------:\n"+o.data.data.error_message)}}catch(e){console.error(e)}wx.hideLoading();if(l.globalData.env=="release"){n.showAlert("错误提示",`出错了，错误码:${o.data.ret}`)}else{n.showAlert("错误提示",`出错了，错误码:${o.data.ret},\r\n 错误信息: `+(o.data.data.error_message||"无")+", 详细错误信息请参考微信开发者工具Console日志输出.")}i({errorCode:o&&o.data&&o.data.ret||-1,data:o&&o.data&&o.data.data||""})}}},fail:function(e){i(e)}})},e=>{n.showAlert("错误提示",`糟糕,服务器出错啦,请稍后重试...`);i("login fail")})})},genObjectDataName:(e,a)=>{return`__${e}_${a}`},submitFormId:function(e,a){const t=getApp();var o=t.globalData.sessionID;if(!o){return}wx.request({url:`${t.globalData.domain}/templateInfo`,data:{appid:e,formId:a,sessionID:o},method:"POST",header:{"content-type":"application/json"},success:function(e){},fail:function(e){}})},jsonToUrlParams:e=>{var a=[];for(var t in e){a.push(t+"="+encodeURIComponent(e[t]))}return a.join("&")},getUserInfo:()=>{return new Promise((e,a)=>{wx.getUserInfo({success:function(a){e(a.userInfo)},fail:function(a){e({})}})})},genEventData:function(e,a,t,o,s=null){const n=getApp();var r=[];if(t.data.objects){for(var i=0;i<t.data.objects.length;++i){var l=t.data.objects[i];var c={id:l,attrs:[]};var g=this.genObjectDataName(l,"");for(var d in t.data){if(d.slice(0,g.length)==g){var u=d.slice(g.length,d.length);if(u==="value"){c["value"]=t.data[d]}else if(u==="item"){c["currentItem"]=t.data[d].item}else{let e=false;for(let a in n.globalData.uiBaseAttr4Server){if(u==n.globalData.uiBaseAttr4Server[a]){e=true;break}}if(!e){c["attrs"].push(u)}}}}r.push(c)}}return{app:{scene:n.globalData.scene},page:{name:a,createTime:t.data.createTime,options:t.data.options||{},elements:r,data:t.data.serverData||{},currentTarget:{id:s?s.id||null:null}},data:o}},showConfirm:(e,a,t)=>{return new Promise((o,s)=>{wx.showModal({title:e||"提示",content:a||"",success:e=>{if(e.confirm){o(t)}else if(e.cancel){s(t)}},fail:e=>{console.log("showModal fail! err:");console.log(e);s(t)}})})},showAlert:(e,a)=>{wx.showModal({title:e||"提示",content:a||"",showCancel:false})},chooseImage:(e,a,t,o)=>{console.log(e);e.params={};return new Promise((s,n)=>{wx.chooseImage({count:a,sizeType:t,sourceType:o,success:function(a){console.log(a);console.log("发生了什么");e.params.tempFilePaths=a.tempFilePaths;console.log(e);s(e)}})})},checkSaveImageAuth:()=>{return new Promise((e,a)=>{let t=wx.getSetting({success:t=>{var o=t.authSetting;console.log(o);const s="scope.writePhotosAlbum";if(s in o&&o[s]){e()}else{if(s in o){wx.showModal({title:"提示",content:'您现在不允许小程序访问手机相册，不能保存到朋友圈，请打开"保存到相册"',success:t=>{if(t.confirm){wx.openSetting({success:t=>{console.log(t);if("scope.writePhotosAlbum"in t.authSetting&&t.authSetting["scope.writePhotosAlbum"]){e()}else{a()}}})}else{a()}},fail:e=>{a()}})}else{wx.authorize({scope:s,success(){e()},fail(){a()}})}}},fail:e=>{console.error("get setting fail!");a()}})})},saveImage:function(e,a){var t=this;e=e||{};return new Promise((o,s)=>{t.checkSaveImageAuth().then(()=>{wx.showLoading({title:"保存中"});wx.downloadFile({url:a,success:function(a){wx.saveImageToPhotosAlbum({filePath:a.tempFilePath,success:function(a){wx.hideLoading();t.showAlert("保存成功","已保存到相册，快去分享吧~");o(e)},fail:function(a){wx.showToast({title:"图片保存失败",icon:"none",duration:1500});s(e)}})},fail:function(a){wx.showToast({title:"图片下载失败",icon:"none",duration:1500});s(e)}})},()=>{wx.showToast({title:"图片保存失败",icon:"none",duration:1500});s(e)})})},wxLogin:function(e,a){wx.login({success:function(t){if(t.code){e({openid:null,code:t.code})}else{console.log("wx.login fail!, err:"+t.errMsg);a(t.errMsg)}},fail:function(e){console.error("wx.login fail! err:"+e);a(e)}})},getWxCode:function(){var e=this;return new Promise((a,t)=>{var o=wx.getStorageSync("openid");if(o){wx.checkSession({success:function(){a({openid:o,code:null})},fail:function(){console.log("session is invalid, relogin");e.wxLogin(a,t)}})}else{e.wxLogin(a,t)}})},login:function(e){var a=this;return new Promise((t,o)=>{const s=getApp();if(s.globalData.sessionID){t({sessionID:s.globalData.sessionID})}else{if(!a.requestingSession){a.requestingSession=true;a.getWxCode().then(n=>{wx.request({url:`${s.globalData.domain}/session`,data:{appid:e,signature:s.globalData.signature,userInfo:{},code:n["code"],openid:n["openid"],uiBaseAttr:s.globalData.uiBaseAttr4Server},method:"POST",header:{"content-type":"application/json"},success:e=>{if("statusCode"in e&&e.statusCode!=200){o("login fail!")}else{s.globalData.sessionID=e.data.data.sessionID;wx.setStorage({key:"openid",data:e.data.data["openid"]});console.log(`get session: ${s.globalData.sessionID}, openid:${e.data.data["openid"]}`);t(e.data.data)}},fail:e=>{console.error("login failed");console.error(e);o(e)},complete:e=>{a.requestingSession=false}})})}else{let e=setInterval(()=>{if(!a.requestingSession){clearInterval(e);t({sessionID:s.globalData.sessionID})}},100)}}})},appBgmAllInOne:e=>{if(wx.createInnerAudioContext){e.bgm=wx.getBackgroundAudioManager();e.soundEffect=wx.createInnerAudioContext();e.soundEffect.onStop(()=>{}),e.soundEffect.onEnded(()=>{})}else{wx.showModal({title:"提示",content:"当前微信版本过低，无法使用该功能，请升级到最新微信版本后重试。"})}},bgmControl:(e,a)=>{if(wx.createInnerAudioContext){if(e.data.bgmstate[0]==1){if(!e.data.bgmstate[1]){a.bgm.pause();e.setData({bgmstate:[1,1]})}else{a.bgm.play();e.setData({bgmstate:[1,0]})}}}},bgmAllInOne:(e,a)=>{if(wx.createInnerAudioContext){e.setData({bgmcontrol:a.bgm.control||false,controlStyle:a.bgm.controlStyle||false,bgmstate:[a.bgm.src==(""||"http://none/")?0:1,+a.bgm.paused],soundEffectState:[a.soundEffect.src==(""||"http://none/")?0:1,+a.soundEffect.paused]})}},getOpenId:()=>{return wx.getStorageSync("openid")},setTitle:e=>{const a=getApp();if(a.globalData.env!="release"){e=e+"-测试版"}wx.setNavigationBarTitle({title:e})}};