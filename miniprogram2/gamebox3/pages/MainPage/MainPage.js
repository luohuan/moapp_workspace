const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onImageTap_MPLXgh:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx2374ed010f4bd862', 'main', 'MainPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
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
    onViewTap_9aHpz5:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx2374ed010f4bd862', 'main', 'MainPage.go_to', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onViewTap_TIrvlK:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                title: evt.data.title,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx2374ed010f4bd862', 'main', 'MainPage.go_to', evt);
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
                        this.data.__share_page = 'MainPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, {});
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
    data: {
    "__grid1_height": "720rpx",
    "__helpBtn_top": "100rpx",
    "__helpBtn_left": "600rpx",
    "__swiper_autoplay": true,
    "__AD3_background": "rgba(0,0,0,0)",
    "__swiper_height": "300rpx",
    "__grid3_data": "",
    "__swiper_indicatorActiveColor": "",
    "__swiper_left": "0rpx",
    "__grid1_data": "",
    "__swiper_width": "700rpx",
    "__AD3_width": "700rpx",
    "__AD1_width": "700rpx",
    "__helpBtn_width": "80rpx",
    "__grid1_width": "730rpx",
    "__AD1_background": "white",
    "objects": [
        "swiper",
        "imgUrls",
        "grid1",
        "AD1",
        "grid3",
        "AD3",
        "helpBtn",
        "AD2"
    ],
    "__AD2_background": "white",
    "__swiper_top": "0rpx",
    "__grid3_columnStr": "1fr 1fr",
    "__imgUrls_data": "",
    "__AD1_height": "200rpx",
    "__AD2_bottom": "0rpx",
    "__helpBtn_height": "80rpx",
    "__grid1_columnStr": "1fr 1fr",
    "__AD1_hidden": false,
    "__grid3_width": "730rpx",
    "__AD3_hidden": false,
    "__swiper_indicatorDots": "",
    "__swiper_current": "",
    "__AD2_width": "750rpx",
    "__grid3_column": 2,
    "__AD2_hidden": false,
    "__grid1_column": 2,
    "__AD3_height": "240rpx",
    "__helpBtn_disabled": ""
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx2374ed010f4bd862", "MainPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx2374ed010f4bd862', 'main', 'MainPage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})