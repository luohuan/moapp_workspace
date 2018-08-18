const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onImageAvatarTap_6tUkwj:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            wx.showToast({
              title: `111`,
              icon: 'success',
              image:undefined,
              duration: 1500
            })

            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `正在分析中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'onReadyPicPage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_mlAare:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'onMoreFunTap', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx021a5f382c69640e`
                        moapp.submitFormId(appid, e.detail.formId)

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
                        this.data.__share_page = 'first'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, {});
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
    onImageTap_DrXrgA:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'previewimage2', evt);
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
    data: {
    "__morefun_background": "#0598cc",
    "__mopicImage_left": "0rpx",
    "__avtar_top": "502rpx",
    "__morefun_hidden": true,
    "__mopicImage_width": "600rpx",
    "__morefun_width": "520rpx",
    "__avtar_height": "164rpx",
    "__mopicImage_top": "0rpx",
    "__mopicImage_height": "900rpx",
    "__morefun_fontSize": "26rpx",
    "__avtar_hidden": true,
    "__morefun_left": "115rpx",
    "__avtar_left": "293rpx",
    "__morefun_color": "#ffffff",
    "objects": [
        "mopicImage",
        "avtar",
        "morefun"
    ],
    "__avtar_width": "164rpx",
    "__morefun_top": "1080rpx",
    "__mopicImage_src": "",
    "__morefun_text": "\u66f4\u591a\u597d\u73a9",
    "__morefun_height": "60rpx",
    "__mopicImage_right": "0rpx",
    "__morefun_disabled": ""
},
    onGetUserInfo_FbHpa5:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'onSaveImage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx021a5f382c69640e", "pageX", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})