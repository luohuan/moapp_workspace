const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onGetUserInfo_QzMrgV:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'yinxiangfazhan', 'page8.onSaveImage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
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
    formIdHandler: function (e) {
                        var appid= `wx08fe2b1ff0c169f2`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    data: {
    "__mopicImage_height": "1220rpx",
    "__mopicImage_left": "0rpx",
    "__avtar_width": "164rpx",
    "__avtar_top": "502rpx",
    "__avtar_left": "293rpx",
    "__mopicImage_src": "",
    "__avtar_height": "164rpx",
    "objects": [
        "mopicImage",
        "avtar"
    ],
    "__mopicImage_top": "0rpx",
    "__mopicImage_width": "720rpx",
    "__avtar_hidden": true,
    "__mopicImage_right": "0rpx"
},
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
                        this.data.__share_page = 'firstpage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, {});
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onImageAvatarTap_rps8JO:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            wx.showToast({
              title: `111`,
              icon: 'success',
              image:undefined,
              duration: 1500
            })

            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'yinxiangfazhan', 'page8.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_DPJO5X:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page8", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: "firstpage",

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
})