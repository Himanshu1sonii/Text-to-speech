
import os
from gtts import gTTS


#if you want new file you can change sample.txt
    abc = open('sample.txt')
   text = abc.read()   #text that you want to convert.

   language = 'en'  # en is for english language

   obj = gTTS(text = text,lang= language,slow = False)
   obj.save("sample.mp3")
   os.system('sample.mp3')
