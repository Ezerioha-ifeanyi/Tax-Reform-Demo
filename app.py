import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(
    page_title="Nigeria Tax Reform Sentiment Analyser",
    page_icon="🇳🇬",
    layout="wide"
)

# 1. Load your HTML file
def load_html():
    with open("demo_webapp.html", "r", encoding="utf-8") as f:
        return f.read()

html_code = load_html()

# 2. Render the HTML in Streamlit
# We set the height to a large value to accommodate the results area and stats
components.html(html_code, height=1200, scrolling=True)