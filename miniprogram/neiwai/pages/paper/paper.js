const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onImageTap_Aa84AS:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxe2deea3328cc56e0', 'main', 'ongg', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__hhh_width": "500rpx",
    "__radio3_fontSize": "35rpx",
    "__radiotext_fontSize": "35rpx",
    "__radiotext_left": "70rpx",
    "__ggg_top": "0rpx",
    "__radio3_color": "",
    "__radio3_checked": "",
    "__ggg_height": "125rpx",
    "__radiotext_top": "150rpx",
    "__ggg_hidden": true,
    "__ggg_left": "0rpx",
    "__hhh_src": "",
    "__radiotext_color": "#040404",
    "__radio3_height": "100rpx",
    "__radio3_value": "",
    "__radiotext_width": "600rpx",
    "__ggg_src": "http://material.motimaster.com/harvey///461a86c0052304000b0271c8e0b38388.jpeg",
    "__ggg_width": "750rpx",
    "__radio3_top": "580rpx",
    "__radiotext_backgroundColor": "#fbfdf7",
    "__hhh_height": "400rpx",
    "__radio3_data": "",
    "__hhh_left": "0rpx",
    "__hhh_top": "230rpx",
    "__radio3_left": "70rpx",
    "objects": [
        "ggg",
        "hhh",
        "radio3",
        "radiotext"
    ],
    "__hhh_hidden": false,
    "__radio3_width": "620rpx",
    "__radio3_disabled": "",
    "__hhh_right": "0rpx"
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
                    var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `题目加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxe2deea3328cc56e0', 'main', 'RadioPageready', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onRadioGroupChange_5rOoFK:  function(evt) {
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

                var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxe2deea3328cc56e0', 'main', 'onNext', evt);
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
                        this.data.__share_page = 'first'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wxe2deea3328cc56e0", "paper", self, {});
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
})