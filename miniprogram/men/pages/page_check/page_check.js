const app=getApp();const moapp=require("../../utils/moapp.js");Page({onGetUserInfo_7asRS2:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"440,0",No:4,gate_name:"俱舍门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_jlTH7k:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"215,75",No:3,gate_name:"禅门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_CFo4jG:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"120,200",No:2,gate_name:"天台门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_CtGEOj:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"15,380",No:7,gate_name:"法相门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_iMqjrQ:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"240,410",No:8,gate_name:"律门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_U0fWZV:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"550,185",No:5,gate_name:"真言门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_AZP2R7:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"365,350",No:9,gate_name:"华严门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_mAX17G:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"540,375",No:10,gate_name:"净土门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_YEZDsU:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"85,330",No:1,gate_name:"成实门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_uT8Byl:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"600,330",No:6,gate_name:"三论门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_0f0fuS:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"175,930",No:11,gate_name:"涅槃门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},onGetUserInfo_Nvu4d5:function(e){var a=this;if(e.detail.userInfo){app.globalData.userInfo=e.detail.userInfo;var t=moapp.genEventData("wx628e03240351132c","page_check",a,e.currentTarget.dataset);Promise.resolve(t).then(function(e){e.params={p:"600,940",No:12,gate_name:"地论门"};return moapp.requestCloudFunction(a,"wx628e03240351132c","main","page_check.save_record",e)}).catch(e=>{})}else{console.log("get user info fail! error message:"+e.detail.errMsg)}},data:{objects:["animabox"],__animabox_hidden:true,__animabox_width:"750rpx",__animabox_height:"1334rpx",__animabox_left:"0rpx",__animabox_top:"0rpx"},onReady:function(){var e=this;var a=moapp.genEventData("wx628e03240351132c","page_check",e,{});Promise.resolve(a).then(function(e){wx.showLoading({title:`加载中...`,mask:true});return e}).then(function(a){return moapp.requestCloudFunction(e,"wx628e03240351132c","main","page_check.onInit",a)}).then(function(e){wx.hideLoading();return e}).catch(e=>{})},onShow:function(e){var a=this;var t=moapp.genEventData("wx628e03240351132c","page_check",a,{});moapp.bgmAllInOne(a,app);Promise.resolve(t).then(function(e){return e}).catch(e=>{})},onShareAppMessage:function(e){var a=this;let t="";const r=[];if(this.data.__share_options){for(let e in this.data.__share_options){r.push(e+"="+this.data.__share_options[e])}}r.push("_openid="+moapp.getOpenId());t=r.join("&");if(this.data.__share_page){}else{this.data.__share_page="page_analyze"}let o={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+t,success:function(e){console.log("share successed");console.log(e);var t=moapp.genEventData("wx628e03240351132c","page_check",a,{});Promise.resolve(t)},fail:function(e){console.log("share failed!");console.log(e);var t=moapp.genEventData("wx628e03240351132c","page_check",a,{});Promise.resolve(t)}};if(this.data.__share_title){o.title=this.data.__share_title}if(this.data.__share_imageUrl){o.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){o.imageUrl=this.data.__share_image}return o},onLoad:function(e){for(let a in e){if(typeof e[a]=="string"){e[a]=decodeURIComponent(e[a])}}this.setData({options:e,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)},formIdHandler:function(e){var a=`wx628e03240351132c`;moapp.submitFormId(a,e.detail.formId)}});