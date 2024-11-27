import streamlit as st
import webbrowser


# Set up the title of the app
st.title("My Past Venture 🚀")

# Button to open the URL in a new tab
if st.button("Open Website"):
    webbrowser.open_new_tab("https://sl-vfx.github.io/")

# Embed the website using an iframe and CSS
st.markdown(
    """
    <style>
    iframe {
        width: 100% !important;
        height: 800px;
        border: none;
    }
    </style>
    <iframe src="https://sl-vfx.github.io/"></iframe>
    """,
    unsafe_allow_html=True,
)

# Additional text below the iframe
st.write("This is the portfolio website I developed for my past venture, SL VFX by IsuruVFX. It showcases the services I offered and the projects we worked on. Feel free to explore the website!")
