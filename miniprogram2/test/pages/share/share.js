const app = getApp();
const moapp = require("../../utils/moapp.js"); 

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
    onSelectorPickerChange_zGoWwE:  function(evt) {
                var self = this;
                
            self.setData({
                __templatetitle_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'share.choose_template', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    data: {
    "__templatetitle_text": "\u9762\u8bd5\u9080\u8bf7\u901a\u77e5",
    "__templatetitle_top": "65rpx",
    "__templatetitle_height": "90rpx",
    "__templatetitle_background": "#256df3",
    "__templatetitle_fontSize": "40rpx",
    "__templatetitle_width": "600rpx",
    "objects": [
        "templatetitle"
    ],
    "__templatetitle_left": "0rpx",
    "__templatetitle_range": [
        "232",
        "2323"
    ],
    "__templatetitle_color": "white",
    "__templatetitle_right": "0rpx",
    "__templatetitle_disabled": "",
    "__templatetitle_value": ""
},
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
                        this.data.__share_page = 'share'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
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
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "share", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
})