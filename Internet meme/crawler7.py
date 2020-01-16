import re
import urllib.request


# 爬取网络小说测试代码
def getNovelContent():

    html = urllib.request.urlopen("http://www.jinyongwang.com/oshu/").read()
    html = html.decode("utf-8")  # 转成该网址的格式

    # <li><a href="/oshu/1450.html">第一回　　古道骏马惊白发</a></li>  #参考

    reg = r'<li><a href="(.*?)">(.*?)</a></li>'  # 正则表达的匹配
    #http://www.jinyongwang.com(?=/oshu/)
    reg = re.compile(reg)  # 可添加可不添加，增加效率
    urls = re.findall(reg, html)
    for url in urls:
        print(url)
getNovelContent()
""""    for url in urls:
        #print(url)
        chapter_url = url[0]  # 章节的超链接
        chapter_title = url[1]  # 章节的名字
        #print(chapter_title)
        chapter_html = urllib.request.urlopen(chapter_url).read()  # 正文内容源代码
        chapter_html = chapter_html.decode("utf-8")
        #</script><p>符号中文</p><p></p><p>
        #</p><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        #r'</script><p>(.*?)</p><p><script async_src=".*?"></script>'
        chapter_reg = r'</script><p>(.*?)</p><p><script async_src=".*?"></script>'

        chapter_reg = re.compile(chapter_reg, re.S)
        chapter_content = re.findall(chapter_reg, chapter_html)
        for content in chapter_content:
            content = content.replace("</p><p>", "")
            #content = content.replace("<br />", "")
            print(content)
            f = open('{}.txt'.format(chapter_title), 'w')
            f.write(content)


getNovelContent()"""