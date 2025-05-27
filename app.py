import streamlit as st
import base64

# App configuration
st.set_page_config(page_title="Aarambh - Order. Play. Dominate.", layout="wide")

# Branding (optional)
st.markdown("<h1 style='text-align:center;color:gold;'>Aarambh - Order. Play. Dominate.</h1>", unsafe_allow_html=True)

# Embed Lovable prototype directly using HTML wrapper
with open("index.html", "r") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1000, scrolling=True)
