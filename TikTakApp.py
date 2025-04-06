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

# Sub-tab logic
sub_tab = None

if main_section == "📄 Tablolarım":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Bilanço", "Gelir Tablosu"])

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

