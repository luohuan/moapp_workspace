const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page3", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onButtonTap_OhOOGs:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page3", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: "page4",

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.navigateTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
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
    data: {
    "__fenxiang_fontSize": "30rpx",
    "objects": [
        "fenxiang"
    ],
    "__fenxiang_left": "0rpx",
    "__fenxiang_text": "\u9080\u8bf7\u597d\u53cb\u6765\u6d4b",
    "__fenxiang_color": "#FFFFFF",
    "__fenxiang_height": "80rpx",
    "__fenxiang_background": "#5e5ca5",
    "__fenxiang_width": "300rpx",
    "__fenxiang_disabled": "",
    "__fenxiang_right": "0rpx",
    "__fenxiang_top": "900rpx"
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
                        this.data.__share_page = 'page1'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page3", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "page3", self, {});
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