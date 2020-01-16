import cv2 as cv
# 参数0表示捕获系统默认摄像头
cap = cv.VideoCapture(0)

cv.namedWindow("video")

# 只要摄像头一开就一直接收帧画面

while cap.isOpened():
    status, frame = cap.read()
    # 判断是否捕获到摄像头下一帧画面
    if status:
        #  高度
        height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        #  宽度
        width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        #  帧数
        FPS = cap.get(cv.CAP_PROP_FPS)
        #  编码格式
        VideoEncode = cap.get(cv.CAP_PROP_FOURCC)
        # 按键检查
        k = cv.waitKey(25) & 0XFF
        key = chr(k)
        if key == 'h':
            cv.imwrite("1.jpg", frame)
            print("帧属性->高度:{0}\t宽度：{1}\tFPS:{2}\t编码格式：{3}".
                  format(height, width, FPS, VideoEncode))

        elif key == 'q':
            break

        cv.imshow('video', frame)

cv.destroyWindow('video')














