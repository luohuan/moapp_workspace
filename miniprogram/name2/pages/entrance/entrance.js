const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onInputChange_y0lnEh:  function(evt) {
                var self = this;
                
            self.setData({
                __input_host_name_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_uLn7T5:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `作图中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.gotoSharePage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_zGQ7Ey:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `作图中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.onCreateTap', evt);
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, {});
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
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.onPullDownRefresh', evt);
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
    onViewTap_MMtdH5:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!false && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_xLdl7D:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.commitName', evt);
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
    onButtonTap_EFDGcG:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                guest_openid: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.showDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'entrance.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__host_name_top": "170rpx",
    "__text3_text": "\u5951\u5408\u5ea6\u6709\u51e0\u5206",
    "__detail_num13_fontSize": "30rpx",
    "__button1_fontSize": "36rpx",
    "__detail_w0_text": "\u90d1",
    "__num13_fontSize": "30rpx",
    "__detail_num12_top": "419rpx",
    "__num04_fontSize": "30rpx",
    "__detail_num30_top": "593rpx",
    "__detail_num32_color": "#333333",
    "__sharebutton1_fontSize": "36rpx",
    "__detail_guest_name_text": "\u674e\u70af",
    "__num10_height": "63rpx",
    "__num30_color": "#333333",
    "__num01_left": "152rpx",
    "__detail_num20_left": "152rpx",
    "__detail_num22_color": "#333333",
    "__guest_name_left": "400rpx",
    "__num40_top": "679rpx",
    "__detail_num00_text": "2",
    "__detail_host_name_top": "170rpx",
    "__detail_w2_color": "#F56E6E",
    "__guest_list_top": "335rpx",
    "__detail_w4_width": "63rpx",
    "__detail_guest_name_color": "#3E4DD2",
    "__w1_text": "\u674e",
    "__detail_w4_color": "#F56E6E",
    "__detail_num20_top": "505rpx",
    "__guest_name_color": "#3E4DD2",
    "__input_host_name_color": "#F46060",
    "__detail_num41_color": "#333333",
    "__detail_guest_name_top": "170rpx",
    "__button1_top": "938rpx",
    "__host_name_left": "70rpx",
    "__detail_num01_left": "152rpx",
    "__w1_left": "152rpx",
    "__detail_host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__detail_num13_height": "63rpx",
    "__w4_text": "\u71d5",
    "__num00_top": "334rpx",
    "__num32_width": "63rpx",
    "__button1_right": "0rpx",
    "__num41_left": "368rpx",
    "__match_detail_mask_width": "100%",
    "__detail_num23_height": "63rpx",
    "__xiangqing_disabled": "",
    "__w3_text": "\u70af",
    "__num04_color": "#F56E6E",
    "__detail_num23_top": "505rpx",
    "__detail_num11_fontSize": "30rpx",
    "__detail_w4_height": "63rpx",
    "__score_text": "87\u5206",
    "__num02_top": "334rpx",
    "__num22_top": "505rpx",
    "__detail_host_avatar_width": "80rpx",
    "__num21_width": "63rpx",
    "__detail_total_num_top": "785rpx",
    "__num00_fontSize": "30rpx",
    "__num22_left": "366rpx",
    "__detail_num20_height": "63rpx",
    "__detail_w3_height": "63rpx",
    "__detail_w2_height": "63rpx",
    "__w2_color": "#F56E6E",
    "__host_avatar_top": "79rpx",
    "__num01_top": "334rpx",
    "__num23_color": "#333333",
    "__button1_background": "rgba(242,64,64,0.82)",
    "__score_right": "0rpx",
    "__num23_width": "63rpx",
    "__num03_height": "63rpx",
    "__num20_height": "63rpx",
    "__host_name_fontSize": "24rpx",
    "__detail_num12_left": "313rpx",
    "__num30_height": "63rpx",
    "__num03_text": "6",
    "__text2_top": "450rpx",
    "__text1_text": "\u6bcf\u4e2a\u6c49\u5b57\u90fd\u6709\u81ea\u5df1\u7684\u70b9\u6570",
    "__xiangqing_color": "#D96363",
    "__num05_color": "#3E4DD2",
    "__createbutton_left": "195rpx",
    "__num14_left": "518rpx",
    "__rest_guests_top": "1330rpx",
    "__score_top": "58rpx",
    "__page2image1_width": "750rpx",
    "__button1_fontWeight": "bolder",
    "__detail_num21_width": "63rpx",
    "__detail_num01_width": "63rpx",
    "__detail_score_text": "87\u5206",
    "__guest_name_text": "\u674e\u70af",
    "__createbutton_fontWeight": "bolder",
    "__detail_num31_fontSize": "30rpx",
    "__detail_num41_height": "63rpx",
    "__w3_left": "364rpx",
    "__num41_height": "63rpx",
    "__w4_width": "63rpx",
    "__detail_num41_top": "679rpx",
    "__page2image1_src": "../../img/bg3.jpg",
    "__w2_left": "259rpx",
    "__detail_w3_width": "63rpx",
    "__match_detail_mask_background": "RGBA(0, 0, 0, 0.7)",
    "__detail_num40_color": "#333333",
    "__detail_num03_color": "#3E4DD2",
    "__detail_host_name_text": "\u90d1\u7ea2\u71d5",
    "__num02_color": "#F56E6E",
    "__detail_guest_name_height": "90rpx",
    "__input_name_box_width": "750rpx",
    "__num12_fontSize": "30rpx",
    "__num21_height": "63rpx",
    "__num13_text": "6",
    "__num12_height": "63rpx",
    "__detail_num05_height": "63rpx",
    "__detail_w5_width": "63rpx",
    "__w4_top": "268rpx",
    "__detail_num00_top": "334rpx",
    "__detail_num02_top": "334rpx",
    "__detail_num30_fontSize": "30rpx",
    "__detail_num03_top": "334rpx",
    "__input_host_name_right": "0rpx",
    "__w0_text": "\u90d1",
    "__match_detail_mask_hidden": true,
    "__num03_top": "334rpx",
    "__detail_w1_fontSize": "36rpx",
    "__createbutton_bottom": "30rpx",
    "__text1_left": "0rpx",
    "__detail_num04_fontSize": "30rpx",
    "__detail_guest_avatar_width": "80rpx",
    "__detail_w4_text": "\u71d5",
    "__createbutton_color": "#FFFFFF",
    "__sharebutton1_left": "195rpx",
    "__detail_total_num_width": "63rpx",
    "__detail_num14_left": "518rpx",
    "__text2_right": "0rpx",
    "__detail_num11_top": "419rpx",
    "__total_num_height": "63rpx",
    "__w2_width": "63rpx",
    "__detail_num40_text": "8",
    "__detail_num02_color": "#F56E6E",
    "__input_name_box_top": "0rpx",
    "__num13_left": "418rpx",
    "__host_name_color": "#F56E6E",
    "__w4_height": "63rpx",
    "__button1_height": "78rpx",
    "__detail_num01_top": "334rpx",
    "__total_num_width": "63rpx",
    "__image1_src": "../../img/bg2.jpg",
    "__detail_w3_text": "\u70af",
    "__detail_num12_height": "63rpx",
    "__num14_color": "#333333",
    "__detail_num00_height": "63rpx",
    "__input_host_name_left": "0rpx",
    "__detail_num02_fontSize": "30rpx",
    "__detail_num05_text": "0",
    "__num05_height": "63rpx",
    "__num22_color": "#333333",
    "__w1_color": "#3E4DD2",
    "__sample_box_left": "0rpx",
    "__w0_top": "268rpx",
    "__sharebutton1_background": "rgba(242,64,64,0.82)",
    "__detail_w2_fontSize": "36rpx",
    "__detail_num05_color": "#3E4DD2",
    "__num23_text": "6",
    "__detail_num10_fontSize": "30rpx",
    "__detail_score_color": "#F56E6E",
    "__detail_num01_fontSize": "30rpx",
    "__w0_color": "#F56E6E",
    "__detail_num22_height": "63rpx",
    "__num30_top": "593rpx",
    "__detail_w2_left": "259rpx",
    "__text2_left": "0rpx",
    "__detail_w0_fontSize": "36rpx",
    "__page2image1_left": "0rpx",
    "__total_num_text": "87",
    "__loading_box_left": "0rpx",
    "__detail_w4_left": "472rpx",
    "__detail_num21_left": "261rpx",
    "__match_box_width": "750rpx",
    "__detail_num05_left": "579rpx",
    "__num05_left": "579rpx",
    "__detail_num20_color": "#333333",
    "__detail_host_avatar_height": "80rpx",
    "__match_detail_mask_height": "100%",
    "__detail_num10_width": "63rpx",
    "__detail_num32_height": "63rpx",
    "__detail_num31_text": "8",
    "__detail_w5_top": "268rpx",
    "__sharebutton1_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b",
    "__guest_name_height": "90rpx",
    "__detail_num03_fontSize": "30rpx",
    "__detail_num40_height": "63rpx",
    "__num13_top": "419rpx",
    "__detail_w1_height": "63rpx",
    "__sample_box_width": "750rpx",
    "__sharebutton1_fontWeight": "bolder",
    "__detail_w5_text": "\u2764",
    "__detail_num31_width": "63rpx",
    "__detail_num40_top": "679rpx",
    "__num14_top": "419rpx",
    "__num32_height": "63rpx",
    "__num32_text": "6",
    "__detail_num31_top": "593rpx",
    "__detail_total_num_fontSize": "45rpx",
    "__num04_width": "63rpx",
    "__num32_fontSize": "30rpx",
    "__detail_num21_text": "7",
    "__detail_num23_text": "6",
    "__detail_num03_width": "63rpx",
    "__detail_num10_height": "63rpx",
    "__detail_w4_top": "268rpx",
    "__num40_width": "63rpx",
    "__createbutton_disabled": "",
    "__num20_left": "152rpx",
    "__w2_text": "\u7ea2",
    "__w0_left": "43rpx",
    "__sharebutton1_disabled": "",
    "__num22_width": "63rpx",
    "__guest_list_width": "686rpx",
    "__detail_num20_fontSize": "30rpx",
    "__detail_host_avatar_left": "133rpx",
    "__num40_left": "262rpx",
    "__xiangqing_height": "45rpx",
    "__detail_guest_avatar_left": "464rpx",
    "__detail_num22_width": "63rpx",
    "__match_detail_mask_top": "0rpx",
    "__detail_num14_fontSize": "30rpx",
    "__createbutton_text": "\u521b\u5efa\u6211\u7684",
    "__num30_width": "63rpx",
    "__num14_width": "63rpx",
    "__host_name_height": "90rpx",
    "__score_fontSize": "42rpx",
    "__num10_color": "#333333",
    "__sharebutton1_bottom": "30rpx",
    "__detail_num11_height": "63rpx",
    "__image1_left": "0rpx",
    "__detail_num23_fontSize": "30rpx",
    "__num11_left": "208rpx",
    "__num04_left": "472rpx",
    "__guest_list_left": "33rpx",
    "__loading_box_top": "0rpx",
    "__detail_num32_left": "421rpx",
    "__num23_top": "505rpx",
    "__detail_num14_text": "0",
    "__num20_top": "505rpx",
    "__detail_num03_height": "63rpx",
    "__detail_num22_fontSize": "30rpx",
    "__detail_guest_avatar_src": "../../img/head2.jpg",
    "__host_name_width": "200rpx",
    "__guest_name_top": "170rpx",
    "__num41_color": "#333333",
    "__xiangqing_text": "\u67e5\u770b\u8be6\u60c5",
    "__num31_color": "#333333",
    "__num01_width": "63rpx",
    "__detail_num04_text": "7",
    "__detail_total_num_left": "318rpx",
    "__num12_color": "#333333",
    "__num41_fontSize": "30rpx",
    "__num20_text": "4",
    "__detail_guest_name_width": "200rpx",
    "__num21_fontSize": "30rpx",
    "__createbutton_width": "360rpx",
    "__detail_num23_width": "63rpx",
    "__detail_num10_text": "4",
    "__detail_num13_color": "#333333",
    "__detail_num11_left": "208rpx",
    "__num11_color": "#333333",
    "__detail_w2_top": "268rpx",
    "__button1_text": "\u63d0\u4ea4",
    "__guest_list_hidden": true,
    "__num11_text": "7",
    "__detail_score_fontSize": "42rpx",
    "__num20_fontSize": "30rpx",
    "__w0_fontSize": "36rpx",
    "__detail_guest_name_left": "400rpx",
    "__num11_width": "63rpx",
    "__host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__num13_color": "#333333",
    "__detail_w0_top": "268rpx",
    "__button1_disabled": "",
    "__detail_num01_height": "63rpx",
    "__score_left": "0rpx",
    "__w3_width": "63rpx",
    "__w5_fontSize": "36rpx",
    "__w5_left": "579rpx",
    "__total_num_left": "318rpx",
    "__w3_color": "#3E4DD2",
    "__xiangqing_fontSize": "22rpx",
    "__num01_height": "63rpx",
    "__num04_height": "63rpx",
    "__w2_top": "268rpx",
    "__detail_num41_left": "368rpx",
    "__detail_num10_top": "419rpx",
    "__num05_text": "0",
    "__detail_num05_fontSize": "30rpx",
    "__detail_num13_top": "419rpx",
    "__w3_top": "268rpx",
    "__detail_num20_width": "63rpx",
    "__num30_text": "7",
    "__detail_w0_color": "#F56E6E",
    "__detail_num30_text": "7",
    "__total_num_top": "785rpx",
    "__num00_color": "#F56E6E",
    "__detail_num01_color": "#3E4DD2",
    "__num20_color": "#333333",
    "__detail_num13_left": "418rpx",
    "__detail_num31_height": "63rpx",
    "__num22_height": "63rpx",
    "__num04_text": "7",
    "__text1_top": "400rpx",
    "__w4_left": "472rpx",
    "__num01_color": "#3E4DD2",
    "__detail_num11_width": "63rpx",
    "__num10_fontSize": "30rpx",
    "__num23_left": "472rpx",
    "__detail_num02_width": "63rpx",
    "__detail_w3_left": "364rpx",
    "__num31_width": "63rpx",
    "__input_host_name_background": "255 255 255 0.3",
    "__detail_w3_top": "268rpx",
    "__num40_color": "#333333",
    "__text3_color": "#FFFFFF",
    "__text1_fontSize": "24rpx",
    "__num22_text": "8",
    "__detail_guest_avatar_top": "79rpx",
    "__w1_height": "63rpx",
    "__page2image1_top": "0rpx",
    "__num10_left": "101rpx",
    "__num03_left": "364rpx",
    "__detail_num41_fontSize": "30rpx",
    "__detail_num02_height": "63rpx",
    "__sample_box_top": "0rpx",
    "__num10_top": "419rpx",
    "__w0_width": "63rpx",
    "__detail_w4_fontSize": "36rpx",
    "__detail_num04_width": "63rpx",
    "__createbutton_height": "78rpx",
    "__detail_num23_left": "472rpx",
    "__guest_avatar_width": "80rpx",
    "__detail_w2_width": "63rpx",
    "__num31_fontSize": "30rpx",
    "__detail_num32_fontSize": "30rpx",
    "__detail_num23_color": "#333333",
    "__detail_w5_fontSize": "36rpx",
    "__detail_num14_height": "63rpx",
    "__text3_left": "0rpx",
    "__num01_text": "8",
    "__detail_num31_color": "#333333",
    "__guest_avatar_left": "464rpx",
    "__sharebutton1_width": "360rpx",
    "__detail_num40_left": "262rpx",
    "__num40_fontSize": "30rpx",
    "__detail_num11_color": "#333333",
    "__host_avatar_width": "80rpx",
    "__num11_fontSize": "30rpx",
    "__match_detail_mask_left": "0rpx",
    "__num30_left": "206rpx",
    "__num00_height": "63rpx",
    "__text2_text": "\u7b97\u4e00\u7b97\u597d\u53cb\u8ddf\u4f60",
    "__xiangqing_fontWeight": "bolder",
    "__detail_num10_color": "#333333",
    "__num32_left": "421rpx",
    "__detail_num32_width": "63rpx",
    "__detail_w0_left": "43rpx",
    "__button1_width": "360rpx",
    "__guest_avatar_height": "80rpx",
    "__detail_guest_name_fontSize": "24rpx",
    "__input_host_name_width": "480rpx",
    "__score_color": "#F56E6E",
    "__w3_height": "63rpx",
    "__detail_num40_width": "63rpx",
    "__detail_w3_fontSize": "36rpx",
    "__detail_num14_top": "419rpx",
    "__detail_num41_text": "7",
    "__xiangqing_left": "558rpx",
    "__w2_fontSize": "36rpx",
    "__num02_width": "63rpx",
    "__detail_num04_color": "#F56E6E",
    "__w5_text": "\u2764",
    "__num03_width": "63rpx",
    "__detail_w1_top": "268rpx",
    "__num14_text": "0",
    "__num32_top": "593rpx",
    "__detail_num02_text": "4",
    "__detail_w1_left": "152rpx",
    "__host_avatar_height": "80rpx",
    "__text3_fontSize": "24rpx",
    "__input_host_name_height": "80rpx",
    "__rest_guests_left": "0rpx",
    "__detail_w2_text": "\u7ea2",
    "__match_box_hidden": true,
    "__detail_num03_text": "6",
    "__detail_num22_text": "8",
    "__detail_w1_text": "\u674e",
    "__num05_width": "63rpx",
    "__detail_num12_text": "8",
    "__detail_num11_text": "7",
    "__num00_width": "63rpx",
    "__num41_width": "63rpx",
    "__input_host_name_value": "",
    "__text3_right": "0rpx",
    "__num00_text": "2",
    "__detail_num41_width": "63rpx",
    "__detail_total_num_height": "63rpx",
    "__num13_width": "63rpx",
    "__detail_num20_text": "4",
    "__num14_fontSize": "30rpx",
    "__w2_height": "63rpx",
    "__detail_host_name_left": "70rpx",
    "__detail_w5_left": "579rpx",
    "__num23_height": "63rpx",
    "__input_host_name_top": "600rpx",
    "__num12_width": "63rpx",
    "__detail_total_num_color": "#F56E6E",
    "__num40_text": "8",
    "__text3_top": "500rpx",
    "__text2_fontSize": "24rpx",
    "__num30_fontSize": "30rpx",
    "__num03_color": "#3E4DD2",
    "__num05_top": "334rpx",
    "__detail_num30_width": "63rpx",
    "__num05_fontSize": "30rpx",
    "__w4_color": "#F56E6E",
    "__w5_height": "63rpx",
    "__detail_num21_height": "63rpx",
    "__num10_width": "63rpx",
    "__guest_avatar_top": "79rpx",
    "__w0_height": "63rpx",
    "__num12_top": "419rpx",
    "__detail_num30_height": "63rpx",
    "__detail_w0_width": "63rpx",
    "__detail_num05_top": "334rpx",
    "__num04_top": "334rpx",
    "__num10_text": "4",
    "__num21_top": "505rpx",
    "__image1_height": "1325rpx",
    "__w4_fontSize": "36rpx",
    "__num02_height": "63rpx",
    "__num31_top": "593rpx",
    "objects": [
        "input_name_box",
        "image1",
        "text1",
        "text2",
        "text3",
        "input_host_name",
        "button1",
        "sample_box",
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
        "match_box",
        "rest_guests",
        "xiangqing",
        "createbutton",
        "match_detail_mask",
        "detail_host_avatar",
        "detail_guest_avatar",
        "detail_score",
        "detail_host_name",
        "detail_guest_name",
        "detail_w0",
        "detail_w1",
        "detail_w2",
        "detail_w3",
        "detail_w4",
        "detail_w5",
        "detail_num00",
        "detail_num01",
        "detail_num02",
        "detail_num03",
        "detail_num04",
        "detail_num05",
        "detail_num10",
        "detail_num11",
        "detail_num12",
        "detail_num13",
        "detail_num14",
        "detail_num20",
        "detail_num21",
        "detail_num22",
        "detail_num23",
        "detail_num30",
        "detail_num31",
        "detail_num32",
        "detail_num40",
        "detail_num41",
        "detail_total_num",
        "loading_box"
    ],
    "__detail_num00_fontSize": "30rpx",
    "__num22_fontSize": "30rpx",
    "__num02_fontSize": "30rpx",
    "__xiangqing_background": "#FFFFFF",
    "__num02_left": "259rpx",
    "__total_num_fontSize": "45rpx",
    "__num21_text": "7",
    "__text1_color": "#FFFFFF",
    "__detail_num13_width": "63rpx",
    "__detail_num21_color": "#333333",
    "__num11_top": "419rpx",
    "__detail_num14_width": "63rpx",
    "__detail_num12_width": "63rpx",
    "__detail_score_top": "58rpx",
    "__match_box_left": "0rpx",
    "__num12_left": "313rpx",
    "__num12_text": "8",
    "__num02_text": "4",
    "__guest_list_height": "940rpx",
    "__num40_height": "63rpx",
    "__detail_num04_left": "472rpx",
    "__loading_box_width": "750rpx",
    "__detail_guest_avatar_height": "80rpx",
    "__guest_name_width": "200rpx",
    "__num03_fontSize": "30rpx",
    "__detail_w1_color": "#3E4DD2",
    "__num14_height": "63rpx",
    "__guest_avatar_src": "../../img/head2.jpg",
    "__detail_num32_top": "593rpx",
    "__detail_num01_text": "8",
    "__detail_num10_left": "101rpx",
    "__rest_guests_data": "",
    "__num31_left": "313rpx",
    "__detail_num21_top": "505rpx",
    "__detail_num04_top": "334rpx",
    "__w1_width": "63rpx",
    "__num13_height": "63rpx",
    "__detail_num05_width": "63rpx",
    "__detail_num30_color": "#333333",
    "__sharebutton1_height": "78rpx",
    "__button1_left": "0rpx",
    "__num01_fontSize": "30rpx",
    "__detail_w3_color": "#3E4DD2",
    "__text2_color": "#FFFFFF",
    "__detail_num21_fontSize": "30rpx",
    "__w1_top": "268rpx",
    "__w3_fontSize": "36rpx",
    "__detail_host_name_width": "200rpx",
    "__input_host_name_placeholder": "\u8bf7\u8f93\u5165\u4f60\u7684\u540d\u5b57",
    "__total_num_color": "#F56E6E",
    "__host_name_text": "\u90d1\u7ea2\u71d5",
    "__num32_color": "#333333",
    "__xiangqing_width": "102rpx",
    "__w5_top": "268rpx",
    "__num41_text": "7",
    "__detail_num22_left": "366rpx",
    "__sample_box_hidden": true,
    "__w5_color": "#3E4DD2",
    "__image1_top": "-40rpx",
    "__detail_w0_height": "63rpx",
    "__detail_num04_height": "63rpx",
    "__createbutton_fontSize": "36rpx",
    "__detail_num03_left": "364rpx",
    "__page2image1_height": "339rpx",
    "__detail_num32_text": "6",
    "__detail_num12_fontSize": "30rpx",
    "__detail_num13_text": "6",
    "__num20_width": "63rpx",
    "__detail_num40_fontSize": "30rpx",
    "__detail_num02_left": "259rpx",
    "__detail_score_right": "0rpx",
    "__detail_num12_color": "#333333",
    "__createbutton_background": "rgba(242,64,64,0.82)",
    "__num11_height": "63rpx",
    "__detail_host_avatar_top": "79rpx",
    "__detail_num00_color": "#F56E6E",
    "__detail_num14_color": "#333333",
    "__detail_host_name_height": "90rpx",
    "__input_name_box_left": "0rpx",
    "__detail_w5_color": "#3E4DD2",
    "__num23_fontSize": "30rpx",
    "__input_name_box_hidden": true,
    "__guest_name_fontSize": "24rpx",
    "__detail_score_left": "0rpx",
    "__w5_width": "63rpx",
    "__detail_num22_top": "505rpx",
    "__detail_num30_left": "206rpx",
    "__detail_w5_height": "63rpx",
    "__xiangqing_top": "50rpx",
    "__image1_width": "750rpx",
    "__text1_right": "0rpx",
    "__num31_height": "63rpx",
    "__sharebutton1_color": "#FFFFFF",
    "__match_box_top": "0rpx",
    "__w1_fontSize": "36rpx",
    "__detail_host_name_fontSize": "24rpx",
    "__detail_num00_left": "43rpx",
    "__detail_num00_width": "63rpx",
    "__button1_color": "#FFFFFF",
    "__num31_text": "8",
    "__num21_color": "#333333",
    "__detail_host_name_color": "#F56E6E",
    "__num21_left": "261rpx",
    "__detail_total_num_text": "87",
    "__detail_w1_width": "63rpx",
    "__num41_top": "679rpx",
    "__num00_left": "43rpx",
    "__host_avatar_left": "133rpx",
    "__detail_num31_left": "313rpx"
},
    onViewTap_0RpoHq:  function(evt) {
                var self = this;
                
            self.setData({
                __rest_guests_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "entrance", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
})