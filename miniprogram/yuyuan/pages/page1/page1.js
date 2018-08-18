const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'page1Ready', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    formIdHandler: function (e) {
                        var appid= `wx468ad783f165eea0`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    data: {
    "__btn_fontSize": "18px",
    "__hostAvatar_top": "20rpx",
    "__hostName_left": "0rpx",
    "__things_width": "100%",
    "__helpBtn_hidden": true,
    "__btn_disabled": "",
    "__hostName_top": "0rpx",
    "__btn_right": "0rpx",
    "__hostAvatar_src": "",
    "__helpBtn_disabled": "",
    "__btn_text": "\u786e\u5b9a",
    "__helpBtn_height": "70rpx",
    "objects": [
        "hostAvatar",
        "hostName",
        "helpBtn",
        "things",
        "btn"
    ],
    "__btn_left": "0rpx",
    "__hostAvatar_right": "0rpx",
    "__hostName_right": "0rpx",
    "__hostName_width": "inherit",
    "__hostAvatar_height": "150rpx",
    "__hostName_color": "#FFFFFF",
    "__helpBtn_width": "70rpx",
    "__helpBtn_top": "70rpx",
    "__things_columnStr": "1fr 1fr 1fr",
    "__hostAvatar_left": "0rpx",
    "__btn_backgroundColor": "#FEB621",
    "__hostName_height": "inherit",
    "__things_column": 3,
    "__hostAvatar_width": "150rpx",
    "__btn_top": "1030rpx",
    "__things_data": "",
    "__helpBtn_left": "650rpx"
},
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
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
                        this.data.__share_page = 'begin'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, {});
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
    onViewTap_UU3b2x:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                index: evt.data.index,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'makeChioce', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_pjJlBV:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx468ad783f165eea0", "page1", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx468ad783f165eea0', 'main', 'submit', evt);
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
})