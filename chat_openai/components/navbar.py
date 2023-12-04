import reflex as rx

def navbar() -> rx.Component:
    return rx.container(
        rx.box(
            rx.text(
                "Chef Yeti",
                class_name="font-bold text-2xl text-blue p-1  mt-3",
            ),
        ),
        rx.box(
            rx.button(
                rx.cond(
                    rx.color_mode == 'light',
                    rx.icon(tag="sun"),
                    rx.icon(tag="moon"),
                ),
                on_click=rx.toggle_color_mode,
                class_name="p-1 mt-3",
            ), 
        ),
        class_name="flex justify-between",
    )