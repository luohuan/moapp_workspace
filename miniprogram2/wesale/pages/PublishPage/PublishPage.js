const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onSelectorPickerChange_AdlCW9:  function(evt) {
                var self = this;
                
            self.setData({
                __picker_type_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onSelectorPickerTextKindChange', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onGetUserInfo_ripFE2:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.clickpickermask', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onInputChange_z1vp40:  function(evt) {
                var self = this;
                
            self.setData({
                __title_input_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onInputConfirm_dNTVES:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.titleInputEnd', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onInputChange_g6gTrk:  function(evt) {
                var self = this;
                
            self.setData({
                __price_input_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onInputConfirm_yWTXmA:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.priceInputEnd', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onTextareaChange_WutkvO:  function(evt) {
                var self = this;
                
            self.setData({
                __description_value: evt.detail.value
            })
            
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_tsDsmF:  function(evt) {
                var self = this;
                
            self.setData({
                __grid_pic_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onImageTap_VB9DeL:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                src: evt.data.src,
pos: evt.data.pos,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onUploadImg', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onImageTap_pjpWdd:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                src: evt.data.src,
pos: evt.data.pos,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onDeleteImg', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_NgEBUW:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onMask01Clicked', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_7li6uj:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onMask02Clicked', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onSwitchChangeTap_g6583z:  function(evt) {
                var self = this;
                
            self.setData({
                __switch_agreement_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onSwitchChangeTap_AHYB35:  function(evt) {
                var self = this;
                
            self.setData({
                __switch_activity_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.detail.value);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_RIsfBQ:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onButtonPublishClicked', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_lfOgc8:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!true && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_3WRd0M:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.hideMask', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onGetPhoneNumber_KFRSxU:  function(evt) {
                    var self = this;

                    if (evt.detail.encryptedData) {
                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);

                        evt_data.encrypted_data = {
                            type: 'phoneNumber',
                            data: evt.detail.encryptedData,
                            iv: evt.detail.iv
                        };
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.getphonenumber', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get phone number fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onViewTap_JJEVTr:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!true && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_NHG0Lh:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onMask01HiddenClicked', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_llftT2:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!true && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_luzt38:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onMask02HiddenClicked', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    data: {
    "objects": [
        "picker_type",
        "pickermask",
        "title_input",
        "price_input",
        "description",
        "grid_pic",
        "switchbox",
        "switch_agreement",
        "switch_activity",
        "mask",
        "mask02",
        "mask03"
    ],
    "__picker_type_text": "\u5546\u54c1\u5c5e\u6027",
    "__picker_type_value": "",
    "__picker_type_disabled": "",
    "__picker_type_range": [
        "\u51fa\u552e",
        "\u6c42\u8d2d",
        "\u8d60\u9001"
    ],
    "__picker_type_color": "#f4bc33",
    "__picker_type_width": "720rpx",
    "__picker_type_height": "100rpx",
    "__picker_type_background": "white",
    "__picker_type_left": "30rpx",
    "__picker_type_top": "0rpx",
    "__picker_type_fontSize": "32rpx",
    "__picker_type_fontWeight": "bold",
    "__pickermask_hidden": true,
    "__pickermask_disabled": "",
    "__pickermask_width": "750rpx",
    "__pickermask_height": "100rpx",
    "__pickermask_left": "0rpx",
    "__pickermask_top": "0rpx",
    "__title_input_placeholder": " \u8f93\u5165\u6807\u9898\uff0c\u5982\u51e4\u51f0\u724c\u81ea\u884c\u8f66\uff0c20\u5b57\u4ee5\u5185",
    "__title_input_value": "",
    "__title_input_width": "720rpx",
    "__title_input_height": "80rpx",
    "__title_input_background": "white",
    "__title_input_left": "0rpx",
    "__title_input_top": "10rpx",
    "__title_input_fontSize": "32rpx",
    "__title_input_fontWeight": "bold",
    "__price_input_placeholder": " \u8f93\u5165\u4ef7\u683c\uff0c\u4fbf\u5b9c\u624d\u662f\u7ade\u4e89\u529b\u54df\uff01",
    "__price_input_value": "",
    "__price_input_width": "720rpx",
    "__price_input_height": "80rpx",
    "__price_input_background": "white",
    "__price_input_left": "0rpx",
    "__price_input_top": "92rpx",
    "__price_input_fontSize": "32rpx",
    "__description_placeholder": " \u8f93\u5165\u63cf\u8ff0\uff0c\u54c1\u724c\u3001\u89c4\u683c\u3001\u51e0\u6210\u65b0\u3001\u53d6\u8d27\u65b9\u5f0f\u3001\u8d2d\u4e70\u6e20\u9053\u3001\u8f6c\u624b\u539f\u56e0\u7b49\u4fe1\u606f\uff0c\u5efa\u8bae150\u5b57\u4ee5\u5185\u54df~",
    "__description_disabled": "",
    "__description_value": "",
    "__description_width": "710rpx",
    "__description_height": "100rpx",
    "__description_left": "20rpx",
    "__description_top": "40rpx",
    "__description_fontSize": "30rpx",
    "__grid_pic_data": "",
    "__grid_pic_column": 3,
    "__grid_pic_width": "700rpx",
    "__grid_pic_height": "210rpx",
    "__grid_pic_left": "0rpx",
    "__grid_pic_top": "20rpx",
    "__grid_pic_right": "0rpx",
    "__switchbox_width": "750rpx",
    "__switchbox_height": "140rpx",
    "__switchbox_left": "0rpx",
    "__switchbox_top": "785rpx",
    "__switch_agreement_checked": "",
    "__switch_agreement_value": "",
    "__switch_agreement_width": "40rpx",
    "__switch_agreement_height": "40rpx",
    "__switch_agreement_left": "30rpx",
    "__switch_agreement_top": "6rpx",
    "__switch_activity_checked": "",
    "__switch_activity_value": "",
    "__switch_activity_width": "40rpx",
    "__switch_activity_height": "40rpx",
    "__switch_activity_left": "30rpx",
    "__switch_activity_top": "70rpx",
    "__mask_hidden": true,
    "__mask_width": "100%",
    "__mask_height": "100%",
    "__mask_background": "RGBA(0, 0, 0, 0.7)",
    "__mask_left": "0rpx",
    "__mask_top": "0rpx",
    "__mask02_hidden": true,
    "__mask02_width": "100%",
    "__mask02_height": "100%",
    "__mask02_background": "RGBA(0, 0, 0, 0.7)",
    "__mask02_left": "0rpx",
    "__mask02_top": "0rpx",
    "__mask03_hidden": true,
    "__mask03_width": "100%",
    "__mask03_height": "100%",
    "__mask03_background": "RGBA(0, 0, 0, 0.7)",
    "__mask03_left": "0rpx",
    "__mask03_top": "0rpx"
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'publish', 'PublishPage.onShow', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "PublishPage", self, {});
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
})