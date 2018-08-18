const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_PQPpjC:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'saveShareImage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__saveShareImage_height": "80rpx",
    "__saveShareImage_disabled": "",
    "__shareImage_height": "704rpx",
    "__avatar_width": "149rpx",
    "__shareImage_top": "23rpx",
    "__saveShareImage_left": "175rpx",
    "__saveShareImage_fontWeight": 900,
    "__shareImage_hidden": true,
    "__saveShareImage_backgroundColor": "#4E7ED8",
    "__saveShareImage_color": "#ffffff",
    "__avatar_left": "297rpx",
    "__shareImage_width": "704rpx",
    "__saveShareImage_width": "400rpx",
    "__avatar_top": "393rpx",
    "__saveShareImage_fontSize": "16px",
    "objects": [
        "shareImage",
        "avatar",
        "saveShareImage"
    ],
    "__avatar_height": "149rpx",
    "__shareImage_left": "23rpx",
    "__saveShareImage_text": "\u4fdd\u5b58\u670b\u53cb\u5708\u6d77\u62a5",
    "__saveShareImage_top": "780rpx",
    "__shareImage_src": "http://material.motimaster.com/harvey///2517b8eeae48e0bbb6fcb29e010332f8.o6zAJswuegJ2dQvOSkJr400-bIlQ"
},
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'shareReady', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
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
})