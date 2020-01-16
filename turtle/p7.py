import turtle as t

t.title("熊猫宝宝")
t.shape("classic")
t.pensize(3)
t.color("black")
t.fillcolor("black")
t.speed(10)
t.hideturtle()
#左耳
t.penup()
t.goto(-105,97)
t.setheading(160)
t.begin_fill()
t.pendown()
t.circle(-30,230)
t.setheading(180)
t.circle(37,90)
t.end_fill()
#右耳
t.penup()
t.goto(105,97)
t.setheading(20)
t.begin_fill()
t.pendown()
t.circle(30,230)
t.setheading(0)
t.circle(-37,90)
t.end_fill()
#头部轮廓
t.penup()
t.goto(-67,140)
t.setheading(30)
t.pendown()
t.circle(-134,60)

t.penup()
t.goto(-50,-25)
t.setheading(180)
t.pendown()
t.circle(-100,30)
t.circle(-30,90)
t.setheading(100)
t.circle(-200,20)

t.penup()
t.goto(50,-25)
t.setheading(0)
t.pendown()
t.circle(100,30)
t.circle(30,90)
t.setheading(80)
t.circle(200,20)

#两熊猫眼
#左眼
t.penup()
t.goto(-90,25)
t.setheading(-45)
t.begin_fill()
t.pendown()
#椭圆绘制技巧
a = 0.2
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.1
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.1
        t.lt(3)
        t.fd(a)
t.end_fill()

t.fillcolor("white")
t.penup()
t.goto(-53,43)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13,360)
t.end_fill()

t.penup()
t.pensize(4)
t.goto(-60,57)
t.setheading(30)
t.pendown()
t.circle(-12,60)
#右眼
t.penup()
t.goto(90,25)
t.setheading(45)
t.pensize(2)
t.fillcolor("black")
t.begin_fill()
t.pendown()
#椭圆绘制技巧
a = 0.2
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.1
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.1
        t.lt(3)
        t.fd(a)
t.end_fill()

t.fillcolor("white")
t.penup()
t.goto(53,43)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13,360)
t.end_fill()

t.penup()
t.pensize(4)
t.goto(60,57)
t.setheading(150)
t.pendown()
t.circle(12,60)

#鼻子和嘴吧
t.penup()
t.goto(-16,20)
t.setheading(-90)
t.fillcolor("black")
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.03
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.03
        t.lt(3)
        t.fd(a)
t.end_fill()

t.penup()
t.goto(-24,0)
t.setheading(-60)
t.pendown()
t.circle(28,120)

#熊肢体
#左肢
t.penup()
t.goto(-65,-24)
t.setheading(-140)
t.begin_fill()
t.pendown()
t.circle(100,40)
t.setheading(180)
t.circle(30,40)
t.setheading(-40)
t.circle(40,40)
t.setheading(-150)
a = 0.5
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.05
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    elif 30 <= i < 60 or 90<=i <100:
        a=a-0.05
        t.lt(3)
        t.fd(a)
t.setheading(93)
t.circle(-150,30)
t.end_fill()

t.penup()
t.goto(-85,-115)
t.setheading(-150)
t.color("gray","gray")
t.begin_fill()
t.pendown()
a = 0.3
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.03
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.03
        t.lt(3)
        t.fd(a)
t.end_fill()
#每个脚趾绘制函数
def toe(x,y):
    t.begin_fill()
    t.goto(x,y)
    t.circle(3,360)
    t.end_fill()

t.penup()
toe(-98,-120)
toe(-96,-110)
toe(-88,-105)
toe(-80,-105)

#右肢
t.color("black")
t.penup()
t.goto(65,-24)
t.setheading(-40)
t.begin_fill()
t.pendown()
t.circle(-100,40)
t.setheading(0)
t.circle(-30,40)
t.setheading(-140)
t.circle(-40,40)
t.setheading(-30)
a = 0.5
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.05
        t.rt(3) #向左转3度
        t.fd(a) #向前走a的步长
    elif 30 <= i < 60 or 90<=i <100:
        a=a-0.05
        t.rt(3)
        t.fd(a)
t.setheading(87)
t.circle(150,30)
t.end_fill()

t.penup()
t.goto(85,-115)
t.setheading(150)
t.color("gray","gray")
t.begin_fill()
t.pendown()
a = 0.3
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.03
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.03
        t.lt(3)
        t.fd(a)
t.end_fill()

t.penup()
toe(98,-120)
toe(96,-110)
toe(88,-105)
toe(80,-105)

t.goto(-57,-140)
t.color("black")
t.setheading(-20)
t.pendown()
t.circle(165,40)

t.penup()
t.goto(0,180)
t.write("Pandas are the most lovely animals", align = "center"
        ,font = ("Times", 18, "bold"))
t.done()
