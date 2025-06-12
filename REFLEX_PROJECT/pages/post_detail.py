import reflex as rx
from REFLEX_PROJECT.components.navbar import navbar
from REFLEX_PROJECT.components.posts import post_list
from REFLEX_PROJECT.state.post_state import PostState


def post_detail_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
              rx.heading(PostState.post['title']),
                rx.text(f"By: {PostState.post['author']}"),
                rx.text(f"On: {PostState.post['created_at']}", class_name="date"),
              class_name = "post_detail_header"
            ),
            rx.box(
                rx.text(PostState.post['body']),
                class_name= "post_detail_body"
            ),
            class_name="main"
        ),
        class_name="page",
    )