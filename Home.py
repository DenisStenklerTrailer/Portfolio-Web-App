import streamlit as st
import pandas



st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Denis Štenkler")
    content = """
    Star sem 26 let. Sem organiziran, discipliniran, samoiniciativen, komunikativen in športnik po duši. 
    Moja glavna dobra lastnost je, da se rad učim in imam veliko željo po nečem novem. 

    Od malih nog se praktično ukvarjam s športom. Pri 7 letih sem se začel ukvarjati s hokejem in ga treniral 11 let,
    nato pa sem se bolj našel v vzdržljivostnih športnih in sedaj resno treniram gorski tek v kombinaciji s kolesarstvom.
    Ukvarjam se tudi z jadralnim padalstvom kjer najbolj prakticiram Hike&Fly letenje kar pomeni hoja v hribe in nato spust s padalom v dolino.
    Šport me je do sedaj vsekakor naučil discipline, vztrajnosti kjer je veliko vzponov in padcev in pa predvsem urejanja dnevnega časa.
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