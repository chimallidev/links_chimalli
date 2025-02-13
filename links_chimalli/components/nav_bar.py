import reflex as rx
from links_chimalli.styles.colors import Color
from links_chimalli.styles.styles import Size
from links_chimalli.styles.fonts import Font, FontWeight

def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "ChimalliDev",
            color=Color.SECONDARY.value,
            font_size=Size.LARGE.value,
            font_family=Font.TITLE.value
        ),
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.MEDIUM.value,
        z_index="999",
        top="0",
        bg=Color.PRIMARY.value
    )