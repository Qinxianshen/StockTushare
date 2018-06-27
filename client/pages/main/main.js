// pages/main/main.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    routers: [
      {
        name: '区块链',
        url: "../blockchain/blockchain",
        icon: '../../images/blockchain.png'
      },
      {
        name: '个股上榜',
        url: "../longhu/longhu",
        icon: '../../images/longhu.png'
      },
      {
        name: '宏观数据',
        url: "../BigData/BigData",
        icon: "../../images/bigdata.png"
      },
      {
        name: '票房',
        url: "../film/film",
        icon: "../../images/film.png"
      },
      {
        name: '大盘数据',
        url: "../Basic/Basic",
        icon: "../../images/refence.png"
      },
      {
        name: '新股',
        url: "../newStock/newStock",
        icon: "../../images/newStock.png"
      },
      {
        name: '销售股解禁',
        url: "../XsgData/XsgData",
        icon: "../../images/xsgData.png"
      },
      {
        name: '停股',
        url: "../StopStock/StopStock",
        icon: "../../images/StopStock.png"
      },
      {
        name: '行业分类',
        url: '../industry/industyclass',
        icon: "../../images/industryclass.png"
      }
    ],
    icon_cover_url:[
      "../../images/HangQin-icon-selected.png",
      "../../images/HangQin-icon-selected.png",
      "../../images/HangQin-icon-selected.png",
      "../../images/HangQin-icon-selected.png",
      "../../images/HangQin-icon-selected.png",
      "../../images/HangQin-icon-selected.png",
    ],
    icon_name:[
      "区块链",
      "龙虎榜",
      "宏观数据",
      "票房",
      "投资参考",
      "分类数据"
    ],
    icon_url:[
      "../new/singerNew",
      "../new/singerNew",
      "../new/singerNew",
      "../new/singerNew",
      "../new/singerNew",
      "../new/singerNew",
    ]
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: url2,
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        console.log(res);
        console.log("sucsdasdcess!!!!!");
      },
      fail: function (res) {
        console.log("ffffffffffffffff!!!!!");
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