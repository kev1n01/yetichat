from gtts import gTTS
import pyttsx3
import uuid, playsound, os  

def tts(text):
    tts = gTTS(text=text, lang='es', slow=False, lang_check=False, tld='es')
    filename=f'{str(uuid.uuid4())}.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    print('audio created')
    os.remove(filename)

def pytts(text, volume: float = 1.0, rate: int = 150):
    engine = pyttsx3.init() 
    engine.setProperty('volume',volume)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()