const app=getApp();const moapp=require("../../utils/moapp.js");Page({data:{objects:["3_1","3_1h","2_1","2_1h","4_1","4_1h","5_1","5_1h","10_1","10_1h","7_1","7_1h","8_1","8_1h","9_1","9_1h","1_1","1_1h","6_1","6_1h","12_1","12_1h","choose","luck"],__3_1_src:"",__3_1_width:"45rpx",__3_1_height:"45rpx",__3_1_left:"0rpx",__3_1_top:"0rpx",__3_1h_src:"",__3_1h_width:"162rpx",__3_1h_height:"162rpx",__3_1h_left:"-43rpx",__3_1h_top:"-36rpx",__2_1_src:"",__2_1_width:"45rpx",__2_1_height:"45rpx",__2_1_left:"0rpx",__2_1_top:"0rpx",__2_1h_src:"",__2_1h_width:"162rpx",__2_1h_height:"162rpx",__2_1h_left:"-43rpx",__2_1h_top:"-36rpx",__4_1_src:"",__4_1_width:"45rpx",__4_1_height:"45rpx",__4_1_left:"0rpx",__4_1_top:"0rpx",__4_1h_src:"",__4_1h_width:"162rpx",__4_1h_height:"162rpx",__4_1h_left:"-43rpx",__4_1h_top:"-36rpx",__5_1_src:"",__5_1_width:"45rpx",__5_1_height:"45rpx",__5_1_left:"0rpx",__5_1_top:"0rpx",__5_1h_src:"",__5_1h_width:"162rpx",__5_1h_height:"162rpx",__5_1h_left:"-43rpx",__5_1h_top:"-36rpx",__10_1_src:"",__10_1_width:"45rpx",__10_1_height:"45rpx",__10_1_left:"0rpx",__10_1_top:"0rpx",__10_1h_src:"",__10_1h_width:"162rpx",__10_1h_height:"162rpx",__10_1h_left:"-43rpx",__10_1h_top:"-36rpx",__7_1_src:"",__7_1_width:"45rpx",__7_1_height:"45rpx",__7_1_left:"0rpx",__7_1_top:"0rpx",__7_1h_src:"",__7_1h_width:"162rpx",__7_1h_height:"162rpx",__7_1h_left:"-43rpx",__7_1h_top:"-36rpx",__8_1_src:"",__8_1_width:"45rpx",__8_1_height:"45rpx",__8_1_left:"0rpx",__8_1_top:"0rpx",__8_1h_src:"",__8_1h_width:"162rpx",__8_1h_height:"162rpx",__8_1h_left:"-43rpx",__8_1h_top:"-36rpx",__9_1_src:"",__9_1_width:"45rpx",__9_1_height:"45rpx",__9_1_left:"0rpx",__9_1_top:"0rpx",__9_1h_src:"",__9_1h_width:"162rpx",__9_1h_height:"162rpx",__9_1h_left:"-43rpx",__9_1h_top:"-36rpx",__1_1_src:"",__1_1_width:"45rpx",__1_1_height:"45rpx",__1_1_left:"0rpx",__1_1_top:"0rpx",__1_1h_src:"",__1_1h_width:"162rpx",__1_1h_height:"162rpx",__1_1h_left:"-43rpx",__1_1h_top:"-36rpx",__6_1_src:"",__6_1_width:"45rpx",__6_1_height:"45rpx",__6_1_left:"0rpx",__6_1_top:"0rpx",__6_1h_src:"",__6_1h_width:"162rpx",__6_1h_height:"162rpx",__6_1h_left:"-43rpx",__6_1h_top:"-36rpx",__12_1_src:"",__12_1_width:"45rpx",__12_1_height:"45rpx",__12_1_left:"0rpx",__12_1_top:"0rpx",__12_1h_src:"",__12_1h_width:"162rpx",__12_1h_height:"162rpx",__12_1h_left:"-43rpx",__12_1h_top:"-36rpx",__choose_color:"#FFFFFF",__choose_left:"0rpx",__choose_top:"600rpx",__choose_right:"0rpx",__choose_fontSize:"30rpx",__luck_color:"#FFFFFF",__luck_left:"0rpx",__luck_top:"900rpx",__luck_right:"0rpx",__luck_fontSize:"30rpx"},onReady:function(){var _=this;var t=moapp.genEventData("wx628e03240351132c","page_test",_,{});Promise.resolve(t).then(function(_){wx.showLoading({title:`加载中...`,mask:true});return _}).then(function(t){return moapp.requestCloudFunction(_,"wx628e03240351132c","main","page_test.onInit",t)}).then(function(_){wx.hideLoading();return _}).catch(_=>{})},onShow:function(_){var t=this;var h=moapp.genEventData("wx628e03240351132c","page_test",t,{});moapp.bgmAllInOne(t,app);Promise.resolve(h).then(function(_){return _}).catch(_=>{})},onShareAppMessage:function(_){var t=this;let h="";const r=[];if(this.data.__share_options){for(let _ in this.data.__share_options){r.push(_+"="+this.data.__share_options[_])}}r.push("_openid="+moapp.getOpenId());h=r.join("&");if(this.data.__share_page){}else{this.data.__share_page="page_analyze"}let e={path:`/pages/${this.data.__share_page}/${this.data.__share_page}?`+h,success:function(_){console.log("share successed");console.log(_);var h=moapp.genEventData("wx628e03240351132c","page_test",t,{});Promise.resolve(h)},fail:function(_){console.log("share failed!");console.log(_);var h=moapp.genEventData("wx628e03240351132c","page_test",t,{});Promise.resolve(h)}};if(this.data.__share_title){e.title=this.data.__share_title}if(this.data.__share_imageUrl){e.imageUrl=this.data.__share_imageUrl}if(this.data.__share_image){e.imageUrl=this.data.__share_image}return e},onLoad:function(_){for(let t in _){if(typeof _[t]=="string"){_[t]=decodeURIComponent(_[t])}}this.setData({options:_,createTime:parseInt(Date.now()/1e3)});wx.showShareMenu({withShareTicket:true})},bgmcontrol:function(){moapp.bgmControl(this,app)}});