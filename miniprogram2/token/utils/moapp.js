const util = require("./util.js");
module.exports = {
  requestingSession: false,   // 标识是否正在请求session，避免重复
  requestCloudFunction: function(page_obj, appid, module_name, func_name, params) {
    var _this = this;
    return new Promise((resolve, reject) => {
      const app = getApp();

      _this.login(appid).then( data => {
        if (app.globalData.userInfo) {  // app.globalData.userInfo是用来临时存放信息的，目的是在“下一次网络请求”时带上
          params.app.userInfo = app.globalData.userInfo;
          delete app.globalData.userInfo;
        }

        wx.request({
        url: `${app.globalData.domain}/cloud`,
        data: {
          session: data.sessionID,
          module: module_name,
          func_name: func_name,
          data: params
        },
        method: 'POST',
        header: {
          'content-type': 'application/json'
        },
        success: (res) => {
          if ('statusCode' in res && res.statusCode != 200) {
            wx.hideLoading();

            _this.showAlert( '错误提示'
              ,`糟糕,服务器出错了,错误码:${res.statusCode},请稍后重试...`);

            reject({
              statusCode: res.statusCode,
              data: res.data
            })
          } else {
            if(res.data.ret == 0) {
              var data = {};
              var serverData = {};

              for(var i in res.data.data) {
                var item = res.data.data[i];
                var cmd = item.cmd;
                var cmd_data = item.data;

                switch(cmd) {
                  case 'setTitle':
                    _this.setTitle(cmd_data);                    
                    break;
                  case 'setAttr': //id, key, value
                    data[_this.genObjectDataName(cmd_data.id, cmd_data.key)] = cmd_data.value;
                    break;
                  case 'goto':  // options
                    let url_params = util.jsonToUrlParams(cmd_data.options || {});                    
                    
                    wx.navigateTo({
                      url: `../${cmd_data.page_name}/${cmd_data.page_name}?${url_params}`
                    });
                    break;
                  case 'redirectTo':  // options
                    let url_reidrect_params = util.jsonToUrlParams(cmd_data.options || {});                    
                    
                    wx.redirectTo({
                      url: `../${cmd_data.page_name}/${cmd_data.page_name}?${url_reidrect_params}`
                    });
                    break;
                  case 'switchTab':
                    wx.switchTab({
                      url: `../${cmd_data.page_name}/${cmd_data.page_name}`
                    })
                  case 'goBack':
                    wx.navigateBack({
                        delta:1
                    });
                    break;
                  case 'setNavibarColor':
                    wx.setNavigationBarColor({
                      frontColor: cmd_data.frontColor == '#000000' ? '#000000' : '#ffffff',   //小程序的frontColor只能设置#ffffff或者#000000
                      backgroundColor: cmd_data.backgroundColor || '#ffffff'
                    });
                    break;
                  case 'showAlert':
                    _this.showAlert(cmd_data.title, cmd_data.content);
                    break;
                  case 'showTips':
                    wx.showToast({
                      title: cmd_data.text,
                      icon: 'success',
                      image:cmd_data.image,
                      duration: cmd_data.duration
                    })
                    break;
                  case 'playBGM':
                  if (wx.createInnerAudioContext) {
                      var t = Date.now();
                      app.bgm.src = cmd_data.src+`#${t}`;
                      app.bgm.control = cmd_data.control
                      // app.bgm.control = false
                      app.bgm.controlStyle = "bgm-" + cmd_data.controlStyle
                      app.bgm.title = 'bgm'
                      app.bgm.autoplay = cmd_data.autoplay
                      app.bgm.loop = cmd_data.loop
                      page_obj.setData({
                          bgmcontrol :+ app.bgm.control,
                          bgmstate: [1, + ! app.bgm.autoplay],
                          controlStyle: app.bgm.controlStyle
                      })
                    }
                    break;
                  case 'pauseBGM':
                    if(page_obj.data.bgmstate && page_obj.data.bgmstate[0] == 1) {
                      app.bgm.pause();
                      page_obj.setData({bgmstate: [1, 1]})
                    }
                    break;
                  case 'resumeBGM':
                    if(page_obj.data.bgmstate && page_obj.data.bgmstate[0] == 1) {
                      app.bgm.play();
                      page_obj.setData({bgmstate: [1, 0]})
                    }
                    break;
                  // getBackgroundAudioManager 的 stop 功能等同于之前的 close
                  // case 'stopBGM':
                  //   if(page_obj.data.bgmstate && page_obj.data.bgmstate[0] == 1) {
                  //     app.bgm.stop();
                  //     page_obj.setData({
                  //         bgmstate: [1, 1]
                  //     }) 
                  //   }
                  //   break;
                  case 'closeBGM':
                    if(page_obj.data.bgmstate && page_obj.data.bgmstate[0] == 1) {
                      app.bgm.src = "http://null"
                      app.bgm.stop();
                      page_obj.setData({
                          bgmcontrol: 0,
                          bgmstate: [0, 1]
                      }) 
                    }
                    break;
                  case 'gotoMiniProgram':
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
                    break;
                  case 'playAudio':
                    if (wx.createInnerAudioContext) {
                      var t = Date.now();
                      app.soundEffect.src = cmd_data.src+`#${t}`
                      app.soundEffect.autoplay = true
                      page_obj.setData({
                        soundEffectState:[1, 0]
                      })
                    }
                    break;
                  case 'setData':
                    serverData[cmd_data.key] = cmd_data.value;
                    break;
                  case 'saveImage':
                    _this.saveImage(null, cmd_data).then().catch(() => {});
                    break;
                  case 'appendData':
                    let key = _this.genObjectDataName(cmd_data.id, 'data');
                    let itemData = page_obj.data[key];

                    itemData.push(cmd_data.value);
                    data[key] = itemData;
                    break;
                  case 'console':
                    console.log(cmd_data.content);
                    break;
                  case 'previewImage':
                    console.log('previewImage')
                    wx.previewImage({
                      'urls':cmd_data
                    })
                    break;
                  case 'wxpay': // 微信支付
                    if (cmd_data.params) {
                      var wxpay_data = cmd_data;
                      let payParam = wxpay_data.params;
                      wx.requestPayment({
                          'timeStamp': payParam.timeStamp,
                          'nonceStr': payParam.nonceStr,
                          'package': payParam.package,
                          'signType': payParam.signType,
                          'paySign': payParam.paySign,
                          'success': function (res) {                              
                              _this.requestCloudFunction(page_obj, appid, module_name, wxpay_data.success.function, params);
                          },
                          'fail': function (res) {
                              console.log(res);
                              let cancel = res.errMsg.indexOf('cancel') > -1;
                              if (params.params) {
                                params.params.wxpayCancel = cancel;
                              } else {
                                params.params = {
                                  wxpayCancel: cancel
                                }
                              }
                              _this.requestCloudFunction(page_obj, appid, module_name, wxpay_data.fail.function, params);
                          }
                      })
                    } else {
                      if (cmd_data.fail) {
                          // (page_obj, appid, module_name, func_name, params)
                          _this.requestCloudFunction(page_obj, appid, module_name, cmd_data.fail.function, params);
                      }

                      console.error('invalid wxpay params:', cmd_data);
                    }
                    break;
                  case 'openWeb':
                    wx.navigateTo({
                       url: '../__web_page/web_page?url=' + cmd_data.url
                    });
                    break;
                  default:
                    console.log('invalid server cmd:' + cmd)
                    break;
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

              params.data = res.data.data;
              if ('resolve' in res.data && (res.data.resolve === false)) {
                wx.hideLoading();
                reject(params);
              } else {
                resolve(params);
              }
            } else {
              console.log(`Execute cloud function fail！error code:${res.data.ret}`);

              try {
                if(res && res.data && res.data.data && 'traceback' in res.data.data) {
                  console.log('---------error traceback---------:\n' + res.data.data.traceback);
                }

                if(res && res.data&& res.data.data && 'error_message' in res.data.data) {
                  console.log('---------error message---------:\n' + res.data.data.error_message);
                }  
              } catch (err) {
                console.error(err);
              }
              

              wx.hideLoading();

              if(app.globalData.env == 'release') {
                _this.showAlert( '错误提示', `出错了，错误码:${res.data.ret}`);
              } else {
                _this.showAlert( '错误提示', 
                  `出错了，错误码:${res.data.ret},\r\n 错误信息: `
                  + (res.data.data.error_message || '无')
                  + ', 详细错误信息请参考微信开发者工具Console日志输出.');
              }
              
              reject({
                errorCode: (res && res.data&& res.data.ret) || -1,
                data: (res && res.data && res.data.data) || ''
              });
            }
          }
        },
        fail: function (res) {
          reject(res);
        },
      })
      }, err => {
        _this.showAlert( '错误提示'
              ,`糟糕,服务器出错啦,请稍后重试...`);
        reject('login fail');
      });      
    });
  },
  genObjectDataName: (id, attr) => {
      return `__${id}_${attr}`;
  },
  submitFormId: function(appid,formId){
    const app = getApp(); 
    var sessionID = app.globalData.sessionID
    if(!sessionID){
      //console.log('没有sessionId 未登陆 不报formId')
      return
    }
    wx.request({
      url: `${app.globalData.domain}/templateInfo`,
      data: {
        appid: appid,
        formId: formId,
        sessionID: sessionID,
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success:function(res){
          //console.log('报formId成功')
      },
      fail: function(res) {
        //console.log('报formId失败')
      }
    })
  },

  jsonToUrlParams: params => {
    var items = []

    for(var k in params) {
      items.push(k + '=' + encodeURIComponent(params[k]));
    }

    return items.join('&');
  },

  getUserInfo: () => {
    return new Promise( (resolve, reject) => {
        wx.getUserInfo({
          success: function(res) {
            resolve(res.userInfo);
          },
          fail: function(res) {
            resolve({});
          }
        });
    });
  },
  // 构造标准事件参数
  genEventData: function(appid, page_name, page_obj, evt_data, currentTarget=null) {
    const app = getApp();
    var elements = [];

    if(page_obj.data.objects) {
      for(var i=0; i<page_obj.data.objects.length; ++i) {
        var id = page_obj.data.objects[i];
        var data = {
          'id': id,
          'attrs': []
        };
          
        var key_head = this.genObjectDataName(id, '');

        for(var k in page_obj.data) {
            if (k.slice(0, key_head.length) == key_head) {
              var attr = k.slice(key_head.length, k.length);            
              if(attr === 'value') {  // value要特殊处理：因为只有value才会带上值
               data['value'] = page_obj.data[k];
              } else if (attr === 'item'){
                data['currentItem'] = page_obj.data[k].item
              } else {
                let isBaseAttr = false;
                for(let i in app.globalData.uiBaseAttr4Server) {
                  if (attr == app.globalData.uiBaseAttr4Server[i]) {
                    isBaseAttr = true;
                    break;
                  }
                }

                if(!isBaseAttr) {
                  data['attrs'].push(attr);
                }
              }
            }
        }

        elements.push(data);
      }
    }

    return {
        app: {
          scene: app.globalData.scene
        },
        page: {
            name: page_name,
            createTime: page_obj.data.createTime,
            options: page_obj.data.options || {},
            elements: elements,
            data: page_obj.data.serverData || {},
            currentTarget: {
              id: currentTarget?(currentTarget.id || null):null
            }
        },
        data: evt_data
    };
  },

  showConfirm: (title, content, data) => {
    return new Promise( (resolve, reject) => {
        wx.showModal({
          title: title || '提示',
          content: content || '',
          success: (res) => {
            if (res.confirm) {
              resolve(data);
            } else if (res.cancel) {
              reject(data);
            }
          },
          fail: (res) => {
            console.log('showModal fail! err:');
            console.log(res);
            reject(data);
          }
        }); // showModal
    }); // promise
  },

  showAlert: (title, content) => {
      wx.showModal({
        title: title || '提示',
        content: content || '',
        showCancel: false
    });
  },
  chooseImage:(evt, count, sizeType, sourceType) => {
    console.log(evt)
    evt.params = {}

      return new Promise((resolve, reject) => {
        wx.chooseImage({
          count: count,
          sizeType: sizeType,
          sourceType: sourceType,
          success:function(res){
            console.log(res)
            console.log('发生了什么')
            evt.params.tempFilePaths = res.tempFilePaths
            console.log(evt)
            resolve(evt)

          }
        })
      })
  },

  checkSaveImageAuth: () => {
    return new Promise( (resolve, reject) => {
      let setting = wx.getSetting({
        success: (res) => {
          var auth = res.authSetting;        
          console.log(auth);
          const authKey = 'scope.writePhotosAlbum';

          if (authKey in auth && auth[authKey]) {
            resolve();              
          } else {
            if (authKey in auth) {
              wx.showModal({
                title: '提示',
                content: '您现在不允许小程序访问手机相册，不能保存到朋友圈，请打开"保存到相册"',
                success: (res) => {
                  if (res.confirm) {
                    wx.openSetting({
                      success: (res) => {
                        console.log(res);
                        if ('scope.writePhotosAlbum' in res.authSetting && res.authSetting['scope.writePhotosAlbum']) {
                            resolve();
                        } else {
                          reject();
                        }
                      }
                    })
                  } else {
                    reject();
                  }
                },
                fail: (res) => {                
                  reject();
                }
              }); // showModal
            } else {
              //resolve();
              wx.authorize({
                scope: authKey,
                success() {
                  resolve();
                },
                fail() {
                  reject();
                }
            })
            }
          }                
        },
      fail: (res) => {
        console.error('get setting fail!');
        reject();
        }
      });
    });    
  },
  saveImage: function(evt, url) {
    var _this = this;

    evt = evt || {};

    return new Promise((resolve, reject) => {
        _this.checkSaveImageAuth().then(() => {
            wx.showLoading({
                'title': '保存中'
            });
            wx.downloadFile({
                url: url,
                success: function(res) {
                    wx.saveImageToPhotosAlbum({
                        filePath: res.tempFilePath,
                        success: function(res) {
                            wx.hideLoading();
                            /*wx.showToast({
                                title: "图片保存成功",
                                icon: 'success',
                                duration: 1500
                            });*/
                            _this.showAlert( '保存成功', '已保存到相册，快去分享吧~');
                            resolve(evt);
                        },
                        fail: function(res) {
                            wx.showToast({
                                title: "图片保存失败",
                                icon: 'none',
                                duration: 1500
                            });
                            reject(evt); // 后端调用saveImage请忽略此处报错
                        }
                    }); // wx.saveImageToPhotosAlbum
                },
                fail: function(res) {
                    wx.showToast({
                        title: "图片下载失败",
                        icon: 'none',
                        duration: 1500
                    });
                    reject(evt);
                }
            }); // wx.downloadFile 
        },
        () => {
          wx.showToast({
              title: "图片保存失败",
              icon: 'none',
              duration: 1500
          });
          reject(evt);
        }
      );
    });
  },
  wxLogin: function(resolve, reject) {
    wx.login({
      success: function(res) {
        if (res.code) {
          resolve({
            'openid': null,
            'code': res.code
          })
        } else {
          console.log('wx.login fail!, err:' + res.errMsg);
          reject(res.errMsg);
        }
      },
      fail: function(res) {
        console.error('wx.login fail! err:' + res);
        reject(res);
      }
    });
  },
  getWxCode: function() {
    var self = this;
    return new Promise((resolve, reject) => {      
      var openid = wx.getStorageSync('openid');
      if(openid) {
        wx.checkSession({
          success: function() {       
            resolve({
              'openid': openid,
              'code': null
            });
          },
          fail: function(){
            // session_key 已经失效，需要重新执行登录流程
            console.log('session is invalid, relogin');
            self.wxLogin(resolve, reject);
          }
        });
      } else {
        self.wxLogin(resolve, reject);
      }
    });
  },
  login: function(appid) {
    var self = this;
    return new Promise( (resolve, reject) => {
      const app = getApp();
      if( app.globalData.sessionID ) {
        resolve({
          'sessionID': app.globalData.sessionID
        });
      } else {
          if (!self.requestingSession) {
              self.requestingSession = true;

            self.getWxCode().then( data => {
                wx.request({
                  url: `${app.globalData.domain}/session`,
                  data: {
                    appid: appid,                    
                    signature: app.globalData.signature,
                    userInfo: {},
                    code: data['code'],
                    openid: data['openid'],
                    uiBaseAttr: app.globalData.uiBaseAttr4Server
                  },
                  method: 'POST',
                  header: {
                    'content-type': 'application/json'
                  },
                  success: (res) => {
                    if ('statusCode' in res && res.statusCode != 200) {
                      reject('login fail!');
                    } else {
                      app.globalData.sessionID = res.data.data.sessionID;
                      wx.setStorage({
                        'key': 'openid',
                        'data': res.data.data['openid']
                      });
                      
                      console.log(`get session: ${app.globalData.sessionID}, openid:${res.data.data['openid']}`);

                      resolve(res.data.data);
                    }
                  },
                  fail: (res) => {
                    console.error('login failed');
                    console.error(res);
                    reject(res);
                  },
                  complete: (res) => {
                      self.requestingSession = false;
                  }               
                })
            });
          } else {
              let timer = setInterval( ()=>{
                    if(!self.requestingSession) {
                        clearInterval(timer)
                        resolve({
                            'sessionID': app.globalData.sessionID
                        });
                    }
              }, 100);
          }
      }
    });
  },
  appBgmAllInOne: (app) =>{
    if (wx.createInnerAudioContext) {
      // app.bgm = wx.getBackgroundAudioManager();
      // 换成旧接口
      app.bgm = wx.createInnerAudioContext();
      app.soundEffect = wx.createInnerAudioContext();
      app.bgm.onPlay(() => { }),
      app.bgm.onPause(() => { }),
      app.bgm.onStop(() => { }),
      app.bgm.onEnded(() => { }),
      app.soundEffect.onStop(() => { }),
      app.soundEffect.onEnded(() => { })
    }else{
      wx.showModal({
        title: '提示',
        content: '当前微信版本过低，无法使用该功能，请升级到最新微信版本后重试。'
      })  
    }
  },
  bgmControl: (self, app) => {
    if (wx.createInnerAudioContext) {
      if (self.data.bgmstate[0] == 1){
        if (! self.data.bgmstate[1]){
          app.bgm.pause()
          self.setData({bgmstate: [1, 1]})
        }
        else {
          app.bgm.play()
          self.setData({bgmstate: [1, 0]})
        } 
      }
    }
  },
  bgmAllInOne: (self, app) =>{
    if (wx.createInnerAudioContext) {
      self.setData({
        bgmcontrol: app.bgm.control || false,
        controlStyle: app.bgm.controlStyle || false,
        bgmstate:[app.bgm.src == ("" || "http://none/")?0:1, + app.bgm.paused],
        soundEffectState:[app.soundEffect.src == ("" || "http://none/")?0:1, + app.soundEffect.paused]
      }); // bgmstate的两个参数分别是：是否存在bgm, bgm是否暂停播放    
    }
  },
  getOpenId: () => {
    return wx.getStorageSync('openid');
  },
  setTitle: (text) => {
    const app = getApp();
    if (app.globalData.env != 'release') {
      text = text + '-测试版'
    }

    wx.setNavigationBarTitle({
      title: text
    });
  }
}
