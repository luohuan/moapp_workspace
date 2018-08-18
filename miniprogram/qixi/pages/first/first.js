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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    data: {
    "__game_img_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__game_img_width": "750rpx",
    "__adbox_top": "950rpx",
    "objects": [
        "adbox",
        "game_img"
    ],
    "__adbox_width": "750rpx",
    "__game_img_height": "175rpx",
    "__adbox_hidden": true,
    "__adbox_height": "175rpx"
},
    formIdHandler: function (e) {
                        var appid= `wx47b494af03bd0aae`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onImageTap_JHmrLO:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'GotoGame', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_1O3Ky0:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                drama_list: "测试",
page: "paper",

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.navigateTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
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
                        this.data.__share_page = 'first'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, {});
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
                    var evt_data = moapp.genEventData("wx47b494af03bd0aae", "first", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'firstReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})