const app=getApp();const moapp=require("../../utils/moapp.js");const qiniuUploader=require("../../utils/qiniuUploader");Page({data:{objects:["webview"],__webview_src:""},onReady:function(){var e=this;var a=moapp.genEventData("wxf7c6308b0e199d50","webview",e,{});Promise.resolve(a).then(function(e){wx.showLoading({title:`加载中...`,mask:true});return e}).then(function(a){return moapp.requestCloudFunction(e,"wxf7c6308b0e199d50","main","webview.onInit",a)}).then(function(e){wx.hideLoading();return e}).catch(e=>{})},onShow:function(e){var a=this;var t=moapp.genEventData("wxf7c6308b0e199d50","webview",a,{});moapp.bgmAllInOne(a,app);Promise.resolve(t).then(function(e){return e}).catch(e=>{})},onShareAppMessage:function(e){var a=this;let t="";const i=[];if(this.data.__share_options){for(let e in this.data.__share_options){i.push(e+"="+this.data.__share_options[e])}}i.push("_openid="+moapp.getOpenId());t=i.join("&");if(this.data.__share_page){}else{this.data.__share_page="listPage"}let o={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+t,success:function(e){console.log("share successed");console.log(e);var t=moapp.genEventData("wxf7c6308b0e199d50","webview",a,{});Promise.resolve(t)},fail:function(e){console.log("share failed!");console.log(e);var t=moapp.genEventData("wxf7c6308b0e199d50","webview",a,{});Promise.resolve(t)}};if(this.data.__share_title){o.title=this.data.__share_title}if(this.data.__share_imageUrl){o.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){o.imageUrl=this.data.__share_image}return o},onLoad:function(e){for(let a in e){if(typeof e[a]=="string"){e[a]=decodeURIComponent(e[a])}}this.setData({options:e,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)}});