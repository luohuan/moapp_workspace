const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onGetUserInfo_sBULRa:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'toBegin', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'mainPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__beginPlay_color": "#663300",
    "__tip1_right": "0rpx",
    "__ansMask_width": "100%",
    "__shareBtn_height": "110rpx",
    "__shareBtn_hidden": true,
    "__bottomBox_bottom": "0rpx",
    "__guest_records_data": "",
    "__authorAvatar_src": "",
    "__ansMask_height": "100%",
    "__tip2_left": "0rpx",
    "__guest_stars_background": "blue",
    "__helpBtn_left": "650rpx",
    "__delete_width": "40rpx",
    "__shareBtn_fontSize": "38rpx",
    "__shareBtn_background": "#FEB621",
    "__delete_src": "http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png",
    "__beginPlay_height": "100rpx",
    "__guest_records_left": "37rpx",
    "__shareBtnAuditing_hidden": false,
    "__tip2_text": "\u2193\u2193\u2193",
    "__bottomBox_width": "750rpx",
    "__beginPlay_bottom": "0rpx",
    "__beginPlay_text": "\u521b\u5efa\u6211\u7684\u597d\u53cb\u56de\u5fc6\u5899 >",
    "__leida_top": "485rpx",
    "__shareBtnAuditing_fontSize": "36rpx",
    "__leida_height": "330rpx",
    "__bottomBox_height": "100rpx",
    "__shareBtn_color": "#663300",
    "__helpBtn_disabled": "",
    "__authorAvatar_top": "453rpx",
    "__helpBtn_height": "70rpx",
    "__backLeida_top": "135rpx",
    "__backLeida_src": "http://material.motimaster.com/yuyuan/Duudle/create/7029a94695b5c003052970aa0c4841bd.png",
    "__beginPlay_disabled": "",
    "__tip1_left": "0rpx",
    "__helpBtn_hidden": true,
    "__delete_height": "40rpx",
    "__shareBtnAuditing_color": "#663300",
    "__helpBtn_width": "70rpx",
    "__guest_detail_data": "",
    "__leida_width": "439rpx",
    "__shareBtn_fontWeight": 600,
    "__shareBtn_bottom": "0rpx",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__authorAvatar_left": "340rpx",
    "__shareBtn_disabled": "",
    "__tip1_top": "580rpx",
    "__ansMask_left": "0rpx",
    "__authorAvatar_height": "70rpx",
    "__backLeida_left": "49rpx",
    "__shareBtnAuditing_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__tip1_fontSize": "36rpx",
    "__authorAvatar_width": "70rpx",
    "__delete_left": "0rpx",
    "objects": [
        "backLeida",
        "leida",
        "authorAvatar",
        "guest_stars",
        "helpBtn",
        "tip1",
        "tip2",
        "guest_records",
        "delete",
        "ansMask",
        "guest_detail",
        "bottomBox",
        "shareBtn",
        "shareBtnAuditing",
        "beginPlay"
    ],
    "__beginPlay_width": "750rpx",
    "__ansMask_top": "0rpx",
    "__ansMask_background": "RGBA(0, 0, 0, 0.7)",
    "__guest_stars_data": "",
    "__helpBtn_top": "70rpx",
    "__tip1_hidden": true,
    "__shareBtnAuditing_background": "#FEB621",
    "__beginPlay_background": "#FEB621",
    "__beginPlay_fontSize": "36rpx",
    "__ansMask_hidden": true,
    "__tip1_color": "#FFFFFF",
    "__shareBtnAuditing_disabled": "",
    "__shareBtn_width": "750rpx",
    "__guest_records_top": "961rpx",
    "__bottomBox_background": "#4E7ED8",
    "__backLeida_height": "679rpx",
    "__shareBtnAuditing_fontWeight": 600,
    "__shareBtnAuditing_height": "100rpx",
    "__beginPlay_fontWeight": 900,
    "__delete_top": "0rpx",
    "__beginPlay_hidden": true,
    "__leida_left": "261rpx",
    "__leida_src": "../../img/leida2.png",
    "__tip2_top": "650rpx",
    "__tip2_fontSize": "36rpx",
    "__tip1_text": "\u70b9\u51fb\u5e95\u90e8\u6309\u94ae\u5206\u4eab\u7ed9\u597d\u53cb\u6765\u6d4b\u5427\uff01",
    "__shareBtnAuditing_width": "750rpx",
    "__shareBtnAuditing_bottom": "0rpx",
    "__tip2_right": "0rpx",
    "__backLeida_width": "650rpx",
    "__tip2_hidden": true,
    "__tip2_color": "#F0739B"
},
    onViewTap_ZNX50x:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_detail_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_GXToYm:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
                        this.data.__share_page = 'begin'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, {});
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
    onViewTap_9EWNhB:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_records_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_cvMwg2:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提示:`,
                content: `查看全部好友的选择(包括未来进入的好友),只需支付金额3.99`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                guest_id: evt.data.guest_openid,
host_id: evt.data.host_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'checkDetailPay', evt);
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
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'mainPageReady', evt);
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_PWx7Md:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                guest_id: evt.data.guest_openid,
host_id: evt.data.host_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'checkDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_sxplKz:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提醒`,
                content: `删除的记录将不能恢复，您确认删除嘛?`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                rid: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'deleteRecord', evt);
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
                        var appid= `wx468ad783f165eea0`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onGetUserInfo_A8ppCv:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx468ad783f165eea0", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'goShare', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})