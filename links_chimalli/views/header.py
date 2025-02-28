import reflex as rx
from links_chimalli.styles.colors import Color
from links_chimalli.styles.styles import Size
from links_chimalli.components.link_icon import link_icon
import links_chimalli.constants as constant

def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.avif",
                fallback="ER",
                variant="solid",
                size="7",
                radius="none",
                margin_top=Size.LARGE.value
            ),
            rx.vstack(
                rx.text.strong(
                    "Erick Roman",
                    color=Color.SECONDARY.value,
                    font_size=Size.BIG.value
                ),
                rx.text(
                    "@chimallidev", 
                    color=Color.PRIMARY.value,
                    font_size=Size.DEFAULT.value,
                    margin_top=Size.ZERO.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        "https://solucionint.com",
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        constant.X,
                        "x"
                    ),
                    margin_top=Size.DEFAULT.value,
                    spacing="5"
                ),
                spacing="0",
                margin_top=Size.DEFAULT.value
            ),
            width="100%",
            align_items="start",
            spacing="4"
        ),
        rx.box(
            bg=Color.SECONDARY.value, 
            height=Size.TINY.value, 
            width="100%"
        ),
        rx.cond(
            details,
            rx.text('''
                Desarrollador autodidacta y freelance, especializado en Python con 
                conocimientos en Kotlin. En este espacio encontrarás todos mis enlaces 
                relevantes. ¡Bienvenid@!🚀
                ''',
                color=Color.SECONDARY.value,
                font_size=Size.DEFAULT.value,
                margin_top=Size.MEDIUM.value
            ),
        ),
        align_items="start",
        width="100%"
    )


    