const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onGetUserInfo_392LTJ:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'submit', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onViewTap_LMotaN:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                index: evt.data.index,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'makeChioce', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    data: {
    "objects": [
        "hostAvatar",
        "hostName",
        "helpBtn",
        "things",
        "btn"
    ],
    "__btn_disabled": "",
    "__hostAvatar_top": "20rpx",
    "__things_column": 3,
    "__hostName_color": "#FFFFFF",
    "__hostName_top": "0rpx",
    "__hostAvatar_right": "0rpx",
    "__things_columnStr": "1fr 1fr 1fr",
    "__btn_backgroundColor": "#FEB621",
    "__hostAvatar_height": "150rpx",
    "__helpBtn_hidden": true,
    "__helpBtn_width": "70rpx",
    "__hostAvatar_src": "",
    "__hostAvatar_width": "150rpx",
    "__hostAvatar_left": "0rpx",
    "__hostName_height": "inherit",
    "__hostName_width": "inherit",
    "__things_data": "",
    "__btn_text": "\u786e\u5b9a",
    "__btn_top": "1030rpx",
    "__helpBtn_left": "650rpx",
    "__btn_left": "0rpx",
    "__btn_fontSize": "18px",
    "__things_width": "100%",
    "__hostName_right": "0rpx",
    "__helpBtn_disabled": "",
    "__btn_right": "0rpx",
    "__helpBtn_top": "70rpx",
    "__helpBtn_height": "70rpx",
    "__hostName_left": "0rpx"
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, {});
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
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page1", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'fs', 'page1Ready', evt);
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