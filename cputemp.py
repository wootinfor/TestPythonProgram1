import urllib2
import json
import time
import datetime
APIKEY = 'oqSRzDP3XmZCxdShLtvEfxye54E'  #改成你的APIKEY
def get_temp():
    file= open("/sys/class/thermal/thermal_zone0/temp") 
    temp=float(file.read())/1000 
    file.close() 
    print ("temp : %.1f" %temp)
    return temp

    
def http_put():
    temperature = get_temp() #获取CPU温度并上传
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/533926029/datapoints'
    values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}

    print ("当前的ISO时间为： %s" %CurTime.isoformat())
    print ("上传的温度值为: %.3f" %temperature)

    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    #打印json内容
    print (jdata)
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', APIKEY)
    request.get_method = lambda:'POST'          # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

while True:
        time.sleep(5)
        resp = http_put()
        print("OneNET请求结果:\n %s" %resp）
        time.sleep(5)