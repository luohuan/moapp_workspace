const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    onSelectorPickerChange_Ji9Q41:  function(evt) {
                var self = this;
                
            self.setData({
                __picker1_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.onSelectorPickerTextChange', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "objects": [
        "picker1"
    ],
    "__picker1_text": "\u70b9\u51fb\u9009\u62e9",
    "__picker1_value": "",
    "__picker1_disabled": "",
    "__picker1_range": [
        "\u6c34\u74f6\u5ea7",
        "\u53cc\u9c7c\u5ea7",
        "\u767d\u7f8a\u5ea7",
        "\u91d1\u725b\u5ea7",
        "\u53cc\u5b50\u5ea7",
        "\u5de8\u87f9\u5ea7",
        "\u72ee\u5b50\u5ea7",
        "\u5904\u5973\u5ea7",
        "\u5929\u67b0\u5ea7",
        "\u5929\u874e\u5ea7",
        "\u5c04\u624b\u5ea7",
        "\u6469\u7faf\u5ea7"
    ],
    "__picker1_color": "black",
    "__picker1_width": "200rpx",
    "__picker1_height": "200rpx",
    "__picker1_left": "0rpx",
    "__picker1_top": "88rpx",
    "__picker1_right": "0rpx",
    "__picker1_fontSize": "26rpx",
    "__picker1_opacity": 0.8
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
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
                        this.data.__share_page = 'index'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
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