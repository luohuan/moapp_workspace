const app=getApp();const moapp=require("../../utils/moapp.js");const qiniuUploader=require("../../utils/qiniuUploader");Page({onGetUserInfo_ZmcF9w:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wxf7c6308b0e199d50","homePage",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){var a={page:"testPage"};var t=a.page;delete a.page;wx.navigateTo({url:`../${t}/${t}?`+moapp.jsonToUrlParams(a)})}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},data:{},onShow:function(e){var a=this;var t=moapp.genEventData("wxf7c6308b0e199d50","homePage",a,{});moapp.bgmAllInOne(a,app);Promise.resolve(t).then(function(e){return e}).catch(e=>{})},onShareAppMessage:function(e){var a=this;let t="";const o=[];if(this.data.__share_options){for(let e in this.data.__share_options){o.push(e+"="+this.data.__share_options[e])}}o.push("_openid="+moapp.getOpenId());t=o.join("&");if(this.data.__share_page){}else{this.data.__share_page="pageentrance"}let s={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+t,success:function(e){console.log("share successed");console.log(e);var t=moapp.genEventData("wxf7c6308b0e199d50","homePage",a,{});Promise.resolve(t)},fail:function(e){console.log("share failed!");console.log(e);var t=moapp.genEventData("wxf7c6308b0e199d50","homePage",a,{});Promise.resolve(t)}};if(this.data.__share_title){s.title=this.data.__share_title}if(this.data.__share_imageUrl){s.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){s.imageUrl=this.data.__share_image}return s},onLoad:function(e){for(let a in e){if(typeof e[a]=="string"){e[a]=decodeURIComponent(e[a])}}this.setData({options:e,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)},formIdHandler:function(e){var a=`wxf7c6308b0e199d50`;moapp.submitFormId(a,e.detail.formId)}});