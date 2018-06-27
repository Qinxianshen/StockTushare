#-*- coding:utf-8 -*-
import tushare as ts
import time


#获取当前时间
def getNowTime():
    nowtime = time.strftime("%Y-%m-%d",time.localtime())
    print(nowtime)
    return nowtime
# 获取实时电影票房数据
# BoxOffice
# 实时票房（万）
# Irank
# 排名
# MovieName
# 影片名
# boxPer
# 票房占比 （ % ）
# movieDay
# 上映天数
# sumBoxOffice
# 累计票房（万）
# time
# 数据获取时间
def GetRealtime_boxoffice():
    df = ts.realtime_boxoffice()
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#获取今日票房
#
# AvgPrice 平均票价
# AvpPeoPle 场均人次
# BoxOffice 单日票房（万）
# BoxOffice_Up 环比变化 （%）
# IRank 排名
# MovieDay 上映天数
# MovieName 影片名
# SumBoxOffice 累计票房（万）
# WomIndex 口碑指数
def GetDayBoxOffice():
    df = ts.day_boxoffice()
    df = df.to_json(force_ascii=False)
    print(df)
    return df
#获取单月电影票房数据
    #
    # Irank 排名
    # MovieName 电影名称
    # WomIndex 口碑指数
    # avgboxoffice 平均票价
    # avgshowcount 场均人次
    # box_pro 月度占比
    # boxoffice 单月票房(万)
    # days 月内天数
    # releaseTime 上映日期
def GetMonthBoxOffice():
    df =  ts.month_boxoffice()
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#获取全国影院单日票房排行数据
    # Attendance 上座率
    # AvgPeople 场均人次
    # CinemaName 影院名称
    # RowNum 排名
    # TodayAudienceCount 当日观众人数
    # TodayBox 当日票房
    # TodayShowCount 当日场次
    # price 场均票价（元）
def GetDayCinema():
    df = ts.day_cinema()
    df = df.head(10)
    df = df.to_json(force_ascii=False)
    print(df)
    return df
#按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据
def GetLongHuData(nowtime):
    df = ts.top_list(nowtime)
    df = df.to_json(force_ascii=False)
    print(df)
    return df

# 获取上证50成份股
#
# 返回值说明：
#
# code：股票代码
# name：股票名称
def Get_sz50s():
    df = ts.get_sz50s()
    print(df)
    return df

#获取每日龙虎榜
# 参数说明：
#
# date：日期，格式YYYY-MM-DD
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
# 返回值说明：
#
# code：代码
# name:名称
# pchange:当日涨跌幅
# amount：龙虎榜成交额(万)
# buy：买入额(万)
# bratio：买入占总成交比例
# sell：卖出额(万)
# sratio：卖出占总成交比例
# reason：上榜原因
# date：日期
def GetDaylonghubang():
    df = ts.top_list(getNowTime())
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#个股上榜统计
# 获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。
#
# 参数说明：
#
# days：统计周期5、10、30和60日，默认为5日
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
# 返回值说明：
#
# code：代码
# name:名称
# count：上榜次数
# bamount：累积购买额(万)
# samount：累积卖出额(万)
# net：净额(万)
# bcount：买入席位数
# scount：卖出席位数
def Getgegushangbang():
    df = ts.cap_tops()
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#营业部上榜统计
# 获取营业部近5、10、30、60日上榜次数、累积买卖等情况。
#
# 参数说明：
#
# days：统计周期5、10、30和60日，默认为5日
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
# 返回值说明：
#
# broker：营业部名称
# count：上榜次数
# bamount：累积购买额(万)
# bcount：买入席位数
# samount：累积卖出额(万)
# scount：卖出席位数
# top3：买入前三股票
def Getyingyeshangbang():
    df = ts.broker_tops()
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#机构席位追踪
# 获取机构近5、10、30、60日累积买卖次数和金额等情况。
#
# 参数说明：
#
# days：统计周期5、10、30和60日，默认为5日
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
# 返回值说明：
#
# code:代码
# name:名称
# bamount:累积买入额(万)
# bcount:买入次数
# samount:累积卖出额(万)
# scount:卖出次数
# net:净额(万)
def Getjigouxiwei():
    df = ts.inst_tops()
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#即时新闻
# 获取即时财经新闻，类型包括国内财经、证券、外汇、期货、港股和美股等新闻信息。数据更新较快，使用过程中可用定时任务来获取。
#
# 参数说明：
#
# top:int，显示最新消息的条数，默认为80条
# show_content:boolean,是否显示新闻内容，默认False
# 返回值说明：
#
# classify :新闻类别
# title :新闻标题
# time :发布时间
# url :新闻链接
# content:新闻内容（在show_content为True的情况下出现）
def GetNew():
    df = ts.get_latest_news()  # 默认获取最近80条新闻数据，只提供新闻类型、链接和标题
    df = ts.get_latest_news(top=5, show_content=True)  # 显示最新5条新闻，并打印出新闻内容
    df = df.to_json(force_ascii=False)
    print(df)
    return df

#信息地雷
# 获取个股信息地雷数据。
#
# 参数说明：
#
# code:股票代码
# date:信息公布日期
# 返回值说明：
#
# title:信息标题
# type:信息类型
# date:公告日期
# url:信息内容URL
def Getxinxidilei():
    df = ts.get_notices(date=getNowTime())
    print(df)
    return df

#新浪股吧
# 获取sina财经股吧首页的重点消息。股吧数据目前获取大概17条重点数据，可根据参数设置是否显示消息内容，默认情况是不显示。
#
# 参数说明：
#
# show_content:boolean,是否显示内容，默认False
# 返回值说明：
#
# title, 消息标题
# content, 消息内容（show_content=True的情况下）
# ptime, 发布时间
# rcounts,阅读次数
def Getxinlangguba():
    df = ts.guba_sina(True)
    df = df.to_json(force_ascii=False)
    print(df)
    return df


def GetStockBasics():
    df = ts.get_stock_basics()
    df = df.to_json(force_ascii=False)
    print(df)
    return df
if __name__ == "__main__":
    getNowTime()
    # GetRealtime_boxoffice()
    # GetDayBoxOffice()
    # GetMonthBoxOffice()
    # GetDayCinema()
    # GetLongHuData('2018-03-21')
    # Get_sz50s()
    # GetDaylonghubang()
    # Getgegushangbang()
    # Getyingyeshangbang()
    # Getxinxidilei()
    # Getxinlangguba()
    GetStockBasics()