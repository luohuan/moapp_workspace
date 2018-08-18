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
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "select", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'setdata', evt);
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
                        this.data.__share_page = 'first'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "select", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "select", self, {});
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
    onSelectorPickerChange_PN5zEQ:  function(evt) {
                var self = this;
                
            self.setData({
                __picker_value: evt.detail.value
            })
            ;
                var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "select", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx263b9c72fc87b39c', 'main', 'save_birth', evt);
            }
            ).then( function(evt) {
            var params = 
            {
                drama_list: "测试",
page: "paper",

            }
            ;
            var page_name = params.page;
            delete params.page;
            wx.navigateTo({
                url: `../${page_name}/${page_name}?` + moapp.jsonToUrlParams(params)
            });
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx263b9c72fc87b39c", "select", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    data: {
    "objects": [
        "picker"
    ],
    "__picker_value": "",
    "__picker_text": "\u70b9\u51fb\u9009\u62e9",
    "__picker_height": "80rpx",
    "__picker_left": "0rpx",
    "__picker_disabled": "",
    "__picker_color": "white",
    "__picker_background": "#ff99cc",
    "__picker_fontSize": "40rpx",
    "__picker_width": "200rpx",
    "__picker_range": [
        [
            "01\u6708",
            "02\u6708",
            "03\u6708",
            "04\u6708",
            "05\u6708",
            "06\u6708",
            "07\u6708",
            "08\u6708",
            "09\u6708",
            "10\u6708",
            "11\u6708",
            "12\u6708"
        ],
        [
            "01\u65e5",
            "02\u65e5",
            "03\u65e5",
            "04\u65e5",
            "05\u65e5",
            "06\u65e5",
            "07\u65e5",
            "08\u65e5",
            "09\u65e5",
            "10\u65e5",
            "11\u65e5",
            "12\u65e5",
            "13\u65e5",
            "14\u65e5",
            "15\u65e5",
            "16\u65e5",
            "17\u65e5",
            "18\u65e5",
            "19\u65e5",
            "20\u65e5",
            "21\u65e5",
            "22\u65e5",
            "23\u65e5",
            "24\u65e5",
            "25\u65e5",
            "26\u65e5",
            "27\u65e5",
            "28\u65e5",
            "29\u65e5",
            "30\u65e5",
            "31\u65e5"
        ]
    ],
    "__picker_top": "650rpx",
    "__picker_right": "0rpx"
},
})