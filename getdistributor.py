# -*- coding: cp936 -*-
from  urllib import urlopen
import re 
def getmap(name,ak='DBab327ad18390ef95a93b91b843583a',city=''):
    name='http://api.map.baidu.com/geocoder/v2/?ak='+ak+'callback=renderOption&output=xml&address='+name+'&city='+city
    data=urlopen(name)
    line=data.readline()
    lat=0
    lng=0
    while(len(line)>0):
        ##判断读取的行是否为需要的信息
        ##获取维度值
        if line.find('\t\t\t\t<lat>')>=0:
            lat=float(re.match('\t\t\t\t<lat>*(.*)</lat>\r\n',line).group(1))
            #line=line.replace('\t\t\t\t<lat>', '')
            #line=line.replace('</lat>\r\n', '')
            #lat=float(line)
        elif line.find('\t\t\t\t<lng>')>=0:
            ##获取经度值
            lng=float(re.match('\t\t\t\t<lng>*(.*)</lng>\r\n',line).group(1))
            #line=line.replace('\t\t\t\t<lng>', '')
            #line=line.replace('</lng>\r\n', '')
            #lng=float(line)
        ###查到数据后退出循环
        if lat!=0 and lng!=0:
            data.close
            return (lat,lng)
        line=data.readline()
    ##未找到位置信息，就返回（0，0）
    if lat==0 and lng==0:
        return (lat,lng)
##读取地址信息文件C:\Users\wenlihaoyu\Desktop\map
import csv
import sys
##from  getmapurl import  getmap
##x DISCODE DISNAME SUBSTR_DISNAME(DISNAME)
##BOSS OFFICECODE OFFICENAME SHOPADDR	CITY

def get_mapdata(file="C:/Users/wenlihaoyu/Desktop/distributor.csv",name='SHOPADDR',city=''):
             
    with open(file, 'rb') as csvfile:
         reader = csv.DictReader(csvfile)
         column = [row[name] for row in reader]
###循环数据，获得对应地址的经纬度信息
    with open("C:/Users/wenlihaoyu/Desktop/map/get_distributor.csv", 'wb') as writefile :
        writer = csv.writer(writefile)
        writer.writerow('address,lat,lng')
        for x in column:
    ##获取经纬度信息
           lat,lng=getmap(name=x,city=city)
        #print x,lat,lng
           y=x,lat,lng
           writer.writerow(y)
           return True
get_mapdata(file="C:/Users/wenlihaoyu/Desktop/distributor.csv",name='SHOPADDR')
