from gtts import gTTS
import os
myobj = gTTS(text='Welcome to Ranjith Kumar - Gerorge Butchart drive!', lang='zh-CN', slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")