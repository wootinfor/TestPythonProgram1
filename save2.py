from wxpy import *
from bypy import ByPy
import os
import time
import datetime
import threading
bot=Bot()
def save(filename, msg):
      fh = open(filename, 'a+', encoding='utf-8')
      msg=msg+'\n'
      fh.write(msg)
      fh.close()
@bot.register()
def face_msg(msg):
    msg1=msg
    msg2=msg
    print(msg2)
    print(msg2.receive_time)
    msg2=str(msg2.receive_time)+str(msg2)
    save('f:\\imag\\xiaoxi.txt', msg2)
    
    image_name = msg1.file_name
    print ('接收图片')
    print (image_name)
    print(msg1.receive_time)
    imagetime=str(msg1.receive_time)
    msg1.get_file('F:\\imag\\' + msg1.file_name)
    path='F:\\imag\\' + msg1.file_name
    
    bp=ByPy()
    bp.upload(localpath= path, remotepath= 'dir_name', ondup='newcopy')
    bp.upload(localpath='f:\\imag\\xiaoxi.txt', remotepath= 'dir_name', ondup='overwrite')
    print('上传成功'+path+'f:\\imag\\xiaoxi.txt')

embed()