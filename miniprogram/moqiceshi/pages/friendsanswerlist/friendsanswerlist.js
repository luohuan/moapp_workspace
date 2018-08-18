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
    onViewTap_2LNnJi:  function(evt) {
                var self = this;
                
            self.setData({
                __friends_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
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
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, {});
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
    data: {
    "__Alert_top": "85rpx",
    "__btn_color": "#FFFFFF",
    "__btn_fontWeight": "bold",
    "__shareBtn_top": "0rpx",
    "__scoreimage_src": "http://material.motimaster.com/appmaker/menlu/3725.png",
    "__btn_disabled": "",
    "__shareBtn_hidden": true,
    "__helpBtn_height": "70rpx",
    "__friendlist_scrollLeft": "",
    "__btn_backgroundColor": "#c64342",
    "__btn_hidden": true,
    "__btn_top": "0rpx",
    "__scoreimage_left": "345rpx",
    "__helpBtn_width": "70rpx",
    "__scoreimage2_left": "280rpx",
    "__shareBtn_color": "#FFFFFF",
    "__friendlist_scrollTop": "",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u56de\u7b54",
    "__scoreimage_width": "300rpx",
    "__Alert_text": "\u5feb\u9080\u8bf7\u597d\u53cb\u6765\u56de\u7b54\uff0c\u6d4b\u6d4b\u4f60\u4eec\u8111\u56de\u8def\u7684\u76f8\u4f3c\u5ea6\u5427\uff01\uff01",
    "__helpBtn_left": "15rpx",
    "__friendlist_top": "150rpx",
    "__Alert_left": "0rpx",
    "__shareBtn_right": "0rpx",
    "__shareBtn_disabled": "",
    "__Alert_color": "#1b272e",
    "__Alert_height": "280rpx",
    "__btn_text": "\u9080\u8bf7\u597d\u53cb\u6765\u56de\u7b54",
    "__shareBtn_width": "360rpx",
    "__btn_height": "88rpx",
    "__Alert_width": "500rpx",
    "__btn_left": "0rpx",
    "__helpBtn_top": "15rpx",
    "__friendlist_right": "0rpx",
    "__friendlist_height": "500rpx",
    "__shareBtn_fontWeight": "bold",
    "__btn_width": "360rpx",
    "__shareBtn_backgroundColor": "#c64342",
    "__scoreimage2_width": "160rpx",
    "__friends_data": "",
    "__scoreimage2_top": "70rpx",
    "__Alert_right": "0rpx",
    "__Alert_fontSize": "13px",
    "__helpBtn_disabled": "",
    "__shareBtn_fontSize": "18px",
    "__shareBtn_height": "88rpx",
    "__scoreimage_top": "40rpx",
    "__friendlist_left": "0rpx",
    "__scoreimage2_height": "166rpx",
    "__friendlist_width": "623rpx",
    "__scoreimage_height": "300rpx",
    "__btn_right": "0rpx",
    "__scoreimage2_src": "http://material.motimaster.com/appmaker/menlu/3745.png",
    "objects": [
        "scoreimage",
        "scoreimage2",
        "helpBtn",
        "friendlist",
        "Alert",
        "friends",
        "btn",
        "shareBtn"
    ],
    "__shareBtn_left": "0rpx",
    "__btn_fontSize": "18px"
},
    onButtonTap_M76Hwy:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'findNewData', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "friendsanswerlist", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'moqiceshi07133', 'GuestInfoLists', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
})