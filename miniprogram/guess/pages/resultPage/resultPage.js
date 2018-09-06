const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    data: {
    "__AD1_left": "0rpx",
    "__AD1_width": "750rpx",
    "__AD1_height": "125rpx",
    "__AD1_top": "990rpx",
    "objects": [
        "AD1"
    ],
    "__AD1_hidden": false
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
                        this.data.__share_page = 'mainPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, {});
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
                    var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onResultReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
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
    onButtonTap_xp3NTT:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'resetIndexList', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onButtonTap_UVIbOw:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "resultPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onSaveImage', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
})