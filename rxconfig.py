import reflex as rx

config = rx.Config(
    app_name="links_chimalli",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://chimallidev-links-web.vercel.app/"
    ]
)