# 语音播报模块
import pyttx3

# 模块初始化
engine = pyttsx3.init()

print('准备开始语音播报...')

# 设置要播报的Unicode字符串
engine.say("人生苦短，我用Python")

# 等待语音播报完毕
engine.runAndWait()
