import reflex as rx
from links_chimalli.components.link_button import link_button
from links_chimalli.components.title import title
import links_chimalli.constants as constant
from links_chimalli.styles.styles import Size
from links_chimalli.components.link_card import link_card

def links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Youtube",
            "Videos sobre programación",
            "icons/youtube.svg",
            constant.YOUTUBE
        ),
        link_button(
            "Tik Tok",
            "Videos cortos sobre pogramación",
            "icons/tik tok.svg",
            constant.TIKTOK
        ),
        link_button(
            "Instagram",
            "Mi día a día como programador",
            "icons/instagram.svg",
            constant.INSTAGRAM
        ),
        rx.box(height=Size.DEFAULT.value),
        link_button(
            "Invítame un café",
            "¿Quieres apoyarme?",
            "icons/coffee.svg",
            constant.SOLUCIONINT
        ),
        title("Destacado"),
        rx.grid(
            link_card(
                "/logo_solucionint.avif",
                '''Sitio web de artículos de diulgación científica 
                sobre ejercicio y habitos saludables.''',
                constant.SOLUCIONINT,
                "Sitio web solucionint"

            ),
            link_card(
                "icons/android.svg",
                "App: solucionint ", 
                constant.APP_SOLUCIONINT,
                "App de solucionint"
            ),
            columns=rx.breakpoints(initial="1", xs="2"),
            spacing="5"
        ),
        title("Contacto"),
        link_button(
            "Email",
            constant.EMAIL,
            "icons/email.svg",
            f"mailto:{constant.EMAIL}"
        ),
        width="100%",
        spacing="4",
        margin_top=Size.BIG.value
    )