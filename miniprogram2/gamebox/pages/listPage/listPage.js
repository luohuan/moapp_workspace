const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onViewTap_UCQpzx:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                appid: evt.data.appid,
title: evt.data.title,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_Ym0IH7:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                name: "ad_2",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.ad_goto', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_btIAm1:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                name: "ad",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.ad_goto', evt);
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
                        this.data.__share_page = 'listPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, {});
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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__ad_2_width": "750rpx",
    "__hidden_ad_top": "500rpx",
    "__swiper1_height": "310rpx",
    "__hidden_ad_left": "0rpx",
    "__ad_2_src": "",
    "__hidden_1_left": "0rpx",
    "__ad_src": "",
    "__ad_top": "370rpx",
    "__ad_2_top": "1030rpx",
    "__grid1_left": "0rpx",
    "objects": [
        "swiper1",
        "dataswiper",
        "hidden_1",
        "recommend",
        "grid1",
        "ad",
        "hidden_ad",
        "all_play",
        "dormitorylist",
        "fenxiang",
        "ad_2"
    ],
    "__fenxiang_width": "210rpx",
    "__fenxiang_fontSize": "35rpx",
    "__fenxiang_hidden": true,
    "__dormitorylist_data": "",
    "__grid1_right": "0rpx",
    "__ad_width": "750rpx",
    "__swiper1_width": "750rpx",
    "__grid1_columnStr": "1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr",
    "__swiper1_autoplay": true,
    "__swiper1_current": "",
    "__swiper1_indicatorActiveColor": "",
    "__grid1_data": "",
    "__fenxiang_color": "#f7ca4e",
    "__all_play_top": "80rpx",
    "__swiper1_indicatorDots": "",
    "__recommend_top": "30rpx",
    "__dataswiper_data": "",
    "__grid1_width": "100%",
    "__all_play_fontWeight": "450",
    "__recommend_left": "20rpx",
    "__grid1_top": "10rpx",
    "__hidden_1_top": "300rpx",
    "__recommend_fontSize": "37rpx",
    "__fenxiang_height": "70rpx",
    "__ad_left": "0rpx",
    "__fenxiang_fontWeight": "900",
    "__ad_2_height": "191rpx",
    "__all_play_left": "20rpx",
    "__fenxiang_disabled": "",
    "__ad_2_left": "0rpx",
    "__ad_height": "191rpx",
    "__grid1_column": 9,
    "__all_play_fontSize": "37rpx",
    "__recommend_fontWeight": "450"
},
    onImageTap_b5VgEs:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                appid: evt.data.appid,
title: evt.data.title,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onViewTap_EMvslA:  function(evt) {
                var self = this;
                
            self.setData({
                __dormitorylist_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx267c13c76965a037", "listPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                appid: evt.data.appid,
title: evt.data.title,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx267c13c76965a037', 'main', 'listPage.go_to', evt);
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
})