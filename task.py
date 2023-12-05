import pywhatkit
from text_to_speech import pytts
from record_microphone import rm, rm2

def exec_task():
    response = rm()
    if response != "":
        from record_microphone import task_queue
        task_queue_result = task_queue.get()
        print(task_queue_result)

        if(task_queue_result == "salir" or task_queue_result == "Salir"):
            return 'Exit'
        
        if(task_queue_result == 'busca en google'):
            sub_task = listenSubTask('Que quieres buscar?')
            pywhatkit.search(sub_task)
            return 'Done'
        
        if(task_queue_result == 'reproduce' or task_queue_result == 'Reproduce'):
            sub_task = listenSubTask('Que quieres reproducir?')
            pywhatkit.playonyt(sub_task)
            return 'Done'

        if(task_queue_result == 'Enviar mensaje a grupo'):
            sub_task = listenSubTask('Que mensaje quieres enviar?')
            pywhatkit.sendwhatmsg_to_group_instantly('I3zEKxnLk8QA2p9suOItlV', sub_task)
            pytts('Mensaje enviado')
            return 'Done'

def listenSubTask(message:str ):
    pytts(message)
    rm2()
    from record_microphone import sub_task_queue
    sub_task_queue_result = sub_task_queue.get()
    print(sub_task_queue_result)
    return sub_task_queue_result