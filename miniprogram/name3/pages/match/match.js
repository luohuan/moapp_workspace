const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onViewTap_QpsTFi:  function(evt) {
                var self = this;
                
            self.setData({
                __rest_guests_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_Jzjxro:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                guest_openid: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'match.showDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, {});
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
    "__detail_num14_color": "#333333",
    "__detail_w5_width": "63rpx",
    "__w2_color": "#F56E6E",
    "__detail_num31_top": "593rpx",
    "__num03_text": "6",
    "__score_color": "#F56E6E",
    "__tip1_top": "420rpx",
    "__detail_num30_height": "63rpx",
    "__num10_height": "63rpx",
    "__detail_num30_width": "63rpx",
    "__num23_height": "63rpx",
    "__detail_num20_height": "63rpx",
    "__detail_w4_height": "63rpx",
    "__num05_color": "#3E4DD2",
    "__sharebutton1_width": "360rpx",
    "__detail_w3_text": "\u70af",
    "__num40_height": "63rpx",
    "__detail_num00_color": "#F56E6E",
    "__detail_num04_height": "63rpx",
    "__detail_num23_color": "#333333",
    "__detail_total_num_fontSize": "45rpx",
    "__guest_avatar_left": "464rpx",
    "__host_name_color": "#F56E6E",
    "__num22_fontSize": "30rpx",
    "__detail_num12_left": "313rpx",
    "__host_name_width": "200rpx",
    "__num21_color": "#333333",
    "__detail_num03_fontSize": "30rpx",
    "__guest_list_height": "940rpx",
    "__num21_top": "505rpx",
    "__detail_w5_fontSize": "36rpx",
    "__guest_name_text": "\u674e\u70af",
    "__w2_left": "259rpx",
    "__w4_color": "#F56E6E",
    "__w2_top": "268rpx",
    "__detail_num01_top": "334rpx",
    "__w2_width": "63rpx",
    "__total_num_fontSize": "45rpx",
    "__num01_height": "63rpx",
    "__num14_width": "63rpx",
    "__detail_num20_left": "152rpx",
    "__detail_num13_width": "63rpx",
    "__detail_score_fontSize": "42rpx",
    "__num02_left": "259rpx",
    "__detail_score_top": "58rpx",
    "__num13_color": "#333333",
    "__num40_color": "#333333",
    "__w4_top": "268rpx",
    "__detail_num12_height": "63rpx",
    "__num12_width": "63rpx",
    "__createbutton_left": "195rpx",
    "__detail_num13_top": "419rpx",
    "__detail_num02_height": "63rpx",
    "__num01_fontSize": "30rpx",
    "__detail_num10_text": "4",
    "__detail_num05_color": "#3E4DD2",
    "__num22_top": "505rpx",
    "__num32_color": "#333333",
    "__tip2_text": "\u70b9\u51fb\u5e95\u90e8\u6309\u94ae\u9080\u8bf7\u597d\u53cb\u6765\u6d4b",
    "__num14_left": "518rpx",
    "__num41_color": "#333333",
    "__w3_color": "#3E4DD2",
    "__w3_left": "364rpx",
    "__detail_total_num_left": "318rpx",
    "__detail_num10_color": "#333333",
    "__host_name_top": "170rpx",
    "__detail_num32_text": "6",
    "__detail_w5_height": "63rpx",
    "__w1_top": "268rpx",
    "__page2image1_top": "0rpx",
    "__match_box_hidden": true,
    "__detail_num32_left": "421rpx",
    "__num23_top": "505rpx",
    "__num11_width": "63rpx",
    "__detail_num05_text": "0",
    "__detail_num32_fontSize": "30rpx",
    "__detail_num23_top": "505rpx",
    "objects": [
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
    "__w0_fontSize": "36rpx",
    "__w3_height": "63rpx",
    "__detail_num21_width": "63rpx",
    "__w5_color": "#3E4DD2",
    "__match_detail_mask_left": "0rpx",
    "__num41_top": "679rpx",
    "__detail_num04_fontSize": "30rpx",
    "__detail_num14_top": "419rpx",
    "__detail_w1_fontSize": "36rpx",
    "__detail_num10_width": "63rpx",
    "__guest_name_width": "200rpx",
    "__detail_num32_color": "#333333",
    "__detail_num01_height": "63rpx",
    "__num13_height": "63rpx",
    "__match_box_background": "#383838",
    "__num30_text": "7",
    "__match_detail_mask_height": "100%",
    "__page2image1_height": "339rpx",
    "__detail_num12_text": "8",
    "__host_avatar_height": "80rpx",
    "__num40_text": "8",
    "__detail_num22_text": "8",
    "__detail_num31_text": "8",
    "__rest_guests_data": "",
    "__detail_w0_top": "268rpx",
    "__detail_score_color": "#F56E6E",
    "__detail_num01_color": "#3E4DD2",
    "__total_num_top": "785rpx",
    "__num11_height": "63rpx",
    "__w5_width": "63rpx",
    "__detail_w0_width": "63rpx",
    "__match_detail_mask_width": "100%",
    "__host_avatar_left": "133rpx",
    "__detail_num23_height": "63rpx",
    "__detail_num20_top": "505rpx",
    "__detail_w4_color": "#F56E6E",
    "__num04_color": "#F56E6E",
    "__detail_total_num_width": "63rpx",
    "__xiangqing_disabled": "",
    "__num12_left": "313rpx",
    "__detail_num14_height": "63rpx",
    "__detail_w2_fontSize": "36rpx",
    "__num41_text": "7",
    "__detail_num40_text": "8",
    "__tip1_left": "0rpx",
    "__createbutton_background": "rgba(242,64,64,0.82)",
    "__xiangqing_text": "\u67e5\u770b\u8be6\u60c5",
    "__num13_left": "418rpx",
    "__num03_top": "334rpx",
    "__loading_box_top": "0rpx",
    "__num30_width": "63rpx",
    "__xiangqing_color": "#D96363",
    "__num05_fontSize": "30rpx",
    "__detail_num11_fontSize": "30rpx",
    "__detail_num04_text": "7",
    "__match_box_top": "0rpx",
    "__createbutton_fontSize": "36rpx",
    "__detail_w3_width": "63rpx",
    "__num32_width": "63rpx",
    "__detail_num21_top": "505rpx",
    "__detail_num31_color": "#333333",
    "__guest_list_left": "33rpx",
    "__detail_num40_top": "679rpx",
    "__num22_text": "8",
    "__w5_text": "\u2764",
    "__detail_num00_left": "43rpx",
    "__num30_left": "206rpx",
    "__num30_color": "#333333",
    "__detail_num03_height": "63rpx",
    "__detail_host_name_fontSize": "24rpx",
    "__num30_top": "593rpx",
    "__detail_num40_color": "#333333",
    "__detail_num12_top": "419rpx",
    "__num10_width": "63rpx",
    "__detail_num10_fontSize": "30rpx",
    "__tip1_right": "0rpx",
    "__tip2_fontSize": "40rpx",
    "__detail_num01_fontSize": "30rpx",
    "__detail_num30_fontSize": "30rpx",
    "__detail_w1_color": "#3E4DD2",
    "__detail_num13_left": "418rpx",
    "__w4_width": "63rpx",
    "__detail_num20_fontSize": "30rpx",
    "__detail_num30_text": "7",
    "__num14_height": "63rpx",
    "__num13_width": "63rpx",
    "__num30_height": "63rpx",
    "__detail_w4_text": "\u71d5",
    "__num05_width": "63rpx",
    "__detail_num01_text": "8",
    "__detail_w5_top": "268rpx",
    "__sample_box_background": "#383838",
    "__num21_width": "63rpx",
    "__num22_height": "63rpx",
    "__detail_num21_text": "7",
    "__num00_text": "2",
    "__tip2_color": "white",
    "__num40_top": "679rpx",
    "__detail_num13_fontSize": "30rpx",
    "__num12_fontSize": "30rpx",
    "__detail_num00_width": "63rpx",
    "__guest_name_height": "90rpx",
    "__num22_width": "63rpx",
    "__w1_width": "63rpx",
    "__sharebutton1_fontWeight": "bolder",
    "__detail_num12_width": "63rpx",
    "__sample_box_hidden": true,
    "__detail_num04_color": "#F56E6E",
    "__xiangqing_top": "50rpx",
    "__guest_list_top": "335rpx",
    "__detail_num14_left": "518rpx",
    "__w5_height": "63rpx",
    "__total_num_height": "63rpx",
    "__detail_num23_left": "472rpx",
    "__detail_w5_text": "\u2764",
    "__num14_color": "#333333",
    "__host_avatar_top": "79rpx",
    "__num01_width": "63rpx",
    "__num23_text": "6",
    "__detail_host_avatar_top": "79rpx",
    "__detail_num02_top": "334rpx",
    "__num40_fontSize": "30rpx",
    "__detail_num13_color": "#333333",
    "__num04_fontSize": "30rpx",
    "__detail_num21_color": "#333333",
    "__num00_width": "63rpx",
    "__detail_num30_color": "#333333",
    "__detail_num05_left": "579rpx",
    "__detail_w2_text": "\u7ea2",
    "__sharebutton1_background": "rgba(242,64,64,0.82)",
    "__num41_height": "63rpx",
    "__detail_num02_fontSize": "30rpx",
    "__num04_text": "7",
    "__num40_width": "63rpx",
    "__num21_left": "261rpx",
    "__createbutton_bottom": "30rpx",
    "__num10_fontSize": "30rpx",
    "__detail_guest_name_fontSize": "24rpx",
    "__num41_width": "63rpx",
    "__num40_left": "262rpx",
    "__detail_host_avatar_height": "80rpx",
    "__detail_w3_color": "#3E4DD2",
    "__detail_num03_text": "6",
    "__detail_host_name_top": "170rpx",
    "__detail_num31_height": "63rpx",
    "__w0_width": "63rpx",
    "__tip1_fontSize": "40rpx",
    "__detail_num40_width": "63rpx",
    "__detail_num11_width": "63rpx",
    "__detail_num03_top": "334rpx",
    "__xiangqing_background": "#FFFFFF",
    "__detail_num00_top": "334rpx",
    "__num31_left": "313rpx",
    "__detail_num32_top": "593rpx",
    "__sharebutton1_fontSize": "36rpx",
    "__num20_width": "63rpx",
    "__detail_num41_left": "368rpx",
    "__w0_height": "63rpx",
    "__detail_w2_height": "63rpx",
    "__num31_fontSize": "30rpx",
    "__num04_left": "472rpx",
    "__match_box_width": "750rpx",
    "__sharebutton1_color": "#FFFFFF",
    "__w4_text": "\u71d5",
    "__w5_top": "268rpx",
    "__createbutton_fontWeight": "bolder",
    "__detail_num13_text": "6",
    "__detail_num22_top": "505rpx",
    "__detail_w5_color": "#3E4DD2",
    "__match_detail_mask_hidden": true,
    "__detail_num12_fontSize": "30rpx",
    "__detail_num11_text": "7",
    "__createbutton_width": "360rpx",
    "__detail_num32_height": "63rpx",
    "__guest_name_left": "400rpx",
    "__sample_box_width": "750rpx",
    "__num02_color": "#F56E6E",
    "__xiangqing_fontWeight": "bolder",
    "__num05_left": "579rpx",
    "__detail_w1_height": "63rpx",
    "__detail_w0_color": "#F56E6E",
    "__w1_height": "63rpx",
    "__score_text": "87\u5206",
    "__num20_left": "152rpx",
    "__num00_height": "63rpx",
    "__detail_guest_name_text": "\u674e\u70af",
    "__num02_fontSize": "30rpx",
    "__num31_width": "63rpx",
    "__num32_top": "593rpx",
    "__createbutton_text": "\u521b\u5efa\u6211\u7684",
    "__host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__createbutton_disabled": "",
    "__detail_num32_width": "63rpx",
    "__num04_width": "63rpx",
    "__detail_guest_name_width": "200rpx",
    "__detail_w2_top": "268rpx",
    "__detail_host_name_color": "#F56E6E",
    "__num11_color": "#333333",
    "__num32_fontSize": "30rpx",
    "__num14_fontSize": "30rpx",
    "__guest_list_width": "686rpx",
    "__detail_num20_text": "4",
    "__sample_box_left": "0rpx",
    "__detail_num00_fontSize": "30rpx",
    "__num14_top": "419rpx",
    "__num12_top": "419rpx",
    "__detail_num20_width": "63rpx",
    "__num02_text": "4",
    "__w2_text": "\u7ea2",
    "__score_top": "58rpx",
    "__num04_height": "63rpx",
    "__detail_num22_height": "63rpx",
    "__score_fontSize": "42rpx",
    "__detail_num02_color": "#F56E6E",
    "__detail_w0_text": "\u90d1",
    "__num01_text": "8",
    "__num00_top": "334rpx",
    "__detail_num05_height": "63rpx",
    "__num00_fontSize": "30rpx",
    "__match_detail_mask_top": "0rpx",
    "__detail_num00_text": "2",
    "__num10_top": "419rpx",
    "__guest_avatar_top": "79rpx",
    "__detail_num12_color": "#333333",
    "__detail_num20_color": "#333333",
    "__w1_text": "\u674e",
    "__detail_guest_name_height": "90rpx",
    "__num12_color": "#333333",
    "__detail_num23_fontSize": "30rpx",
    "__num23_left": "472rpx",
    "__detail_num04_left": "472rpx",
    "__detail_num14_text": "0",
    "__detail_host_name_text": "\u90d1\u7ea2\u71d5",
    "__detail_score_text": "87\u5206",
    "__w5_fontSize": "36rpx",
    "__num02_top": "334rpx",
    "__num10_text": "4",
    "__num32_left": "421rpx",
    "__detail_total_num_top": "785rpx",
    "__num05_text": "0",
    "__detail_num13_height": "63rpx",
    "__detail_num11_color": "#333333",
    "__tip2_right": "0rpx",
    "__num01_left": "152rpx",
    "__num23_color": "#333333",
    "__detail_num05_width": "63rpx",
    "__detail_num04_width": "63rpx",
    "__num03_fontSize": "30rpx",
    "__w5_left": "579rpx",
    "__match_box_left": "0rpx",
    "__detail_w5_left": "579rpx",
    "__num10_left": "101rpx",
    "__detail_w1_top": "268rpx",
    "__guest_avatar_src": "../../img/head2.jpg",
    "__w0_top": "268rpx",
    "__detail_w3_fontSize": "36rpx",
    "__num22_left": "366rpx",
    "__sharebutton1_bottom": "30rpx",
    "__host_name_height": "90rpx",
    "__detail_num04_top": "334rpx",
    "__num12_text": "8",
    "__detail_num41_top": "679rpx",
    "__detail_num10_top": "419rpx",
    "__detail_total_num_height": "63rpx",
    "__num20_color": "#333333",
    "__tip1_color": "white",
    "__detail_num02_left": "259rpx",
    "__num22_color": "#333333",
    "__detail_num41_fontSize": "30rpx",
    "__detail_w1_left": "152rpx",
    "__detail_w1_width": "63rpx",
    "__detail_w3_height": "63rpx",
    "__w2_height": "63rpx",
    "__detail_num31_left": "313rpx",
    "__guest_list_hidden": true,
    "__score_left": "300rpx",
    "__num32_text": "6",
    "__guest_avatar_width": "80rpx",
    "__detail_w3_left": "364rpx",
    "__detail_num10_left": "101rpx",
    "__detail_score_left": "300rpx",
    "__detail_num02_width": "63rpx",
    "__detail_num00_height": "63rpx",
    "__num11_top": "419rpx",
    "__xiangqing_left": "558rpx",
    "__xiangqing_fontSize": "22rpx",
    "__detail_w3_top": "268rpx",
    "__detail_num21_fontSize": "30rpx",
    "__detail_num03_color": "#3E4DD2",
    "__host_name_text": "\u90d1\u7ea2\u71d5",
    "__sharebutton1_disabled": "",
    "__sample_box_top": "0rpx",
    "__detail_num30_left": "206rpx",
    "__detail_num22_fontSize": "30rpx",
    "__sharebutton1_height": "78rpx",
    "__detail_num22_color": "#333333",
    "__detail_w0_fontSize": "36rpx",
    "__w3_fontSize": "36rpx",
    "__createbutton_color": "#FFFFFF",
    "__detail_num40_height": "63rpx",
    "__num03_height": "63rpx",
    "__num13_fontSize": "30rpx",
    "__loading_box_width": "750rpx",
    "__detail_guest_avatar_top": "79rpx",
    "__host_name_fontSize": "24rpx",
    "__detail_guest_name_top": "170rpx",
    "__detail_num01_width": "63rpx",
    "__detail_num05_fontSize": "30rpx",
    "__w0_left": "43rpx",
    "__num03_left": "364rpx",
    "__sharebutton1_left": "195rpx",
    "__detail_num41_text": "7",
    "__detail_num22_left": "366rpx",
    "__w4_fontSize": "36rpx",
    "__detail_num02_text": "4",
    "__num20_fontSize": "30rpx",
    "__detail_w0_height": "63rpx",
    "__num03_width": "63rpx",
    "__loading_box_left": "0rpx",
    "__num31_height": "63rpx",
    "__num13_top": "419rpx",
    "__detail_w1_text": "\u674e",
    "__detail_num01_left": "152rpx",
    "__detail_num31_width": "63rpx",
    "__num20_text": "4",
    "__total_num_text": "87",
    "__xiangqing_height": "45rpx",
    "__detail_guest_avatar_width": "80rpx",
    "__page2image1_width": "750rpx",
    "__w4_height": "63rpx",
    "__w0_color": "#F56E6E",
    "__num00_color": "#F56E6E",
    "__num41_left": "368rpx",
    "__host_avatar_width": "80rpx",
    "__detail_host_name_left": "70rpx",
    "__detail_num22_width": "63rpx",
    "__num23_width": "63rpx",
    "__w2_fontSize": "36rpx",
    "__w1_left": "152rpx",
    "__detail_guest_avatar_height": "80rpx",
    "__detail_num03_width": "63rpx",
    "__detail_w0_left": "43rpx",
    "__detail_num05_top": "334rpx",
    "__num11_left": "208rpx",
    "__detail_num21_height": "63rpx",
    "__tip1_text": "\u6682\u65f6\u8fd8\u6ca1\u6709\u597d\u53cb\u6765\u8ddf\u4f60\u5339\u914d\u5594",
    "__detail_host_avatar_src": "http://material.motimaster.com/appmaker/lijiong/2315.png",
    "__num02_width": "63rpx",
    "__total_num_width": "63rpx",
    "__num05_height": "63rpx",
    "__detail_num41_color": "#333333",
    "__num04_top": "334rpx",
    "__detail_w4_top": "268rpx",
    "__num41_fontSize": "30rpx",
    "__detail_host_name_width": "200rpx",
    "__num01_top": "334rpx",
    "__w3_width": "63rpx",
    "__detail_num11_left": "208rpx",
    "__guest_name_top": "170rpx",
    "__detail_num11_height": "63rpx",
    "__detail_host_avatar_width": "80rpx",
    "__detail_w2_color": "#F56E6E",
    "__detail_num23_text": "6",
    "__detail_num21_left": "261rpx",
    "__w1_fontSize": "36rpx",
    "__detail_guest_name_color": "#3E4DD2",
    "__num03_color": "#3E4DD2",
    "__detail_num23_width": "63rpx",
    "__tip2_top": "520rpx",
    "__xiangqing_width": "102rpx",
    "__detail_num14_width": "63rpx",
    "__num12_height": "63rpx",
    "__w0_text": "\u90d1",
    "__detail_num40_fontSize": "30rpx",
    "__tip2_left": "0rpx",
    "__detail_num41_width": "63rpx",
    "__detail_guest_name_left": "400rpx",
    "__detail_num31_fontSize": "30rpx",
    "__num31_text": "8",
    "__guest_name_fontSize": "24rpx",
    "__num05_top": "334rpx",
    "__num00_left": "43rpx",
    "__num31_color": "#333333",
    "__detail_total_num_color": "#F56E6E",
    "__detail_num40_left": "262rpx",
    "__num11_text": "7",
    "__detail_num14_fontSize": "30rpx",
    "__detail_host_avatar_left": "133rpx",
    "__detail_num03_left": "364rpx",
    "__num10_color": "#333333",
    "__detail_num11_top": "419rpx",
    "__num21_text": "7",
    "__guest_name_color": "#3E4DD2",
    "__detail_num30_top": "593rpx",
    "__detail_w4_fontSize": "36rpx",
    "__num20_top": "505rpx",
    "__num30_fontSize": "30rpx",
    "__createbutton_height": "78rpx",
    "__w3_top": "268rpx",
    "__page2image1_src": "../../img/bg3.jpg",
    "__num13_text": "6",
    "__detail_guest_avatar_src": "../../img/head2.jpg",
    "__detail_guest_avatar_left": "464rpx",
    "__w4_left": "472rpx",
    "__num21_fontSize": "30rpx",
    "__num32_height": "63rpx",
    "__w3_text": "\u70af",
    "__detail_host_name_height": "90rpx",
    "__host_name_left": "70rpx",
    "__num14_text": "0",
    "__total_num_left": "318rpx",
    "__total_num_color": "#F56E6E",
    "__detail_w2_width": "63rpx",
    "__detail_num41_height": "63rpx",
    "__detail_w2_left": "259rpx",
    "__num31_top": "593rpx",
    "__detail_w4_width": "63rpx",
    "__w1_color": "#3E4DD2",
    "__detail_w4_left": "472rpx",
    "__num20_height": "63rpx",
    "__page2image1_left": "0rpx",
    "__num11_fontSize": "30rpx",
    "__match_detail_mask_background": "RGBA(0, 0, 0, 0.7)",
    "__num02_height": "63rpx",
    "__guest_avatar_height": "80rpx",
    "__num23_fontSize": "30rpx",
    "__num01_color": "#3E4DD2",
    "__detail_num10_height": "63rpx",
    "__sharebutton1_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b",
    "__num21_height": "63rpx",
    "__detail_total_num_text": "87"
},
    onViewTap_ktTDG9:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
    formIdHandler: function (e) {
                        var appid= `wx01434b3ed0010d28`
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, {});
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
    onGetUserInfo_Qci2iy:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `作图中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'match.onCreateTap', evt);
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
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'match.onPullDownRefresh', evt);
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
    onButtonTap_sa0DpH:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `作图中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'match.gotoSharePage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx01434b3ed0010d28", "match", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx01434b3ed0010d28', 'main', 'match.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
})