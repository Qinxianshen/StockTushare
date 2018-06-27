// pages/post/Basic.js
var STOCK_URL = "http://150.95.177.133:5000/GetHistData/";
Page({
  data: {
    data: {},
    name:"",
    StockCode:"",
    code:0,
    open:"",
    close:"",
    high:"",
    low:"",
    turnover:""
  },
  onLoad: function (options) {
    var that = this;
    var code = options.code;
    that.setData({
      code:code
    });
    console.log("code!!!!!!!!!!!!!!!!!!!!!!"+code);
    wx.showToast({
      title: '加载中...',
      icon: 'loading',
      duration: 10000
    });

    wx.request({
      url: STOCK_URL + code.toString(),
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var data = res.data.data;
        data = JSON.parse(data);
        console.log(data);
        that.setData({
          data: data,
          code:code,
          open:data.open,
          close:data.close,
          high:data.high,
          low:data.low,
          turnover:data.turnover
        });
        wx.hideToast();
      }
    });

  }
})