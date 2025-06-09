import reflex as rx
from REFLEX_PROJECT.components.navbar import navbar

def create_post_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
                rx.text("Create Post"),
                class_name="main"
            ),
        class_name="page",
    )