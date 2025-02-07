import reflex as rx
from links_chimalli.components.nav_bar import nav_bar

def index() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.center(
            rx.heading(
                "¡Hola Chimalli Digital!", 
                as_="h1", 
                size="5",
                weight="bold"
            )
        )
    )

app=rx.App()
app.add_page(index)
app._compile