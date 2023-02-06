import streamlit as st
import pandas



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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source code]({row['url']})")
with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source code]({row['url']})")