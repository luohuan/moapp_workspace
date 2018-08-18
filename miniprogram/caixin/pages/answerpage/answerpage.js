const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
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
                            
                            
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, {});
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
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, {});
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
    onGetUserInfo_XZ2fbu:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'AnswerTap1', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onGetUserInfo_qBMHtS:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'AnswerTap2', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'answerPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    formIdHandler: function (e) {
                        var appid= `wx18610e0755615e2f`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    data: {
    "__question_width": "600rpx",
    "__setAns3_color": "#FFD886",
    "__setAns4_top": "780rpx",
    "__setAns3_left": "125rpx",
    "__setAns1_background": "rgba(17,17,17,0.39)",
    "__setAns3_disabled": "",
    "__setAns2_top": "560rpx",
    "__setAns4_fontSize": "28rpx",
    "__setAns3_background": "rgba(17,17,17,0.39)",
    "__setAns3_top": "670rpx",
    "__setAns2_color": "#FFD886",
    "__subtitle_fontWeight": "bold",
    "__subtitle_top": "220rpx",
    "__setAns4_left": "125rpx",
    "__hostimage_width": "150rpx",
    "__setAns4_disabled": "",
    "__question_right": "0rpx",
    "__setAns4_height": "80rpx",
    "objects": [
        "hostimage",
        "subtitle",
        "question",
        "setAns1",
        "setAns2",
        "setAns3",
        "setAns4"
    ],
    "__setAns2_disabled": "",
    "__setAns3_fontSize": "28rpx",
    "__question_top": "310rpx",
    "__setAns4_background": "rgba(17,17,17,0.39)",
    "__hostimage_height": "150rpx",
    "__setAns2_left": "125rpx",
    "__question_color": "#FFFFFF",
    "__setAns3_width": "500rpx",
    "__subtitle_fontSize": "32rpx",
    "__hostimage_src": "",
    "__question_height": "60rpx",
    "__hostimage_right": "0rpx",
    "__question_fontSize": "37rpx",
    "__hostimage_top": "20rpx",
    "__setAns1_top": "450rpx",
    "__setAns1_left": "125rpx",
    "__subtitle_color": "#FEB621",
    "__setAns4_width": "500rpx",
    "__hostimage_left": "0rpx",
    "__setAns1_fontSize": "28rpx",
    "__setAns1_width": "500rpx",
    "__question_left": "0rpx",
    "__setAns1_disabled": "",
    "__setAns3_height": "80rpx",
    "__subtitle_right": "0rpx",
    "__setAns4_color": "#FFD886",
    "__setAns2_fontSize": "28rpx",
    "__setAns1_height": "80rpx",
    "__subtitle_left": "0rpx",
    "__setAns1_color": "#FFD886",
    "__setAns2_background": "rgba(17,17,17,0.39)",
    "__setAns2_height": "80rpx",
    "__question_fontWeight": "bold",
    "__setAns2_width": "500rpx"
},
    onGetUserInfo_vgbB29:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'AnswerTap4', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onGetUserInfo_7tQWJv:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx18610e0755615e2f", "answerpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'AnswerTap3', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})