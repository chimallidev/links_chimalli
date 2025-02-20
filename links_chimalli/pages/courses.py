import reflex as rx
from links_chimalli.components.nav_bar import nav_bar
from links_chimalli.views.header import header
from links_chimalli.views.courses_links import courses_links
import links_chimalli.styles.styles as styles 
from links_chimalli.routes import Route
from links_chimalli.styles.styles import Size
from links_chimalli.components.footer import footer
import utils as utils

@rx.page(
        route=Route.CURSOS.value,
        title= utils.courses_title,
        description= utils.courses_description,
        image= utils.preview,
        meta= utils.courses_meta 
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        nav_bar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                spacing="0"
            ),
        ),
        footer()
    )