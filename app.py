import streamlit as st

# App configuration
st.set_page_config(page_title="Aarambh - Order. Play. Dominate.", layout="wide")

# Embed the Lovable prototype directly
lovable_url = "https://aarambh-alert-composer.lovable.app/"
iframe_code = f"""
<iframe src="{lovable_url}" width="100%" height="1000" style="border:none;"></iframe>
"""
st.markdown("<h1 style='text-align:center;color:gold;'>Aarambh - Order. Play. Dominate.</h1>", unsafe_allow_html=True)
st.components.v1.html(iframe_code, height=1000)
