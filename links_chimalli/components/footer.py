import reflex as rx
import datetime
from links_chimalli.styles.styles import Size
from links_chimalli.styles.colors import Color

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="avatar.avif",
                height=Size.XX_BIG.value,
                width=Size.XX_BIG.value,
                alt="""Logotipo de ChimalliDev. Letras 'C' y 'D' 
                sobre un escudo azteca color turquesa."""
            ),
            rx.link(
                rx.box(
                    rx.hstack(
                        rx.text(f"©2021-{datetime.date.today().year} "),
                        rx.text("ChimalliDev by Erick Roman ", color=Color.PRIMARY.value),
                        rx.text("v1.")
                    )
                ),
                href="",
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=Color.SECONDARY.value,
                _hover={"color": Color.PRIMARY.value}
            ),
            padding_bottom=Size.X_BIG.value,
            padding_x=Size.BIG.value,
            spacing="4",
            align_items="center"
            
        )
    )