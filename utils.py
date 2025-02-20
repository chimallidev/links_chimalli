import reflex as rx

#Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es")

preview="/avatar.avif"

_meta=[
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@chimallidev"}
]

#Index

index_title="ChimalliDev | Desarrollador especializado en Python"
index_description="""Hola soy Erick Roman, desarrollador autodidacta 
y freelance, especializado en Python con conocimientos en Kotlin."""

index_meta=[
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]

index_meta.extend(_meta)

#Cursos

courses_title="Chimallidev | Recursos gratis"
courses_description="Recursos gratis para aprender programación. Python."

courses_meta=[
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description}
]

courses_meta.extend(_meta)