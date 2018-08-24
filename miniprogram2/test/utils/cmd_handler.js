const util = require("./util.js");

module.exports = {    
    __setTitle(ctx, cmd_data, page_data) {
        ctx.moapp.setTitle(cmd_data);
    },
    __setAttr(ctx, cmd_data, page_data) {
        page_data[ctx.moapp.genObjectDataName(cmd_data.id, cmd_data.key)] = cmd_data.value;
    },
    __goto(ctx, cmd_data, page_data) {
        let url_params = util.jsonToUrlParams(cmd_data.options || {});
                
        wx.navigateTo({
          url: `../${cmd_data.page_name}/${cmd_data.page_name}?${url_params}`
        });
    },
    __redirectTo(ctx, cmd_data, page_data) {
        let url_reidrect_params = util.jsonToUrlParams(cmd_data.options || {});                
        wx.redirectTo({
          url: `../${cmd_data.page_name}/${cmd_data.page_name}?${url_reidrect_params}`
        });
    },
    __switchTab(ctx, cmd_data, page_data) {
        wx.switchTab({
          url: `../${cmd_data.page_name}/${cmd_data.page_name}`
        });
    },
    __goBack(ctx, cmd_data, page_data) {
        wx.navigateBack({
            delta:1
        });
    },
    __setNavibarColor(ctx, cmd_data, page_data) {
        wx.setNavigationBarColor({
          frontColor: cmd_data.frontColor == '#000000' ? '#000000' : '#ffffff',   //小程序的frontColor只能设置#ffffff或者#000000
          backgroundColor: cmd_data.backgroundColor || '#ffffff'
        });
    },
    __showAlert(ctx, cmd_data, page_data) {
        ctx.moapp.showAlert(cmd_data.title, cmd_data.content);
    },
    __showTips(ctx, cmd_data, page_data) {
        wx.showToast({
          title: cmd_data.text,
          icon: 'success',
          image:cmd_data.image,
          duration: cmd_data.duration
        })
    },
    __gotoMiniProgram(ctx, cmd_data, page_data) {
        wx.navigateToMiniProgram({
          appId: cmd_data.appid,
          path: cmd_data.path,
          success: function(res) {
            console.log('跳转小程序成功')
          },fail:function(res){
            console.log('跳转小程序失败，错误信息:');
            console.log(res);
          }
        })
    },
    __saveImage(ctx, cmd_data, page_data) {
        ctx.moapp.saveImage(null, cmd_data).then().catch(() => {});
    },
    __appendData(ctx, cmd_data, page_data) {
        let key = ctx.moapp.genObjectDataName(cmd_data.id, 'data');
        let itemData = ctx.page_obj.data[key];

        itemData.push(cmd_data.value);
        page_data[key] = itemData;
    },
    __console(ctx, cmd_data, page_data) {        
        console.log(cmd_data.content);
    },
    __previewImage(ctx, cmd_data, page_data) {        
        wx.previewImage({
          'urls':cmd_data
        })
    },
    __wxpay(ctx, cmd_data, page_data) {
        if (cmd_data.params) {
          let payParam = cmd_data.params;
          wx.requestPayment({
              'timeStamp': payParam.timeStamp,
              'nonceStr': payParam.nonceStr,
              'package': payParam.package,
              'signType': payParam.signType,
              'paySign': payParam.paySign,
              'success': function (res) {                              
                  ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.success.function, ctx.params);
              },
              'fail': function (res) {
                  console.log(res);
                  let cancel = res.errMsg.indexOf('cancel') > -1;
                  if (ctx.params.params) {
                    ctx.params.params.wxpayCancel = cancel;
                  } else {
                    ctx.params.params = {
                      wxpayCancel: cancel
                    }
                  }
                  ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.fail.function, ctx.params);
              }
          })
        } else {
          if (cmd_data.fail) {
              ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.fail.function, ctx.params);
          }

          console.error('invalid wxpay params:', cmd_data);
        }
    },
    __openWeb(ctx, cmd_data, page_data) {
        let url = cmd_data.url;
        let openid = ctx.moapp.getOpenId();
        const app = getApp(); 
        var sessionID = app.globalData.sessionID;
        let domain = encodeURIComponent(`${app.globalData.domain}/cloud`);

        let ext_info = `openid=${openid}&sessionid=${sessionID}&interface=${domain}`;

        if (url.indexOf("?")>-1) {
          url = url + '&' + ext_info;
        } else {
          url = url + '?' + ext_info;
        }
        console.log(url);
        wx.navigateTo({
           url: '../__web_page/web_page?url=' + encodeURIComponent(url)
        });
    },
    __makePhoneCall(ctx, cmd_data, page_data) {
        wx.makePhoneCall({
          phoneNumber: cmd_data.phone_number
        });
    },
    __getWeRunData(ctx, cmd_data, page_data) {
        ctx.moapp.checkAuthSetting('scope.werun', '小程序需要读取您的微信运动数据，请打开"微信运动步数"').then(() => {
          wx.getWeRunData({
              success(res) {
                  ctx.params.encrypted_data = {
                      'type': 'weRunData',
                      'data': res.encryptedData,
                      'iv': res.iv
                  }
                  ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.success.function, ctx.params);
              },
              fail(res) {
                  console.error('get wx run data fail!', res);
                  ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.fail.function, ctx.params);
              }
          });
        },
        err => {
          ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.fail.function, ctx.params);
        }
      );
    },
    __uploadImage(ctx, cmd_data, page_data){
      console.log('uploadImage')
      var upcmd_data = cmd_data
      wx.chooseImage({
        count: upcmd_data.count,
        sizeType: ['original', 'compressed'],
        sourceType: upcmd_data.sourceType,
        sizeType: upcmd_data.sizeType,
        success: function (res) { 
          wx.showLoading({
            title: '上传中0/' + res.tempFilePaths.length,
          })
          var tempFilePaths = res.tempFilePaths
          var len_file = tempFilePaths.length
          var up_success = 0;
          var success_url = []
          var up_fail = 0
          var total_up = 0
          const app = getApp();
          for (var i = 0; i < len_file; i++) {
            wx.uploadFile({
              url: `${app.globalData.upload}`,
              filePath: tempFilePaths[i],
              name: 'file',
              formData: {
                'appid': ctx.appid,
              },
              success: function (res) {
                var data = JSON.parse(res.data)
                if (res.statusCode == 200) {
                  up_success += 1;
                  total_up += 1;
                  success_url.push(data.url)
                  wx.showLoading({
                    title: '上传中' + up_success + '/' + tempFilePaths.length,
                  })
                } else {
                  total_up += 1;
                  up_fail += 1
                }
              },
              fail:function(){
                total_up += 1;
                up_fail += 1
              },
              complete:function(){
                if (total_up == len_file){
                  console.log(ctx.params)
                  ctx.params.params = {}
                  ctx.params.params.urls = success_url
                  ctx.params.params.images = success_url
                  ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, upcmd_data.success.function, ctx.params);
                  wx.hideLoading()
                  wx.showToast({
                    title: '上传完成',
                  })
                }
              }
            })
          }
        },
        fail:function(){
          console.log('选择图片失败')
          ctx.moapp.requestCloudFunction(ctx.page_obj, ctx.appid, ctx.module_name, cmd_data.fail.function, ctx.params);
        }
      })
    },
    __playBGM(ctx, cmd_data, page_data) {
      const app = getApp(); 
      if (wx.createInnerAudioContext) {    
        var t = Date.now();
        app.bgm.src = cmd_data.src+`#${t}`;  // 兼容处理
        app.bgm.control = cmd_data.control;
        app.bgm.controlStyle = "bgm-" + cmd_data.controlStyle;
        app.bgm.title = 'bgm';
        app.bgm.autoplay = cmd_data.autoplay;
        app.bgm.loop = cmd_data.loop;
        page_data.bgmcontrol = + app.bgm.control;
        page_data.bgmstate = [1, + ! app.bgm.autoplay];
        page_data.controlStyle = app.bgm.controlStyle;
      };
    },
    __pauseBGM(ctx, cmd_data, page_data) {
      const app = getApp(); 
      if(ctx.page_obj.data.bgmstate && ctx.page_obj.data.bgmstate[0] == 1) {
        app.bgm.pause();
        page_data.bgmstate = [1, 1];
      };
    },
    __resumeBGM(ctx, cmd_data, page_data) {
      const app = getApp();
      if(ctx.page_obj.data.bgmstate && ctx.page_obj.data.bgmstate[0] == 1) {
        app.bgm.pause();
        page_data.bgmstate = [1, 0];
      };
    },
    __closeBGM(ctx, cmd_data, page_data) {
      const app = getApp();
      if(ctx.page_obj.data.bgmstate && ctx.page_obj.data.bgmstate[0] == 1) {
        app.bgm.src = "http://null";
        app.bgm.control = false
        app.bgm.stop();
        page_data.bgmstate = [0, 1];
        page_data.bgmcontrol = 0;
      };     
    },
    __playAudio(ctx, cmd_data, page_data) {
      const app = getApp();
      if (wx.createInnerAudioContext) {
        var t = Date.now();
        app.soundEffect.src = cmd_data.src+`#${t}`;
        app.soundEffect.autoplay = true;
        page_data.soundEffectState = [1,0];
      };
    },
    execute:  function(page_obj, appid, module_name, params, res_data, moapp_obj) {
        const app = getApp();
        var _this = moapp_obj;
        var data = {};
        var serverData = {};

        for(var i in res_data) {
            var item = res_data[i];
            var cmd = item.cmd;
            
            var fn_name = '__' + cmd;
            if (fn_name in this) {
                var cmd_data = item.data;
                this[fn_name]({
                    'page_obj': page_obj,
                    'appid': appid,
                    'moapp': moapp_obj,
                    'module_name': module_name,
                    'params': params
                }, cmd_data, data);
            } else {
                var cmd_data = item.data;
                switch(cmd) {
                  case 'setData':
                    serverData[cmd_data.key] = cmd_data.value;
                    break;              
                  default:
                    console.log('invalid server cmd:' + cmd)
                    break;
                }
            }            
        }
        if (JSON.stringify(serverData) != "{}") {
            var oldData = page_obj.data.serverData || {};

            for (var k in serverData) {
              oldData[k] = serverData[k];
            }

            data['serverData'] = oldData;
        }

        if (JSON.stringify(data)!="{}" && page_obj) {
            page_obj.setData(data);                
        }
    }
}