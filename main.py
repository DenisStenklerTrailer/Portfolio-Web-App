import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Denis Štenkler")
    content = """
    Ime mi je Denis Štenkler
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have build in python. Feel free to contact me!
"""
st.text(content2)