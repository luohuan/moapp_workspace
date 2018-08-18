const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    onfinish_pFm4iM:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'analy.analyFuc', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_Ffrkem:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'analy.startAnaly', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_5B2LcY:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then(function(evt){
            var evt = evt_data
            return moapp.chooseImage(evt, 9, ['compressed', 'original'], ['album', 'camera']);
        }
        ).then(
            function(evt){
                    
                    console.log(evt)
                    console.log(evt_data)

                    return new Promise((resolve, reject) => {
                    console.log('为什么没有反映')
                        qiniuUploader.upload(evt.params.tempFilePaths[0], (res) => {
                                console.log('上传成功')
                                console.log(res)
                                evt.params.imageURL = res.imageURL
                                resolve(evt)
                            }, (error) => {
                                console.log('上传失败')
                                console.log('error: ' + error);
                                reject()
                            }
                          , {
                            region: 'SCN', // 华南区
                            uptokenURL: 'https://dev.mozigu.net/moapp/token',
                            domain: 'http://oypxibwiu.bkt.clouddn.com',
                            shouldUseQiniuFileName: true,
                          }
                    );
                })
            }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'analy.uploadImage', evt);
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
    onButtonTap_McB8uA:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'analy.saveFuc', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
                        this.data.__share_page = 'index'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, {});
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
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "analy", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'analy.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__start_top": "1050rpx",
    "__savebtn_text": "\u4fdd\u5b58\u6211\u7684\u7a7f\u642d\u6210\u7ee9\u5355",
    "__kuang_right": "0rpx",
    "__date_fontSize": "35rpx",
    "__start_disabled": "",
    "__photo_src": "",
    "__start_right": "0rpx",
    "__sharebtn_hidden": true,
    "__xian_src": "",
    "__counter_config": "",
    "__score_left": "445rpx",
    "__wenzi_src": "http://material.motimaster.com/liuhongjie1532426719000/\u672a\u6807\u9898-1.png",
    "__photo_height": "750rpx",
    "__start_background": "#e87d67",
    "__result_fontSize": "35rpx",
    "__kuang_top": "50rpx",
    "__result_top": "830rpx",
    "__kuang_left": "0rpx",
    "__start_text": "\u5f00\u59cb\u5206\u6790",
    "__photo_hidden": true,
    "__savebtn_left": "0rpx",
    "__start_height": "90rpx",
    "__start_left": "0rpx",
    "__score_top": "65rpx",
    "__wenzi_hidden": true,
    "__savebtn_hidden": true,
    "__photo_width": "670rpx",
    "__xian_height": "100rpx",
    "__counter_stop": "",
    "__savebtn_width": "450rpx",
    "__result_hidden": true,
    "__savebtn_height": "80rpx",
    "__sharebtn_disabled": "",
    "__wenzi_left": "450rpx",
    "objects": [
        "date",
        "photo",
        "kuang",
        "xian",
        "wenzi",
        "score",
        "result",
        "start",
        "savebtn",
        "sharebtn",
        "counter"
    ],
    "__score_hidden": true,
    "__xian_width": "696rpx",
    "__sharebtn_height": "80rpx",
    "__sharebtn_top": "1150rpx",
    "__result_left": "25rpx",
    "__savebtn_right": "0rpx",
    "__score_height": "55rpx",
    "__sharebtn_background": "#e87d67",
    "__photo_left": "0rpx",
    "__wenzi_height": "55rpx",
    "__xian_left": "0rpx",
    "__kuang_hidden": true,
    "__wenzi_top": "5rpx",
    "__savebtn_background": "#e87d67",
    "__photo_right": "0rpx",
    "__kuang_src": "",
    "__counter_color": "#ffffff",
    "__xian_right": "0rpx",
    "__score_src": "",
    "__date_left": "25rpx",
    "__kuang_height": "772rpx",
    "__start_width": "250rpx",
    "__date_top": "5rpx",
    "__xian_hidden": true,
    "__sharebtn_fontSize": "40rpx",
    "__photo_background": "#eeeeee",
    "__sharebtn_right": "0rpx",
    "__start_fontSize": "40rpx",
    "__result_width": "650rpx",
    "__sharebtn_text": "\u5206\u4eab\u7ed9\u597d\u53cb\u4e00\u8d77\u7528",
    "__score_width": "235rpx",
    "__savebtn_top": "1050rpx",
    "__savebtn_disabled": "",
    "__result_height": "200rpx",
    "__sharebtn_width": "450rpx",
    "__photo_top": "60rpx",
    "__xian_top": "60rpx",
    "__sharebtn_left": "0rpx",
    "__savebtn_fontSize": "40rpx",
    "__wenzi_width": "180rpx",
    "__kuang_width": "696rpx"
},
})