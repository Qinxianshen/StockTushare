// pages/news/news.js
var news_URL = "http://150.95.177.133:5000/GetNew";
var url2 = "http://interface.sina.cn/wap_api/layout_col.d.json?&showcid=56261?&show_num=10";
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgUrls: [
      'http://150.95.177.133:5000/GetBitcoinPic',
      'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
      'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg'
    ],
    indicatorDots: true,
    autoplay: true,
    interval: 5000,
    duration: 1000,
    data : {},
    title:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onSwiperTap:function(event){
    var postId = event.target.dataset.postId;
    wx.navigateTo({
      url: "../new/singerNew",
    })
  },
  onLoad: function (options) {
    var that = this
      /**
   * 加载提示
   */
    wx.showToast({
      title: '加载中...',
      icon: 'loading',
      duration: 20000
    });

    wx.request({
      url: news_URL,
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var data = res.data.data;
        data = JSON.parse(data);
        console.log(data);
        console.log(data);
        that.setData({
          data: data,
          title: data.title
        });
        wx.hideToast();
      }
    });
  
  }
})