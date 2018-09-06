const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onGetUserInfo_ZC32i5:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onViewTap_U9QGwR:  function(evt) {
                var self = this;
                
            self.setData({
                __dormitorylist_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                url: evt.data.url,
type: evt.data.type,
appid: evt.data.appid,
path: evt.data.path,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'liebiao2', 'firstpage.go_mini', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_WZXo2A:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: evt.data.url,
name: evt.data.name,

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.navigateTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx08fe2b1ff0c169f2`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    data: {
    "__swiper1_current": "",
    "__swiper1_top": "15rpx",
    "__swiper1_width": "750rpx",
    "__swiper1_indicatorActiveColor": "#FF8C69",
    "__dormitorydata_data": "",
    "__swiper1_left": "0rpx",
    "__dormitorylist_data": "",
    "__swiper1_autoplay": true,
    "objects": [
        "swiper1",
        "dormitorydata",
        "dormitorylist"
    ],
    "__dormitorylist_left": "0rpx",
    "__swiper1_height": "300rpx",
    "__dormitorylist_top": "400rpx",
    "__swiper1_indicatorDots": true
},
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
                        this.data.__share_page = 'firstpage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, {});
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
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'liebiao2', 'firstpage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "firstpage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})