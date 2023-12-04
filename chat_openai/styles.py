# Common styles for questions and answers.
shadow = "rgba(115, 115, 115, 0.2) 2px 3px 8px"
accent_color = "#CEFFF4"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    bg="#d8c0fc", margin_left=chat_margin, color="#010101", float="right"
)
answer_style = message_style | dict(
    bg="#bcfcbb", margin_right=chat_margin, color="#010101"
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)
button_style_send = dict(box_shadow=shadow, color="#010101")
button_style_microphone = dict(box_shadow=shadow, color="#010101")