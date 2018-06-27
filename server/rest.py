#-*- coding:utf-8 -*-
from flask import Flask
from restfultools import *
from getData import *
import tushare as ts
import json
from flask import  jsonify

app = Flask(__name__)


#时间路由
@app.route('/getNowTime')
def RouteGetNowTime():
    return fullResponse(R200_OK,getNowTime())
#当前票房
@app.route('/GetRealtime_boxoffice')
def RouteGetRealtime_boxoffice():
    data = GetRealtime_boxoffice()
    data = json.loads(data)
    print(data)
    return jsonify({'status': R200_OK, 'BoxOffice':str(data['BoxOffice']),
             'MovieName':str(data['MovieName']),'movieDay':str(data['movieDay']),
             'boxPer':str(data['boxPer'])})
    #return fullResponse(R200_OK,GetRealtime_boxoffice())
#今日票房
@app.route('/GetDayBoxOffice')
def RouteGetDayBoxOffice():
    return fullResponse(R200_OK,GetDayBoxOffice())


#获取单月电影票房数据
@app.route('/GetMonthBoxOffice')
def RouteGetMonthBoxOffice():
    return fullResponse(R200_OK,GetMonthBoxOffice())

#获取全国影院单日票房排行数据
@app.route('/GetDayCinema')
def RouteGetDayCinema():
    return fullResponse(R200_OK,GetDayCinema())


#按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据
@app.route('/GetDayCinema')
def RouteGetLongHuData():
    return fullResponse(R200_OK,GetLongHuData(getNowTime()))

#获取上证50成份股
@app.route('/GetSZ50')
def RouteGetSZ50():
    return fullResponse(R200_OK,Get_sz50s())

#获取每日龙虎榜
@app.route('/GetDaylonghubang')
def RouteGetDaylonghubang():
    return fullResponse(R200_OK,GetDaylonghubang())

#个股上榜统计
@app.route('/Getgegushangbang')
def RouteGetgegushangbang():
    return fullResponse(R200_OK,Getgegushangbang())

#营业部上榜统计
@app.route('/Getyingyeshangbang')
def RouteGetyingyeshangbang():
    return fullResponse(R200_OK,Getyingyeshangbang())

#机构席位追踪
@app.route('/Getjigouxiwei')
def RouteGetjigouxiwei():
    return fullResponse(R200_OK,Getjigouxiwei())

#获取即时新闻
@app.route('/GetNew')
def RouteGetNew():
    return fullResponse(R200_OK,GetNew())

#获取信息地雷(信息空)
@app.route('/Getxinxidilei')
def RouteGetxinxidilei():
    return fullResponse(R200_OK,Getxinxidilei())

#新浪股吧
@app.route('/Getxinlangguba')
def RouteGetxinlangguba():
    return fullResponse(R200_OK,Getxinlangguba)

if __name__ == '__main__':
    app.run(host='0.0.0.0')