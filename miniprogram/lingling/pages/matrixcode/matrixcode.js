const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    data: {
    "objects": [
        "mopicImage"
    ],
    "__mopicImage_width": "650rpx",
    "__mopicImage_src": "",
    "__mopicImage_left": "50rpx",
    "__mopicImage_top": "50rpx",
    "__mopicImage_height": "650rpx"
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "matrixcode", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'CreatMatrixCode', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "matrixcode", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
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
    onButtonTap_p2NE2k:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "matrixcode", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'save', evt);
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "matrixcode", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "matrixcode", self, {});
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