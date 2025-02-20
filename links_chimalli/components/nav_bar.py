import reflex as rx
from links_chimalli.styles.colors import Color
from links_chimalli.styles.styles import Size
from links_chimalli.styles.fonts import Font
from links_chimalli.routes import Route

def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(
                "ChimalliDev",
                color=Color.SECONDARY.value,
                font_size=Size.LARGE.value,
                font_family=Font.TITLE.value
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.MEDIUM.value,
        z_index="999",
        top="0",
        bg=Color.PRIMARY.value
    )