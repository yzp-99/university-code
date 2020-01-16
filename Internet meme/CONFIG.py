from urllib import request
import re
url ="https://y.qq.com/portal/player.html"
#  爬音乐测试代码
response = request.urlopen(url)
html = response.read().decode('utf-8')
music_id = int(re.findall(r'MusicId=(\d+)', html)[0]) #  字符串整数
#print(music_id)
# 拼接数据

#music_name = re.findall(r'<title>(.*)</title>', html)[0].split('/')[0].strip()

#musicword = re.findall(r'<div class-"textgeci show"id="showtext">(.*?)</div>', html, re.S)

#with open('%s.txt'% music_name, 'w', encoding= 'utf-8') as f:
  #  f.write(musicword)

music_url = "http://96.ierge.cn/%d/%d/%d.mp3" % (music_id//30000, music_id//20000, music_id)

print(music_url)
#下载MP3数据

data = request.urlopen(music_url).read()
#  写MP3文件
with open("%s.mp3"% music_id, 'wb') as f:
  #  f.write(data)
