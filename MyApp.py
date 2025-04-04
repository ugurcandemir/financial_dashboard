import streamlit as st
from PIL import Image

st.sidebar.title("Ana Menü")

bilanco = st.Page("pages/page_1.py" , title="Bilanço" , icon="📊")
gelir_gider = st.Page("pages/page_2.py" , title="Gelir-Gider" , icon="💰")
gelir_gider_raporu = st.Page("pages/page_3.py" , title="Gelir-Gider Raporu" , icon="📃")
envanter = st.Page("pages/page_4.py" , title="Envanter" , icon="📦")
nakit = st.Page("pages/page_5.py" , title="Nakit Akışı" , icon="💵")

pg = st.navigation([bilanco, gelir_gider, gelir_gider_raporu, envanter, nakit])
pg.run()