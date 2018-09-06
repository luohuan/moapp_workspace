const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onButtonTap_gUfPBS:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            moapp.showAlert(`温馨提示:`, `只有主人能看哦~`);
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_zD2AHr:  function(evt) {
                var self = this;
                
            self.setData({
                __rest_guests_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_vCuyYw:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!true && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onInputChange_XPGid0:  function(evt) {
                var self = this;
                
            self.setData({
                __input_host_name_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_NyZXU2:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                state: "host",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'changeName', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_tqfcMp:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                state: "host",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'changeName', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_7wSB6e:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
    onImageTap_5vC0sg:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.banner2Tap', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onButtonTap_p2lHpX:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                guest_openid: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.showDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_8f8jNQ:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提示:`,
                content: `查看全部好友的匹配详情（包括未来进入的好友），只需支付金额4.99元。`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                guest_openid: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.onPay', evt);
        }
        )
            
                    }else if(res.cancel) {
                        console.log('用户点击取消')
                        
                    }
                }
            })
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx08fe2b1ff0c169f2`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onButtonTap_nzqRfc:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请稍微等一下下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.gotoSharePage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_ehrjAj:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.commmitchangeName', evt);
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
    onImageTap_I8tELB:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.banner1Tap', evt);
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
    onGetUserInfo_c1mdJZ:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请耐心等待一下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.onCreateTap', evt);
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
    data: {
    "__change_name_mask_height": "100%",
    "__detail_num30_color": "#333333",
    "__detail_num31_height": "63rpx",
    "__loading_box_height": "1333rpx",
    "__wenan_top": "860rpx",
    "__createbutton_width": "360rpx",
    "__detail_score_left": "0rpx",
    "__match_detail_mask_width": "100%",
    "__detail_score_right": "0rpx",
    "__w2_fontSize": "36rpx",
    "__createbutton_fontWeight": "bolder",
    "__num13_text": "6",
    "__detail_num00_fontSize": "30rpx",
    "__detail_num01_left": "152rpx",
    "__detail_w3_top": "268rpx",
    "__num14_width": "63rpx",
    "__num23_color": "#333333",
    "__num01_left": "152rpx",
    "__sharebutton1_fontWeight": "bolder",
    "__num31_text": "8",
    "__detail_w0_fontSize": "36rpx",
    "__text3_top": "40rpx",
    "__detail_num14_top": "419rpx",
    "__guest_name_button_height": "40rpx",
    "__detail_num12_height": "63rpx",
    "__num10_width": "63rpx",
    "__guest_avatar_left": "464rpx",
    "__detail_num31_width": "63rpx",
    "__sample_box_left": "0rpx",
    "__detail_num02_width": "63rpx",
    "__banner1_width": "750rpx",
    "__num01_color": "#3E4DD2",
    "__detail_num22_text": "8",
    "__detail_w2_top": "268rpx",
    "__banner1_hidden": true,
    "__detail_num30_text": "7",
    "__sharebutton1_width": "330rpx",
    "__detail_total_num_fontSize": "45rpx",
    "__num31_height": "63rpx",
    "__num23_text": "6",
    "__detail_total_num_right": "0rpx",
    "__detail_num01_text": "8",
    "__detail_host_avatar_left": "133rpx",
    "__host_name_height": "40rpx",
    "__score_color": "#F56E6E",
    "__num30_top": "593rpx",
    "__match_detail_mask_hidden": true,
    "__host_avatar_height": "80rpx",
    "__wenan_right": "0rpx",
    "__w4_top": "268rpx",
    "__num22_text": "8",
    "__detail_num21_fontSize": "30rpx",
    "__detail_w0_color": "#F56E6E",
    "__detail_num05_left": "579rpx",
    "__w3_color": "#3E4DD2",
    "__createbutton_color": "#3c3a59",
    "__detail_num04_fontSize": "30rpx",
    "__num23_top": "505rpx",
    "__banner2_hidden": true,
    "__detail_num11_left": "208rpx",
    "__w5_width": "63rpx",
    "__guest_name_top": "170rpx",
    "__num00_fontSize": "30rpx",
    "__num30_width": "63rpx",
    "__detail_num10_text": "4",
    "__loading_box_width": "750rpx",
    "__detail_num32_text": "6",
    "__host_name_button_color": "#F56E6E",
    "__num21_color": "#333333",
    "__num12_text": "8",
    "__detail_num05_top": "334rpx",
    "__banner2_left": "33rpx",
    "__button1_right": "0rpx",
    "__num04_left": "472rpx",
    "__w2_height": "63rpx",
    "__host_name_top": "170rpx",
    "__detail_num01_width": "63rpx",
    "__button1_top": "338rpx",
    "__banner2_top": "0rpx",
    "__num03_fontSize": "30rpx",
    "__detail_num41_fontSize": "30rpx",
    "__w2_top": "268rpx",
    "__button1_text": "\u63d0\u4ea4",
    "__guest_list_height": "1140rpx",
    "__createbutton_height": "78rpx",
    "__detail_num32_top": "593rpx",
    "__host_name_background": "rgba(0,0,0,0)",
    "__total_num_right": "0rpx",
    "__detail_num32_left": "421rpx",
    "__input_host_name_width": "480rpx",
    "__detail_num10_height": "63rpx",
    "__detail_num02_height": "63rpx",
    "__num05_top": "334rpx",
    "__num32_top": "593rpx",
    "__detail_num20_fontSize": "30rpx",
    "__detail_num10_left": "101rpx",
    "__detail_num14_height": "63rpx",
    "__w1_fontSize": "36rpx",
    "__detail_guest_avatar_height": "80rpx",
    "__num14_height": "63rpx",
    "__tip1_color": "white",
    "__detail_w4_left": "472rpx",
    "__detail_host_name_height": "90rpx",
    "__detail_num11_color": "#333333",
    "__num10_top": "419rpx",
    "__sharebutton1_text": "\u8ddf\u670b\u53cb\u5708\u597d\u53cb\u7b97",
    "__num14_color": "#333333",
    "__detail_num41_top": "679rpx",
    "__num14_top": "419rpx",
    "__match_box_background": "#383838",
    "__detail_num00_width": "63rpx",
    "__num12_width": "63rpx",
    "__num11_left": "208rpx",
    "__sharebutton1_bottom": "30rpx",
    "__num10_text": "4",
    "__detail_num20_height": "63rpx",
    "__detail_w4_height": "63rpx",
    "__input_host_name_top": "150rpx",
    "__detail_num02_color": "#F56E6E",
    "__guest_list_left": "33rpx",
    "__host_name_button_top": "170rpx",
    "__detail_w5_top": "268rpx",
    "__num10_fontSize": "30rpx",
    "__detail_w2_fontSize": "36rpx",
    "__w5_height": "63rpx",
    "__detail_num10_color": "#333333",
    "__button1_height": "78rpx",
    "__num05_text": "0",
    "__num03_height": "63rpx",
    "__host_avatar_left": "133rpx",
    "__host_name_left": "123rpx",
    "__detail_num03_text": "6",
    "__num00_text": "2",
    "__createbutton_fontSize": "30rpx",
    "__sample_box_hidden": true,
    "__detail_num12_text": "8",
    "__detail_num32_width": "63rpx",
    "__num11_color": "#333333",
    "__num21_text": "7",
    "__num23_left": "472rpx",
    "__guest_name_button_top": "170rpx",
    "__w0_top": "268rpx",
    "__detail_num04_width": "63rpx",
    "__detail_w3_height": "63rpx",
    "__detail_total_num_text": "87",
    "__page2image1_left": "0rpx",
    "__text3_fontSize": "40rpx",
    "__detail_num12_top": "419rpx",
    "__match_detail_mask_left": "0rpx",
    "__detail_w1_height": "63rpx",
    "__detail_score_color": "#F56E6E",
    "__detail_host_name_top": "170rpx",
    "__detail_w3_left": "364rpx",
    "__guest_list_hidden": true,
    "__num02_text": "4",
    "__w3_height": "63rpx",
    "__total_num_text": "87",
    "__host_name_disabled": "",
    "__detail_guest_avatar_left": "464rpx",
    "__w1_color": "#3E4DD2",
    "__num13_color": "#333333",
    "__sample_box_width": "750rpx",
    "__host_avatar_width": "80rpx",
    "__detail_num30_left": "206rpx",
    "__banner2_width": "686rpx",
    "__num22_height": "63rpx",
    "objects": [
        "banner1",
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
        "tip1",
        "tip2",
        "host_name_button",
        "guest_name_button",
        "wenan",
        "rest_guests",
        "banner2",
        "mad",
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
        "wenan2",
        "change_name_mask",
        "text3",
        "input_host_name",
        "button1",
        "loading_box"
    ],
    "__loading_box_top": "0rpx",
    "__num14_text": "0",
    "__score_top": "58rpx",
    "__detail_num00_color": "#F56E6E",
    "__detail_num11_text": "7",
    "__detail_w5_color": "#3E4DD2",
    "__detail_w1_left": "152rpx",
    "__detail_num31_top": "593rpx",
    "__detail_num00_height": "63rpx",
    "__button1_disabled": "",
    "__tip1_fontSize": "40rpx",
    "__sharebutton1_height": "78rpx",
    "__num05_left": "579rpx",
    "__detail_num04_height": "63rpx",
    "__w2_left": "259rpx",
    "__detail_num11_height": "63rpx",
    "__wenan_width": "600rpx",
    "__detail_num01_color": "#3E4DD2",
    "__button1_fontWeight": "bolder",
    "__text3_left": "0rpx",
    "__wenan2_background": "white",
    "__num03_width": "63rpx",
    "__num05_width": "63rpx",
    "__num00_top": "334rpx",
    "__total_num_color": "#F56E6E",
    "__banner2_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__num32_height": "63rpx",
    "__host_name_fontSize": "24rpx",
    "__num05_fontSize": "30rpx",
    "__detail_score_fontSize": "42rpx",
    "__num20_left": "152rpx",
    "__detail_w3_fontSize": "36rpx",
    "__wenan_fontSize": "27rpx",
    "__detail_w1_fontSize": "36rpx",
    "__detail_num03_color": "#3E4DD2",
    "__detail_num02_top": "334rpx",
    "__num31_width": "63rpx",
    "__num22_left": "366rpx",
    "__detail_guest_name_height": "90rpx",
    "__tip1_top": "420rpx",
    "__num02_height": "63rpx",
    "__createbutton_left": "195rpx",
    "__detail_num40_color": "#333333",
    "__num20_color": "#333333",
    "__detail_num41_left": "368rpx",
    "__detail_guest_name_width": "200rpx",
    "__num02_color": "#F56E6E",
    "__tip2_top": "520rpx",
    "__tip2_fontSize": "40rpx",
    "__detail_w1_width": "63rpx",
    "__num32_text": "6",
    "__detail_num00_left": "43rpx",
    "__detail_num21_width": "63rpx",
    "__tip1_right": "0rpx",
    "__detail_num13_fontSize": "30rpx",
    "__host_name_width": "100rpx",
    "__num23_width": "63rpx",
    "__banner2_height": "160rpx",
    "__detail_guest_avatar_src": "../../img/head2.jpg",
    "__num00_left": "43rpx",
    "__num03_color": "#3E4DD2",
    "__detail_num00_text": "2",
    "__detail_num03_width": "63rpx",
    "__num30_text": "7",
    "__detail_num20_left": "152rpx",
    "__detail_total_num_color": "#F56E6E",
    "__num21_fontSize": "30rpx",
    "__guest_name_button_width": "100rpx",
    "__num20_text": "4",
    "__detail_w4_fontSize": "36rpx",
    "__num02_width": "63rpx",
    "__num30_height": "63rpx",
    "__detail_num10_top": "419rpx",
    "__num41_height": "63rpx",
    "__detail_num23_left": "472rpx",
    "__detail_w2_color": "#F56E6E",
    "__change_name_mask_width": "100%",
    "__num02_top": "334rpx",
    "__num20_top": "505rpx",
    "__num22_color": "#333333",
    "__match_box_width": "750rpx",
    "__w4_left": "472rpx",
    "__num11_text": "7",
    "__detail_num14_text": "0",
    "__detail_num21_height": "63rpx",
    "__createbutton_text": "\u521b\u5efa\u6211\u7684",
    "__detail_num12_width": "63rpx",
    "__detail_guest_avatar_top": "79rpx",
    "__num40_width": "63rpx",
    "__detail_host_name_width": "200rpx",
    "__detail_w0_width": "63rpx",
    "__detail_num12_color": "#333333",
    "__detail_w0_left": "43rpx",
    "__change_name_mask_hidden": true,
    "__detail_num01_top": "334rpx",
    "__detail_num21_left": "261rpx",
    "__host_name_color": "#F56E6E",
    "__num12_height": "63rpx",
    "__detail_guest_name_top": "170rpx",
    "__host_name_button_hidden": true,
    "__num40_text": "8",
    "__mad_height": "92px",
    "__w3_width": "63rpx",
    "__input_host_name_value": "",
    "__num32_fontSize": "30rpx",
    "__detail_w2_width": "63rpx",
    "__score_fontSize": "42rpx",
    "__detail_host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__detail_num23_width": "63rpx",
    "__detail_num03_height": "63rpx",
    "__detail_host_name_color": "#F56E6E",
    "__detail_num41_color": "#333333",
    "__detail_num20_color": "#333333",
    "__guest_name_button_left": "454rpx",
    "__num13_height": "63rpx",
    "__num41_text": "7",
    "__num03_left": "364rpx",
    "__button1_width": "360rpx",
    "__wenan_left": "0rpx",
    "__num11_width": "63rpx",
    "__button1_fontSize": "36rpx",
    "__detail_num14_fontSize": "30rpx",
    "__page2image1_width": "750rpx",
    "__detail_num30_fontSize": "30rpx",
    "__detail_num02_left": "259rpx",
    "__input_host_name_color": "#F46060",
    "__num40_height": "63rpx",
    "__w1_height": "63rpx",
    "__detail_w3_width": "63rpx",
    "__detail_num41_height": "63rpx",
    "__w0_width": "63rpx",
    "__num04_height": "63rpx",
    "__guest_avatar_width": "80rpx",
    "__detail_w4_width": "63rpx",
    "__detail_num23_top": "505rpx",
    "__page2image1_height": "339rpx",
    "__num04_width": "63rpx",
    "__detail_num10_width": "63rpx",
    "__num41_color": "#333333",
    "__detail_num01_fontSize": "30rpx",
    "__detail_num22_top": "505rpx",
    "__num32_left": "421rpx",
    "__num03_text": "6",
    "__detail_w5_left": "579rpx",
    "__guest_avatar_height": "80rpx",
    "__detail_num04_text": "7",
    "__detail_num32_height": "63rpx",
    "__detail_score_top": "58rpx",
    "__detail_w1_top": "268rpx",
    "__change_name_mask_top": "0rpx",
    "__num00_width": "63rpx",
    "__num32_color": "#333333",
    "__detail_host_name_background": "rgba(0,0,0,0)",
    "__num41_width": "63rpx",
    "__sample_box_background": "#383838",
    "__detail_num30_width": "63rpx",
    "__num31_fontSize": "30rpx",
    "__guest_name_color": "#3E4DD2",
    "__total_num_top": "785rpx",
    "__text3_right": "0rpx",
    "__w1_top": "268rpx",
    "__num40_left": "262rpx",
    "__detail_num40_height": "63rpx",
    "__num23_fontSize": "30rpx",
    "__detail_num13_top": "419rpx",
    "__num21_top": "505rpx",
    "__detail_num32_fontSize": "30rpx",
    "__num31_color": "#333333",
    "__num20_fontSize": "30rpx",
    "__detail_guest_name_fontSize": "24rpx",
    "__num00_color": "#F56E6E",
    "__num13_left": "418rpx",
    "__guest_name_height": "40rpx",
    "__detail_num05_color": "#3E4DD2",
    "__detail_num22_width": "63rpx",
    "__detail_w3_color": "#3E4DD2",
    "__detail_num30_top": "593rpx",
    "__guest_name_button_color": "#3E4DD2",
    "__w2_width": "63rpx",
    "__sample_box_top": "0rpx",
    "__change_name_mask_left": "0rpx",
    "__host_name_hidden": true,
    "__page2image1_src": "../../img/bg3.jpg",
    "__rest_guests_data": "",
    "__num11_fontSize": "30rpx",
    "__detail_num30_height": "63rpx",
    "__num01_text": "8",
    "__detail_num22_height": "63rpx",
    "__detail_w0_height": "63rpx",
    "__detail_num20_text": "4",
    "__num04_text": "7",
    "__button1_left": "0rpx",
    "__num01_height": "63rpx",
    "__detail_host_avatar_width": "80rpx",
    "__page2image1_top": "0rpx",
    "__num10_height": "63rpx",
    "__w4_width": "63rpx",
    "__num20_width": "63rpx",
    "__sharebutton1_left": "380rpx",
    "__detail_host_avatar_height": "80rpx",
    "__detail_guest_name_left": "400rpx",
    "__match_detail_mask_top": "0rpx",
    "__detail_num21_text": "7",
    "__num04_top": "334rpx",
    "__w1_width": "63rpx",
    "__guest_name_width": "100rpx",
    "__num05_color": "#3E4DD2",
    "__detail_w0_top": "268rpx",
    "__detail_num03_fontSize": "30rpx",
    "__match_detail_mask_background": "RGBA(0, 0, 0, 0.7)",
    "__guest_name_hidden": true,
    "__num21_width": "63rpx",
    "__detail_num41_width": "63rpx",
    "__score_right": "0rpx",
    "__detail_num14_left": "518rpx",
    "__detail_num40_left": "262rpx",
    "__host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__w1_left": "152rpx",
    "__guest_name_fontSize": "24rpx",
    "__input_host_name_left": "0rpx",
    "__w4_height": "63rpx",
    "__detail_num13_text": "6",
    "__detail_num04_top": "334rpx",
    "__tip1_left": "0rpx",
    "__button1_background": "rgba(242,64,64,0.82)",
    "__num10_left": "101rpx",
    "__detail_num03_top": "334rpx",
    "__num03_top": "334rpx",
    "__num41_fontSize": "30rpx",
    "__detail_num41_text": "7",
    "__input_host_name_height": "80rpx",
    "__num01_top": "334rpx",
    "__detail_num31_text": "8",
    "__num30_left": "206rpx",
    "__detail_score_text": "87\u5206",
    "__detail_num23_height": "63rpx",
    "__num02_left": "259rpx",
    "__w5_fontSize": "36rpx",
    "__num01_width": "63rpx",
    "__num04_color": "#F56E6E",
    "__tip2_text": "\u70b9\u51fb\u5e95\u90e8\u6309\u94ae\u9080\u8bf7\u7ed9\u597d\u53cb\u5f00\u59cb\u8ba1\u7b97",
    "__num05_height": "63rpx",
    "__num21_height": "63rpx",
    "__detail_num05_text": "0",
    "__text3_text": "\u4fee\u6539\u4f60\u7684\u540d\u5b57:",
    "__num22_width": "63rpx",
    "__detail_num00_top": "334rpx",
    "__w0_color": "#F56E6E",
    "__detail_num04_color": "#F56E6E",
    "__num12_fontSize": "30rpx",
    "__input_host_name_background": "255 255 255 0.3",
    "__num13_top": "419rpx",
    "__detail_num10_fontSize": "30rpx",
    "__detail_num31_color": "#333333",
    "__detail_num13_width": "63rpx",
    "__w3_left": "364rpx",
    "__detail_num13_height": "63rpx",
    "__detail_num05_width": "63rpx",
    "__createbutton_disabled": "",
    "__sharebutton1_background": "rgba(242,64,64,0.82)",
    "__host_name_button_fontSize": "24rpx",
    "__detail_num32_color": "#333333",
    "__tip1_text": "\u6682\u65f6\u8fd8\u6ca1\u6709\u597d\u53cb\u6765\u8ddf\u4f60\u5339\u914d\u54e6~",
    "__detail_num14_width": "63rpx",
    "__detail_host_name_fontSize": "24rpx",
    "__detail_num13_left": "418rpx",
    "__guest_avatar_src": "../../img/head2.jpg",
    "__num22_fontSize": "30rpx",
    "__wenan2_top": "860rpx",
    "__detail_num05_height": "63rpx",
    "__detail_num02_text": "4",
    "__tip2_left": "0rpx",
    "__wenan2_left": "0rpx",
    "__num31_left": "313rpx",
    "__wenan2_width": "600rpx",
    "__match_box_hidden": false,
    "__w5_top": "268rpx",
    "__score_text": "87\u5206",
    "__num11_height": "63rpx",
    "__detail_num12_fontSize": "30rpx",
    "__num04_fontSize": "30rpx",
    "__mad_left": "33rpx",
    "__match_detail_mask_height": "100%",
    "__loading_box_left": "0rpx",
    "__tip2_color": "white",
    "__detail_num40_text": "8",
    "__sharebutton1_fontSize": "36rpx",
    "__score_left": "0rpx",
    "__num23_height": "63rpx",
    "__detail_num40_fontSize": "30rpx",
    "__detail_w2_height": "63rpx",
    "__num20_height": "63rpx",
    "__detail_num11_width": "63rpx",
    "__num40_top": "679rpx",
    "__guest_name_left": "454rpx",
    "__banner1_height": "155rpx",
    "__detail_num04_left": "472rpx",
    "__num12_top": "419rpx",
    "__detail_w2_left": "259rpx",
    "__detail_num23_color": "#333333",
    "__num41_left": "368rpx",
    "__detail_w5_width": "63rpx",
    "__num41_top": "679rpx",
    "__host_name_button_height": "40rpx",
    "__detail_num21_color": "#333333",
    "__num00_height": "63rpx",
    "__match_box_left": "0rpx",
    "__detail_num14_color": "#333333",
    "__detail_w1_color": "#3E4DD2",
    "__guest_name_button_hidden": true,
    "__banner1_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__detail_num31_left": "313rpx",
    "__total_num_left": "0rpx",
    "__wenan2_right": "0rpx",
    "__detail_num23_text": "6",
    "__num02_fontSize": "30rpx",
    "__num12_left": "313rpx",
    "__num12_color": "#333333",
    "__input_host_name_placeholder": "\u8bf7\u8f93\u5165\u4f60\u7684\u540d\u5b57",
    "__detail_num21_top": "505rpx",
    "__detail_w4_color": "#F56E6E",
    "__host_avatar_top": "79rpx",
    "__num10_color": "#333333",
    "__total_num_fontSize": "45rpx",
    "__w0_left": "43rpx",
    "__detail_num01_height": "63rpx",
    "__detail_num05_fontSize": "30rpx",
    "__host_name_button_width": "100rpx",
    "__detail_num31_fontSize": "30rpx",
    "__guest_list_width": "686rpx",
    "__tip2_right": "0rpx",
    "__w5_left": "579rpx",
    "__detail_w4_top": "268rpx",
    "__num30_color": "#333333",
    "__detail_host_name_disabled": "",
    "__num31_top": "593rpx",
    "__detail_host_avatar_top": "79rpx",
    "__detail_num22_left": "366rpx",
    "__detail_num22_fontSize": "30rpx",
    "__detail_guest_name_color": "#3E4DD2",
    "__num14_fontSize": "30rpx",
    "__num13_fontSize": "30rpx",
    "__createbutton_background": "rgba(255,206,48,0.9)",
    "__detail_num12_left": "313rpx",
    "__loading_box_background": "#383838",
    "__mad_width": "686rpx",
    "__w3_top": "268rpx",
    "__detail_w5_fontSize": "36rpx",
    "__wenan2_fontSize": "28rpx",
    "__num14_left": "518rpx",
    "__w4_color": "#F56E6E",
    "__w5_color": "#3E4DD2",
    "__mad_hidden": false,
    "__guest_name_button_fontSize": "24rpx",
    "__guest_list_top": "335rpx",
    "__change_name_mask_background": "RGBA(0, 0, 0, 0.7)",
    "__host_name_button_left": "123rpx",
    "__w3_fontSize": "36rpx",
    "__detail_num13_color": "#333333",
    "__num40_color": "#333333",
    "__num13_width": "63rpx",
    "__detail_num23_fontSize": "30rpx",
    "__detail_num02_fontSize": "30rpx",
    "__detail_host_name_left": "70rpx",
    "__detail_total_num_top": "785rpx",
    "__input_host_name_right": "0rpx",
    "__sharebutton1_color": "#FFFFFF",
    "__mad_top": "0rpx",
    "__button1_color": "#FFFFFF",
    "__guest_avatar_top": "79rpx",
    "__createbutton_bottom": "30rpx",
    "__detail_num40_width": "63rpx",
    "__detail_total_num_left": "0rpx",
    "__detail_num11_fontSize": "30rpx",
    "__w0_fontSize": "36rpx",
    "__detail_w5_height": "63rpx",
    "__w4_fontSize": "36rpx",
    "__detail_guest_avatar_width": "80rpx",
    "__w2_color": "#F56E6E",
    "__sharebutton1_disabled": "",
    "__num21_left": "261rpx",
    "__detail_num40_top": "679rpx",
    "__num32_width": "63rpx",
    "__match_box_top": "155rpx",
    "__num11_top": "419rpx",
    "__detail_num11_top": "419rpx",
    "__detail_num03_left": "364rpx",
    "__detail_num20_width": "63rpx",
    "__num40_fontSize": "30rpx",
    "__num30_fontSize": "30rpx",
    "__detail_num22_color": "#333333",
    "__text3_color": "#FFFFFF",
    "__detail_num20_top": "505rpx",
    "__num22_top": "505rpx",
    "__w0_height": "63rpx",
    "__wenan_background": "white",
    "__num01_fontSize": "30rpx"
},
    onButtonTap_NfoLnM:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                state: "guest",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'changeName', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_7Wfz7A:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                state: "guest",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'changeName', evt);
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, {});
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
    onImageTap_sWtkmO:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.deleteMask', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "match", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'main', 'match.onPullDownRefresh', evt);
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
})