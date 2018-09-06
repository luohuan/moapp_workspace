const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onRadioGroupChange_ansnFm:  function(evt) {
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

                var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page10", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'xiaoshirenge', 'page10.onNext', evt);
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
                        this.data.__share_page = 'firstpage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page10", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page10", self, {});
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
    "__radiotext_color": "#040404",
    "__questionImg_width": "364rpx",
    "__questionImg_right": "0rpx",
    "__radiotext_fontSize": "35rpx",
    "__radio3_data": "",
    "__radiotext_left": "70rpx",
    "__radiotext_top": "390rpx",
    "__questionImg_src": "",
    "__radio3_color": "",
    "__radiotext_backgroundColor": "#fbfdf7",
    "__questionImg_left": "0rpx",
    "__radiotext_width": "600rpx",
    "__radio3_top": "510rpx",
    "__radio3_fontSize": "35rpx",
    "__radio3_height": "130rpx",
    "__radio3_checked": "",
    "__radio3_disabled": "",
    "objects": [
        "questionImg",
        "radio3",
        "radiotext"
    ],
    "__radio3_width": "660rpx",
    "__radio3_left": "70rpx",
    "__questionImg_height": "358rpx",
    "__questionImg_top": "55rpx",
    "__radio3_value": ""
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page10", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx08fe2b1ff0c169f2', 'xiaoshirenge', 'page10.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx08fe2b1ff0c169f2", "page10", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})