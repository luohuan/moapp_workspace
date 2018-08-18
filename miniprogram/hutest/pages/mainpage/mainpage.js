const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_ZVAXtG:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                guest_id: evt.data.guest_openid,
host_id: evt.data.host_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'checkDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_W5vQAq:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_records_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__midline_background": "#FFF",
    "__shareBtn_disabled": "",
    "__delete_src": "http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png",
    "__midline_hidden": true,
    "__ansMask_left": "0rpx",
    "__tip2_hidden": true,
    "__delete_left": "0rpx",
    "__beginPlay_bottom": "0rpx",
    "__leida_left": "261rpx",
    "__beginPlay_text": "\u521b\u5efa\u6211\u7684\u96f7\u8fbe\u56fe >",
    "__guest_records_top": "996rpx",
    "__beginPlay_height": "100rpx",
    "__shareBtn_background": "#4E7ED8",
    "__ansMask_width": "100%",
    "__delete_height": "40rpx",
    "__shareBtn_width": "750rpx",
    "__authorAvatar_left": "340rpx",
    "__shareBtn_height": "100rpx",
    "__bottomBox_height": "100rpx",
    "__delete_width": "40rpx",
    "__ansMask_hidden": true,
    "__backLeida_src": "http://img.mogodeer.cn/images/diudiu/xingzuozhun/leida.png",
    "__delete_top": "0rpx",
    "__shareBtn_fontWeight": 600,
    "__beginPlay_fontSize": "36rpx",
    "__bottomBox_width": "750rpx",
    "__tip1_top": "580rpx",
    "__guest_detail_data": "",
    "__helpBtn_top": "100rpx",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__guest_stars_background": "blue",
    "__leida_top": "485rpx",
    "__backLeida_width": "650rpx",
    "__beginPlay_disabled": "",
    "__midline_bottom": "28rpx",
    "__helpBtn_height": "80rpx",
    "__beginPlay_hidden": true,
    "__helpBtn_left": "600rpx",
    "__beginPlay_width": "750rpx",
    "__authorAvatar_src": "",
    "__tip2_text": "\u2193\u2193\u2193",
    "__backLeida_left": "49rpx",
    "__tip1_color": "#F0739B",
    "__tip2_color": "#F0739B",
    "__authorAvatar_width": "70rpx",
    "__ansMask_top": "0rpx",
    "__guest_records_data": "",
    "__tip1_left": "0rpx",
    "__leida_width": "439rpx",
    "__ansMask_background": "RGBA(0, 0, 0, 0.7)",
    "__ansMask_height": "100%",
    "__helpBtn_disabled": "",
    "__backLeida_top": "135rpx",
    "__shareBtn_color": "#ffffff",
    "__beginPlay_background": "#4E7ED8",
    "__leida_src": "../../img/leida2.png",
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
        "midline",
        "beginPlay"
    ],
    "__beginPlay_fontWeight": 900,
    "__helpBtn_hidden": true,
    "__tip2_right": "0rpx",
    "__tip1_text": "\u70b9\u51fb\u53f3\u4e0a\u89d2\u5206\u4eab\u7ed9\u4f60\u7684\u597d\u53cb\u6765\u6d4b",
    "__guest_stars_data": "",
    "__authorAvatar_top": "453rpx",
    "__bottomBox_bottom": "0rpx",
    "__tip2_left": "0rpx",
    "__tip1_hidden": true,
    "__beginPlay_color": "#ffffff",
    "__authorAvatar_height": "70rpx",
    "__helpBtn_width": "80rpx",
    "__midline_height": "50rpx",
    "__tip1_right": "0rpx",
    "__midline_width": "2rpx",
    "__leida_height": "330rpx",
    "__tip2_fontSize": "36rpx",
    "__tip2_top": "650rpx",
    "__guest_records_left": "37rpx",
    "__midline_right": "380rpx",
    "__bottomBox_background": "#4E7ED8",
    "__shareBtn_bottom": "0rpx",
    "__tip1_fontSize": "36rpx",
    "__shareBtn_fontSize": "36rpx",
    "__backLeida_height": "679rpx"
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
                        this.data.__share_page = 'begin'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'mainPageReady', evt);
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
    onViewTap_Tgt8iV:  function(evt) {
                var self = this;
                
            self.setData({
                __guest_detail_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_CssTX5:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提醒`,
                content: `删除的匹配将不能恢复，您确认删除嘛?`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                rid: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'deleteRecord', evt);
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
    onGetUserInfo_4XVX3V:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'toBegin', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onViewTap_g1nsPY:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'mainPageReady', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
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
    onGetUserInfo_wP0tjj:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'goShare', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})