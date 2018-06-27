// pages/blockchain/blockchain.js
var STOCK_URL = "http://150.95.177.133:5000/GetBlockChainOhlcv";
Page({
  data: {
    data: {},
    MovieName: {},
    length:0
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
          length: data.length
        });
        wx.hideToast();
      }
    });

  }
})