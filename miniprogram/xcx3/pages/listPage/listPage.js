const app=getApp();const moapp=require("../../utils/moapp.js");const qiniuUploader=require("../../utils/qiniuUploader");Page({onGetUserInfo_xRyS64:function(t){var a=this;if(t.detail.userInfo){app.globalData.userInfo=t.detail.userInfo;var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset);Promise.resolve(e).then(function(t){wx.showLoading({title:`加载中...`,mask:true});return t}).then(function(t){return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.computeNameScore",t)}).then(function(t){wx.hideLoading();return t}).catch(t=>{})}else{console.log("get user info fail! error message:"+t.detail.errMsg)}},onImageTap_L7o2WM:function(t){var a=this;var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset);Promise.resolve(e).then(function(t){t.params={path:t.data.path,appid:t.data.appid,title:t.data.title,tyepe:t.data.type};return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.go_to",t)}).catch(t=>{})},onViewTap_Mx5xog:function(t){var a=this;a.setData({__grid1_item:t.currentTarget.dataset});var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset,t.currentTarget);Promise.resolve(e).then(function(t){t.params={path:t.data.path,appid:t.data.appid,title:t.data.title,tyepe:t.data.type};return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.go_to",t)}).catch(t=>{})},onImageTap_KaORLY:function(t){var a=this;var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset);Promise.resolve(e).then(function(t){t.params={name:"ad"};return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.ad_goto",t)}).catch(t=>{})},onViewTap_9rJWA6:function(t){var a=this;a.setData({__dormitorylist_item:t.currentTarget.dataset});var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset,t.currentTarget);Promise.resolve(e).then(function(t){t.params={path:t.data.path,appid:t.data.appid,type:t.data.type,title:t.data.title};return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.go_to",t)}).catch(t=>{})},onImageTap_unBKdv:function(t){var a=this;var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,t.currentTarget.dataset);Promise.resolve(e).then(function(t){t.params={name:"ad_2"};return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","listPage.ad_goto",t)}).catch(t=>{})},data:{objects:["auditing_box","image1","text1","button1","neirong","swiper1","dataswiper","hidden_1","recommend","grid1","ad","hidden_ad","all_play","dormitorylist","fenxiang","ad_2"],__auditing_box_hidden:true,__auditing_box_width:"750rpx",__auditing_box_left:"0rpx",__auditing_box_top:"0rpx",__image1_src:"http://material.motimaster.com/harvey/5455/myrose/89c33fb1592b3b3289d94ff08dd984aa.jpg",__image1_width:"750rpx",__image1_height:"1325rpx",__image1_left:"0rpx",__image1_top:"-40rpx",__text1_text:"算算好友跟你的名字能得多少分",__text1_color:"#FFFFFF",__text1_left:"0rpx",__text1_top:"400rpx",__text1_right:"0rpx",__text1_fontSize:"24rpx",__button1_text:"提交",__button1_disabled:"",__button1_color:"#FFFFFF",__button1_width:"360rpx",__button1_height:"78rpx",__button1_background:"rgba(242,64,64,0.82)",__button1_left:"0rpx",__button1_top:"938rpx",__button1_right:"0rpx",__button1_fontSize:"36rpx",__button1_fontWeight:"bolder",__neirong_hidden:true,__neirong_left:"0rpx",__neirong_top:"0rpx",__swiper1_indicatorDots:"",__swiper1_autoplay:true,__swiper1_indicatorActiveColor:"",__swiper1_width:"750rpx",__swiper1_height:"310rpx",__dataswiper_data:"",__hidden_1_left:"0rpx",__hidden_1_top:"300rpx",__recommend_left:"20rpx",__recommend_top:"30rpx",__recommend_fontSize:"37rpx",__recommend_fontWeight:"450",__grid1_data:"",__grid1_left:"0rpx",__grid1_top:"10rpx",__grid1_right:"0rpx",__ad_src:"",__ad_width:"750rpx",__ad_height:"191rpx",__ad_left:"0rpx",__ad_top:"370rpx",__hidden_ad_left:"0rpx",__hidden_ad_top:"500rpx",__all_play_left:"20rpx",__all_play_top:"80rpx",__all_play_fontSize:"37rpx",__all_play_fontWeight:"450",__dormitorylist_data:"",__fenxiang_hidden:true,__fenxiang_disabled:"",__fenxiang_color:"#f7ca4e",__fenxiang_width:"210rpx",__fenxiang_height:"70rpx",__fenxiang_fontSize:"35rpx",__fenxiang_fontWeight:"900",__ad_2_src:"",__ad_2_width:"750rpx",__ad_2_height:"191rpx",__ad_2_left:"0rpx",__ad_2_top:"1030rpx"},onReady:function(){var t=this;var a=moapp.genEventData("wx6acc1db2845590f6","listPage",t,{});Promise.resolve(a).then(function(t){wx.showLoading({title:`加载中...`,mask:true});return t}).then(function(a){return moapp.requestCloudFunction(t,"wx6acc1db2845590f6","main","listPage.onInit",a)}).then(function(t){wx.hideLoading();return t}).catch(t=>{})},onShow:function(t){var a=this;var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,{});moapp.bgmAllInOne(a,app);Promise.resolve(e).then(function(t){return t}).catch(t=>{})},onShareAppMessage:function(t){var a=this;let e="";const _=[];if(this.data.__share_options){for(let t in this.data.__share_options){_.push(t+"="+this.data.__share_options[t])}}_.push("_openid="+moapp.getOpenId());e=_.join("&");if(this.data.__share_page){}else{this.data.__share_page="listPage"}let r={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+e,success:function(t){console.log("share successed");console.log(t);var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,{});Promise.resolve(e)},fail:function(t){console.log("share failed!");console.log(t);var e=moapp.genEventData("wx6acc1db2845590f6","listPage",a,{});Promise.resolve(e)}};if(this.data.__share_title){r.title=this.data.__share_title}if(this.data.__share_imageUrl){r.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){r.imageUrl=this.data.__share_image}return r},onLoad:function(t){for(let a in t){if(typeof t[a]=="string"){t[a]=decodeURIComponent(t[a])}}this.setData({options:t,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)},formIdHandler:function(t){var a=`wx6acc1db2845590f6`;moapp.submitFormId(a,t.detail.formId)}});