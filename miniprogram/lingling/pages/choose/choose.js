const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "choose", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'answerQuestionReady', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "choose", self, {});
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
    data: {
    "__quenumber_fontWeight": "normal",
    "__quenumber_height": "30rpx",
    "__questionBox_left": "130rpx",
    "__qa_top": "650rpx",
    "__questionBox_height": "200rpx",
    "__questionBox_width": "510rpx",
    "__questionBox_fontSize": "17px",
    "__questionBox_color": "#000D2F",
    "__queimage_right": "0rpx",
    "__qa_checked": "",
    "__quenumber_width": "30rpx",
    "__qa_value": "",
    "__qa_width": "600rpx",
    "__queimage_height": "350rpx",
    "__qa_right": "0rpx",
    "__queimage_src": "",
    "__quenumber_left": "30rpx",
    "__qa_color": "",
    "__quenumber_top": "30rpx",
    "__qa_data": "",
    "objects": [
        "quenumber",
        "questionBox",
        "queimage",
        "qa"
    ],
    "__queimage_left": "0rpx",
    "__qa_height": "160rpx",
    "__quenumber_fontSize": "17px",
    "__qa_left": "0rpx",
    "__qa_fontSize": "30rpx",
    "__qa_disabled": "",
    "__questionBox_top": "30rpx",
    "__queimage_width": "600rpx",
    "__queimage_top": "210rpx"
},
    onRadioGroupChange_tRuxx1:  function(evt) {
                var self = this;
                
            self.setData({
                __qa_value: evt.detail.value
            })
            ;

                 const datas = self.data.__qa_data
                    for(const d of datas){
                      //console.log(d.value)
                      //console.log(evt.detail.value)
                      if(d.value == evt.detail.value){
                        d.cls = 'choosed'
                      }else{
                        d.cls = 'normal'
                      }
                    }
                    console.log(datas)
                    self.setData({
                      __qa_data: datas
                    })

                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "choose", self, evt.detail.value);
                Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'afterAnswer', evt);
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
                        this.data.__share_page = 'entrance'
                    }
                    //console.log(this.data.__share_page)

                    let shareInfo = {
                        
                        path: `/pages/${this.data.__share_page}/${this.data.__share_page}?`+options,
                        success: function(res) {
                            console.log('share successed');
                            console.log(res);
                            
                            
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "choose", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "choose", self, {});
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