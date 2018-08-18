const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "share", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "share", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'share.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__saveShareImage_top": "780rpx",
    "__shareImage_right": "0rpx",
    "__saveShareImage_color": "#ffffff",
    "__saveShareImage_disabled": "",
    "__shareImage_width": "700rpx",
    "__shareImage_left": "0rpx",
    "__shareImage_top": "23rpx",
    "__saveShareImage_width": "400rpx",
    "__saveShareImage_fontWeight": 900,
    "__saveShareImage_backgroundColor": "rgba(242,64,64,0.82)",
    "__saveShareImage_left": "175rpx",
    "__saveShareImage_height": "80rpx",
    "__saveShareImage_fontSize": "16px",
    "__shareImage_height": "700rpx",
    "objects": [
        "shareImage",
        "saveShareImage"
    ],
    "__shareImage_src": "http://img.mogodeer.cn/images/diudiu/xingzuozhun/erweima5.jpg",
    "__saveShareImage_text": "\u4fdd\u5b58\u670b\u53cb\u5708\u6d77\u62a5"
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "share", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "share", self, {});
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
    onButtonTap_3bzaRM:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "share", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'share.saveShareImage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
})