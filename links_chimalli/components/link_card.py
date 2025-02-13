import reflex as rx
from links_chimalli.styles.styles import Size
from links_chimalli.styles.colors import Color

def link_card(image:str, body:str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.card(
                rx.center(
                    rx.image(
                        src=image,
                        alt=alt,
                        height=Size.XXX_BIG.value,
                        width=Size.XXX_BIG.value
                )
                ),
                padding=Size.X_DEF.value,
                justify="center",
                width="100%"
            ),
            rx.text(
                body,
                color=Color.GRAY.value,
                _hover={"color":Color.PRIMARY.value},
                white_space="normal"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )