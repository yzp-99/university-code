import requests
from multiprocessing import Pool

# 爬电影测试代码
def temp(i):
    #  电影片段文件的http://vipmp4i.vodfile.m1905.com/201911181127/ba9cc46f9036eb448eb458b13efb2677/movie/2018/05/08/m2018050804FPO4ORM7GE0O8S/0210A91CB6860894A1BAA397F.mp4
#          https://leshi.cdn-zuyida.com/20180127/mO2ad0Th/800kb/hls/KwDM28077000.ts
    url = "" % i

    # 模拟浏览器
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

    # 使用requests.get方法返回当前url的信息
    r = requests.get(url, headers=headers)
    #  打印返回的信息
    print(r)
    with open('{}'.format(url[-10:]), 'wb') as f:
        f.write(r.content)



if __name__ == '__main__':
    pool = Pool(20)  # 开20个进程
    for i in range(2300):
        pool.apply_async(temp, (i,))

    pool.close()
    pool.join()
