const app=getApp();const moapp=require("../../utils/moapp.js");const qiniuUploader=require("../../utils/qiniuUploader");Page({onGetUserInfo_qzhm2I:function(a){var e=this;if(a.detail.userInfo){app.globalData.userInfo=a.detail.userInfo;var t=moapp.genEventData("wx8978abc3aab37e9e","first",e,a.currentTarget.dataset);Promise.resolve(t).then(function(a){var e={page:"paper",drama_list:"测试"};var t=e.page;delete e.page;wx.navigateTo({url:`../${t}/${t}?`+moapp.jsonToUrlParams(e)})}).catch(a=>{})}else{console.log("get user info fail! error message:"+a.detail.errMsg)}},data:{},onReady:function(){var a=this;var e=moapp.genEventData("wx8978abc3aab37e9e","first",a,{});Promise.resolve(e).then(function(a){wx.showLoading({title:`加载中...`,mask:true});return a}).then(function(e){return moapp.requestCloudFunction(a,"wx8978abc3aab37e9e","mainoook","firstReady",e)}).then(function(a){wx.hideLoading();return a}).catch(a=>{})},onShow:function(a){var e=this;var t=moapp.genEventData("wx8978abc3aab37e9e","first",e,{});moapp.bgmAllInOne(e,app);Promise.resolve(t).then(function(a){return a}).catch(a=>{})},onShareAppMessage:function(a){var e=this;let t="";const o=[];if(this.data.__share_options){for(let a in this.data.__share_options){o.push(a+"="+this.data.__share_options[a])}}o.push("_openid="+moapp.getOpenId());t=o.join("&");if(this.data.__share_page){}else{this.data.__share_page="first"}let s={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+t,success:function(a){console.log("share successed");console.log(a);var t=moapp.genEventData("wx8978abc3aab37e9e","first",e,{});Promise.resolve(t)},fail:function(a){console.log("share failed!");console.log(a);var t=moapp.genEventData("wx8978abc3aab37e9e","first",e,{});Promise.resolve(t)}};if(this.data.__share_title){s.title=this.data.__share_title}if(this.data.__share_imageUrl){s.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){s.imageUrl=this.data.__share_image}return s},onLoad:function(a){for(let e in a){if(typeof a[e]=="string"){a[e]=decodeURIComponent(a[e])}}this.setData({options:a,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)},formIdHandler:function(a){var e=`wx8978abc3aab37e9e`;moapp.submitFormId(e,a.detail.formId)}});