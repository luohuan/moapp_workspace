const app=getApp();const moapp=require("../../utils/moapp.js");Page({onViewTap_L0lVCa:function(e){var t=this;t.setData({__guest_records_item:e.currentTarget.dataset});var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset,e.currentTarget);Promise.resolve(a).then(function(e){return e}).catch(e=>{})},onButtonTap_CVLPAi:function(e){var t=this;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset);Promise.resolve(a).then(function(e){e.params={host_id:e.data.host_openid,guest_id:e.data.guest_openid};return moapp.requestCloudFunction(t,"wxaa8fe119f5c62d23","main","checkDetail",e)}).catch(e=>{})},onButtonTap_SPkFFr:function(e){var t=this;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset);Promise.resolve(a).then(function(e){wx.showModal({title:`温馨提示:`,content:`查看全部好友的选择(包括未来进入的好友),需支付金额9.9元`,success:function(a){if(a.confirm){console.log("用户点击确定");Promise.resolve(e).then(function(e){e.params={host_id:e.data.host_openid,guest_id:e.data.guest_openid};return moapp.requestCloudFunction(t,"wxaa8fe119f5c62d23","main","checkDetailPay",e)})}else if(a.cancel){console.log("用户点击取消")}}})}).catch(e=>{})},onImageTap_LDqvJM:function(e){var t=this;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset);Promise.resolve(a).then(function(e){wx.showModal({title:`温馨提醒`,content:`删除的记录将不能恢复，您确认删除嘛?`,success:function(a){if(a.confirm){console.log("用户点击确定");Promise.resolve(e).then(function(e){e.params={rid:e.data.id};return moapp.requestCloudFunction(t,"wxaa8fe119f5c62d23","main","deleteRecord",e)})}else if(a.cancel){console.log("用户点击取消")}}})}).catch(e=>{})},onViewTap_I1mLD8:function(e){var t=this;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset,e.currentTarget);Promise.resolve(a).then(function(e){if(!false&&e.page.currentTarget.id){var a=moapp.genObjectDataName(e.page.currentTarget.id,"hidden");let n={};n[a]=true;t.setData(n)}return e}).catch(e=>{})},onViewTap_MuCwy0:function(e){var t=this;t.setData({__guest_detail_item:e.currentTarget.dataset});var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset,e.currentTarget);Promise.resolve(a).then(function(e){return e}).catch(e=>{})},onGetUserInfo_ywU49Q:function(e){var t=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset);Promise.resolve(a).then(function(e){return moapp.requestCloudFunction(t,"wxaa8fe119f5c62d23","main","goShare",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_QURGqg:function(e){var t=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,e.currentTarget.dataset);Promise.resolve(a).then(function(e){return moapp.requestCloudFunction(t,"wxaa8fe119f5c62d23","main","toBegin",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},data:{objects:["backLeida","leida","authorAvatar","guest_stars","helpBtn","tip1","tip2","guest_records","delete","ansMask","guest_detail","bottomBox","shareBtn","shareBtnAuditing","beginPlay"],__backLeida_src:"http://material.motimaster.com/yuyuan/Duudle/create/7029a94695b5c003052970aa0c4841bd.png",__backLeida_width:"650rpx",__backLeida_height:"679rpx",__backLeida_left:"49rpx",__backLeida_top:"135rpx",__leida_src:"../../img/leida2.png",__leida_width:"439rpx",__leida_height:"330rpx",__leida_left:"261rpx",__leida_top:"485rpx",__authorAvatar_src:"",__authorAvatar_width:"70rpx",__authorAvatar_height:"70rpx",__authorAvatar_left:"340rpx",__authorAvatar_top:"453rpx",__guest_stars_data:"",__guest_stars_background:"blue",__helpBtn_hidden:true,__helpBtn_disabled:"",__helpBtn_width:"70rpx",__helpBtn_height:"70rpx",__helpBtn_left:"650rpx",__helpBtn_top:"70rpx",__tip1_text:"目前还没有好友来测，快点击底部按钮，去邀请好友来回忆吧！",__tip1_hidden:true,__tip1_color:"#FFFFFF",__tip1_left:"0rpx",__tip1_top:"580rpx",__tip1_right:"0rpx",__tip1_fontSize:"36rpx",__tip2_text:"↓↓↓",__tip2_hidden:true,__tip2_color:"#F0739B",__tip2_left:"0rpx",__tip2_top:"650rpx",__tip2_right:"0rpx",__tip2_fontSize:"36rpx",__guest_records_data:"",__guest_records_left:"37rpx",__guest_records_top:"961rpx",__delete_src:"http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png",__delete_width:"40rpx",__delete_height:"40rpx",__delete_left:"0rpx",__delete_top:"0rpx",__ansMask_hidden:true,__ansMask_width:"100%",__ansMask_height:"100%",__ansMask_background:"RGBA(0, 0, 0, 0.7)",__ansMask_left:"0rpx",__ansMask_top:"0rpx",__guest_detail_data:"",__bottomBox_width:"750rpx",__bottomBox_height:"100rpx",__bottomBox_background:"#4E7ED8",__bottomBox_bottom:"0rpx",__shareBtn_text:"邀请好友来测 >",__shareBtn_hidden:true,__shareBtn_disabled:"",__shareBtn_color:"#663300",__shareBtn_width:"750rpx",__shareBtn_height:"110rpx",__shareBtn_background:"#FEB621",__shareBtn_bottom:"0rpx",__shareBtn_fontSize:"38rpx",__shareBtn_fontWeight:600,__shareBtnAuditing_text:"邀请好友来测 >",__shareBtnAuditing_hidden:false,__shareBtnAuditing_disabled:"",__shareBtnAuditing_color:"#663300",__shareBtnAuditing_width:"750rpx",__shareBtnAuditing_height:"100rpx",__shareBtnAuditing_background:"#FEB621",__shareBtnAuditing_bottom:"0rpx",__shareBtnAuditing_fontSize:"36rpx",__shareBtnAuditing_fontWeight:600,__beginPlay_text:"创建我的好友回忆墙 >",__beginPlay_hidden:true,__beginPlay_disabled:"",__beginPlay_color:"#663300",__beginPlay_width:"750rpx",__beginPlay_height:"100rpx",__beginPlay_background:"#FEB621",__beginPlay_bottom:"0rpx",__beginPlay_fontSize:"36rpx",__beginPlay_fontWeight:900},onReady:function(){var e=this;var t=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",e,{});Promise.resolve(t).then(function(e){wx.showLoading({title:`加载中...`,mask:true});return e}).then(function(t){return moapp.requestCloudFunction(e,"wxaa8fe119f5c62d23","main","mainPageReady",t)}).then(function(e){wx.hideLoading();return e}).catch(e=>{})},onShow:function(e){var t=this;var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,{});moapp.bgmAllInOne(t,app);Promise.resolve(a).then(function(e){return e}).catch(e=>{})},onPullDownRefresh:function(){wx.showNavigationBarLoading();var e=this;var t=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",e,{});Promise.resolve(t).then(function(t){return moapp.requestCloudFunction(e,"wxaa8fe119f5c62d23","main","mainPageReady",t)}).then(e=>{wx.hideNavigationBarLoading();wx.stopPullDownRefresh()}).catch(e=>{console.log("onPulldownRefresh exception, err:");console.log(e);wx.hideNavigationBarLoading();wx.stopPullDownRefresh()})},onShareAppMessage:function(e){var t=this;let a="";const n=[];if(this.data.__share_options){for(let e in this.data.__share_options){n.push(e+"="+this.data.__share_options[e])}}n.push("_openid="+moapp.getOpenId());a=n.join("&");if(this.data.__share_page){}else{this.data.__share_page="begin"}let r={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+a,success:function(e){console.log("share successed");console.log(e);var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,{});Promise.resolve(a)},fail:function(e){console.log("share failed!");console.log(e);var a=moapp.genEventData("wxaa8fe119f5c62d23","mainpage",t,{});Promise.resolve(a)}};if(this.data.__share_title){r.title=this.data.__share_title}if(this.data.__share_imageUrl){r.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){r.imageUrl=this.data.__share_image}return r},onLoad:function(e){for(let t in e){if(typeof e[t]=="string"){e[t]=decodeURIComponent(e[t])}}this.setData({options:e,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)},formIdHandler:function(e){var t=`wxaa8fe119f5c62d23`;moapp.submitFormId(t,e.detail.formId)}});