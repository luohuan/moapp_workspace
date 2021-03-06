const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "share", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'shareReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_2obaxg:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "share", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'saveShareImage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShareAppMessage: function(opt) {
                    var self = this;
                    let options = '';
                    const optionsArray = [];
                    if(this.data.__share_options){
                       for(let k in this.data.__share_options){
                            optionsArray.push(k+'='+this.data.__share_options[k]);
                        }
                    }
                    
                    optionsArray.push('_openid='+moapp.getOpenId());
                    options = optionsArray.join("&");

                    if(this.data.__share_page){
                        //console.log('此页面分享的页面是:'+ this.data.__share_page)
                    }else {
                        this.data.__share_page = 'begin'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "share", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "share", self, {});
                            Promise.resolve(evt_data)
                        }
                    }

                    if(this.data.__share_title){
                        shareInfo.title = this.data.__share_title;                    
                    }

                    if(this.data.__share_imageUrl){
                        shareInfo.imageUrl = this.data.__share_imageUrl;                    
                    }

                    if(this.data.__share_image){
                        shareInfo.imageUrl = this.data.__share_image;                    
                    }

                    return shareInfo;                
                },
    data: {
    "__shareImage_src": "http://material.motimaster.com/yuyuan/Duudle/create/93c539e06f357977dc224f88e952ba3f.jpg",
    "__avatar_top": "393rpx",
    "__saveShareImage_top": "780rpx",
    "__saveShareImage_fontWeight": 900,
    "__saveShareImage_width": "400rpx",
    "__saveShareImage_height": "80rpx",
    "__saveShareImage_disabled": "",
    "__saveShareImage_fontSize": "16px",
    "__avatar_height": "149rpx",
    "__avatar_width": "149rpx",
    "__saveShareImage_hidden": true,
    "__saveShareImage_color": "#663300",
    "__avatar_left": "297rpx",
    "__shareImage_left": "23rpx",
    "objects": [
        "shareImage",
        "avatar",
        "saveShareImage"
    ],
    "__saveShareImage_backgroundColor": "#FEB621",
    "__shareImage_width": "704rpx",
    "__shareImage_height": "704rpx",
    "__shareImage_top": "23rpx",
    "__saveShareImage_left": "175rpx",
    "__shareImage_hidden": true,
    "__saveShareImage_text": "\u4fdd\u5b58"
},
    onLoad: function(options) {
            for (let k in options){
                if(typeof(options[k]) == 'string') {
                    options[k] = decodeURIComponent(options[k])
                }
            }
            this.setData({
                options: options,
                createTime: parseInt(Date.now()/1000)
            });           
            wx.showShareMenu({withShareTicket: true});
        },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "share", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})