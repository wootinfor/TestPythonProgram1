from wxpy import *
from bypy import ByPy
import os
import time
import datetime
import threading
bot = Bot(console_qr=True,cache_path=True)
@bot.register()
def face_msg(msg):
    image_name = msg.file_name
    print ('接收图片')
    print (image_name)
    print(msg.receive_time)
    imagetime=str(msg.receive_time)
    msg.get_file('/root/weixin/' + msg.file_name)
    path='/root/weixin/' + msg.file_name
    
    bp=ByPy()
    bp.upload(localpath= path, remotepath= 'dir_name', ondup='newcopy')
    print('上传成功'+path)

embed()