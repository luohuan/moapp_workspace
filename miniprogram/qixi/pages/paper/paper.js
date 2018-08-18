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
    onImageTap_ZbTsd9:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'GotoGame', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onRadioGroupChange_GWLS85:  function(evt) {
                var self = this;
                
            self.setData({
                __radio3_value: evt.detail.value
            })
            ;

                 const datas = self.data.__radio3_data
                    for(const d of datas){
                      //console.log(d.value)
                      //console.log(evt.detail.value)
                      if(d.value == evt.detail.value){
                        d.cls = 'choosed'
                      }else{
                        d.cls = 'normal'
                      }
                    }
                    console.log(datas)
                    self.setData({
                      __radio3_data: datas
                    })

                var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'onNext', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onImageTap_UZ17XL:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'previewimage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__radio3_checked": "",
    "__questionImg_width": "380rpx",
    "__radiotext_fontSize": "35rpx",
    "__radio3_left": "70rpx",
    "objects": [
        "questionImg",
        "radio3",
        "radiotext",
        "adbox",
        "game_img"
    ],
    "__questionImg_src": "",
    "__adbox_top": "1000rpx",
    "__radiotext_backgroundColor": "#fbfdf7",
    "__radio3_fontSize": "35rpx",
    "__game_img_height": "175rpx",
    "__game_img_width": "750rpx",
    "__questionImg_top": "10rpx",
    "__radio3_disabled": "",
    "__radiotext_color": "#040404",
    "__adbox_hidden": true,
    "__radio3_width": "660rpx",
    "__radiotext_left": "70rpx",
    "__adbox_width": "750rpx",
    "__radio3_color": "",
    "__game_img_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__radiotext_top": "290rpx",
    "__adbox_height": "175rpx",
    "__radio3_height": "130rpx",
    "__questionImg_left": "180rpx",
    "__radio3_data": "",
    "__radiotext_width": "600rpx",
    "__questionImg_height": "270rpx",
    "__radio3_top": "410rpx",
    "__radio3_value": ""
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
                        this.data.__share_page = 'first'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, {});
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
                    var evt_data = moapp.genEventData("wx47b494af03bd0aae", "paper", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `题目加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx47b494af03bd0aae', 'main', 'RadioPageready', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})