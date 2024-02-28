import streamlit as st
from st_pages import Page
from st_pages import Section
from st_pages import show_pages
from st_pages import add_page_title

st.title("My App")
add_page_title("Tren")

show_pages(
    [
        Page("page_title.py", "Home",":house:"),
        Page("page_home.py", "Problem Statement",":bookmark_tabs:"),
        Page("page_one.py", "Visualization 1", ":chart_with_downwards_trend:"),
        Page("page_two.py", "Visualization 2", ":bar_chart:"),
        Page("page_three.py", "Visualization 3", ":card_index:"),
        Page("page_four.py", "Visualization 4", ":cinema:"),
        Page("page_five.py", "Conclusion", ":page_facing_up:"),
        Page("page_six.py", "Suggestion", ":loudspeaker:"),
        Page("page_seven.py", "Data Source", ":book:"),
        Page("page_eight.py", "Contact", ":phone:"),
    ]
)