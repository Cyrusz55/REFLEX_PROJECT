import reflex as rx
from REFLEX_PROJECT.state.post_state import PostState


def update_post_model() -> rx.Component:
    return rx.dialog.root(
    rx.dialog.trigger(rx.link("Edit Post", size="1")),
    rx.dialog.content(
        rx.dialog.title("Edit Post"),
        rx.flex(
            rx.text(
                "Title",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
            rx.input(
                default_value=PostState.post['title'],
                placeholder="Enter your title",
            ),
            rx.text(
                "Body",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
            rx.text_area(name="Body", placeholder="Enter The Post Body", on_change=PostState.body, value=PostState.post["body"]),


        ),
        rx.flex(
            rx.dialog.close(
                rx.button(
                    "Cancel",
                    color_scheme="gray",
                    variant="soft",
                ),
            ),
            rx.dialog.close(
                rx.button("Save"),
            ),
            spacing="3",
            margin_top="16px",
            justify="end",
        ),
    ),
)