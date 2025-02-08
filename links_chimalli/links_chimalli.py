import reflex as rx
from links_chimalli.components.nav_bar import nav_bar
from links_chimalli.views.header.header import header
import links_chimalli.styles.styles as styles 
from links_chimalli.styles.styles import Size
from links_chimalli.styles.colors import Color

def index() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.center(
            rx.vstack(
                header(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                spacing="0"
            )
        )
    )

app=rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app._compile