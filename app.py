import streamlit as st

# Configure Streamlit for minimal layout
st.set_page_config(page_title="Aarambh", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit’s default padding, menu, footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Fullscreen Lovable Prototype
lovable_url = "https://aarambh-alert-composer.lovable.app/"
iframe_code = f"""
<iframe src="{lovable_url}" width="100%" height="1000px" style="border:none;"></iframe>
"""
st.components.v1.html(iframe_code, height=1000, scrolling=True)
