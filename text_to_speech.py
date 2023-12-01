from gtts import gTTS
import pyttsx3
import uuid, playsound, os

def tts(text, language):
    tts = gTTS(text=text, lang=language, slow=False, lang_check=False, tld='com.mx')
    filename=f'{str(uuid.uuid4())}.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    print('audio created')
    os.remove(filename)

def pytts(text):
    engine = pyttsx3.init()
    engine.say(text)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 125)
    engine.runAndWait()