from enum import Enum
from links_chimalli.styles.colors import Color
from .fonts import Font, FontWeight
import reflex as rx

#Constants
MAX_WIDTH="600px"
#Sizes

STYLESHEETS=[
    "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@500;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@500;700&display=swap"
]

class Size(Enum):
    ZERO="0px !important"
    TINY="0.2em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    X_DEF="1.2em"
    LARGE="1.5em"
    BIG="2em"
    X_BIG="3em"
    XX_BIG="5em"
    XXX_BIG="8em"

BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "font_weight":FontWeight.MEDIUM.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
        "color":Color.SECONDARY.value,
        "font_family":Font.TITLE.value,
        "font_weight":FontWeight.BOLD.value
    },
    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding":Size.SMALL.value,
        "color":Color.SECONDARY.value, 
        "background_color":Color.GRAY.value,
        "white_space": "normal",
        "text_align": "start",
        "border_radius": "0px",
        "_hover":{
            "background_color": Color.PRIMARY.value
        }
    },
    rx.link:{
        "text_decoration": "none",
        "_hover":{}
    },
    rx.card:{
        "background_color": Color.SECONDARY.value
    }
}
navbar_title_style= dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.BOLD.value,
    font_size=Size.LARGE.value
)

title_style= dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style= dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.X_DEF.value,
    color=Color.SECONDARY.value
)

button_body_style= dict(
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=Color.SECONDARY.value
)