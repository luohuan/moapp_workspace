const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    data: {
    "__guest_list_top": "340rpx",
    "__guest_avatar_width": "80rpx",
    "__text1_color": "#FFFFFF",
    "__num21_height": "63rpx",
    "__num41_height": "63rpx",
    "__w0_text": "\u90d1",
    "__score_left": "0rpx",
    "__num20_color": "#333333",
    "__host_avatar_top": "79rpx",
    "__total_num_width": "63rpx",
    "__text1_text": "\u6bcf\u4e2a\u6c49\u5b57\u90fd\u6709\u81ea\u5df1\u7684\u70b9\u6570",
    "__num30_top": "593rpx",
    "__button1_left": "0rpx",
    "__text1_left": "0rpx",
    "__w5_color": "#3E4DD2",
    "__num12_text": "8",
    "__text2_left": "0rpx",
    "__sharebutton1_disabled": "",
    "__w2_fontSize": "36rpx",
    "__text1_top": "400rpx",
    "__guest_list_hidden": true,
    "__button1_background": "rgba(242,64,64,0.82)",
    "__w1_top": "268rpx",
    "__score_top": "58rpx",
    "__num13_top": "419rpx",
    "__sharebutton1_bottom": "30rpx",
    "__image1_top": "-40rpx",
    "__total_num_left": "318rpx",
    "__w1_color": "#3E4DD2",
    "__num10_width": "63rpx",
    "__num00_fontSize": "30rpx",
    "__num13_left": "418rpx",
    "__button1_width": "360rpx",
    "__input_host_name_top": "600rpx",
    "__num41_width": "63rpx",
    "__w4_color": "#F56E6E",
    "__score_color": "#F56E6E",
    "__num11_width": "63rpx",
    "__w3_height": "63rpx",
    "__text1_right": "0rpx",
    "__num23_color": "#333333",
    "__w1_fontSize": "36rpx",
    "__num05_color": "#3E4DD2",
    "__button1_fontWeight": "bolder",
    "__w1_left": "152rpx",
    "__button1_height": "78rpx",
    "__num31_height": "63rpx",
    "__num41_top": "679rpx",
    "__image1_height": "1325rpx",
    "__num04_top": "334rpx",
    "__w4_left": "472rpx",
    "__num04_width": "63rpx",
    "__num21_fontSize": "30rpx",
    "__guest_list_left": "33rpx",
    "__total_num_height": "63rpx",
    "__box2_hidden": true,
    "__num04_text": "7",
    "__num41_fontSize": "30rpx",
    "__num40_text": "8",
    "__num02_text": "4",
    "__guest_avatar_src": "../../img/head2.jpg",
    "__button1_fontSize": "36rpx",
    "__input_host_name_placeholder": "\u8bf7\u8f93\u5165\u4f60\u7684\u540d\u5b57",
    "__num22_height": "63rpx",
    "__input_host_name_value": "",
    "__num14_height": "63rpx",
    "__host_avatar_height": "80rpx",
    "__num14_top": "419rpx",
    "__num11_text": "7",
    "__guest_list_height": "950rpx",
    "__num04_left": "472rpx",
    "__num14_width": "63rpx",
    "__w3_fontSize": "36rpx",
    "__num03_top": "334rpx",
    "__score_fontSize": "42rpx",
    "__num10_fontSize": "30rpx",
    "__sharebutton1_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b",
    "__num02_left": "259rpx",
    "objects": [
        "box1",
        "image1",
        "text1",
        "text2",
        "text3",
        "input_host_name",
        "button1",
        "box2",
        "page2image1",
        "guest_list",
        "host_avatar",
        "guest_avatar",
        "score",
        "host_name",
        "guest_name",
        "w0",
        "w1",
        "w2",
        "w3",
        "w4",
        "w5",
        "num00",
        "num01",
        "num02",
        "num03",
        "num04",
        "num05",
        "num10",
        "num11",
        "num12",
        "num13",
        "num14",
        "num20",
        "num21",
        "num22",
        "num23",
        "num30",
        "num31",
        "num32",
        "num40",
        "num41",
        "total_num",
        "sharebutton1",
        "loading"
    ],
    "__num23_text": "6",
    "__num02_fontSize": "30rpx",
    "__text3_top": "500rpx",
    "__num03_height": "63rpx",
    "__guest_name_text": "\u674e\u70af",
    "__w2_top": "268rpx",
    "__sharebutton1_height": "78rpx",
    "__total_num_text": "87",
    "__input_host_name_background": "255 255 255 0.3",
    "__num05_fontSize": "30rpx",
    "__w3_width": "63rpx",
    "__num02_height": "63rpx",
    "__w3_top": "268rpx",
    "__num21_left": "261rpx",
    "__num30_height": "63rpx",
    "__num23_left": "472rpx",
    "__num31_width": "63rpx",
    "__num30_left": "206rpx",
    "__w0_color": "#F56E6E",
    "__num21_text": "7",
    "__num01_left": "152rpx",
    "__host_avatar_left": "133rpx",
    "__box1_left": "0rpx",
    "__num04_color": "#F56E6E",
    "__num32_left": "421rpx",
    "__button1_text": "\u63d0\u4ea4",
    "__loading_top": "0rpx",
    "__w3_left": "364rpx",
    "__num00_text": "2",
    "__guest_name_fontSize": "24rpx",
    "__box2_width": "750rpx",
    "__num20_left": "152rpx",
    "__num21_top": "505rpx",
    "__num41_left": "368rpx",
    "__w0_width": "63rpx",
    "__text3_fontSize": "24rpx",
    "__button1_disabled": "",
    "__sharebutton1_fontSize": "36rpx",
    "__input_host_name_right": "0rpx",
    "__page2image1_height": "339rpx",
    "__button1_top": "938rpx",
    "__num10_height": "63rpx",
    "__num00_height": "63rpx",
    "__total_num_fontSize": "45rpx",
    "__guest_avatar_left": "464rpx",
    "__num32_color": "#333333",
    "__button1_color": "#FFFFFF",
    "__guest_avatar_height": "80rpx",
    "__num12_fontSize": "30rpx",
    "__num03_color": "#3E4DD2",
    "__num22_left": "366rpx",
    "__page2image1_src": "../../img/bg3.jpg",
    "__num20_height": "63rpx",
    "__num13_height": "63rpx",
    "__text2_fontSize": "24rpx",
    "__num22_width": "63rpx",
    "__score_right": "0rpx",
    "__guest_name_width": "200rpx",
    "__num11_top": "419rpx",
    "__w2_text": "\u7ea2",
    "__num00_left": "43rpx",
    "__w3_color": "#3E4DD2",
    "__num23_top": "505rpx",
    "__num32_fontSize": "30rpx",
    "__total_num_top": "785rpx",
    "__num32_height": "63rpx",
    "__num11_fontSize": "30rpx",
    "__num11_height": "63rpx",
    "__num03_fontSize": "30rpx",
    "__num01_top": "334rpx",
    "__text3_text": "\u5951\u5408\u5ea6\u6709\u51e0\u5206",
    "__guest_name_left": "400rpx",
    "__num05_width": "63rpx",
    "__input_host_name_color": "#F46060",
    "__num00_color": "#F56E6E",
    "__w5_height": "63rpx",
    "__num10_left": "101rpx",
    "__button1_right": "0rpx",
    "__num11_left": "208rpx",
    "__w4_width": "63rpx",
    "__text1_fontSize": "24rpx",
    "__w4_height": "63rpx",
    "__box2_left": "0rpx",
    "__num22_text": "8",
    "__num32_width": "63rpx",
    "__host_name_color": "#F56E6E",
    "__num31_fontSize": "30rpx",
    "__w5_text": "\u2764",
    "__num32_top": "593rpx",
    "__num14_fontSize": "30rpx",
    "__num40_height": "63rpx",
    "__loading_left": "0rpx",
    "__loading_width": "750rpx",
    "__w0_fontSize": "36rpx",
    "__num05_text": "0",
    "__host_name_height": "90rpx",
    "__num12_width": "63rpx",
    "__num22_top": "505rpx",
    "__num12_top": "419rpx",
    "__text3_color": "#FFFFFF",
    "__num12_height": "63rpx",
    "__image1_width": "750rpx",
    "__num21_color": "#333333",
    "__num10_text": "4",
    "__host_name_left": "70rpx",
    "__num41_color": "#333333",
    "__input_host_name_left": "0rpx",
    "__num40_left": "262rpx",
    "__num13_text": "6",
    "__box1_hidden": true,
    "__w5_width": "63rpx",
    "__host_name_top": "170rpx",
    "__num22_color": "#333333",
    "__num30_fontSize": "30rpx",
    "__num01_width": "63rpx",
    "__num12_left": "313rpx",
    "__host_name_width": "200rpx",
    "__sharebutton1_width": "360rpx",
    "__w1_text": "\u674e",
    "__num04_fontSize": "30rpx",
    "__num20_fontSize": "30rpx",
    "__image1_src": "../../img/bg2.jpg",
    "__sharebutton1_left": "195rpx",
    "__text2_top": "450rpx",
    "__num20_width": "63rpx",
    "__num04_height": "63rpx",
    "__sharebutton1_fontWeight": "bolder",
    "__num01_fontSize": "30rpx",
    "__num13_width": "63rpx",
    "__text3_left": "0rpx",
    "__num05_height": "63rpx",
    "__w2_left": "259rpx",
    "__guest_name_color": "#3E4DD2",
    "__w3_text": "\u70af",
    "__page2image1_left": "0rpx",
    "__w5_left": "579rpx",
    "__score_text": "87\u5206",
    "__w4_fontSize": "36rpx",
    "__num12_color": "#333333",
    "__num01_text": "8",
    "__num14_left": "518rpx",
    "__num32_text": "6",
    "__text2_text": "\u7b97\u4e00\u7b97\u597d\u53cb\u8ddf\u4f60",
    "__num02_top": "334rpx",
    "__guest_avatar_top": "79rpx",
    "__num23_height": "63rpx",
    "__num41_text": "7",
    "__image1_left": "0rpx",
    "__num13_color": "#333333",
    "__guest_list_width": "686rpx",
    "__num05_top": "334rpx",
    "__num00_width": "63rpx",
    "__w1_width": "63rpx",
    "__host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__text2_right": "0rpx",
    "__input_host_name_width": "480rpx",
    "__box1_top": "0rpx",
    "__w0_height": "63rpx",
    "__num30_color": "#333333",
    "__num31_left": "313rpx",
    "__guest_name_top": "170rpx",
    "__host_avatar_width": "80rpx",
    "__num14_text": "0",
    "__w4_text": "\u71d5",
    "__page2image1_width": "750rpx",
    "__num01_color": "#3E4DD2",
    "__num03_width": "63rpx",
    "__num14_color": "#333333",
    "__num21_width": "63rpx",
    "__w5_fontSize": "36rpx",
    "__num10_top": "419rpx",
    "__w0_top": "268rpx",
    "__box1_width": "750rpx",
    "__num20_top": "505rpx",
    "__sharebutton1_color": "#FFFFFF",
    "__num40_fontSize": "30rpx",
    "__page2image1_top": "0rpx",
    "__sharebutton1_background": "rgba(242,64,64,0.82)",
    "__num31_top": "593rpx",
    "__num30_text": "7",
    "__num05_left": "579rpx",
    "__host_name_fontSize": "24rpx",
    "__w2_height": "63rpx",
    "__num03_text": "6",
    "__num40_top": "679rpx",
    "__w5_top": "268rpx",
    "__num11_color": "#333333",
    "__num20_text": "4",
    "__num01_height": "63rpx",
    "__w2_color": "#F56E6E",
    "__box2_top": "0rpx",
    "__num31_text": "8",
    "__w4_top": "268rpx",
    "__num10_color": "#333333",
    "__num30_width": "63rpx",
    "__num23_width": "63rpx",
    "__num02_color": "#F56E6E",
    "__num22_fontSize": "30rpx",
    "__text2_color": "#FFFFFF",
    "__num00_top": "334rpx",
    "__num23_fontSize": "30rpx",
    "__input_host_name_height": "80rpx",
    "__host_name_text": "\u90d1\u7ea2\u71d5",
    "__num40_color": "#333333",
    "__w0_left": "43rpx",
    "__text3_right": "0rpx",
    "__w2_width": "63rpx",
    "__num13_fontSize": "30rpx",
    "__num31_color": "#333333",
    "__num03_left": "364rpx",
    "__num40_width": "63rpx",
    "__guest_name_height": "90rpx",
    "__w1_height": "63rpx",
    "__num02_width": "63rpx",
    "__total_num_color": "#F56E6E"
},
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_5MTCpW:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'create2.go_create2', evt);
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
    onButtonTap_1rcHUM:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `作图中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'create2.gotoCreate3', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onInputChange_dGtsjE:  function(evt) {
                var self = this;
                
            self.setData({
                __input_host_name_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, {});
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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "create2", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'create2.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})