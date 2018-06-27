// pages/longhu/longhu.js
var STOCK_URL = "http://150.95.177.133:5000/Getgegushangbang";
Page({
  data: {
    data: {},
    name: {}
  },
  onLoad: function (options) {
    var that = this
    wx.showToast({
      title: '加载中...',
      icon: 'loading',
      duration: 10000
    });

    wx.request({
      url: STOCK_URL,
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var data = res.data.data;
        data = JSON.parse(data);
        console.log(data);
        that.setData({
          data: data,
          name: data.name
        });
        wx.hideToast();
      }
    });

  }
})