const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onButtonTap_3oOorB:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                id: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'deleteItemData', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'GuestInfoLists', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onGetUserInfo_e3h3jF:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'Delete', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onViewTap_EvFpTH:  function(evt) {
                var self = this;
                
            self.setData({
                __friends_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_0MbtFo:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'findNewData', evt);
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
    "__scoreimage_top": "40rpx",
    "__scoreimage2_width": "160rpx",
    "__btn_disabled": "",
    "__btn_fontWeight": "bold",
    "__shareBtn_disabled": "",
    "__shareBtn_right": "0rpx",
    "__helpBtn_left": "15rpx",
    "__scoreimage_width": "300rpx",
    "__shareBtn_fontSize": "15px",
    "__scoreimage_height": "300rpx",
    "__helpBtn_top": "15rpx",
    "__shareBtn_height": "88rpx",
    "__scoreimage2_height": "166rpx",
    "__Alert_height": "280rpx",
    "__helpBtn_width": "70rpx",
    "__shareBtn_hidden": true,
    "__shareBtn_width": "255rpx",
    "__shareBtn_color": "#FFFFFF",
    "__btn_height": "88rpx",
    "__Alert_fontSize": "13px",
    "__Alert_top": "85rpx",
    "__friendlist_top": "150rpx",
    "__helpBtn_height": "70rpx",
    "__btn_left": "0rpx",
    "__scoreimage2_left": "280rpx",
    "__friendlist_height": "500rpx",
    "__Alert_color": "#1b272e",
    "__friendlist_scrollLeft": "",
    "__friendlist_right": "0rpx",
    "__Alert_width": "500rpx",
    "__btn_hidden": true,
    "__btn_color": "#FFFFFF",
    "__btn_backgroundColor": "#c64342",
    "__scoreimage2_top": "70rpx",
    "__shareBtn_text": "\u9080\u8bf7\u597d\u53cb\u5339\u914d",
    "__shareBtn_fontWeight": "bold",
    "__btn_fontSize": "15px",
    "__friendlist_left": "0rpx",
    "__shareBtn_top": "0rpx",
    "__scoreimage_left": "345rpx",
    "__scoreimage2_src": "http://material.motimaster.com/appmaker/menlu/3745.png",
    "__Alert_right": "0rpx",
    "__helpBtn_disabled": "",
    "__btn_top": "0rpx",
    "__shareBtn_backgroundColor": "#c64342",
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
    "__btn_right": "0rpx",
    "__friendlist_scrollTop": "",
    "__Alert_left": "0rpx",
    "__scoreimage_src": "http://material.motimaster.com/appmaker/menlu/3725.png",
    "__btn_text": "\u9080\u8bf7\u597d\u53cb\u5339\u914d",
    "__friendlist_width": "623rpx",
    "__btn_width": "255rpx",
    "__Alert_text": "\u76ee\u524d\u8fd8\u6ca1\u6709\u597d\u53cb\u548c\u4f60\u5339\u914d\u5466~\u5feb\u9080\u8bf7\u597d\u53cb\u5339\u914d\u5427\uff01",
    "__friends_data": "",
    "__shareBtn_left": "0rpx"
},
    formIdHandler: function (e) {
                        var appid= `wx87dcda9739af9cb1`
                        moapp.submitFormId(appid, e.detail.formId)

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
                            
                            
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "friendsanswerlist", self, {});
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