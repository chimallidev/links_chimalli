import reflex as rx
from links_chimalli.styles.styles import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )