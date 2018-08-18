const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onGetUserInfo_g8KGEa:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'entrance.computeNameScore', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, {});
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
    data: {
    "__loading_box_top": "0rpx",
    "__text1_top": "400rpx",
    "__input_name_box_hidden": true,
    "__image1_src": "../../img/bg2.jpg",
    "__input_name_box_width": "750rpx",
    "__image1_height": "1325rpx",
    "__text2_text": "\u7b97\u4e00\u7b97\u597d\u53cb\u8ddf\u4f60",
    "__input_host_name_right": "0rpx",
    "__auditing_box_left": "0rpx",
    "__text2_top": "450rpx",
    "__button1_fontWeight": "bolder",
    "objects": [
        "input_name_box",
        "image1",
        "text1",
        "text2",
        "text3",
        "input_host_name",
        "button1",
        "auditing_box",
        "loading_box"
    ],
    "__text1_right": "0rpx",
    "__input_name_box_top": "0rpx",
    "__loading_box_width": "750rpx",
    "__loading_box_left": "0rpx",
    "__image1_left": "0rpx",
    "__text1_fontSize": "24rpx",
    "__text3_left": "0rpx",
    "__text1_color": "#FFFFFF",
    "__text3_text": "\u5951\u5408\u5ea6\u6709\u51e0\u5206",
    "__input_host_name_placeholder": "\u8bf7\u8f93\u5165\u4f60\u7684\u540d\u5b57",
    "__text1_left": "0rpx",
    "__text3_right": "0rpx",
    "__auditing_box_width": "750rpx",
    "__button1_color": "#FFFFFF",
    "__button1_disabled": "",
    "__input_host_name_top": "600rpx",
    "__text3_top": "500rpx",
    "__auditing_box_hidden": true,
    "__button1_fontSize": "36rpx",
    "__image1_top": "-40rpx",
    "__input_name_box_left": "0rpx",
    "__text2_left": "0rpx",
    "__text2_fontSize": "24rpx",
    "__button1_width": "360rpx",
    "__input_host_name_color": "#F46060",
    "__input_host_name_value": "",
    "__text2_color": "#FFFFFF",
    "__button1_left": "0rpx",
    "__button1_right": "0rpx",
    "__text1_text": "\u6bcf\u4e2a\u540d\u5b57\u90fd\u6709\u81ea\u5df1\u7684\u70b9\u6570",
    "__text2_right": "0rpx",
    "__text3_color": "#FFFFFF",
    "__text3_fontSize": "24rpx",
    "__button1_height": "78rpx",
    "__input_host_name_height": "80rpx",
    "__input_host_name_background": "255 255 255 0.3",
    "__button1_background": "rgba(242,64,64,0.82)",
    "__input_host_name_width": "480rpx",
    "__button1_top": "938rpx",
    "__input_host_name_left": "0rpx",
    "__image1_width": "750rpx",
    "__auditing_box_top": "0rpx",
    "__button1_text": "\u63d0\u4ea4"
},
    onGetUserInfo_wsgfHA:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'entrance.commitName', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    formIdHandler: function (e) {
                        var appid= `wx01434b3ed0010d28`
                        moapp.submitFormId(appid, e.detail.formId)

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
                            
                            
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, {});
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
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'entrance.onPullDownRefresh', evt);
            }
            ).then( res => {
                        wx.hideNavigationBarLoading();
                        wx.stopPullDownRefresh();
                    }).catch( err => {
                        console.log("onPulldownRefresh exception, err:");
                        console.log(err);
                        wx.hideNavigationBarLoading();
                        wx.stopPullDownRefresh();
                    })
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'entrance.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onInputChange_Y7tjx3:  function(evt) {
                var self = this;
                
            self.setData({
                __input_host_name_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onInputChange_EDp5sE:  function(evt) {
                var self = this;
                
            self.setData({
                __input_host_name_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "entrance", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
})