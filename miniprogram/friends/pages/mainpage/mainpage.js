const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onButtonTap_qG2hFU:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                host_id: evt.data.host_openid,
guest_id: evt.data.guest_openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'checkDetail', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_s3t6I2:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'toBegin', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onViewTap_V42gjp:  function(evt) {
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
    data: {
    "__tip1_hidden": true,
    "__ansMask_hidden": true,
    "__ansMask_top": "0rpx",
    "__beginPlay_width": "750rpx",
    "__bottomBox_height": "100rpx",
    "__tip2_top": "650rpx",
    "__backLeida_height": "679rpx",
    "__tip1_left": "0rpx",
    "__tip2_fontSize": "36rpx",
    "__midline_background": "#FFF",
    "__shareBtn_fontSize": "36rpx",
    "__leida_height": "330rpx",
    "__tip1_text": "\u70b9\u51fb\u5e95\u90e8\u6309\u94ae\u5206\u4eab\u7ed9\u4f60\u7684\u597d\u53cb\u6765\u6d4b",
    "__ansMask_height": "100%",
    "__tip1_top": "580rpx",
    "__delete_left": "0rpx",
    "__tip2_left": "0rpx",
    "__helpBtn_width": "70rpx",
    "__delete_src": "http://material.motimaster.com/harvey///4fe3d04c831c479268f0d039e0c5f88b.png",
    "__tip1_fontSize": "36rpx",
    "__midline_hidden": true,
    "__leida_left": "261rpx",
    "__tip1_color": "#F0739B",
    "__leida_src": "../../img/leida2.png",
    "__authorAvatar_height": "70rpx",
    "__ansMask_width": "100%",
    "__guest_records_data": "",
    "__beginPlay_background": "#FEB621",
    "__beginPlay_color": "#663300",
    "__tip2_color": "#F0739B",
    "__beginPlay_text": "\u521b\u5efa\u6211\u7684\u597d\u53cb\u6e05\u5355 >",
    "__shareBtn_width": "750rpx",
    "__ansMask_background": "RGBA(0, 0, 0, 0.7)",
    "__guest_records_top": "961rpx",
    "__backLeida_width": "650rpx",
    "__backLeida_src": "http://material.motimaster.com/yuyuan/Duudle/create/7029a94695b5c003052970aa0c4841bd.png",
    "__shareBtn_fontWeight": 600,
    "__backLeida_top": "135rpx",
    "__helpBtn_top": "70rpx",
    "__shareBtn_disabled": "",
    "__delete_width": "40rpx",
    "__bottomBox_width": "750rpx",
    "__midline_right": "380rpx",
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
    "__shareBtn_bottom": "0rpx",
    "__authorAvatar_src": "",
    "__shareBtn_background": "#FEB621",
    "__guest_stars_data": "",
    "__midline_width": "2rpx",
    "__beginPlay_bottom": "0rpx",
    "__delete_height": "40rpx",
    "__guest_records_left": "37rpx",
    "__tip2_text": "\u2193\u2193\u2193",
    "__bottomBox_background": "#4E7ED8",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b >",
    "__leida_width": "439rpx",
    "__beginPlay_height": "100rpx",
    "__guest_stars_background": "blue",
    "__helpBtn_hidden": true,
    "__beginPlay_fontSize": "36rpx",
    "__shareBtn_height": "100rpx",
    "__midline_height": "50rpx",
    "__backLeida_left": "49rpx",
    "__authorAvatar_width": "70rpx",
    "__authorAvatar_top": "453rpx",
    "__leida_top": "485rpx",
    "__beginPlay_hidden": true,
    "__bottomBox_bottom": "0rpx",
    "__helpBtn_left": "650rpx",
    "__beginPlay_fontWeight": 900,
    "__shareBtn_color": "#663300",
    "__tip1_right": "0rpx",
    "__tip2_right": "0rpx",
    "__delete_top": "0rpx",
    "__guest_detail_data": "",
    "__ansMask_left": "0rpx",
    "__helpBtn_disabled": "",
    "__tip2_hidden": true,
    "__authorAvatar_left": "340rpx",
    "__beginPlay_disabled": "",
    "__helpBtn_height": "70rpx",
    "__midline_bottom": "28rpx"
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'mainPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_37itMC:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'goShare', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
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
    onPullDownRefresh:  function () {
                    wx.showNavigationBarLoading();
                    var self = this;                    
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, {});
                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'mainPageReady', evt);
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
    onViewTap_cZAbo3:  function(evt) {
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
    onImageTap_CHYxoR:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "mainpage", self, evt.currentTarget.dataset);
                
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
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'deleteRecord', evt);
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onViewTap_VAds3K:  function(evt) {
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
})