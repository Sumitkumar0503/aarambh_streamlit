import streamlit as st
import base64

# App configuration
st.set_page_config(page_title="Aarambh - Order. Play. Dominate.", layout="wide")
st.sidebar.title("Aarambh Navigation")

# Sidebar for Page Navigation
page = st.sidebar.radio("Go to:", ["🎮 Play Now", "📸 Gallery & Presentations"])

# Branding
st.markdown("<h1 style='text-align:center;color:gold;'>Aarambh - Order. Play. Dominate.</h1>", unsafe_allow_html=True)

if page == "🎮 Play Now":
    st.subheader("Enjoy the Game!")
    # Masked or shortened Lovable URL
    iframe_url = "https://aarambh-alert-composer.lovable.app/"  # Replace with a bit.ly link if desired
    st.components.v1.iframe(src=iframe_url, width=1400, height=800, scrolling=True)

elif page == "📸 Gallery & Presentations":
    st.subheader("Experiment Highlights")

    # Display images from assets folder
    image_files = [
        "assets/WhatsApp Image 2025-05-27 at 11.33.57 AM.jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.33.28 AM.jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.32.51 AM.jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.32.19 AM (1).jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.32.19 AM.jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.31.14 AM (1).jpeg",
        "assets/WhatsApp Image 2025-05-27 at 11.31.14 AM.jpeg"
    ]
    for img in image_files:
        st.image(img, use_column_width=True)

    st.subheader("Presentations")
    pdf_files = [
        "Project Aarambh_NPs (1).pdf",
        "Aarambh - Gamification Experiment - PPT.pdf"
    ]
    for pdf_file in pdf_files:
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

# Footer Branding
st.markdown("---")
st.markdown("<p style='text-align:center;'>Aarambh - Order. Play. Dominate.</p>", unsafe_allow_html=True)
