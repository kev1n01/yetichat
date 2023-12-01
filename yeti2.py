import openai
import speech_recognition as sr
from queue import Queue
from text_to_speech import pytts

#declare the API key
openai.api_key = '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'

#declare the queue for the transcript of the microphone input and the default text chat message
transcript_queue = Queue()
text_chat_default = "Hola, ¿En qué puedo ayudarte?"
text_chat_after_sleep = "Qué sueño tengo, ¿qué quieres?"
text_chat_before_sleep = "Adiós, mi rey"

def record_microphone(audio = None):
    r, mic = sr.Recognizer(), sr.Microphone()
    with mic as source:
        print("Escuchando...")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language='es-ES')
            transcript_queue.put(text)
            print("User: ", text, end="\r\n")
        except:
            print("No te he entendido, ¿puedes repetirlo?", end="\r\n")
            transcript_queue.put("")

def handle_conversation():
    active = False
    sleep = False
    while True:
        record_microphone()
        transcript_result = transcript_queue.get()
        
        if not sleep and not active and transcript_result == "yeti":
            active = True
            pytts(text_chat_default)
            print("\nAI: ", text_chat_default, end="\r\n")
            continue

        if sleep and transcript_result == "yeti":
            active = True
            sleep = False
            pytts(text_chat_after_sleep)
            print("\nAI: ", text_chat_after_sleep, end="\r\n")
            continue
        
        if active and transcript_result == "yeti adios" or transcript_result == "yeti apagate" or transcript_result == "yeti apágate":
            pytts(text_chat_before_sleep)
            print("\nAI: ", text_chat_before_sleep, end="\r\n")
            active = False
            sleep = True
            continue

        if not sleep and active and transcript_result != "":
            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = [
                    {
                        'role': 'system',
                        'content': 'You are a highly intelligent chatbot, answer the questions given within a maximum of 200 characters.'
                    },
                    {
                        'role': 'user',
                        'content': transcript_result
                    }
                ]
            )

            text = response['choices'][0]['message']['content']
            pytts(text)
            print("\nAI: ", text, end="\r\n")

handle_conversation()