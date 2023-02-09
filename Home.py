import streamlit as st
import pandas



st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Denis Štenkler")
    content = """
    I am 26 years old. I am organized, disciplined, self-initiative, communicative and an athlete at heart. 
    My main good quality is that I like to learn and I have a great desire for something new.

    I have been involved in sports since I was a child. I started playing hockey at the age of 7 and played it for 11 years,
    then I found myself more into endurance sports and now I seriously train trail running in combination with cycling.
    I am also passionate paraglider, where I mainly practice Hike&Fly flying, which means walking into the mouintains and then flying into the valley.
    So far, sport has definitely taught me discipline, persistence, where there are many ups and downs, and above all, managing the time of day.

    """
    st.info(content)


content2 = """
Below you can find some of the apps I have build in python.
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
            if str(row['website']) != "nan":
                st.write(f"[Website]({row['website']})")

with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source code]({row['url']})")
            if str(row['website']) != "nan":
                st.write(f"[Website]({row['website']})")