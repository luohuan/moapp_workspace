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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "paper", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `题目加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'RadioPageready', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onRadioGroupChange_u9rkb3:  function(evt) {
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

                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "paper", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'onNext', evt);
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "paper", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "paper", self, {});
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "paper", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "__radioim_width": "300rpx",
    "__radiotext_color": "#040404",
    "__radio3_color": "",
    "__radio3_value": "",
    "__radiotext_fontSize": "35rpx",
    "__radioim_src": "",
    "__radiotext_width": "600rpx",
    "__radio3_checked": "",
    "__radioim_top": "250rpx",
    "__radiotext_backgroundColor": "#fbfdf7",
    "__radio3_disabled": "",
    "__radio3_top": "600rpx",
    "__radio3_data": "",
    "objects": [
        "radio3",
        "radiotext",
        "radioim"
    ],
    "__radiotext_top": "30rpx",
    "__radiotext_left": "70rpx",
    "__radioim_height": "300rpx",
    "__radio3_width": "620rpx",
    "__radioim_left": "0rpx",
    "__radioim_right": "0rpx",
    "__radio3_height": "140rpx",
    "__radio3_left": "70rpx",
    "__radio3_fontSize": "35rpx"
},
})