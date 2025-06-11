"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from REFLEX_PROJECT.pages.home import index
from REFLEX_PROJECT.pages.create_post import create_post_page

from REFLEX_PROJECT.state.post_state import PostState
import reflex as rx





app = rx.App(
    stylesheets = [
        "/styles/main.css"
    ]
)
app.add_page(index, on_load=[
    PostState.load_posts
])

app.add_page(create_post_page, route="/create_post")

