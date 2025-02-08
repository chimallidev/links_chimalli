from enum import Enum
from links_chimalli.styles.colors import Color

#Constants
MAX_WIDTH="600px"
#Sizes
class Size(Enum):
    ZERO="0px !important"
    TINY="0.2em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    X_DEF="1.2em"
    LARGE="1.5em"
    BIG="2em"

BASE_STYLE={
    "background_color": Color.BACKGROUND.value
}