const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
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
                        this.data.__share_page = 'indexPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            //console.log(res);
                            console.log(`/pages/${self.data.__share_page}/${self.data.__share_page}?`+options)
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "sharePage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "sharePage", self, {});
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

                    console.log(`share page info:
/pages/${self.data.__share_page}/${self.data.__share_page}?`+options);

                    return shareInfo;                
                },
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "sharePage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
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
    data: {
    "__no_result_box_width": "750rpx",
    "__text1_height": "140rpx",
    "__btn_box_right": "0rpx",
    "__send_left": "0rpx",
    "__text1_width": "370rpx",
    "__btn_box_left": "0rpx",
    "__share_width": "402rpx",
    "__send_disabled": "",
    "__shareImage_height": "750rpx",
    "__btn_box_width": "750rpx",
    "__shareImage_top": "0rpx",
    "__text1_hidden": true,
    "__share_height": "90rpx",
    "__text1_right": "0rpx",
    "__send_width": "402rpx",
    "__text1_background": "#ffffff",
    "objects": [
        "no_result_box",
        "text1",
        "shareImage",
        "btn_box",
        "send",
        "share"
    ],
    "__shareImage_src": "",
    "__share_right": "0rpx",
    "__shareImage_left": "0rpx",
    "__share_left": "0rpx",
    "__shareImage_width": "750rpx",
    "__send_top": "0rpx",
    "__no_result_box_left": "0rpx",
    "__text1_top": "550rpx",
    "__text1_left": "0rpx",
    "__no_result_box_top": "0rpx",
    "__share_top": "134rpx",
    "__send_right": "0rpx",
    "__btn_box_top": "930rpx",
    "__share_disabled": "",
    "__send_height": "90rpx"
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "sharePage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'sharePage.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onGetUserInfo_MsSjQu:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "sharePage", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'sharePage.onSaveImage', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
})