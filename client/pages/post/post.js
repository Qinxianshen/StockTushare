// pages/post/post.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    focus: false,
    inputValue: 0
  },
  bindButtonTap: function () {
    var that = this;
    var temp = 0;
    that.setData({
      focus: true
    });
    console.log(that.data.inputValue)
    temp = that.data.inputValue;
    wx.navigateTo({
      url: 'Basic?code=' + temp　　// 页面 A
    })

  },
  bindKeyInput: function (e) {
    var that = this;
    that.setData({
      inputValue: e.detail.value
    });
    console.log(e.detail.value);
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  onShow: function () {
    // Do something when page show.  
    console.log(inputValue);
  },  

})