import reflex as rx
from chat_openai import styles
from chat_openai.state import State
from chat_openai.components.loading_icon import loading_icon

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=styles.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=styles.answer_style,
        ),
        margin_y="1em",
        overflow="hidden",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
        bg="rgba(56, 56, 56, 0.18)",
        padding="1em",
        min_height="20em",
        max_height="30em",
        margin_top="1em",
        border_radius="8px",
        class_name="overflow-y-auto overscroll-y-auto",
    )

def messageWithVoice() -> rx.Component:
    return rx.box(
        rx.cond(
            State.is_active_microphone,
            rx.text(
                "Escuchando...",
                text_align="center",
                padding="1em",
            ),
            rx.text(""),
        ),
        min_height="1em",
    )
    
def audioview() -> rx.Component:
    return rx.box(
        rx.cond(
            State.path_audio != "",
            rx.audio(
                url=State.path_audio,
                width="400px",
                height="70px",
                controls=True,
                playing=True,
            ),
        )
        
    ) 
    
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            on_change=State.set_question,
            placeholder="Input a question here...", 
            style=styles.input_style,
            is_disabled=State.processing,
            ),
        rx.button(
            rx.cond(
                State.processing,
                loading_icon(height="1em", fill="010101"),
                rx.text("Send"),
            ),
            type_="submit",
            color_scheme="blue",
            on_click=State.answer,
            is_disabled=State.processing,
        ),
        rx.button(
            rx.cond(
                State.is_active_microphone,
                State.get_text_mic_on,
                State.get_text_mic_off,
            ),
            is_disabled=State.is_active_microphone,
            color_scheme="red",
            style=styles.button_style_microphone,
            on_click=State.active_microphone_infinite,
        ),
        
    )