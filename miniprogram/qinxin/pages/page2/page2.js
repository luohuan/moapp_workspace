const app = getApp();
const moapp = require("../../utils/moapp.js"); 
const qiniuUploader = require("../../utils/qiniuUploader")
Page({
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
            wx.showLoading({
              title: `加载中...`,
              mask: true
            });

            return evt;
        }
        ).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.onInit', evt);
            }
            ).then( function(evt) {
            wx.hideLoading();
            return evt
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onViewTap_VPLUyb:  function(evt) {
                var self = this;
                
            self.setData({
                __zgrid_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_2FvnqK:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.showMask', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    data: {
    "__pyqt_left": "0rpx",
    "__zx_text": "\u518d\u5199\u4e00\u4e2a",
    "__my_right": "0rpx",
    "__qq_hidden": true,
    "__chats_fontSize": "25rpx",
    "__pyq_color": "white",
    "__box_scrollLeft": "",
    "__pyq_height": "240rpx",
    "__lwd_top": "550rpx",
    "__my_left": "0rpx",
    "__my_fontSize": "35rpx",
    "__hy_height": "200rpx",
    "__ztx_height": "130rpx",
    "__chats_width": "300rpx",
    "__lw_hidden": true,
    "__wx_text": "\u81ea\u5df1\u8bd5\u8bd5",
    "__hy_disabled": "",
    "__wx_disabled": "",
    "__xy_top": "115rpx",
    "__lw_height": "160rpx",
    "__zxd_hidden": true,
    "__pyqd_height": "290rpx",
    "__my_height": "20rpx",
    "__wx_left": "5rpx",
    "__zxd_left": "0rpx",
    "__lwd_hidden": true,
    "__sd_width": "300rpx",
    "__qq_width": "155rpx",
    "__pyqt_src": "",
    "__pyqt_right": "0rpx",
    "__zx_disabled": "",
    "__wxd_hidden": true,
    "__xy_hidden": true,
    "__chats_color": "white",
    "__pyq_width": "50rpx",
    "__wxd_background": "rgba(238,238,238,0.4)",
    "__ztx_left": "141rpx",
    "__mask01_hidden": true,
    "__ztx_width": "130rpx",
    "__zxd_background": "rgba(238,238,238,0.4)",
    "__cha_width": "40rpx",
    "__lw_left": "697rpx",
    "__my_color": "white",
    "__sd_top": "100rpx",
    "__mask01_top": "0rpx",
    "__wx_width": "50rpx",
    "__zxd_width": "60rpx",
    "__pyqd_hidden": true,
    "__hy_width": "50rpx",
    "__cha_hidden": true,
    "__hyd_width": "60rpx",
    "__cha_left": "585rpx",
    "__sd_left": "290rpx",
    "__hyd_hidden": true,
    "__lw_width": "50rpx",
    "__lwd_width": "60rpx",
    "__pyqd_width": "60rpx",
    "__hyd_left": "690rpx",
    "__hy_color": "white",
    "__qq_src": "http://material.motimaster.com/aelegy1532068254000/b885b4c063fa0e7d17d8392934321164.png",
    "__pyqd_background": "rgba(238,238,238,0.4)",
    "__zx_left": "5rpx",
    "__cha_src": "http://material.motimaster.com/aelegy1532309104000/6657e831422976be16417e982a3bd617\u526f\u672c.png",
    "__zxd_top": "550rpx",
    "__pyq_fontSize": "30rpx",
    "objects": [
        "box",
        "my",
        "chats",
        "xy",
        "ztx",
        "qq",
        "sd",
        "zgrid",
        "cha",
        "wxd",
        "wx",
        "hyd",
        "hy",
        "pyqd",
        "pyq",
        "zxd",
        "zx",
        "lwd",
        "lw",
        "mask01",
        "pyqt"
    ],
    "__lwd_left": "690rpx",
    "__wxd_top": "550rpx",
    "__zx_height": "160rpx",
    "__hyd_top": "400rpx",
    "__pyq_hidden": true,
    "__hy_left": "697rpx",
    "__wxd_width": "60rpx",
    "__xy_left": "565rpx",
    "__box_width": "750rpx",
    "__hy_hidden": true,
    "__wx_hidden": true,
    "__zxd_height": "220rpx",
    "__xy_src": "http://material.motimaster.com/aelegy1532071513000/\u4e0b\u763e.png",
    "__hy_fontSize": "30rpx",
    "__zx_top": "580rpx",
    "__ztx_src": "",
    "__lw_disabled": "",
    "__wx_top": "580rpx",
    "__my_width": "500rpx",
    "__chats_hidden": true,
    "__mask01_background": "RGBA(0, 0, 0, 0.7)",
    "__chats_top": "280rpx",
    "__qq_top": "60rpx",
    "__pyqt_top": "300rpx",
    "__pyq_left": "697rpx",
    "__hyd_background": "rgba(238,238,238,0.4)",
    "__lw_fontSize": "30rpx",
    "__lw_top": "580rpx",
    "__wx_color": "white",
    "__hy_text": "\u5206\u4eab\u7ed9\u597d\u53cb",
    "__zx_hidden": true,
    "__mask01_width": "100%",
    "__mask01_height": "100%",
    "__chats_height": "20rpx",
    "__box_scrollTop": "",
    "__lw_text": "\u6211\u4e5f\u6765\u73a9",
    "__cha_top": "5rpx",
    "__chats_left": "450rpx",
    "__sd_hidden": true,
    "__lwd_height": "220rpx",
    "__my_hidden": true,
    "__wx_height": "160rpx",
    "__chats_text": "\u70b9\u51fb\u7ea2\u53c9\u53ef\u4ee5\u5220\u9664\u54e6~",
    "__zgrid_data": "",
    "__xy_height": "100rpx",
    "__mask01_left": "0rpx",
    "__pyq_top": "725rpx",
    "__wx_fontSize": "30rpx",
    "__pyqd_top": "700rpx",
    "__wxd_height": "220rpx",
    "__zx_width": "50rpx",
    "__lwd_background": "rgba(238,238,238,0.4)",
    "__box_height": "1234rpx",
    "__cha_height": "40rpx",
    "__zx_fontSize": "30rpx",
    "__xy_width": "100rpx",
    "__lw_color": "white",
    "__ztx_top": "73rpx",
    "__sd_src": "http://material.motimaster.com/aelegy1532069627000/\u5370\u8c61.png",
    "__zx_color": "white",
    "__sd_height": "75rpx",
    "__my_top": "500rpx",
    "__pyq_disabled": "",
    "__wxd_left": "0rpx",
    "__hyd_height": "250rpx",
    "__qq_left": "130rpx",
    "__box_hidden": true,
    "__pyqd_left": "690rpx",
    "__hy_top": "425rpx",
    "__qq_height": "155rpx"
},
    onButtonTap_OIj9wp:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.czj', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_e607J7:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.zjx', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onButtonTap_wgwy6I:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.onSaveImage', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onViewTap_WA9FO1:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset, evt.currentTarget);
                
                Promise.resolve(evt_data).then( function(evt) {
            if(!false && evt.page.currentTarget.id) {
                var dataName = moapp.genObjectDataName(evt.page.currentTarget.id, 'hidden');
                let data = {};
                data[dataName] = true;
                self.setData(data);
            }
            
            return evt;
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
    onButtonTap_AAZCQm:  function(evt) {
                var self = this;
                ;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.brx', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onImageTap_acyljz:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, evt.currentTarget.dataset);
                
                Promise.resolve(evt_data).then( function(evt) {
            wx.showModal({
                title: `提示`,
                content: `是否确认删除`,
                success:function(res){
                    if(res.confirm){
                        console.log('用户点击确定')
                        
                Promise.resolve(evt).then( function(evt) {
            evt.params = 
            {
                fs: evt.data.f,
ns: evt.data.n,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx777413533a93b0cf', 'main', 'page2.shan', evt);
        }
        )
            
                    }else if(res.cancel) {
                        console.log('用户点击取消')
                        
                    }
                }
            })
        }).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
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
                        this.data.__share_page = 'page1'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx777413533a93b0cf", "page2", self, {});
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