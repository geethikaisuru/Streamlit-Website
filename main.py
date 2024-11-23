import streamlit as st


st.set_page_config(page_title="Geethika Isuru", page_icon="🧊", layout="wide", initial_sidebar_state="auto")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Geethika Isuru")
    content = """
    I am an entrepreneur & a software engineer with a passion for data science and machine learning. I have experience in developing web applications, data analysis, and machine learning models. I am currently working as a software engineer at a software company in Sri Lanka. I have a bachelor's degree in ICT from the University of Sri Jayewardenepura. I am also a self-taught data scientist and machine learning engineer. I have completed several online courses in data science and machine learning. I am always eager to learn new technologies and improve my skills. I am looking for opportunities to work on challenging projects in data science and machine learning.
                """
    st.write(content)
    

def main():
    pass

if __name__ == "__main__":
    main()