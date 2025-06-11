import reflex as rx
from REFLEX_PROJECT.components.navbar import navbar
from REFLEX_PROJECT.components.posts import post_list



def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            post_list(

            ),
            class_name = "main"
        ),
        class_name = "page",

    )