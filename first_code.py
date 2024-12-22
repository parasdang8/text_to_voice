from gtts import gTTS
import os
import googletrans
from googletrans import Translator
translator = Translator()

myText = "we the people of india have soliventry and secular society" 

language = "en"


print("Choose voice gender:")
print("1. Male")
print("2. Female")
voice_choice = input("Enter 1 or 2: ")


if voice_choice == "1":
    tld = "co.uk"  # Use 'co.uk' for a male voice
else:
    tld = "com"  # Use 'com' for a female voice

output = gTTS(text=myText, lang=language, tld=tld, slow=False)
output.save("output.mp3")
os.system("start output.mp3")


print(translator.translate(myText))