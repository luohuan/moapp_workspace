const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
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
                        this.data.__share_page = 'mainpage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, {});
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onGetUserInfo_3fozkx:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'setAns3', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'onQuestPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_9yR4i3:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'setAns2', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onGetUserInfo_V2MRJT:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'setAns1', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    data: {
    "__setAns4_disabled": "",
    "__question_width": "650rpx",
    "__setAns3_color": "#FFD886",
    "__setAns4_top": "830rpx",
    "__setAns3_left": "125rpx",
    "__setAns1_background": "rgba(17,17,17,0.39)",
    "__setAns3_disabled": "",
    "__setAns1_left": "125rpx",
    "__question_height": "60rpx",
    "__setAns2_top": "610rpx",
    "__question_fontSize": "37rpx",
    "__setAns1_top": "500rpx",
    "__setAns2_background": "rgba(17,17,17,0.39)",
    "__setAns2_width": "500rpx",
    "__setAns4_width": "500rpx",
    "__setAns4_left": "125rpx",
    "__setAns1_fontSize": "28rpx",
    "__question_right": "0rpx",
    "__setAns1_width": "500rpx",
    "__question_left": "0rpx",
    "__setAns3_background": "rgba(17,17,17,0.39)",
    "objects": [
        "question",
        "setAns1",
        "setAns2",
        "setAns3",
        "setAns4"
    ],
    "__setAns2_disabled": "",
    "__setAns1_disabled": "",
    "__setAns4_fontSize": "28rpx",
    "__setAns3_height": "80rpx",
    "__setAns3_fontSize": "28rpx",
    "__question_top": "360rpx",
    "__setAns4_background": "rgba(17,17,17,0.39)",
    "__setAns4_height": "80rpx",
    "__setAns3_top": "720rpx",
    "__setAns4_color": "#FFD886",
    "__setAns2_fontSize": "28rpx",
    "__setAns1_height": "80rpx",
    "__setAns2_left": "125rpx",
    "__setAns1_color": "#FFD886",
    "__setAns3_width": "500rpx",
    "__setAns2_height": "80rpx",
    "__question_fontWeight": "bold",
    "__question_color": "#FFFFFF",
    "__setAns2_color": "#FFD886"
},
    formIdHandler: function (e) {
                        var appid= `wx18610e0755615e2f`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onGetUserInfo_YfYUiQ:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "questpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'setAns4', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})