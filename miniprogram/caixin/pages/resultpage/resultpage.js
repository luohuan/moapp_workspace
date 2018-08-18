const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
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
                        this.data.__share_page = 'mainpage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, {});
                            Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'onShare', evt);
            }
            )
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, {});
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
    onButtonTap_XiQcfg:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                visit_id: evt.data.openid,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'maskShow', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_obdWKf:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'onguanggao', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_5G3dDu:  function(evt) {
                var self = this;
                
            self.setData({
                __hostAns_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'resultPageReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_69gd82:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'cancel', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_fpLK6r:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: "questpage",

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.redirectTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_kIXcni:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
    onButtonTap_ruqGDP:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `温馨提示:`,
                content: `查看全部好友的答题详情（包括未来进入的好友），只需支付金额9.9元。`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'onPay', evt);
                    }else if(res.cancel) {
                        console.log('用户点击取消')
                        
                    }
                }
            })
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_4LmZG1:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'toInvitePage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_WB0phQ:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
                    var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, {});
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
    "__low_top": "0rpx",
    "__invitButton_height": "90rpx",
    "__payBtn_color": "black",
    "__payBtn_text": "\u770bTA\u7684\u9009\u62e9",
    "__shownum_fontSize": "28rpx",
    "__ansMask_top": "0rpx",
    "__noAnswer_top": "0rpx",
    "__hostName_top": "0rpx",
    "__oneQuestionList_data": "",
    "__hostAvatar_right": "0rpx",
    "__ansMask_background": "RGBA(0, 0, 0, 0.7)",
    "__shownum_top": "55rpx",
    "__showShare_height": "37rpx",
    "__invitButton_hidden": true,
    "__invitButton_background": "#FEB621",
    "__helpBtn_width": "64rpx",
    "__showShare_background": "#FEB621",
    "__showdetail_right": "0rpx",
    "__showShare_fontSize": "22rpx",
    "__shareButton_width": "500rpx",
    "__payBtn_top": "98rpx",
    "__invitButton_text": "\u9080\u8bf7\u597d\u53cb\u6765\u505a\u9898",
    "__showdetail_left": "0rpx",
    "__payBtn_height": "37rpx",
    "__above_fontWeight": "bold",
    "__invitButton_color": "#663300",
    "__guanggao_hidden": true,
    "__visitAns_data": "",
    "__showShare_left": "442rpx",
    "__payBtn_left": "442rpx",
    "__hostName_color": "#FEB621",
    "__ansMask_width": "100%",
    "__invitButton_width": "500rpx",
    "__shareButton_left": "120rpx",
    "__shareButton_disabled": "",
    "__shareButton_background": "#FEB621",
    "__shareButton_fontSize": "40rpx",
    "__ansMask_left": "0rpx",
    "__showdetail_height": "75rpx",
    "__noAnswer_left": "0rpx",
    "__low_fontWeight": "bold",
    "__helpBtn_top": "48rpx",
    "__shownum_left": "0rpx",
    "__payBtn_fontSize": "22rpx",
    "__guanggao_height": "125rpx",
    "__low_height": "50rpx",
    "__payBtn_width": "130rpx",
    "__QAagain_left": "0rpx",
    "__guanggao_width": "750rpx",
    "__showShare_width": "130rpx",
    "__QAagain_hidden": true,
    "__mask_left": "0rpx",
    "__hostAns_data": "",
    "__QAagain_text": "\u6211\u4e5f\u8981\u51fa\u9898",
    "__mask_top": "0rpx",
    "__QAagain_disabled": "",
    "__showdetail_background": "#000000",
    "__helpBtn_left": "32rpx",
    "__showShare_text": "\u770bTA\u7684\u9009\u62e9",
    "__hostName_left": "0rpx",
    "__payBtn_hidden": true,
    "__hostAvatar_left": "0rpx",
    "__hostName_fontSize": "38rpx",
    "__above_left": "0rpx",
    "__ansMask_height": "100%",
    "__low_right": "0rpx",
    "__QAagain_background": "#FEB621",
    "__QAagain_top": "1000rpx",
    "__shownum_color": "#FFFFFF",
    "__shareButton_height": "90rpx",
    "__showShare_top": "98rpx",
    "__mask_height": "100%",
    "__low_width": "550rpx",
    "__showShare_disabled": "",
    "__shareButton_color": "#663300",
    "__low_color": "#FFD886",
    "objects": [
        "hostAvatar",
        "hostName",
        "shownum",
        "oneQuestionList",
        "showShare",
        "payBtn",
        "noAnswer",
        "invitButton",
        "guanggao",
        "shareButton",
        "showdetail",
        "QAagain",
        "helpBtn",
        "ansMask",
        "above",
        "hostAns",
        "low",
        "visitAns",
        "mask"
    ],
    "__showdetail_fontSize": "40rpx",
    "__QAagain_fontSize": "40rpx",
    "__showShare_hidden": true,
    "__above_color": "#FFD886",
    "__invitButton_disabled": "",
    "__payBtn_disabled": "",
    "__invitButton_top": "900rpx",
    "__shownum_right": "0rpx",
    "__QAagain_right": "0rpx",
    "__showdetail_text": "\u67e5\u770b\u7b54\u6848\u8be6\u60c5",
    "__ansMask_hidden": true,
    "__oneQuestionList_width": "100%",
    "__showdetail_disabled": "",
    "__hostAvatar_src": "",
    "__payBtn_background": "#FEB621",
    "__hostAvatar_width": "150rpx",
    "__showdetail_hidden": true,
    "__low_left": "0rpx",
    "__noAnswer_right": "0rpx",
    "__shareButton_text": "\u9080\u8bf7\u597d\u53cb\u6765\u505a\u9898",
    "__helpBtn_hidden": true,
    "__low_fontSize": "33rpx",
    "__invitButton_left": "120rpx",
    "__guanggao_bottom": "0rpx",
    "__mask_background": "RGBA(0, 0, 0, 0.7)",
    "__noAnswer_bottom": "0rpx",
    "__showdetail_color": "#FEB621",
    "__showdetail_width": "500rpx",
    "__QAagain_color": "#663300",
    "__mask_width": "100%",
    "__QAagain_height": "90rpx",
    "__QAagain_width": "500rpx",
    "__showShare_color": "black",
    "__invitButton_fontSize": "40rpx",
    "__above_top": "0rpx",
    "__hostAvatar_height": "150rpx",
    "__guanggao_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__above_fontSize": "33rpx",
    "__helpBtn_disabled": "",
    "__helpBtn_height": "64rpx",
    "__mask_hidden": true,
    "__shareButton_hidden": true,
    "__above_right": "0rpx",
    "__hostAvatar_top": "20rpx",
    "__showdetail_top": "900rpx",
    "__hostName_right": "0rpx",
    "__shareButton_top": "950rpx"
},
    onButtonTap_1Tbm9S:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx18610e0755615e2f', 'main', 'showDetail', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_oSPNEZ:  function(evt) {
                var self = this;
                
            self.setData({
                __oneQuestionList_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_F8mO5L:  function(evt) {
                var self = this;
                
            self.setData({
                __visitAns_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx18610e0755615e2f", "resultpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
})