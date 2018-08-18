const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    onButtonTap_P0LHfL:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.dy', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__xz0_data": "",
    "__loading_box_width": "750rpx",
    "__wg_color": "white",
    "__wg_disabled": "",
    "__auditing_box_hidden": true,
    "__dy2box_right": "0rpx",
    "__wg_width": "50rpx",
    "__first_width": "520rpx",
    "__auditing_box_left": "0rpx",
    "__xz0_columnStr": "1fr 1fr 1fr",
    "__dy0box_width": "540rpx",
    "__dy2_data": "",
    "__box1_width": "750rpx",
    "__first_top": "10rpx",
    "__now_height": "80rpx",
    "__xz1_data": "",
    "__wgd_width": "60rpx",
    "__xz1box_hidden": true,
    "__first_height": "80rpx",
    "__dy1_height": "300rpx",
    "__dy2box_hidden": true,
    "__wg_fontSize": "30rpx",
    "__loading_box_height": "1333rpx",
    "__wg_top": "580rpx",
    "__first_placeholder": "\u270e\u7b2c\u4e00\u5370\u8c61",
    "__xz2_data": "",
    "__xz0box_height": "300rpx",
    "__dy1box_height": "300rpx",
    "__xz2_width": "540rpx",
    "__dy1box_top": "30rpx",
    "__xz0box_width": "540rpx",
    "__yinxiang_color": "white",
    "__xz2_height": "300rpx",
    "__sbya_width": "650rpx",
    "__dy1_columnStr": "1fr 1fr 1fr",
    "__sbya_left": "0rpx",
    "__dy0box_top": "30rpx",
    "__create_height": "1234rpx",
    "__xz2_columnStr": "1fr 1fr 1fr",
    "__dy1box_left": "0rpx",
    "__xz0box_left": "0rpx",
    "__auditing_box_width": "750rpx",
    "__box1_hidden": true,
    "__dy1_column": 3,
    "__xz1box_left": "0rpx",
    "__dy2box_top": "30rpx",
    "__dy0_column": 3,
    "__yinxiang_right": "0rpx",
    "__sbya_right": "0rpx",
    "__first_background": "rgba(238,238,238,0.05)",
    "__yinxiang_top": "300rpx",
    "__xz1_column": 3,
    "__wg_left": "697rpx",
    "__xz0_column": 3,
    "__xz1_columnStr": "1fr 1fr 1fr",
    "__xz2box_top": "30rpx",
    "__now_background": "rgba(238,238,238,0.05)",
    "__xz1box_right": "0rpx",
    "__xz0_width": "540rpx",
    "__dy0box_right": "0rpx",
    "__dy2_columnStr": "1fr 1fr 1fr",
    "__dy2_height": "300rpx",
    "__dy0_height": "300rpx",
    "__xz2box_height": "300rpx",
    "__dy0_data": "",
    "__wgd_hidden": true,
    "objects": [
        "box",
        "sbya",
        "dy0box",
        "dy0",
        "dy1box",
        "dy1",
        "dy2box",
        "dy2",
        "first",
        "box1",
        "xz0box",
        "xz0",
        "xz1box",
        "xz1",
        "xz2box",
        "xz2",
        "now",
        "create",
        "loading_box",
        "auditing_box",
        "yinxiang",
        "wgd",
        "wg"
    ],
    "__yinxiang_width": "200rpx",
    "__xz0box_top": "30rpx",
    "__sbya_top": "450rpx",
    "__wg_hidden": true,
    "__box_width": "750rpx",
    "__auditing_box_top": "0rpx",
    "__dy2box_left": "0rpx",
    "__xz1_width": "540rpx",
    "__loading_box_top": "0rpx",
    "__now_placeholder": "\u270e\u73b0\u5728\u7684\u5370\u8c61",
    "__wg_text": "\u53ea\u60f3\u56f4\u89c2",
    "__dy1box_hidden": true,
    "__sbya_height": "410rpx",
    "__dy0box_height": "300rpx",
    "__dy0box_left": "0rpx",
    "__dy0_columnStr": "1fr 1fr 1fr",
    "__wgd_top": "550rpx",
    "__now_value": "",
    "__loading_box_left": "0rpx",
    "__yinxiang_height": "100rpx",
    "__xz1box_top": "30rpx",
    "__dy1_width": "540rpx",
    "__xz2box_hidden": true,
    "__dy2box_width": "540rpx",
    "__dy2_width": "540rpx",
    "__xz1box_height": "300rpx",
    "__wgd_height": "220rpx",
    "__wg_height": "160rpx",
    "__dy2_column": 3,
    "__dy2box_height": "300rpx",
    "__now_left": "20rpx",
    "__xz1box_width": "540rpx",
    "__dy1box_right": "0rpx",
    "__dy0_width": "540rpx",
    "__first_left": "20rpx",
    "__xz2box_right": "0rpx",
    "__wgd_left": "690rpx",
    "__xz2box_width": "540rpx",
    "__yinxiang_fontSize": "60rpx",
    "__xz0box_right": "0rpx",
    "__box1_height": "1200rpx",
    "__first_value": "",
    "__now_color": "white",
    "__auditing_box_height": "1333rpx",
    "__box_height": "1200rpx",
    "__now_top": "10rpx",
    "__dy1box_width": "540rpx",
    "__create_width": "750rpx",
    "__xz2box_left": "0rpx",
    "__create_hidden": true,
    "__xz2_column": 3,
    "__first_color": "white",
    "__now_width": "520rpx",
    "__dy1_data": "",
    "__wgd_background": "rgba(238,238,238,0.4)",
    "__xz0_height": "300rpx",
    "__box_hidden": true,
    "__xz1_height": "300rpx",
    "__yinxiang_left": "0rpx"
},
    onGetUserInfo_RS8mMr:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.commit', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onInputChange_bYBOJA:  function(evt) {
                var self = this;
                
            self.setData({
                __now_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_filjuK:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.wga', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, {});
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
    onButtonTap_7LyZ3m:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.hyp1', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onInputChange_O44E5v:  function(evt) {
                var self = this;
                
            self.setData({
                __first_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_GabUZR:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.dy', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_BRRcme:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.create', evt);
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
    onButtonTap_TLhf03:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.hyp0', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_qLW7gp:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx1: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.xz', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx777413533a93b0cf`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onButtonTap_LHoXZG:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.dy', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_qWrcMx:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx1: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.xz', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_jy8AfD:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.xyt', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_fnFPmP:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                yx1: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page1.xz', evt);
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
                        this.data.__share_page = 'page1'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx777413533a93b0cf", "page1", self, {});
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