import reflex as rx
import links_chimalli.styles.styles as styles
from links_chimalli.pages.index import index
from links_chimalli.pages.courses import courses


app=rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-CHX2SC8XHB"),
        rx.script("""
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-CHX2SC8XHB');
        """)
    ]
)