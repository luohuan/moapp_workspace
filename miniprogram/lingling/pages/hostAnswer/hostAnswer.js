const app = getApp();
const moapp = require("../../utils/moapp.js"); 

Page({
    bgmcontrol: function(){
            moapp.bgmControl(this, app)                
        },
    onReady:  function () {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, {});

                    Promise.resolve(evt_data).then( function(evt) {
                return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'findHostData', evt);
            }
            ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onShow:  function (opt) {
                    var self = this;
                    var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, {});
                    moapp.bgmAllInOne(self, app);
                    Promise.resolve(evt_data).then( function(evt) {
            return evt;
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
                }
            ,
    onButtonTap_nAS3Fz:  function(evt) {
                var self = this;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, evt.currentTarget.dataset);
                Promise.resolve(evt_data).then( function(evt) {
            evt.params = 
            {
                id: evt.data.id,

            }
            ;
            return moapp.requestCloudFunction(self, 'wx87dcda9739af9cb1', 'main', 'deleteHostItemData', evt);
        }
        ).catch( err => {/*console.log("Event exception, err:");console.log(JSON.stringify(err));*/})
            }
            ,
    onViewTap_kt5M8L:  function(evt) {
                var self = this;
                
            self.setData({
                __hostAnswerlist_item: evt.currentTarget.dataset
            })
            ;
                var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, evt.currentTarget.dataset, evt.currentTarget);
                
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
    "objects": [
        "hostAnswerlist"
    ],
    "__hostAnswerlist_top": "0rpx",
    "__hostAnswerlist_left": "0rpx",
    "__hostAnswerlist_data": ""
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
                            
                            
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, {});
                            Promise.resolve(evt_data)
                        },
                        fail: function(res) {
                            console.log('share failed!');
                            console.log(res);
                            var evt_data = moapp.genEventData("wx87dcda9739af9cb1", "hostAnswer", self, {});
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