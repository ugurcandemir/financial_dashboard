import streamlit as st
from PIL import Image

# Set Streamlit page config
st.set_page_config(
    page_title="TikTak Finansal Analiz Platformu",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load logo image
logo = Image.open("tiktak_logo.png")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Global font and background */
        body, html {
            background-color: white;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Top logo-title section */
        .header-container {
            display: flex;
            align-items: center;
            padding: 10px 0;
            border-bottom: 2px solid #e0e0e0;
        }

        .header-container img {
            width: 60px;
            margin-right: 20px;
        }

        .header-container h1 {
            font-size: 28px;
            color: #C8102E;  /* Reddish pink */
            margin: 0;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #fff;
            border-right: 1px solid #ddd;
        }

        .sidebar-title {
            font-size: 16px;
            font-weight: bold;
            color: #C8102E;
        }
    </style>
""", unsafe_allow_html=True)

# Header layout
col1, col2 = st.columns([1, 6])
with col1:
    # st.image(logo, use_column_width=False)
    st.image(logo, use_container_width=False)
with col2:
    st.markdown("<h1 class='header-container'>Finansal Analiz Platformu</h1>", unsafe_allow_html=True)

# Sidebar navigation with icons
st.sidebar.markdown("<p class='sidebar-title'>📊 Araçlarım</p>", unsafe_allow_html=True)

# Main sections
main_section = st.sidebar.radio(
    "Menü",
    [
        "📄 Tablolarım",
        "📈 Analizlerim",
        "🚗 Filo ve Değerleme",
        "📑 Raporum"
    ]
)


import pandas as pd
import plotly.express as px

# Helper function to load data
def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"Dosya yüklenirken hata oluştu: {e}")
        return pd.DataFrame()

# Charting section with session state to allow multiple charts
def chart_creator(df, key_prefix="chart"):
    if not df.empty:
        st.markdown("---")
        st.markdown("### 📊 Görsel Oluştur")

        # Initialize session state list
        if f"{key_prefix}_charts" not in st.session_state:
            st.session_state[f"{key_prefix}_charts"] = []

        with st.form(key=f"{key_prefix}_form"):
            chart_type = st.selectbox("Grafik Türü Seçin", ["Çizgi (Line)", "Bar", "Alan (Area)", "Pasta (Pie)", "Dağılım (Scatter)"])
            x_col = st.selectbox("X Eksen Kolonu", df.columns, key=f"{key_prefix}_x")
            y_col = st.selectbox("Y Eksen Kolonu", df.columns, key=f"{key_prefix}_y")
            submitted = st.form_submit_button("Grafiği Ekle")

            if submitted:
                st.session_state[f"{key_prefix}_charts"].append((chart_type, x_col, y_col))

        for idx, (chart_type, x_col, y_col) in enumerate(st.session_state[f"{key_prefix}_charts"]):
            st.markdown(f"#### Grafik {idx+1}: {chart_type}")
            try:
                if chart_type == "Çizgi (Line)":
                    fig = px.line(df, x=x_col, y=y_col)
                elif chart_type == "Bar":
                    fig = px.bar(df, x=x_col, y=y_col)
                elif chart_type == "Alan (Area)":
                    fig = px.area(df, x=x_col, y=y_col)
                elif chart_type == "Pasta (Pie)":
                    fig = px.pie(df, names=x_col, values=y_col)
                elif chart_type == "Dağılım (Scatter)":
                    fig = px.scatter(df, x=x_col, y=y_col)
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Grafik çizilirken hata oluştu: {e}")

# Sub-tab logic
sub_tab = None

if main_section == "📄 Tablolarım":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Bilanço", "Gelir Tablosu"])

    st.markdown(f"#### {sub_tab}")

    if sub_tab == "Bilanço":
        df = load_excel("file_example_XLS_10.xls")
        st.dataframe(df)
        chart_creator(df, key_prefix="bilanco")

    elif sub_tab == "Gelir Tablosu":
        df = load_excel("file_example_XLS_102.xls")
        st.dataframe(df)
        chart_creator(df, key_prefix="gelir")

elif main_section == "📈 Analizlerim":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Rasyo", "Trend", "Yüzde Analizi", "Karşılaştırmalı Analiz"])

elif main_section == "🚗 Filo ve Değerleme":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Filo", "Araç Değerleme"])

# Main content area
st.markdown(f"### {main_section}")

if main_section == "📑 Raporum":
    st.write("Burada rapor çıktılarınızı oluşturabilirsiniz.")
elif sub_tab:
    st.markdown(f"#### {sub_tab}")
    st.write(f"`{sub_tab}` içeriği buraya gelecek...")

