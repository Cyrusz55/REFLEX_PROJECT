"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from REFLEX_PROJECT.pages.home import index
from REFLEX_PROJECT.pages.create_post import create_post_page
import reflex as rx



app = rx.App(
    stylesheets = [
        "/styles/main.css"
    ]
)
app.add_page(index)

app.add_page(create_post_page, route="/create_post")

