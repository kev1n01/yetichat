import reflex as rx
from chat_openai.components.chat import messageWithVoice, chat, action_bar, audioview
from chat_openai.components.navbar import navbar
def index() -> rx.Component:
  return rx.container(
    navbar(),
    chat(),
    # audioview(),
    messageWithVoice(),
    action_bar(),
  ) 

app = rx.App()
app.add_page(index,title="Yeti Chat",)
app.compile()