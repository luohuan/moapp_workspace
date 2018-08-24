const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'beginReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_In04t5:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'indexsubmit', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    data: {
    "__hostName_top": "0rpx",
    "__imageAvatar_right": "0rpx",
    "__tip_color": "#FFD886",
    "__helpBtn_width": "70rpx",
    "__imageAvatar_left": "0rpx",
    "__things_width": "100%",
    "__hostName_width": "inherit",
    "__btn_backgroundColor": "#FEB621",
    "__tip_left": "0rpx",
    "__entrance_width": "750rpx",
    "__entrance_top": "0rpx",
    "__btn_disabled": "",
    "__hostName_left": "0rpx",
    "__hostName_right": "0rpx",
    "__btn_top": "1030rpx",
    "__things_columnStr": "1fr 1fr 1fr",
    "__loading_box_top": "0rpx",
    "objects": [
        "entrance",
        "imageAvatar",
        "tip",
        "hostName",
        "helpBtn",
        "things",
        "btn",
        "loading_box"
    ],
    "__helpBtn_height": "70rpx",
    "__things_column": 3,
    "__btn_fontSize": "18px",
    "__helpBtn_left": "650rpx",
    "__btn_text": "\u786e\u5b9a",
    "__helpBtn_hidden": true,
    "__imageAvatar_top": "10rpx",
    "__hostName_height": "inherit",
    "__btn_left": "0rpx",
    "__helpBtn_disabled": "",
    "__things_data": "",
    "__entrance_hidden": true,
    "__loading_box_width": "750rpx",
    "__btn_right": "0rpx",
    "__entrance_left": "0rpx",
    "__hostName_color": "#FFFFFF",
    "__imageAvatar_width": "120rpx",
    "__tip_text": "\u3010\u8bbe\u7f6e\u4f60\u7684\u6ee1\u5206\u597d\u53cb\u6807\u51c6\u3011",
    "__tip_top": "130rpx",
    "__imageAvatar_height": "120rpx",
    "__tip_right": "0rpx",
    "__helpBtn_top": "70rpx",
    "__loading_box_left": "0rpx"
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
                        this.data.__share_page = 'begin'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, {});
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
    formIdHandler: function (e) {
                        var appid= `wxaa8fe119f5c62d23`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onViewTap_lIuUoj:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                index: evt.data.index,

            }
            ;
            return moapp.requestCloudFunction(self, 'wxaa8fe119f5c62d23', 'main', 'makeChioce', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wxaa8fe119f5c62d23", "begin", self, {});
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
})