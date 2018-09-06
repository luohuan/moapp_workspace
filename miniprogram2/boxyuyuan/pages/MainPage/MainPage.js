const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    data: {
    "__AD2_bottom": "0rpx",
    "__morefun_height": "45rpx",
    "__grid1_width": "730rpx",
    "__AD1_height": "200rpx",
    "__AD3_background": "rgba(0,0,0,0)",
    "__grid3_column": 2,
    "__AD1_hidden": false,
    "__imgUrls_data": "",
    "__fenxiang_fontWeight": "900",
    "__swiper_indicatorActiveColor": "",
    "__fenxiang_disabled": "",
    "__box_background": "white",
    "__grid3_columnStr": "1fr 1fr",
    "__recommend_left": "20rpx",
    "__AD2_background": "white",
    "__swiper_current": "",
    "__grid3_data": "",
    "__recommend_fontWeight": "450",
    "__swiper_autoplay": true,
    "__helpBtn_left": "640rpx",
    "__morefun2_fontSize": "37rpx",
    "__fenxiang_hidden": true,
    "__box_width": "720rpx",
    "__AD3_hidden": false,
    "__morefun2_fontWeight": "450",
    "__ad_src": "",
    "__helpBtn_height": "60rpx",
    "__AD2_hidden": false,
    "__grid1_height": "950rpx",
    "__AD2_height": "200rpx",
    "__recommend_top": "310rpx",
    "__AD2_width": "750rpx",
    "__grid1_column": 2,
    "__fenxiang_width": "180rpx",
    "__helpBtn_disabled": "",
    "__helpBtn_hidden": true,
    "__AD3_height": "200rpx",
    "__swiper_height": "300rpx",
    "__swiper_top": "0rpx",
    "__swiper_left": "0rpx",
    "__fenxiang_fontSize": "35rpx",
    "__helpBtn_top": "310rpx",
    "__box_height": "300rpx",
    "__AD3_width": "700rpx",
    "__swiper_indicatorDots": "",
    "__grid3_width": "730rpx",
    "__helpBtn_width": "60rpx",
    "__recommend_fontSize": "37rpx",
    "__grid1_data": "",
    "__morefun_width": "750rpx",
    "objects": [
        "box",
        "swiper",
        "imgUrls",
        "recommend",
        "helpBtn",
        "grid1",
        "AD1",
        "ad",
        "morefun",
        "morefun2",
        "grid3",
        "AD3",
        "fenxiang",
        "AD2"
    ],
    "__swiper_width": "710rpx",
    "__morefun_hidden": true,
    "__grid1_columnStr": "1fr 1fr",
    "__fenxiang_height": "60rpx",
    "__box_hidden": true,
    "__AD1_width": "700rpx",
    "__fenxiang_color": "#f7ca4e"
},
    onViewTap_YfPT46:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx3d29f3f59fee8a87', 'main', 'MainPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx3d29f3f59fee8a87', 'main', 'MainPage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
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
                        this.data.__share_page = 'MainPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, {});
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
    onViewTap_vWaVp7:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx3d29f3f59fee8a87', 'main', 'MainPage.go_to', evt);
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
    onImageTap_EgHgvL:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                name: "ad",

            }
            ;
            return moapp.requestCloudFunction(self, 'wx3d29f3f59fee8a87', 'main', 'MainPage.ad_goto', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_PTdadD:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx3d29f3f59fee8a87", "MainPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx3d29f3f59fee8a87', 'main', 'MainPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
})