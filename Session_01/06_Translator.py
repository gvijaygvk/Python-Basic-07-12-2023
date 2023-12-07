import time

from googletrans import Translator, constants
from gtts import gTTS
import os
tex_in = input("Enter the text to translate :")
translator = Translator()
lang_list = ['ta', 'te', 'hi','ml']
for lan in lang_list:
    translation = translator.translate(tex_in, dest=lan)
    print(translation.text)
    myobj = gTTS(text=translation.text, lang=lan, slow=False)
    myobj.save(f"welcome1{lan}.mp3")
    os.system(f"start welcome1{lan}.mp3")
    time.sleep(5)
# how are you? welcome to python turorial