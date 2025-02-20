import reflex as rx
from links_chimalli.components.link_button import link_button
from links_chimalli.components.title import title
import links_chimalli.constants as constant
from links_chimalli.styles.styles import Size
from links_chimalli.components.link_card import link_card
from links_chimalli.routes import Route

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Python desde cero",
            "Fundamentos de python",
            "/icons/python.svg",
            constant.YOUTUBE
        ),
        link_button(
            "Vacío",
            "Próximamente",
            "/icons/empty.svg",
            Route.CURSOS.value,
            is_external=False
        ),
        link_button(
            "Vacío",
            "Próximamente",
            "/icons/empty.svg",
            Route.CURSOS.value,
            is_external=False
        ),
        link_button(
            "Vacío",
            "Próximamente",
            "/icons/empty.svg",
            Route.CURSOS.value,
            is_external=False
        ),
        title("Mucho más en"),
        link_button(
            "Youtube",
            "Videos sobre programación",
            "/icons/youtube.svg",
            constant.YOUTUBE
        ),
        width="100%",
        spacing="4",
        margin_top=Size.SMALL.value
    )