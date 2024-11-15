import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()









# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/dp.jpeg", width = 180)
with col2:
    st.title("Danish Aziz", anchor=False)
    st.write("B.Tech. IIT Bombay ' 2024")
    st.write(
        "Data Scientist | AI Innovator"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATION ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    -Experience in Data Anlytics, Machine Learning, NLP, LLM, RAG
    -Strong hands-on-experience and knowledge in Python and its libraries
    In-depth understanding of Statistical principles
    """

)
# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, pandas, numpy, pytorch), SQL
    -Modeling: Machine Learning, Deep Learning, Natural Language Processing
    Databases: MongoDB, MySQL
    """
)
