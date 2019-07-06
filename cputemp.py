import urllib2
import json
import time
import datetime
APIKEY = 'oqSRzDP3XmZCxdShLtvEfxye54E'
def get_temp():
        # 打开文件 
        file = open("/sys/class/thermal/thermal_zone0/temp") 
        temp = float(file.read()) / 1000 
        file.close() 
        print "CPU的温度值为: %.3f" %temp 
        return temp
        
        
def http_put():
    temperature = get_temp() 
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/533941417/datapoints'
    values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}

    print "当前的ISO时间为： %s" %CurTime.isoformat()
    print "上传的温度值为: %.3f" %temperature

    jdata = json.dumps(values)            
    print jdata
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', APIKEY)
    request.get_method = lambda:'POST'  
    request = urllib2.urlopen(request)
    return request.read()

while True:
        time.sleep(5)
        resp = http_put()
        print "OneNET请求结果:\n %s" %resp
        time.sleep(5)