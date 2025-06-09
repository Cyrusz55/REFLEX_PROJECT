import reflex as rx
from REFLEX_PROJECT.components.navbar import navbar


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.text("Index Page"),
            class_name = "main"
        ),
        class_name = "page",

    )