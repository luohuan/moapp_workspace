const app=getApp();const moapp=require("../../utils/moapp.js");Page({data:{},onReady:function(){var a=this;var e=moapp.genEventData("wx6acc1db2845590f6","payment",a,{});Promise.resolve(e).then(function(a){wx.showLoading({title:`加载中...`,mask:true});return a}).then(function(e){return moapp.requestCloudFunction(a,"wx6acc1db2845590f6","main","payment.onInit",e)}).then(function(a){wx.hideLoading();return a}).catch(a=>{})},onShow:function(a){var e=this;var t=moapp.genEventData("wx6acc1db2845590f6","payment",e,{});moapp.bgmAllInOne(e,app);Promise.resolve(t).then(function(a){return a}).catch(a=>{})},onShareAppMessage:function(a){var e=this;let t="";const n=[];if(this.data.__share_options){for(let a in this.data.__share_options){n.push(a+"="+this.data.__share_options[a])}}n.push("_openid="+moapp.getOpenId());t=n.join("&");if(this.data.__share_page){}else{this.data.__share_page="listPage"}let o={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+t,success:function(a){console.log("share successed");console.log(a);var t=moapp.genEventData("wx6acc1db2845590f6","payment",e,{});Promise.resolve(t)},fail:function(a){console.log("share failed!");console.log(a);var t=moapp.genEventData("wx6acc1db2845590f6","payment",e,{});Promise.resolve(t)}};if(this.data.__share_title){o.title=this.data.__share_title}if(this.data.__share_imageUrl){o.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){o.imageUrl=this.data.__share_image}return o},onLoad:function(a){for(let e in a){if(typeof a[e]=="string"){a[e]=decodeURIComponent(a[e])}}this.setData({options:a,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)}});