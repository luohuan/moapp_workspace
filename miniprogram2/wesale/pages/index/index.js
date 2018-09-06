const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    onCheckBoxGroupChang2e_OA8sFB:  function(evt) {
                var self = this;
                
            self.setData({
                __swiper3_value: evt.detail.current
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.current);               
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onImageTap_f5i9iO:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                index: evt.data.index,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.clickBanner', evt);
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onViewTap_QifJ3r:  function(evt) {
                var self = this;
                
            self.setData({
                __list1_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    onImageTap_T55lWN:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            var params = 
            {
                page: "goods_info",
goods_id: evt.data.goodsid,

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
    onSelectorPickerChange_etS4RV:  function(evt) {
                var self = this;
                
            self.setData({
                __picker2_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "index", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.onSelectorPickerButtonChange', evt);
            }
            ).catch( err => {console.log("Event exception, err:");console.log(JSON.stringify(err));})
            }
            ,
    data: {
    "objects": [
        "swiper3",
        "imgUrls",
        "list1",
        "picker2"
    ],
    "__swiper3_current": "",
    "__swiper3_indicatorDots": "",
    "__swiper3_autoplay": true,
    "__swiper3_indicatorActiveColor": "",
    "__swiper3_value": "",
    "__swiper3_width": "750rpx",
    "__swiper3_height": "285rpx",
    "__swiper3_top": "0rpx",
    "__imgUrls_data": "",
    "__list1_data": "",
    "__picker2_text": "\u5546\u54c1\u5c5e\u6027",
    "__picker2_value": "",
    "__picker2_disabled": "",
    "__picker2_range": [
        "\u5168\u90e8",
        "\u51fa\u552e",
        "\u6c42\u8d2d",
        "\u8d60\u9001"
    ],
    "__picker2_color": "#F4bc33",
    "__picker2_width": "150rpx",
    "__picker2_height": "60rpx",
    "__picker2_background": "rgba(255,255,255,0.50)",
    "__picker2_left": "0rpx",
    "__picker2_top": "0rpx",
    "__picker2_fontSize": "30rpx"
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
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.onInit', evt);
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
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'index.onShow', evt);
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
                            console.log(res);
                            
                            
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
})