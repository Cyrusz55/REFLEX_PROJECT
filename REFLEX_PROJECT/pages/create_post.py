import reflex as rx
from REFLEX_PROJECT.components.navbar import navbar
from REFLEX_PROJECT.state.post_state import PostState

def create_post_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
                rx.heading("Create Post"),
                rx.form(
                  rx.box(
                      rx.text("Title", class_name="form-label"),
                      rx.input(name="title", placeholder="Enter Title", type="text", class_name="form-input"),
                      class_name="form-group"
                  ),
                    rx.box(
                        rx.text("Body", class_name="form-label"),
                        rx.text_area(name="Body", placeholder="Enter The Post Body", class_name="form-input"),
                        class_name="form-group"
                    ),
                    rx.box(
                        rx.button("Save Post", type="submit"),
                        class_name = "form-group",
                    ),

                    on_submit = PostState.create_post
                ),
                class_name="main",
            ),
        class_name="page",
    )