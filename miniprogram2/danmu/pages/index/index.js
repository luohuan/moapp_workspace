const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    itemtap_rEsiA6:  function(evt) {
                var self = this;
                
            self.setData({
                __danmu_value: evt.detail.value
            })
            
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'danmutest', 'test', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onButtonTap_OaoP91:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: "second",

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.navigateTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onInputChange_kKrezg:  function(evt) {
                var self = this;
                
            self.setData({
                __inputDanmu_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.value);
               
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'danmutest', 'InputOnChange', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onGetUserInfo_xhKwQ9:  function(evt) {
                    var self = this;

                    if (evt.detail.userInfo) {
                        app.globalData.userInfo = evt.detail.userInfo;

                        var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset);
                        Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'danmutest', 'sendBarrage', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                    } else {
                        console.log('get user info fail! error message:' + evt.detail.errMsg);
                    }
                }
                ,
    onButtonTap_yl2O4q:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                id: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'danmutest', 'onRecommandTap', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onCheckBoxGroupChang2e_9pn4Eu:  function(evt) {
                var self = this;
                
            self.setData({
                __tip2_value: evt.detail.current
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.current);               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    data: {
    "objects": [
        "danmu",
        "inputDanmu",
        "recommands",
        "tip2",
        "imgUrls"
    ],
    "__danmu_data": "",
    "__danmu_value": "",
    "__danmu_danmuFontSize": 25,
    "__danmu_danmuLineHeight": 35,
    "__danmu_danmuBackground": "linear-gradient(to right, rgba(255,255,255,1), rgba(255,255,255,0))",
    "__danmu_danmuStyle": "",
    "__danmu_danmuTailImage": "",
    "__danmu_danmuAvatarStyle": "width:35rpx;height:35rpx;left:0;",
    "__danmu_danmuTailImageStyle": "",
    "__danmu_danmuTeadImage": "",
    "__danmu_danmuHeadImageStyle": "",
    "__danmu_danmuHeight": 35,
    "__danmu_danmuMargin": 20,
    "__danmu_danmuRowNumber": 5,
    "__inputDanmu_placeholder": "",
    "__inputDanmu_value": "",
    "__inputDanmu_color": "white",
    "__inputDanmu_width": "400rpx",
    "__inputDanmu_height": "60rpx",
    "__inputDanmu_left": "50rpx",
    "__inputDanmu_bottom": "320rpx",
    "__inputDanmu_fontSize": "27rpx",
    "__recommands_data": "",
    "__recommands_left": "50rpx",
    "__recommands_bottom": "150rpx",
    "__tip2_current": "",
    "__tip2_indicatorDots": "",
    "__tip2_autoplay": true,
    "__tip2_indicatorActiveColor": "",
    "__tip2_value": "",
    "__tip2_width": "200rpx",
    "__tip2_height": "60rpx",
    "__tip2_left": "50rpx",
    "__tip2_bottom": "320rpx",
    "__imgUrls_data": ""
},
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'danmutest', 'indexReady', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
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
                        this.data.__share_page = 'index'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            //console.log(res);
                            console.log(`/pages/${self.data.__share_page}/${self.data.__share_page}?`+options)
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, {});
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

                    console.log(`share page info:
/pages/${self.data.__share_page}/${self.data.__share_page}?`+options);

                    return shareInfo;                
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
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    formIdHandler: function (e) {
                        var appid= `wx263b9c72fc87b39c`
                        moapp.submitFormId(appid, e.detail.formId)

                    },
})