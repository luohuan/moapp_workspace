//index.js
//获取应用实例
const app = getApp()
var onload_e = {}
var randomHeightListMod = [
  // 'left:750rpx;bottom:27%;',
  'left:750rpx;bottom:31%;',
  'left:750rpx;bottom:35%;',
  'left:750rpx;bottom:39%;',
  'left:750rpx;bottom:43%;',
  'left:750rpx;bottom:47%;',
  'left:750rpx;bottom:51%;',
  'left:750rpx;bottom:55%;',
  'left:750rpx;bottom:59%;',
]
var huishourandomHeightListMod = []

var aaa, bbb, ccc, ddd, eee, fff
var jishiqi = 1
var cishu = 1
var fsjsq = 0
var smallTime = 0
var runtime = 20
var index = 0 //用来给isOpenList每一个元素进行改值

var isFirstOpenIndex = true

Page({
  data: {
    animationData: {},
    userInfo: {},
    topenId: '',
    wopenId: '',
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    isSend: false,
    num: 0, //用来判断月亮旁边的星星个数
    sentence: '',
    isOpenList: [],
    isOpen: false,
    isAppend: false,
    isPaused: false,
    isNiming: true,
    isStarComing: false,
    isYourself: false,
    isGotoYourself: false,
    isFirstOpen: true,
    isFirstOpen2: true,
    isTohoutai: false,
    windowWidth: 0,
    fangzhi:false,
    tavatar: '',
    sleepList: [],
    hour: '',
    minute: '',
    second: '',
    toneLeft: [
      ['', 1, ''],
      ['animation-delay: 2s', 3, 'animation-delay: 1s'],
      ['animation-delay: 3s', 5, 'animation-delay: 2s'],
      ['animation-delay: 4s', 7, 'animation-delay: 3s'],
      ['animation-delay: 5s', 9, 'animation-delay: 4s'],
      ['animation-delay: 6s', 11, 'animation-delay: 5s']
    ],

    toneRight: [
      ['', 2, ''],
      ['animation-delay: 2s', 4, 'animation-delay: 1s'],
      ['animation-delay: 3s', 6, 'animation-delay: 2s'],
      ['animation-delay: 4s', 8, 'animation-delay: 3s'],
      ['animation-delay: 5s', 10, 'animation-delay: 4s'],
      ['animation-delay: 6s', 12, 'animation-delay: 5s']
    ],

    randomHeightList: [],
    dansentencelist: [
      [1, '1s'],
      [2, '1s'],
      [3, '1s'],
      [4, '1s'],
      [5, '7s'],
      [6, '7s'],
      [7, '7s'],
      [8, '7s'],
    ],
    dansentencelistcang: [],
    tmpdansentencelist: [],
    talkList: ['我喜欢你的性格~', '其实我想和你表白很久了', '我喜欢你很久了~', '我喜欢听你的歌', '其实你欠我500块钱', '其实你人挺不错的', '别熬夜了早点睡', '我觉得你是我见过最瘦的人', '今天我看到你了'],
    talkListNow: ['我喜欢你的性格~', '其实我想和你表白很久了', '我喜欢你很久了~'],
    i: 0,
    isUp: false,
    isFirstOpen: true,
    inputValue: '',
  },

  onLoad: function(e) {
    onload_e = e
    wx.getSystemInfo({
      success: res => {
        this.setData({
          windowWidth: res.windowHeight
        })
      },
    })
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
    // 获取分享者的openId,如果不是从分享的卡片进入的小程序，则进入自己的主页

    // 如果是从场景值那边进入的小程序，先判断是从二维码分享来的还是从卡片分享来的
    if (JSON.stringify(e) != "{}") {
      // 如果不是从二维码进来的
      // 判断值是不是undefined的方法
      if (typeof(e.scene) === 'undefined') {
        console.log('zhixing')
        app.globalData.topenId = e.user
        this.setData({
          topenId: e.user,
        })
      } else {
        var scene1 = decodeURIComponent(e.scene)
        app.globalData.topenId = scene1
        this.setData({
          topenId: scene1,
        })
      }
    } else {
      app.globalData.topenId = '',
        this.setData({
          topenId: '',
        })
    }
    // callback
    if (this.userInfoReadyCallback) {
      this.userInfoReadyCallback(res)
    }
    // 把分享者的openId传给后台
    if (app.globalData.userInfo) {
      wx.login({
        success: res => {
          wx.request({
            url: 'https://www.yangshuxian.xyz:80/sleep/loginOrRegister/',
            data: {
              'name': app.globalData.userInfo.nickName,
              'avatar': app.globalData.userInfo.avatarUrl,
              'topenId': this.data.topenId,
              'js_code': res.code,
            },
            method: 'POST',
            header: {
              "Content-Type": "application/x-www-form-urlencoded"
            },
            success: res => {
              console.log('第一个login:', res.data)
              app.globalData.wopenId = res.data[0]
              
              // 如果是直接进入的小程序，即进入自己的主页，那就从后台拿到自己的openID后赋值给topenId
              if (JSON.stringify(e) === "{}") {
                app.globalData.topenId = res.data[0]
                this.setData({
                  topenId: res.data[0],
                  isYourself: true,
                  isGotoYourself: true,
                })
              } else if (typeof (e.scene) === 'undefined') {
                //如果是扫自己转发的小程序码
                if (e.user === res.data[0]){
                  this.setData({
                    isYourself: true, 
                    isGotoYourself: true,
                  })
                }
              } else {
                var scene = decodeURIComponent(e.scene)
                //如果进入的是自己转发出去的卡片
                if (scene === res.data[0]) {
                  this.setData({
                    isYourself: true,
                    isGotoYourself: true,
                  })
                }
              }
              this.setData({
                tavatar: res.data[3],
                fangzhi: res.data[4],
              })

              var huaListcang = res.data[1]
              var huaList = res.data[2]
              var isOpenListLocal = []
              var randomHeightList = []
              var i = 0
              for (i in huaList) {
                isOpenListLocal.push(false)
                randomHeightList.push(' ')
              }
              if(huaList.length === 0){
                this.setData({
                  num:0
                })
              }else{
                this.setData({
                  num: parseInt(i) + 1
                })
              }
              this.setData({
                userInfo: app.globalData.userInfo,
                dansentencelist: huaList,
                dansentencelistcang: huaListcang,
                isOpenList: isOpenListLocal,
                randomHeightList: randomHeightList,
              })
              runtime = i * 1.8 + 17
              this.sankai()
            }
          })
        }
      });
    }
    app.userInfoReadyCallback = res => {
      var userInfo = JSON.parse(res.rawData)
      console.log('主页登录后callback:', userInfo.nickName)
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
      wx.login({
        success: res => {
          wx.request({
            url: 'https://www.yangshuxian.xyz:80/sleep/loginOrRegister/',
            data: {
              'name': app.globalData.userInfo.nickName,
              'avatar': app.globalData.userInfo.avatarUrl,
              'topenId': this.data.topenId,
              'js_code': res.code,
            },
            method: 'POST',
            header: {
              "Content-Type": "application/x-www-form-urlencoded"
            },
            success: res => {
              console.log('第一个login:', res.data)
              app.globalData.wopenId = res.data[0]
              
              // 如果是直接进入的小程序，即进入自己的主页，那就从后台拿到自己的openID后赋值给topenId
              if (JSON.stringify(e) === "{}") {
                app.globalData.topenId = res.data[0]
                this.setData({
                  topenId: res.data[0],
                  isYourself: true,
                  isGotoYourself: true,
                })
              } else if (typeof (e.scene) === 'undefined') {
                if (e.user === res.data[0]) {
                  this.setData({
                    isYourself: true,
                    isGotoYourself: true,
                  })
                }
              } else {
                var scene = decodeURIComponent(e.scene)
                if (scene === res.data[0]) {
                  this.setData({
                    isYourself: true,
                    isGotoYourself: true,
                  })
                }
              }
              this.setData({
                tavatar: res.data[3],
                fangzhi:res.data[4],
              })

              var huaListcang = res.data[1]
              var huaList = res.data[2]
              var isOpenListLocal = []
              var randomHeightList = []
              var i = 0
              for (i in huaList) {
                isOpenListLocal.push(false)
                randomHeightList.push(' ')
              }
              if (huaList.length === 0) {
                this.setData({
                  num: 0
                })
              } else {
                this.setData({
                  num: parseInt(i) + 1
                })
              }
              this.setData({
                userInfo: app.globalData.userInfo,
                dansentencelist: huaList,
                dansentencelistcang: huaListcang,
                isOpenList: isOpenListLocal,
                randomHeightList: randomHeightList,
              })
              runtime = i * 1.8 + 17
              this.sankai()
            }
          })
        }
      });
    }
  },

  onReady: function() {},

  onShow: function() {
    app.globalData.isDelete
    if (!isFirstOpenIndex && app.globalData.isTohoutai){
      wx.showLoading({
        title:'重新加载中……',
        mask:true,
      })
      this.setData({
        isTohoutai:false,
        isOpenList: [],
        randomHeightList: [],
        dansentencelist: [
          [1, '1s'],
          [2, '1s'],
          [3, '1s'],
          [4, '1s'],
          [5, '7s'],
          [6, '7s'],
          [7, '7s'],
          [8, '7s'],
        ],
        dansentencelistcang: [],
        tmpdansentencelist: [],
      })
      randomHeightListMod = [
        // 'left:750rpx;bottom:27%;',
        'left:750rpx;bottom:31%;',
        'left:750rpx;bottom:35%;',
        'left:750rpx;bottom:39%;',
        'left:750rpx;bottom:43%;',
        'left:750rpx;bottom:47%;',
        'left:750rpx;bottom:51%;',
        'left:750rpx;bottom:55%;',
        'left:750rpx;bottom:59%;',
      ]
      huishourandomHeightListMod = []
      jishiqi = 1
      cishu = 1
      fsjsq = 0
      smallTime = 0
      // runtime = 20
      index = 0 //用来给isOpenList每一个元素进行改值
      clearInterval(ccc)
      clearInterval(ddd)
      clearInterval(eee)
      clearTimeout(fff)
      app.globalData.isTohoutai = false
      this.onLoad({})
      wx.hideLoading()
    }
    else{
      isFirstOpenIndex = false
    }
    var that = this;
    var myDate = new Date();
    var duration = 79200 - myDate.getHours() * 3600 - myDate.getMinutes() * 60 - myDate.getSeconds()
    if (duration < 0) {
      duration = 86400 + duration
    }
    function countDown(times) {
      var timer = null;
      timer = setInterval(function () {
        var day = 0,
          hour = 0,
          minute = 0,
          second = 0; //时间默认值
        if (times > 0) {
          day = Math.floor(times / (60 * 60 * 24));
          hour = Math.floor(times / (60 * 60)) - (day * 24);
          minute = Math.floor(times / 60) - (day * 24 * 60) - (hour * 60);
          second = Math.floor(times) - (day * 24 * 60 * 60) - (hour * 60 * 60) - (minute * 60);
        }
        if (day <= 9) day = '0' + day;
        if (hour <= 9) hour = '0' + hour;
        if (minute <= 9) minute = '0' + minute;
        if (second <= 9) second = '0' + second;
        that.setData({
          hour: hour + ':',
          minute: minute + ':',
          second: second,
        })
        // console.log(day + "天:" + hour + "小时：" + minute + "分钟：" + second + "秒");
        times--;
        fsjsq += 1
        // console.log(fsjsq)
        if (times === 0) {
          times = 86400
          // console.log('流星语来临')
          // wx.showToast({
          //   title: '流星语来啦！！！！！快看看都有谁来许愿了~~~~',
          //   icon: 'none',
          //   duration: 4000,
          // })
          that.setData({
            isOpen: false,
          })
          that.setData({
            tmpdansentencelist: that.data.dansentencelist,
            isStarComing: true,
            isOpen: true,
          })
        }
        if (times === 79260) {
          // console.log('流星语还有一分钟就要隐藏啦！！！')
          // wx.showToast({
          //   title: '流星语还有一分钟就要隐藏啦！！！',
          //   icon: 'none',
          //   duration: 4000,
          // })
        }
        if (times === 79200) {
          // console.log('流星语隐藏')
          // wx.showToast({
          //   title: '流星语隐藏，明天等你哟~',
          //   icon: 'none',
          //   duration: 4000,
          // })
          that.setData({
            tmpdansentencelist: that.data.dansentencelistcang,
            isStarComing: false,
          })
        }
      }, 1000);
    }
    countDown(duration)
  },

  sankai: function () {
    var that = this
    var randomHeightListLocal = []
    var isOpenListLocal
    var danlistLocal
    // if (this.data.dansentencelist)
    if (this.data.dansentencelist.length == 0) {
      runtime = 4
    }
    // if (cishu <= 2) {
    //   if (!this.data.isStarComing) {
    //     wx.showToast({
    //       title: '今晚22点解开流星的密语~',
    //       icon: 'none',
    //       duration: 2000,
    //     })
    //     cishu += 1
    //   }
    // }

    // ————————————————————————每过1.8s让一个弹幕动起来—————————————————————————————
    ccc = setInterval(function () {
      // console.log(index, danlistLocal.length - 1)
      // 放在这里给Local赋值而不放在外面是因为当要send的时候data里面的数据
      // 如果不每1.8s重新获取一次的话，
      // 只会拿到初始化时候的最原始的data
      isOpenListLocal = that.data.isOpenList
      danlistLocal = that.data.dansentencelist
      if (index <= danlistLocal.length - 1) {
        isOpenListLocal[index] = true //让当前index的弹幕动起来
        var tmp = Math.floor((Math.random() * randomHeightListMod.length)) //获取randomHeightListMod里面随机一个高度
        randomHeightListLocal[index] = [randomHeightListMod[tmp]] //把获取到的随机高度放入randomHeightListLocal中间变量
        huishourandomHeightListMod.push(randomHeightListMod[tmp])
        randomHeightListMod.splice(tmp, 1)
        that.setData({
          isOpenList: isOpenListLocal,
          randomHeightList: randomHeightListLocal
        })
        index += 1
      }
    }, 1800)

    // ———————等待前四个弹幕过后，每过1.8s把randomHeightListMod列表pop出来的元素放回去，让后来的弹幕可以有更多的选择，因为前四个弹幕过后刚好是第一个弹幕完全出现——————
    ddd = setInterval(function () {
      if (index >= 4) {
        // console.log('huishourandomHeightListMod的长度：', huishourandomHeightListMod.length)
        if (huishourandomHeightListMod.length) {
          randomHeightListMod.push(huishourandomHeightListMod[0])
          huishourandomHeightListMod.splice(0, 1)
          // console.log('huishourandomHeightListMod:', huishourandomHeightListMod)
        }
      }
    }, 1800)

    // ———————————————————————当全部的弹幕发送消失完后执行一次刷新————————————————————————
    var danmushuaxinFun = function () {
      index = 0
      if (typeof (isOpenListLocal) !== 'undefined') {
        if (isOpenListLocal.length !== 0) {
          for (var i in isOpenListLocal) {
            isOpenListLocal[i] = false
          }
          for (var j in huishourandomHeightListMod) {
            randomHeightListMod.push(huishourandomHeightListMod[0])
            huishourandomHeightListMod.splice(0, 1)
          }
          that.setData({
            isOpenList: isOpenListLocal,
          })
          //———————————————————————————————————————————————————————————————————————————
          //清除是由于setInterval的循环时间runtime
          //在初始化的时候就定好了中途不能动态改变，只能清除当前循环改了循环时间之后再定义另一个循环
          //———————————————————————————————————————————————————————————————————————————
          clearInterval(eee)
          runtime = i * 1.8 + 17
          eee = setInterval(danmushuaxinFun, runtime * 1000 - 1700)
        }
      }
    }
    eee = setInterval(danmushuaxinFun, runtime * 1000 - 1700)
    // ——————————————————————————————————————————————————————————————————————————————

  },

  send: function (e) {
    if (this.data.inputValue === '') {
      wx.showToast({
        title: '还没写寄语哟~',
        image: '../../images/yueliang.png',
      })
    } else {
      wx.request({
        url: 'https://www.yangshuxian.xyz:80/sleep/sendTalk/',
        data: {
          topenId: app.globalData.topenId,
          wopenId: app.globalData.wopenId,
          sentence: this.data.inputValue,
          isNiming: this.data.isNiming,
        },
        method: 'POST',
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        success: e => {
          // ————————————————————————————————给已有的弹幕列表及时插入要发送的弹幕————————————————————————————————
          console.log(e)
          var that = this;
          var sentence = this.data.inputValue
          if (!this.data.isStarComing) {
            if (sentence.length >= 5) {
              sentence = sentence.slice(0, 3) + '■■■■■■■'
            } else if (sentence.length === 4) {
              sentence = sentence.slice(0, 2) + '■■■■■■■'
            } else {
              sentence = '■■■■■■■'
            }
          }
          if (this.data.isNiming) {
            var newdanmu = [sentence, "", "../../images/niming.jpeg", "color:red;", "background: linear-gradient(to left, rgba(253, 225, 167,0), rgba(253, 225, 167,1));"]
          } else {
            var newdanmu = [sentence, "", app.globalData.userInfo.avatarUrl, "color:red;", "background: linear-gradient(to left, rgba(253, 225, 167,0), rgba(253, 225, 167,1));"]
          }


          var dansentencelistLocal = this.data.dansentencelist
          var dansentencelistcangLocal = this.data.dansentencelistcang
          var isOpenListLocal = this.data.isOpenList
          dansentencelistLocal.splice(index, 0, newdanmu)
          dansentencelistcangLocal.splice(index, 0, newdanmu)
          isOpenListLocal.splice(index, 0, false)
          console.log(this.data.num)
          this.setData({
            isSend: !this.data.isSend,
            isUp: false,
            dansentencelist: dansentencelistLocal,
            dansentencelistcang: dansentencelistcangLocal,
            isOpenList: isOpenListLocal,
            num: this.data.num + 1
          })
          console.log(this.data.num)
          // ——————————————————————————————————————————————————
          // 设置一个setTimeout用来保证本次弹幕的滚动时长，
          // 并清除下面sankai函数的setInterval，
          // 等当前setTimeout结束的时候再创建一个setInterval，
          // 分两种，第一种，弹幕没完全显示出来，也就是不在末尾加入弹幕的话，
          // setTimeout的时长就是16s(一个弹幕完全运行的时间-1s)加上后面还有未显示弹幕的个数*1.8s
          // 第二种，弹幕完全显示出来，setTimeout的时长就是16s
          // ——————————————————————————————————————————————————
          var nowruntime = 0
          if (index <= dansentencelistLocal.length) {
            nowruntime = 16 + (dansentencelistLocal.length - index - 1) * 1.8
          } else {
            nowruntime = 16
          }

          clearInterval(eee)           //清除这一轮的setInteval,让这一个setTimeout代替这一轮的setInteval
          clearTimeout(fff)            //如果一整个弹幕循环内发送了多次弹幕，要把上一次的setTimeout给clear掉

          //设置setTimeout
          fff = setTimeout(function () {
            index = 0
            for (var i in isOpenListLocal) {
              isOpenListLocal[i] = false
            }
            for (var j in huishourandomHeightListMod) {
              randomHeightListMod.push(huishourandomHeightListMod[0])
              huishourandomHeightListMod.splice(0, 1)
            }
            that.setData({
              isOpenList: isOpenListLocal,
            })
            runtime = i * 1.8 + 17
            // 重新创建setInterval
            var danmushuaxinFun = function () {
              index = 0
              for (var i in isOpenListLocal) {
                isOpenListLocal[i] = false
              }
              for (var j in huishourandomHeightListMod) {
                randomHeightListMod.push(huishourandomHeightListMod[0])
                huishourandomHeightListMod.splice(0, 1)
              }
              that.setData({
                isOpenList: isOpenListLocal,
              })
              //———————————————————————————————————————————————————————————————————————————
              //清除是由于setInterval的循环时间runtime
              //在初始化的时候就定好了中途不能动态改变，只能清除当前循环改了循环时间之后再定义另一个循环
              //———————————————————————————————————————————————————————————————————————————
              clearInterval(eee)
              runtime = i * 1.8 + 17
              eee = setInterval(danmushuaxinFun, runtime * 1000 - 1700)
            }

            eee = setInterval(danmushuaxinFun, runtime * 1000 - 1700)

          }, nowruntime * 1000)

          console.log('send:', this.data.dansentencelist, this.data.dansentencelistcang)


          // ——————————————————————————等待输入框流星飞行时间完成后把输入框复原——————————————————————————————
          aaa = setTimeout(function () {
            that.setData({
              isSend: !that.data.isSend,
              inputValue: '',
            })
          }, 1800)
        }
      })
    }
  },

  onShareAppMessage: function(e) {
    return {
      title: '来这说出平时不敢对我说的话吧~',
      path: '/pages/index/index?user=' + app.globalData.wopenId,
    }
  },

  onHide:function(){
    app.globalData.isTohoutai = true
  },

  // 第一次获取用户信息，主动点击登录按钮
  getUserInfo: function(e1) {
    console.log('获取用户信息', e1.detail.userInfo)
    app.globalData.userInfo = e1.detail.userInfo
    this.setData({
      userInfo: e1.detail.userInfo,
      hasUserInfo: true,
    })
    wx.login({
      success: res => {
        wx.request({
          url: 'https://www.yangshuxian.xyz:80/sleep/loginOrRegister/',
          data: {
            'name': app.globalData.userInfo.nickName,
            'avatar': app.globalData.userInfo.avatarUrl,
            'topenId': this.data.topenId,
            'js_code': res.code,
          },
          method: 'POST',
          header: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          success: res => {
            console.log('用户第一次的login:', res.data, onload_e)
            app.globalData.wopenId = res.data[0]
            
            // 如果是直接进入的小程序，即进入自己的主页，那就从后台拿到自己的openID后赋值给topenId
            if (JSON.stringify(onload_e) === "{}") {
              app.globalData.topenId = res.data[0]
              this.setData({
                topenId: res.data[0],
                isYourself: true,
                isGotoYourself: true,
              })
            } else if (typeof (onload_e.scene) === 'undefined') {
              //如果是扫自己转发的小程序码
              if (onload_e.user === res.data[0]) {
                this.setData({
                  isYourself: true,
                  isGotoYourself: true,
                })
              }
            } else {
              var scene = decodeURIComponent(onload_e.scene)
              //如果进入的是自己转发出去的卡片
              if (scene === res.data[0]) {
                this.setData({
                  isYourself: true,
                  isGotoYourself: true,
                })
              }
            }
            this.setData({
              tavatar: res.data[3],
              fangzhi: res.data[4],
            })

            var huaListcang = res.data[1]
            var huaList = res.data[2]
            var isOpenListLocal = []
            var randomHeightList = []
            for (var i in huaList) {
              isOpenListLocal.push(false)
              randomHeightList.push(' ')
            }
            this.setData({
              userInfo: app.globalData.userInfo,
              dansentencelist: huaList,
              dansentencelistcang: huaListcang,
              isOpenList: isOpenListLocal,
              randomHeightList: randomHeightList,
              num: parseInt(i) + 1
            })
            runtime = i * 1.8 + 17
            this.sankai()
          }
        })
      }
    });
  },

  goto: function() {},

  finishInput: function(e) {
    if (e.type === 'blur') {
      this.setData({
        sentece: e.detail.value,
        inputValue: e.detail.value
      })
    } else {
      this.setData({
        sentece: e.detail.value,
        inputValue: e.detail.value
      })
      this.send();
    }
  },

  startAndPaused: function() {
    this.setData({
      isPaused: !this.data.isPaused
    })
    if (this.data.isPaused) {
      app.globalData.backgroundAudioManager.pause()
    } else {
      app.globalData.backgroundAudioManager.play()
    }
  },

  upAndDown: function() {
    this.setData({
      isUp: true,
      isFirstOpen2: false,
    })
  },

  // 换一批
  huanyipi: function() {
    if (this.data.i === 6) {
      this.setData({
        i: 0,
        talkListNow: this.data.talkList.slice(0, 3)
      })
    } else {
      var i = this.data.i
      this.setData({
        talkListNow: this.data.talkList.slice(i + 3, i + 6),
        i: i + 3
      })
    }
  },

  xuanze: function(e) {
    this.setData({
      inputValue: e.currentTarget.dataset.id,
      isUp:true
    })
  },
  juzidown: function() {
    this.setData({
      isUp: false,
    })
  },
  shiming: function() {
    this.setData({
      isNiming: !this.data.isNiming,
    })
  },
  tips: function() {
    wx.previewImage({
      urls: ['https://jordoncat.oss-cn-shenzhen.aliyuncs.com/images/sleeptalk.jpg'],
    })
  },
  share: function() {
    wx.navigateTo({
      url: '../guanli/guanli',
    })
  },
  guanli: function() {
    if (this.data.isGotoYourself) {
      wx.navigateTo({
        url: '../fenxiang/fenxiang',
      })
    } else {
      this.setData({
        isGotoYourself: true,
        isFirstOpen: false
      })
      clearInterval(ccc)
      clearInterval(ddd)
      clearInterval(eee)
      this.onLoad({})
    }
  }
})