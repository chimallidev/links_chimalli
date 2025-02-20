import reflex as rx
from links_chimalli.styles.styles import Size
import links_chimalli.styles.styles as styles

def link_button(title:str, body:str, image:str, url:str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.X_BIG.value,
                    height=Size.X_BIG.value,
                    margin=Size.DEFAULT.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing="2",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            ),
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )