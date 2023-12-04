import speech_recognition as sr
from queue import Queue
task_queue = Queue()
sub_task_queue = Queue()

def rm(audio = None):
    r, mic = sr.Recognizer(), sr.Microphone()
    with mic as source:
        print("Escuchando micro 2...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        if text != "":
            task_queue.put(text)  
            print("user task 2: ", text, end="\r\n")
            return text
        else:
            task_queue.put("")
            rm()
            return ""
        

def rm2(audio = None):
    r, mic = sr.Recognizer(), sr.Microphone()
    with mic as source:
        print("Escuchando micro 3...")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio, language='es-ES')
            sub_task_queue.put(text)  
            print("user task 3: ", text, end="\r\n")
        except: 
            sub_task_queue.put("")
            rm2()

def micToWeb():
    r, mic = sr.Recognizer(), sr.Microphone()
    with mic as source:
        print("Escuchando para web...")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio, language='es-ES')
            # if text != "":
            #     print("msg to web: ", text, end="\r\n")
            #     return text
            # else:
            #     micToWeb()
            #     return ""
        except:
            micToWeb()
