const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    data: {
    "__questionImg_top": "30rpx",
    "__bg2_width": "100%",
    "__questionImg_height": "300rpx",
    "__radio3_checked": "",
    "__radiotext_backgroundColor": "#fbfdf7",
    "__radio3_width": "660rpx",
    "__bg2_src": "http://img.mogodeer.cn/image/xixi/yuelaoqianxian/bg2.jpg",
    "__bg2_height": "100%",
    "__radiotext_width": "600rpx",
    "__adbox_height": "175rpx",
    "__questionImg_left": "0rpx",
    "__questionImg_src": "",
    "__adbox_top": "1000rpx",
    "__questionImg_right": "0rpx",
    "__radio3_data": "",
    "__game_img_width": "750rpx",
    "__adbox_width": "750rpx",
    "__radiotext_left": "70rpx",
    "__radio3_left": "70rpx",
    "__radio3_value": "",
    "__radio3_top": "410rpx",
    "__radio3_disabled": "",
    "objects": [
        "bg2",
        "questionImg",
        "radio3",
        "radiotext",
        "adbox",
        "game_img"
    ],
    "__questionImg_width": "280rpx",
    "__game_img_height": "175rpx",
    "__radiotext_fontSize": "35rpx",
    "__radiotext_top": "290rpx",
    "__radio3_color": "",
    "__game_img_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__radio3_fontSize": "35rpx",
    "__adbox_hidden": true,
    "__radiotext_color": "#040404",
    "__radio3_height": "130rpx"
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
                            
                            
                            var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, {});
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
                    var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `题目加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'RadioPageready', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onImageTap_rO43dk:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'previewimage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onRadioGroupChange_IsuPQa:  function(evt) {
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

                var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'onNext', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onImageTap_HUKQQ0:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx021a5f382c69640e', 'main', 'GotoGame', evt);
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx021a5f382c69640e", "paper", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})