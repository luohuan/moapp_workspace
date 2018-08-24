const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onViewTap_uEC1ps:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_detail_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'mainPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onViewTap_zFcowT:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
                            
                            
                            var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, {});
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
    onViewTap_Svcn1o:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_records_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    formIdHandler: function (e) {
                        var appid= `wxaa8fe119f5c62d23`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onImageTap_to5F73:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset);
                
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
            return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'deleteRecord', evt);
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
    data: {
    "__shareBtn_color": "#663300",
    "__helpBtn_hidden": true,
    "__backLeida_height": "679rpx",
    "__guest_stars_background": "blue",
    "__backLeida_src": "http://material.motimaster.com/yuyuan/Duudle/create/7029a94695b5c003052970aa0c4841bd.png",
    "__tip2_color": "#F0739B",
    "__tip1_color": "#FFFFFF",
    "__shareBtn_hidden": true,
    "__tip1_fontSize": "36rpx",
    "__bottomBox_width": "750rpx",
    "__ansMask_height": "100%",
    "__shareBtn_width": "750rpx",
    "__shareBtn_fontWeight": 600,
    "__tip1_text": "\u76ee\u524d\u8fd8\u6ca1\u6709\u597d\u53cb\u6765\u6d4b\uff0c\u5feb\u70b9\u51fb\u5e95\u90e8\u6309\u94ae\uff0c\u53bb\u9080\u8bf7\u597d\u53cb\u6765\u56de\u5fc6\u5427\uff01",
    "__shareBtn_disabled": "",
    "__shareBtnAuditing_color": "#663300",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__tip2_left": "0rpx",
    "__bottomBox_background": "#4E7ED8",
    "__beginPlay_background": "#FEB621",
    "__leida_width": "439rpx",
    "__shareBtnAuditing_fontSize": "36rpx",
    "__beginPlay_color": "#663300",
    "__guest_records_left": "37rpx",
    "__delete_src": "http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png",
    "__tip2_hidden": true,
    "__shareBtnAuditing_width": "750rpx",
    "__beginPlay_disabled": "",
    "__helpBtn_height": "70rpx",
    "__shareBtnAuditing_bottom": "0rpx",
    "__leida_top": "485rpx",
    "__shareBtnAuditing_disabled": "",
    "__bottomBox_height": "100rpx",
    "__leida_height": "330rpx",
    "__beginPlay_height": "100rpx",
    "__shareBtn_height": "110rpx",
    "__backLeida_left": "49rpx",
    "__tip1_left": "0rpx",
    "__guest_records_top": "961rpx",
    "__shareBtn_fontSize": "38rpx",
    "__delete_width": "40rpx",
    "__guest_stars_data": "",
    "__shareBtnAuditing_fontWeight": 600,
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
    "__leida_left": "261rpx",
    "__beginPlay_text": "\u521b\u5efa\u6211\u7684\u597d\u53cb\u56de\u5fc6\u5899 >",
    "__backLeida_top": "135rpx",
    "__ansMask_width": "100%",
    "__delete_left": "0rpx",
    "__delete_height": "40rpx",
    "__leida_src": "../../img/leida2.png",
    "__authorAvatar_width": "70rpx",
    "__shareBtn_background": "#FEB621",
    "__tip2_right": "0rpx",
    "__helpBtn_left": "650rpx",
    "__helpBtn_disabled": "",
    "__ansMask_hidden": true,
    "__tip1_hidden": true,
    "__shareBtnAuditing_background": "#FEB621",
    "__authorAvatar_left": "340rpx",
    "__ansMask_top": "0rpx",
    "__helpBtn_top": "70rpx",
    "__helpBtn_width": "70rpx",
    "__shareBtn_bottom": "0rpx",
    "__tip1_right": "0rpx",
    "__tip2_top": "650rpx",
    "__beginPlay_width": "750rpx",
    "__beginPlay_hidden": true,
    "__bottomBox_bottom": "0rpx",
    "__authorAvatar_height": "70rpx",
    "__ansMask_background": "RGBA(0, 0, 0, 0.7)",
    "__guest_records_data": "",
    "__backLeida_width": "650rpx",
    "__tip1_top": "580rpx",
    "__tip2_fontSize": "36rpx",
    "__shareBtnAuditing_height": "100rpx",
    "__ansMask_left": "0rpx",
    "__delete_top": "0rpx",
    "__authorAvatar_top": "453rpx",
    "__beginPlay_fontWeight": 900,
    "__shareBtnAuditing_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__tip2_text": "\u2193\u2193\u2193",
    "__shareBtnAuditing_hidden": false,
    "__beginPlay_fontSize": "36rpx",
    "__authorAvatar_src": "",
    "__beginPlay_bottom": "0rpx",
    "__guest_detail_data": ""
},
    onGetUserInfo_QvKQS6:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'goShare', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_OXWoQi:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提示:`,
                content: `查看全部好友的选择(包括未来进入的好友),需支付金额9.9元`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                host_id: evt.data.host_openid,
guest_id: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'checkDetailPay', evt);
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
                    var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'mainPageReady', evt);
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
    onButtonTap_8x6UC4:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                host_id: evt.data.host_openid,
guest_id: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'checkDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_pR216w:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'toBegin', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})