
import turtle
import time
#  设置画布大小
#  t.screensize(canvwidth= None,canvheight= None,bg=None)  #  参数分别为宽度，高度，背景颜色
#  t.setup(width=0.5,height=0.75,startx=None,starty=None)
#  参数 ： width,height:输入宽和高为整数时，表示像素，为小数时，表示占据屏幕的比列（startx,starty):
# 这一坐标表示矩形窗口左上角顶点的位置，如果为空，则窗口位于屏幕中心
#画笔属性
#  t.pensize():设置画笔的宽度，t.pencolor()：传入参数设置画笔颜色，可以是字符串"red",也可以是RGB3元组"#ffooff"
#   t.speed(0-10):  设置画笔移动速度，0-10整数，数字越大越快
#

# 调用turtle中的Pen函数创建画布
t = turtle.Pen()

# 矩形 画笔运动命令
for i in range(0,4):
    #   往前画一条直线，移动100个像素
    t.forward(100)
    #   左转弯90度
    t.left(90)
    t.reset()  # 擦除画布，并将海龟放回开始的位置                       t.clear()只清除屏幕，海龟仍然在原位
    time.sleep(1) # 停一秒
    t.right(90)   # 右转90度，顺时针
    t.backward() #后退
    t.up()  #抬笔停止作画
    t.down()  #落笔开始作画
    t.goto(x,y)   # 将画笔移动到坐标x,y的位置
    t.circle()     # 画圆
    setx()   #将当前x轴移动到指定位置

    sety()   #将当前y轴移动到指定位置
    setheading(90)  #设置当前朝向为90角度
    home()    # 设置当前画笔位置为原点，朝向东
    dot()    #  绘制一个指定直径和颜色的圆点

   # 画笔控制命令
    t.fillcolor(colorstring)   # 绘制图形的填充颜色
    t.color(color1,color2)   # 同时设置pencolor=color1,fillcolor=color2
    t.filing()    # 返回当前是否在填充状态
    t.begin_fill()   # 准备开始填充图形
    t.end_fill()   # 填充完成
    t.hideturtle()  # 隐藏画笔的turtle形状
    t.showturtle()   # 显示画笔的turtle形状
    t.undo()        #  撤销上一个turtle动作
    stamp()    #  复制当前图形
    t.write(s[,font=("font-name",font_size,"font_type")])   #  写文本，s为文本内容，font是字体参数，分别为字体名称，大小和类型

    #  t.mainloop()  启动事件循环-调用tk中的mainloop()函数，必须是最后一个语句



