const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, {});
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
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
    onViewTap_aJ0xvv:  function(evt) {
                var self = this;
                
            self.setData({
                __friends_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onGetUserInfo_mGpDE5:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'entranceReady', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    data: {
    "__solgn_left": "0rpx",
    "__resulename_fontWeight": "bold",
    "__scoreimage_src": "http://material.motimaster.com/appmaker/menlu/3861.png",
    "__helpBtn_height": "70rpx",
    "__solgn_color": "#000000",
    "__score_top": "285rpx",
    "__friendlist_scrollLeft": "",
    "__scoreimage_left": "0rpx",
    "__solgn_top": "400rpx",
    "__helpBtn_width": "70rpx",
    "__metoo_top": "495rpx",
    "__solgn_fontSize": "15px",
    "__solgn_right": "0rpx",
    "__metoo_backgroundColor": "#c64342",
    "__friendlist_scrollTop": "",
    "__scoreimage_width": "500rpx",
    "__scoreimage2_src": "http://material.motimaster.com/appmaker/menlu/3745.png",
    "__friendlist_top": "690rpx",
    "__metoo_text": "\u6211\u4e5f\u8981\u51fa\u9898",
    "__metoo_left": "188rpx",
    "__scoreimage_right": "0rpx",
    "__helpBtn_top": "535rpx",
    "__resulename_fontSize": "20px",
    "__friendlist_height": "550rpx",
    "__score_fontSize": "20px",
    "__scoreimage2_width": "85rpx",
    "__metoo_width": "363rpx",
    "__scoreimage2_top": "162rpx",
    "__metoo_color": "#FFFFFF",
    "__metoo_disabled": "",
    "__helpBtn_left": "600rpx",
    "__scoreimage_height": "500rpx",
    "__helpBtn_disabled": "",
    "__scoreimage_top": "10rpx",
    "__friendlist_left": "76rpx",
    "__scoreimage2_left": "200rpx",
    "__resulename_top": "30rpx",
    "__scoreimage2_height": "85rpx",
    "__metoo_height": "90rpx",
    "__friendlist_width": "623rpx",
    "__resulename_left": "0rpx",
    "__resulename_color": "#000000",
    "__score_color": "#b4205e",
    "objects": [
        "resulename",
        "helpBtn",
        "scoreimage",
        "scoreimage2",
        "score",
        "solgn",
        "friendlist",
        "friends",
        "metoo"
    ],
    "__friends_data": "",
    "__score_left": "200rpx",
    "__resulename_right": "0rpx",
    "__metoo_fontSize": "15px"
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
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "relationshipresult", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'onCompareAnswer', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})