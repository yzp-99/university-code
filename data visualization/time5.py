from pyecharts.charts import Bar



CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
clothes_v1 = [5, 20, 36, 10, 75, 90]
clothes_v2 = [10, 25, 8, 60, 20, 80]

bar = Bar('我的第一个图表', '这里是副标题')
bar.use_theme('dark')
bar.add('商家A', CLOTHES, clothes_v1)
bar.add('商家B', CLOTHES, clothes_v2)

bar.render(r'multi.html')