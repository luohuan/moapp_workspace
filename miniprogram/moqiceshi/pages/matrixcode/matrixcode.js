const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    onImageTap_AUk8Ko:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'onMoreFunTap', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, {});
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
    onButtonTap_TA3aDj:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'save', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__mopicImage_left": "50rpx",
    "__mopicImage_src": "",
    "__savebtnbefore_left": "0rpx",
    "__savebtnbefore_right": "0rpx",
    "__mopicImage_top": "50rpx",
    "__ljad_width": "750rpx",
    "__savebtnbefore_backgroundColor": "#ffffff",
    "__savebtnbefore_width": "456rpx",
    "__savebtnbefore_disabled": "",
    "__defaultImage_left": "50rpx",
    "__ad_height": "175rpx",
    "__defaultImage_height": "650rpx",
    "__savebtnbefore_top": "810rpx",
    "__savebtnbefore_height": "88rpx",
    "__savebtnbefore_text": "\u4fdd\u5b58\u6d77\u62a5",
    "__savebtnbefore_fontWeight": "bold",
    "__defaultImage_top": "50rpx",
    "__defaultImage_width": "650rpx",
    "__ljad_top": "1030rpx",
    "__ad_bottom": "0rpx",
    "__savebtnbefore_color": "#c64342",
    "__defaultImage_src": "",
    "__ad_width": "750rpx",
    "objects": [
        "mopicImage",
        "defaultImage",
        "savebtnbefore",
        "ad",
        "ljad"
    ],
    "__ljad_hidden": true,
    "__ljad_height": "91px",
    "__mopicImage_height": "650rpx",
    "__savebtnbefore_fontSize": "15px",
    "__mopicImage_width": "650rpx"
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "matrixcode", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'CreatMatrixCode', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})