import reflex as rx
from typing import List, Dict
from REFLEX_PROJECT.state.post_state import PostState

def render_post(post: Dict[str, str]):
    return rx.box(
        rx.box(
            rx.heading(post["title"]),
            rx.text(f"By: {post['author']}"),
            class_name="post_header"
        ),
        rx.box(
            rx.text(post["created_at"]),
            rx.text(post["body"]),
          class_name="post_body"
        ),
        class_name="post"
    )

def post_list() -> rx.Component:
    return rx.box(
        rx.heading("latest Posts", size="6"),
        rx.foreach(
            PostState.posts.reverse(),
            render_fn=render_post
        ),
        class_name="posts"
    )