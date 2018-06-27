// pages/new/singerNew.js
var news_URL = "http://150.95.177.133:5000/GetNew";
Page({

  /**
   * 页面的初始数据
   */
  data: {
    title:"",
    Content_from:"",
    Content_date:"",
    Content_num:"30",
    content:"",
    img_src: 'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg'
  },

  /**
   * 生命周期函数--监听页面加载"
   */
  onLoad: function (options) {
      console.log("!!!!!!!!!!!!!!!!!!!!"+options.id);
      var that = this
      var id = options.id;
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
          that.setData({
            data: data,
            title: data.title[id],
            Content_from: data.classify[id],
            Content_date:data.time[id],
            content: data.content[id]
          });
          wx.hideToast();
        }
      });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    this.requestData();
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})