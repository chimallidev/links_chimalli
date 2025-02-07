import reflex as rx
from links_chimalli.styles.colors import Color
from links_chimalli.styles.styles import Size

def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Chimalli",
            rx.text.strong("Dev"),
            color=Color.SECONDARY.value
        ),
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        bg=Color.PRIMARY.value
    )