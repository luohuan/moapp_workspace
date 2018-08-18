const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    data: {
    "__dataGrid_width": "690rpx",
    "__morefun_disabled": "",
    "__tips_height": "67rpx",
    "__anslist_height": "70rpx",
    "__AD1_left": "0rpx",
    "__current_count_left": "318rpx",
    "__percent_fontSize": "57rpx",
    "__dataGrid_left": "0rpx",
    "__coin_width": "240rpx",
    "__mask01_left": "0rpx",
    "__honorary_title_left": "0rpx",
    "__tips_text": "\u63d0\u793a-30\ud83d\udcb0",
    "__mask01_top": "0rpx",
    "__percent_color": "#f35c5c",
    "__honorary_title_fontSize": "58rpx",
    "__morefun_text": "\u66f4\u591a\u597d\u73a9",
    "__dataGrid_right": "0rpx",
    "__anslist_data": "",
    "__tips_top": "548rpx",
    "__dataGrid_height": "200rpx",
    "__anslist_right": "0rpx",
    "__dataGrid_columnStr": "1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr",
    "__AD1_hidden": false,
    "__coin_text": "\ud83d\udcb0\u91d1\u5e01:20",
    "__mask01_background": "RGBA(0, 0, 0, 0.7)",
    "__picture_height": "270rpx",
    "__dataGrid_data": "",
    "__honorary_title_color": "#ff0000",
    "__current_count_color": "#f35c5c",
    "__mask01_height": "100%",
    "__anslist_left": "0rpx",
    "__coin_top": "548rpx",
    "__tips_right": "0rpx",
    "__percent_left": "219rpx",
    "__tips_left": "0rpx",
    "__picture_width": "432rpx",
    "__q_num_top": "0rpx",
    "__mask01_hidden": true,
    "__q_num_right": "0rpx",
    "__current_count_fontSize": "58rpx",
    "__honorary_title_top": "62rpx",
    "__q_num_color": "#ff0000",
    "__picture_left": "133rpx",
    "__coin_left": "40rpx",
    "__morefun_left": "500rpx",
    "__dataGrid_column": 8,
    "__honorary_title_right": "0rpx",
    "__tips_disabled": "",
    "__tips_width": "210rpx",
    "__current_count_top": "332rpx",
    "__morefun_width": "210rpx",
    "__AD1_top": "990rpx",
    "__AD1_width": "750rpx",
    "__morefun_height": "67rpx",
    "__AD1_height": "125rpx",
    "__coin_height": "67rpx",
    "__q_num_left": "0rpx",
    "__mask01_width": "100%",
    "objects": [
        "q_num",
        "picture",
        "coin",
        "tips",
        "morefun",
        "anslist",
        "dataGrid",
        "AD1",
        "mask01",
        "current_count",
        "percent",
        "honorary_title"
    ],
    "__morefun_top": "20rpx",
    "__picture_top": "149rpx",
    "__anslist_top": "654rpx",
    "__percent_top": "420rpx",
    "__q_num_fontSize": "40rpx",
    "__dataGrid_top": "743rpx",
    "__picture_src": "",
    "__anslist_width": "750rpx"
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onGuessReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_12UAK7:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                id: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onAnswerClick', evt);
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
                        this.data.__share_page = 'mainPage'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, {});
                            Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'shareOptions', evt);
            }
            )
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, {});
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
                    var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_dTVhYn:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                tag: evt.data.tag,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onClick', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_2cb7VK:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onSaveImage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_qjdKVK:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onMoreFun', evt);
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
    onButtonTap_UYgDBD:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onTipsClick', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onImageTap_WEfNEf:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onContinuePlay', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_E42zWU:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!true && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_X8GXlE:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx91f13354f5356b6c", "GuessPage", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx91f13354f5356b6c', 'main', 'onContinuePlay', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
})