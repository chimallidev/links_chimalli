import reflex as rx
from links_chimalli.styles.colors import Color
from links_chimalli.styles.styles import Size
from links_chimalli.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar.avif",
                fallback="ER",
                variant="solid",
                size="9",
                radius="none"
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
                    font_size=Size.X_DEF.value,
                    margin_top=Size.ZERO.value
                ),
                rx.hstack(
                    link_icon(
                        "/github.svg",
                        "https://solucionint.com",
                        "GitHub"
                    ),
                    link_icon(
                        "/github.svg",
                        "https://solucionint.com",
                        "GitHub"
                    ),
                    link_icon(
                        "/github.svg",
                        "https://solucionint.com",
                        "GitHub"
                    ),
                margin_top=Size.MEDIUM.value,
                spacing="5"
                ),
                spacing="0",
                margin_top=Size.X_DEF.value

            )
        ),
        rx.box(
            bg=Color.SECONDARY.value, 
            height=Size.TINY.value, 
            width="100%"
        ),
        rx.text('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            In accumsan cursus diam, non fermentum ligula viverra vitae. 
            Cras enim massa, sagittis nec nisl eu, condimentum volutpat ligula. 
            Sed eget bibendum eros. Fusce pretium et dolor sit amet pulvinar. 
        ''',
        color=Color.SECONDARY.value,
        font_size=Size.DEFAULT.value,
        margin_top=Size.MEDIUM.value
        ),
        align_items="start"
    )

    