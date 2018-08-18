const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    data: {
    "__saveShareImage_height": "80rpx",
    "__saveShareImage_text": "\u4fdd\u5b58\u670b\u53cb\u5708\u6d77\u62a5",
    "__shareImage_top": "23rpx",
    "__saveShareImage_color": "#ffffff",
    "__saveShareImage_left": "175rpx",
    "__avatar_width": "149rpx",
    "__saveShareImage_fontWeight": 900,
    "__saveShareImage_fontSize": "16px",
    "__avatar_top": "393rpx",
    "__shareImage_right": "0rpx",
    "objects": [
        "shareImage",
        "avatar",
        "saveShareImage"
    ],
    "__shareImage_src": "http://img.mogodeer.cn/images/diudiu/xingzuozhun/erweima5.jpg",
    "__shareImage_height": "700rpx",
    "__saveShareImage_disabled": "",
    "__shareImage_left": "0rpx",
    "__shareImage_width": "700rpx",
    "__saveShareImage_backgroundColor": "rgba(242,64,64,0.82)",
    "__avatar_left": "297rpx",
    "__avatar_height": "149rpx",
    "__saveShareImage_width": "400rpx",
    "__saveShareImage_top": "780rpx"
},
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create3", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create3", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'create3.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_Ud5iF5:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create3", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'create3.saveShareImage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
                        this.data.__share_page = 'create2'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create3", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create3", self, {});
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
})