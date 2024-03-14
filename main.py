import streamlit as st
from st_pages import Page
from st_pages import Section
from st_pages import show_pages
from st_pages import add_page_title

st.title("My App")
add_page_title("Tren")

show_pages(
    [
        Page("background.py", "Home",":house:"),
        Page("problem_statement.py", "Problem Statement",":bookmark_tabs:"),
        Page("income_outcome.py", "Income vs Outcome", ":chart_with_downwards_trend:"),
        Page("type_outcome.py", "Type of Outcome", ":bar_chart:"),
        Page("composition_income.py", "Composition of Income", ":card_index:"),
        Page("income_ump.py", "Income vs UMP", ":cinema:"),
        Page("conclusion.py", "Conclusion", ":page_facing_up:"),
        Page("suggestion.py", "Suggestion", ":loudspeaker:"),
        Page("data_source.py", "Data Source", ":book:"),
        Page("contact.py", "Contact", ":phone:"),
    ]
)