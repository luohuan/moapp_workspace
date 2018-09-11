const app = getApp();
const moapp = require("../../utils/moapp.js"); 

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
                        this.data.__share_page = 'indexPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            //console.log(res);
                            console.log(`/pages/${self.data.__share_page}/${self.data.__share_page}?`+options)
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, {});
                            Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onShareSuccessed', evt);
            }
            )
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, {});
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

                    console.log(`share page info:
/pages/${self.data.__share_page}/${self.data.__share_page}?`+options);

                    return shareInfo;                
                },
    onButtonTap_ZbnO2Q:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请稍微等一下下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onPayAll', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    itemtap_BEdsoP:  function(evt) {
                var self = this;
                
            self.setData({
                __danmu_value: evt.detail.value
            })
            
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.barrageItemTap', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_jczmCy:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                select_id: "text1",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onSelectTag', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onViewTap_qv4Llc:  function(evt) {
                var self = this;
                
            self.setData({
                __showboxes_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    itemtap_OK2vk4:  function(evt) {
                var self = this;
                
            self.setData({
                __danmu_value: evt.detail.value
            })
            
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.barrageItemTap', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    data: {
    "__result_text_list_top": "0rpx",
    "__danmu_danmuHeadImageStyle": "",
    "__result_box_width": "750rpx",
    "__selected_text1_color": "white",
    "__input2_placeholder": "\u8bf7\u9009\u62e9\u6216\u5728\u8fd9\u91cc\u8f93\u5165\u4f60\u7684\u7b54\u6848",
    "__go_share_btn_width": "402rpx",
    "__selected_text1_width": "296rpx",
    "__mask_width": "100%",
    "__btn_result_box_bottom": "0rpx",
    "__btn_change_height": "50rpx",
    "__selected_text4_width": "280rpx",
    "__danmu_danmuStyle": "",
    "__selected_text3_fontSize": "26rpx",
    "__no_result_box_top": "0rpx",
    "__avatar_box_top": "0rpx",
    "__host_box_height": "100%",
    "__resultText_scrollTop": "",
    "__resultText_scrollLeft": "",
    "__resultText_top": "400rpx",
    "__showText_right": "0rpx",
    "__btn_result_box_left": "0rpx",
    "__bigger_text_width": "550rpx",
    "__im_list_scrollTop": "",
    "__pay_box_hidden": true,
    "__btn_result_box_disabled": "",
    "__input2_value": "",
    "__go_share_btn_hidden": false,
    "__host_avatar_right": "0rpx",
    "__host_avatar_src": "",
    "__host_avatar_width": "160rpx",
    "__danmu_danmuFontSize": 32,
    "__selected_text4_fontSize": "26rpx",
    "__empty_height": "100rpx",
    "__guest_box_width": "750rpx",
    "__guest_box_height": "100%",
    "__btn_result_box_height": "100rpx",
    "__btn_create_im_width": "750rpx",
    "__result_box_hidden": true,
    "__pay_one_disabled": "",
    "__pay_all_background": "#7dcdad",
    "__btn_change_width": "50rpx",
    "__selected_text1_top": "0rpx",
    "__btn_ok_fontSize": "30rpx",
    "__go_share_btn_top": "800rpx",
    "__pay_all_top": "300rpx",
    "__no_result_box_width": "750rpx",
    "__bigger_text_color": "white",
    "__go_share_btn_right": "0rpx",
    "__pay_one_background": "#ec866e",
    "__selected_text2_color": "white",
    "__guest_box_hidden": true,
    "__input_box_height": "240rpx",
    "__text_shareGuide_height": "100rpx",
    "__im_list_top": "40rpx",
    "__result_box_left": "0rpx",
    "__pay_all_width": "214rpx",
    "__mask_background": "RGBA(0, 0, 0, 0.7)",
    "__im_list_hidden": true,
    "__selected_text4_left": "244rpx",
    "__empty_hidden": false,
    "__im_list_left": "0rpx",
    "__result_box_top": "0rpx",
    "__host_box_width": "100%",
    "__go_share_btn_height": "90rpx",
    "__danmu_danmuTeadImage": "",
    "__empty_fontSize": "30rpx",
    "__bigger_box_top": "300rpx",
    "__pay_box_height": "400rpx",
    "__btn_create_im_disabled": "",
    "__showText_height": "630rpx",
    "__im_list_scrollLeft": "",
    "__bigger_text_height": "200rpx",
    "__btn_change_left": "650rpx",
    "__danmu_danmuHeight": 120,
    "__pay_all_text": "\u00a59.9\u67e5\u770b\u5168\u90e8",
    "__pay_box_width": "670rpx",
    "__pay_one_fontSize": "30rpx",
    "__input_box_width": "700rpx",
    "__btn_ok_text": "\u53d1\u5c04\ud83d\udc97",
    "__pay_all_height": "74rpx",
    "__bigger_text_top": "10rpx",
    "__bigger_text_left": "0rpx",
    "__bigger_box_width": "600rpx",
    "__danmu_value": "",
    "__guest_box_left": "0rpx",
    "__mask_left": "0rpx",
    "__selected_text1_left": "0rpx",
    "__img_src": "http://material.motimaster.com/suyu1536458821000/\u661f\u7a7a2.png",
    "__empty_text": "\u5176\u4ed6\u4eba\u8fd8\u6ca1\u6709\u56de\u7b54\u54e6 \u4f60\u6765\u505a\u7b2c\u4e00\u4e2a\u5427",
    "__guest_box_top": "0rpx",
    "__host_avatar_height": "160rpx",
    "__go_share_btn_left": "0rpx",
    "__input2_width": "529rpx",
    "__host_box_left": "0rpx",
    "__input2_height": "50rpx",
    "__result_text_list_data": "",
    "__btn_ok_width": "120rpx",
    "__danmu_danmuLineHeight": 120,
    "__input_box_top": "850rpx",
    "__img_top": "0rpx",
    "__text_shareGuide_background": "rgba(255, 255, 255,0.3)",
    "__pay_all_color": "#000000",
    "__selected_text4_color": "white",
    "__btn_ok_height": "50rpx",
    "__resultText_right": "0rpx",
    "__pay_box_right": "0rpx",
    "__showboxes_left": "0rpx",
    "__selected_text3_height": "60rpx",
    "__empty_top": "400rpx",
    "__selected_text3_color": "white",
    "__pay_one_height": "74rpx",
    "__selected_text1_height": "60rpx",
    "__btn_create_im_left": "0rpx",
    "__result_text_list_left": "0rpx",
    "__showboxes_top": "0rpx",
    "__bigger_text_fontSize": "40rpx",
    "__mask_hidden": true,
    "__text_shareGuide_hidden": true,
    "__btn_result_box_hidden": true,
    "__empty_right": "0rpx",
    "__danmu_danmuTailImage": "http://material.motimaster.com/suyu1536647462000/xingxing.png",
    "__bigger_box_height": "600rpx",
    "__pay_one_text": "\u00a54.99\u5077\u770b\u4e00\u4e0b",
    "__selected_text3_width": "220rpx",
    "__danmu_danmuBackground": "",
    "__btn_create_im_height": "100rpx",
    "__btn_result_box_width": "750rpx",
    "__pay_all_left": "386rpx",
    "__showText_left": "0rpx",
    "__go_share_btn_fontSize": "32rpx",
    "__pay_all_fontSize": "30rpx",
    "__text_shareGuide_left": "150rpx",
    "__pay_box_background": "#ffffff",
    "__showboxes_right": "0rpx",
    "__host_box_top": "0rpx",
    "__avatar_box_left": "0rpx",
    "__showboxes_width": "724rpx",
    "__result_text_list_width": "724rpx",
    "__selected_text4_top": "80rpx",
    "__input2_color": "white",
    "__danmu_danmuAvatarStyle": "width:50rpx;height:50rpx;left:0;top:30rpx",
    "__selected_text2_fontSize": "26rpx",
    "__btn_change_disabled": "",
    "__btn_ok_top": "0rpx",
    "objects": [
        "img",
        "host_box",
        "go_share_btn",
        "no_result_box",
        "text_shareGuide",
        "result_box",
        "resultText",
        "result_text_list",
        "danmu",
        "btn_result_box",
        "guest_box",
        "avatar_box",
        "host_avatar",
        "showText",
        "empty",
        "im_list",
        "showboxes",
        "input_box",
        "input2",
        "btn_ok",
        "selected_text1",
        "selected_text2",
        "selected_text3",
        "selected_text4",
        "btn_change",
        "btn_create_im",
        "mask",
        "bigger_box",
        "bigger_text",
        "pay_box",
        "pay_one",
        "pay_all"
    ],
    "__empty_color": "white",
    "__resultText_left": "0rpx",
    "__mask_height": "100%",
    "__showboxes_column": 1,
    "__selected_text3_top": "80rpx",
    "__selected_text1_fontSize": "26rpx",
    "__go_share_btn_disabled": "",
    "__pay_box_top": "360rpx",
    "__pay_all_disabled": "",
    "__selected_text2_top": "0rpx",
    "__avatar_box_width": "750rpx",
    "__text_shareGuide_width": "450rpx",
    "__no_result_box_left": "0rpx",
    "__pay_one_width": "214rpx",
    "__input2_top": "0rpx",
    "__result_text_list_right": "0rpx",
    "__showText_width": "724rpx",
    "__pay_one_top": "300rpx",
    "__input2_left": "20rpx",
    "__danmu_data": "",
    "__selected_text2_left": "320rpx",
    "__im_list_right": "0rpx",
    "__danmu_danmuMargin": 20,
    "__selected_text4_height": "60rpx",
    "__selected_text3_left": "0rpx",
    "__result_text_list_column": 1,
    "__im_list_height": "630rpx",
    "__img_width": "750rpx",
    "__bigger_box_left": "0rpx",
    "__mask_top": "0rpx",
    "__host_avatar_top": "60rpx",
    "__btn_ok_left": "600rpx",
    "__danmu_danmuTailImageStyle": "width:60rpx;height:60rpx;right:0;top:30rpx",
    "__host_avatar_left": "0rpx",
    "__btn_ok_background": "#ec866e",
    "__bigger_text_text": "\u8c01\u5728\u8bc4\u4ef7\u4f60\u4e00\u770b\u5c31\u77e5\u9053",
    "__btn_change_top": "150rpx",
    "__danmu_danmuRowNumber": 4,
    "__input2_fontSize": "30rpx",
    "__btn_create_im_bottom": "0rpx",
    "__resultText_hidden": true,
    "__text_shareGuide_top": "800rpx",
    "__pay_one_color": "#000000",
    "__btn_result_box_right": "0rpx",
    "__showboxes_data": "",
    "__pay_box_left": "0rpx",
    "__resultText_width": "724rpx",
    "__btn_create_im_right": "0rpx",
    "__img_height": "1300rpx",
    "__input_box_left": "20rpx",
    "__selected_text2_width": "330rpx",
    "__bigger_box_right": "0rpx",
    "__im_list_width": "724rpx",
    "__empty_width": "280rpx",
    "__img_left": "0rpx",
    "__pay_one_left": "70rpx",
    "__showText_top": "160rpx",
    "__resultText_height": "620rpx",
    "__empty_left": "0rpx",
    "__selected_text2_height": "60rpx",
    "__btn_ok_disabled": ""
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onButtonTap_Ui23dL:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onGoToPlay', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onGetUserInfo_gPTtT2:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请稍微等一下下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.gotoSharePage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onButtonTap_ishWYB:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请稍微等一下下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onPayOne', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_wtNP0V:  function(evt) {
                var self = this;
                
            self.setData({
                __result_text_list_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_eSR9cB:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onShowPay', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_hcWvKu:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onChangeTags', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_ZvLUXS:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                select_id: "text4",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onSelectTag', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
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
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onViewTap_Ag8RJc:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                item_id: evt.data.id,
item_text: evt.data.text,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onShowMask', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_V2E1vf:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                select_id: "text2",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onSelectTag', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_5EtJHU:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!false && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_j1s5of:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `请稍微等一下...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.gotoSharePage', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_hubB59:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                select_id: "text3",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onSelectTag', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onInputChange_OYmoFa:  function(evt) {
                var self = this;
                
            self.setData({
                __input2_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onGetUserInfo_MBjdF1:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "indexPage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'indexPage.onAnswerSubmit', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})