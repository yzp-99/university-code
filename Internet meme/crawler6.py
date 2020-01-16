import re
from urllib import request

url = "https://y.qq.com/portal/player.html"

response = request.urlopen(url)
html = response.read().decode('utf-8')

music_id = int(re.findall(r'MusicId-()')[0])

music_url = (r"http://[a-z]\.[a-z]\.qqmusic\.qq.com/[0-9],[A-Za-z]\.m4a?guid=[0-9]&key=[0-9],[A-Z]%uin0&[a-z]=[0-9]")
#music_url = "https://isure.stream.qqmusic.qq.com/C400001z5XSY0VRovU.m4a?guid=7934275328&vkey=40B8C6D0014BF8C21960E45A53D01E04CE15189897B0EAA758D39C0AE51C9F9A623C071C6929CBD71C18E75868128C38A839CB137B353D60&uin=0&fromtag=66"
data = request.urlopen(music_url).read()
#  写MP3文件
with open("123.m4a", 'wb') as f:
    f.write(data)

print(music_url)
#//y.gtimg.cn/c/=/music/portal/js/common/map.js,/music/portal/js/common/music/mod.js?r=" + parseInt(new Date()/600000) ;
#	l = d.getElementsByTagName("head")[0];