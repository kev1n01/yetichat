import reflex as rx

def navbar() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Chef Yeti",
                class_name="font-bold text-2xl text-white mt-4 p-1 justify-center",
            ),
        )
    )