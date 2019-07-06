from wxpy import *
from bypy import ByPy
import os
import time
import datetime
import threading
bot=Bot()
bp=ByPy()
def save(filename, msg):
      fh = open(filename, 'a+', encoding='utf-8')
      msg=msg+'\n'
      fh.write(msg)
      fh.close()
@bot.register()
def face_msg(msg):
    msg2=msg
    print(msg2)
    print(msg2.receive_time)
    print(msg2.type)
    global Folder_1
    if msg2.type==TEXT:
          print('这个是字符串类型')
          print(msg2.text)
          Folder_1=str(msg2.text)
          print(Folder_1)
          Folder_1.replace(' ','')
          Folder_1.replace(':','')
          Folder_1.replace('(','')
          Folder_1.replace(')','')
          print(Folder_1)
          text1=str(msg2.receive_time)+str(msg2)
          save('/root/weixin/xiaoxi.txt', text1)
    else:
            print('错误')
            image_name = msg2.file_name
            print ('接收图片')
            print (image_name)
            print(msg2.receive_time)
            print('folder_1'+Folder_1)
            msg2.get_file('/root/weixin/' + msg2.file_name)
            path='/root/weixin/' + msg2.file_name
            print('path'+path)
            print('chuangjian'+'dir_name/'+Folder_1)
            Folder_2=Folder_1+'new'
            bp.mkdir(Folder_2)
            bp.upload(localpath= path, remotepath= Folder_2, ondup='newcopy')
            print('上传成功'+path)
    
embed()