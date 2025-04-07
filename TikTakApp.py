import streamlit as st
from PIL import Image


import pandas as pd
import plotly.express as px
from fpdf import FPDF
from io import BytesIO
import base64

import plotly.express as px
import pandas as pd
import streamlit as st

import pandas as pd
import plotly.express as px


import unicodedata


import os
from markdown2 import markdown
from bs4 import BeautifulSoup
import tempfile


import pandas as pd


import streamlit as st
import pandas as pd
import pydeck as pdk

import pandas as pd
import joblib


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



# Helper function to load data
def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"Dosya yüklenirken hata oluştu: {e}")
        return pd.DataFrame()



def remove_accents(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

# # Charting section with session state to allow multiple charts
# def chart_creator(df, key_prefix="chart"):
#     if not df.empty:
#         st.markdown("---")
#         st.markdown("### 📊 Görsel Oluştur")

#         # Initialize session state list
#         if f"{key_prefix}_charts" not in st.session_state:
#             st.session_state[f"{key_prefix}_charts"] = []

#         with st.form(key=f"{key_prefix}_form"):
#             chart_type = st.selectbox("Grafik Türü Seçin", ["Çizgi (Line)", "Bar", "Alan (Area)", "Pasta (Pie)", "Dağılım (Scatter)"])
#             x_col = st.selectbox("X Eksen Kolonu", df.columns, key=f"{key_prefix}_x")
#             y_col = st.selectbox("Y Eksen Kolonu", df.columns, key=f"{key_prefix}_y")
#             submitted = st.form_submit_button("Grafiği Ekle")

#             if submitted:
#                 st.session_state[f"{key_prefix}_charts"].append((chart_type, x_col, y_col))

#         for idx, (chart_type, x_col, y_col) in enumerate(st.session_state[f"{key_prefix}_charts"]):
#             st.markdown(f"#### Grafik {idx+1}: {chart_type}")
#             try:
#                 if chart_type == "Çizgi (Line)":
#                     fig = px.line(df, x=x_col, y=y_col)
#                 elif chart_type == "Bar":
#                     fig = px.bar(df, x=x_col, y=y_col)
#                 elif chart_type == "Alan (Area)":
#                     fig = px.area(df, x=x_col, y=y_col)
#                 elif chart_type == "Pasta (Pie)":
#                     fig = px.pie(df, names=x_col, values=y_col)
#                 elif chart_type == "Dağılım (Scatter)":
#                     fig = px.scatter(df, x=x_col, y=y_col)
#                 st.plotly_chart(fig, use_container_width=True)
#             except Exception as e:
#                 st.warning(f"Grafik çizilirken hata oluştu: {e}")


# def filtered_chart_section(df, key_prefix="chart"):
#     st.markdown("### 📋 Tablo")
#     df = df.copy()

#     # Filter by year
#     years = df["Yıllar"].unique()
#     selected_years = st.multiselect("Yıllara Göre Filtrele", years, default=years, key=f"{key_prefix}_years")
#     df = df[df["Yıllar"].isin(selected_years)]

#     # Filter by columns (excluding Yıllar)
#     all_columns = df.columns.drop("Yıllar")
#     selected_columns = st.multiselect("Değişkenleri Seçin", all_columns, default=all_columns[:3], key=f"{key_prefix}_cols")
#     # filtered_df = df[["Yıllar"] + selected_columns.tolist()]
#     filtered_df = df[["Yıllar"] + selected_columns]

#     st.dataframe(filtered_df)

#     # Section: chart builder
#     st.markdown("---")
#     st.markdown("### 📊 Görsel Oluştur")

#     if f"{key_prefix}_charts" not in st.session_state:
#         st.session_state[f"{key_prefix}_charts"] = []

#     with st.form(key=f"{key_prefix}_form"):
#         chart_type = st.selectbox("Grafik Türü Seçin", ["Çizgi (Line)", "Bar", "Alan (Area)", "Pasta (Pie)", "Dağılım (Scatter)"], key=f"{key_prefix}_chart_type")
#         x_col = st.selectbox("X Eksen Kolonu", filtered_df.columns, index=0, key=f"{key_prefix}_x")
#         y_col = st.selectbox("Y Eksen Kolonu", filtered_df.columns, index=1 if len(filtered_df.columns) > 1 else 0, key=f"{key_prefix}_y")
#         add_chart = st.form_submit_button("Grafiği Ekle")

#         if add_chart:
#             st.session_state[f"{key_prefix}_charts"].append((chart_type, x_col, y_col))

#     for idx, (chart_type, x_col, y_col) in enumerate(st.session_state[f"{key_prefix}_charts"]):
#         st.markdown(f"#### Grafik {idx+1}: {chart_type} ({x_col} vs {y_col})")
#         try:
#             if chart_type == "Çizgi (Line)":
#                 fig = px.line(filtered_df, x=x_col, y=y_col)
#             elif chart_type == "Bar":
#                 fig = px.bar(filtered_df, x=x_col, y=y_col)
#             elif chart_type == "Alan (Area)":
#                 fig = px.area(filtered_df, x=x_col, y=y_col)
#             elif chart_type == "Pasta (Pie)":
#                 fig = px.pie(filtered_df, names=x_col, values=y_col)
#             elif chart_type == "Dağılım (Scatter)":
#                 fig = px.scatter(filtered_df, x=x_col, y=y_col)
#             st.plotly_chart(fig, use_container_width=True)
#         except Exception as e:
#             st.warning(f"Grafik çizilirken hata oluştu: {e}")


def filtered_chart_section(df, key_prefix="chart"):
    st.markdown("### 📋 Tablo")
    df = df.copy()

    # Filter by year
    years = df["Yıllar"].unique()
    selected_years = st.multiselect("Yıllara Göre Filtrele", years, default=years, key=f"{key_prefix}_years")
    df = df[df["Yıllar"].isin(selected_years)]

    # Filter by columns (excluding Yıllar)
    all_columns = df.columns.drop("Yıllar")
    selected_columns = st.multiselect("Değişkenleri Seçin", all_columns, default=all_columns[:3], key=f"{key_prefix}_cols")
    filtered_df = df[["Yıllar"] + selected_columns]
    st.dataframe(filtered_df)

    # Chart builder with export
    chart_creator_with_export(filtered_df, key_prefix=key_prefix)


def chart_creator_with_export(df, key_prefix="chart"):
    st.markdown("---")
    st.markdown("### 📊 Görsel Oluştur")

    if f"{key_prefix}_charts" not in st.session_state:
        st.session_state[f"{key_prefix}_charts"] = []

    with st.form(key=f"{key_prefix}_form"):
        chart_type = st.selectbox("Grafik Türü Seçin", ["Çizgi (Line)", "Bar", "Alan (Area)", "Pasta (Pie)", "Dağılım (Scatter)"], key=f"{key_prefix}_chart_type")
        x_col = st.selectbox("X Eksen Kolonu", df.columns, index=0, key=f"{key_prefix}_x")
        y_col = st.selectbox("Y Eksen Kolonu", df.columns, index=1 if len(df.columns) > 1 else 0, key=f"{key_prefix}_y")
        add_chart = st.form_submit_button("Grafiği Ekle")

        if add_chart:
            st.session_state[f"{key_prefix}_charts"].append((chart_type, x_col, y_col))

    # Display and export charts
    for idx, (chart_type, x_col, y_col) in enumerate(st.session_state[f"{key_prefix}_charts"]):
        st.markdown(f"#### Grafik {idx+1}: {chart_type} ({x_col} vs {y_col})")
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

            if st.session_state.get("reports"):
                export_to = st.selectbox(f"Grafik {idx+1} için rapor seçin", list(st.session_state["reports"].keys()), key=f"{key_prefix}_export_{idx}")
                if st.button(f"Grafiği '{export_to}' raporuna aktar", key=f"{key_prefix}_export_btn_{idx}"):
                    st.session_state["reports"][export_to]["charts"].append(fig)
                    st.success(f"Görsel '{export_to}' raporuna eklendi.")
        except Exception as e:
            st.warning(f"Grafik çizilirken hata oluştu: {e}")


def display_fleet_data():
    st.markdown("### 🚘 Otomobil Filosu Verisi")

    # Load the data
    df = pd.read_excel("otomobil_filosu_verisi.xlsx")

    # Column selection (no year filtering)
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect("Görüntülenecek Değişkenleri Seçin", all_columns, default=all_columns[:5], key="filo_cols")

    # Display the selected columns
    st.dataframe(df[selected_columns])




def display_fleet_data():
    st.markdown("### 🚘 Otomobil Filosu Verisi")

    # Load the fleet dataset
    df = pd.read_excel("otomobil_filosu_verisi.xlsx")

    # Column selection
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect("Görüntülenecek Değişkenleri Seçin", all_columns, default=all_columns[:5], key="filo_cols")

    # Display selected columns
    st.dataframe(df[selected_columns])

    # Map visualization section
    st.markdown("### 📍 Araç Canlı Takip")

    # Parse coordinates from "Anlık Konum" column
    df[["lat", "lon"]] = df["Anlık Konum"].str.split(",", expand=True).astype(float)

    # Prepare the map layer to visualize vehicle locations as scatter points
    # Each point represents a vehicle, with a red color and a radius of 80
    # The points are interactive (pickable) to show additional information on hover
    layer = pdk.Layer(
        "ScatterplotLayer",  # Type of layer to render scatter points
        data=df,  # Data source containing vehicle locations
        get_position='[lon, lat]',  # Extract longitude and latitude for positioning
        get_radius=380,  # Radius of each scatter point
        get_fill_color=[255, 0, 0, 160],  # Red color with some transparency
        pickable=True  # Enable interactivity for tooltips
    )

    # Define the tooltip to display vehicle license plate ("Plaka") on hover
    tooltip = {
        # "html": "<b>Plaka:</b> {Plaka}",  # HTML content for the tooltip
        "html": "{Plaka}",  # HTML content for the tooltip
        "style": {"backgroundColor": "white", "color": "black"}  # Tooltip styling
    }

    # Set the initial view state of the map
    # Center the map around the average latitude and longitude of the vehicles
    # Set the zoom level to 9 and pitch to 0 for a top-down view
    view_state = pdk.ViewState(
        latitude=df["lat"].mean(),  # Center latitude
        longitude=df["lon"].mean(),  # Center longitude
        zoom=9,  # Zoom level
        pitch=0  # Camera angle (0 for top-down view)
    )

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))



def run_car_valuation_form():
    st.markdown("### 🚗 Araç Değerleme Formu")

    # Input form fields
    with st.form("valuation_form"):
        col1, col2 = st.columns(2)
        with col1:
            marka = st.selectbox("Marka", ["Mercedes", "Hyundai", "Toyota", "Renault", "Volkswagen"])
            model = st.text_input("Model")
            yakit = st.selectbox("Yakıt Türü", ["Benzin", "Dizel", "Elektrik"])
        with col2:
            yil = st.number_input("Model Yılı", min_value=1990, max_value=2025, value=2020)
            km = st.number_input("Güncel KM", min_value=0, value=50000)
            motor = st.number_input("Motor Gücü (HP)", min_value=30, value=100)

        segment = st.selectbox("Segment", ["Bütçe", "Aile", "Premium"])
        kaza_durumu = st.selectbox("Kaza Durumu", ["Var", "Yok"])

        submitted = st.form_submit_button("Değerleme Yap")

    if submitted:
        # Load model
        try:
            model = joblib.load("car_value_model.pkl")
        except Exception as e:
            st.error(f"Model yüklenemedi: {e}")
            return

        # Create input DataFrame
        input_df = pd.DataFrame([{
            "Marka": marka,
            "Model": model,
            "Yıl": yil,
            "Güncel KM": km,
            "Yakıt": yakit,
            "Motor Gücü (HP)": motor,
            "Segment": segment,
            "Kaza Durumu": kaza_durumu
        }])

        # Predict
        try:
            prediction = model.predict(input_df)[0]
            st.success(f"Tahmini Araç Değeri: {int(prediction):,} TL")
        except Exception as e:
            st.error(f"Tahmin sırasında hata oluştu: {e}")


def run_common_size_analysis():
    st.markdown("## 📊 Yüzde Yöntemi ile Analiz (Common-Size Analysis)")

    # Load both datasets
    df_bilanco = pd.read_excel("yapay_bilanco_2020_2024.xlsx", index_col=0)
    df_gelir = pd.read_excel("yapay_gelir_tablosu_2020_2024.xlsx", index_col=0)

    # ----------- BİLANÇO ANALİZİ -----------
    st.markdown("### 📘 Bilanço")
    bilanco_columns = df_bilanco.columns.tolist()

    selected_cols_bilanco = st.multiselect(
        "Görüntülenecek Yıllar (Bilanço)",
        bilanco_columns,
        default=bilanco_columns,
        key="bilanco_years"
    )

    if selected_cols_bilanco:
        base_column_bilanco = st.selectbox(
            "Baz Alınacak Yıl (Bilanço)",
            selected_cols_bilanco,
            key="bilanco_base"
        )

        df_bilanco_view = df_bilanco[selected_cols_bilanco]
        df_bilanco_common = df_bilanco_view.divide(df_bilanco_view[base_column_bilanco], axis=0) * 100
        st.dataframe(df_bilanco_common.style.format("{:.2f} %"))

    st.markdown("---")

    # ----------- GELİR TABLOSU ANALİZİ -----------
    st.markdown("### 📙 Gelir Tablosu")
    gelir_columns = df_gelir.columns.tolist()

    selected_cols_gelir = st.multiselect(
        "Görüntülenecek Yıllar (Gelir Tablosu)",
        gelir_columns,
        default=gelir_columns,
        key="gelir_years"
    )

    if selected_cols_gelir:
        base_column_gelir = st.selectbox(
            "Baz Alınacak Yıl (Gelir Tablosu)",
            selected_cols_gelir,
            key="gelir_base"
        )

        df_gelir_view = df_gelir[selected_cols_gelir]
        df_gelir_common = df_gelir_view.divide(df_gelir_view[base_column_gelir], axis=0) * 100
        st.dataframe(df_gelir_common.style.format("{:.2f} %"))


def run_trend_analysis():
    st.markdown("## 📈 Trend Analizi (Yatay Yüzde Değişim)")

    # ---- BİLANÇO TREND ANALİZİ ----
    # Load balance sheet data (assumes first column is "Yıllar")
    df_bilanco = pd.read_excel("yapay_bilanco_2020_2024.xlsx")
    # Pivot: set "Yıllar" as index and then transpose so that rows = financial items, columns = years.
    df_bilanco_pivot = df_bilanco.set_index("Yıllar").T

    # Get the list of available years (now from the columns)
    bilanco_years = df_bilanco_pivot.columns.tolist()
    selected_bilanco_years = st.multiselect(
        "Görüntülenecek Yıllar (Bilanço)",
        bilanco_years,
        default=bilanco_years,
        key="trend_bilanco_years"
    )

    if selected_bilanco_years:
        base_year_bilanco = st.selectbox(
            "Baz Yıl (Bilanço)",
            selected_bilanco_years,
            key="trend_bilanco_base"
        )

        # Work on the selected columns
        df_bilanco_selected = df_bilanco_pivot[selected_bilanco_years].copy()
        df_bilanco_trend = df_bilanco_selected.copy()

        # For each financial item (row), compute the trend relative to the base year
        for idx in df_bilanco_trend.index:
            base_val = df_bilanco_selected.loc[idx, base_year_bilanco]
            if base_val != 0:
                df_bilanco_trend.loc[idx] = (df_bilanco_selected.loc[idx] / base_val) * 100
            else:
                df_bilanco_trend.loc[idx] = 0

        st.dataframe(df_bilanco_trend.style.format("{:.2f} %"))

    st.markdown("---")

    # ---- GELİR TABLOSU TREND ANALİZİ ----
    df_gelir = pd.read_excel("yapay_gelir_tablosu_2020_2024.xlsx")
    df_gelir_pivot = df_gelir.set_index("Yıllar").T

    gelir_years = df_gelir_pivot.columns.tolist()
    selected_gelir_years = st.multiselect(
        "Görüntülenecek Yıllar (Gelir Tablosu)",
        gelir_years,
        default=gelir_years,
        key="trend_gelir_years"
    )

    if selected_gelir_years:
        base_year_gelir = st.selectbox(
            "Baz Yıl (Gelir Tablosu)",
            selected_gelir_years,
            key="trend_gelir_base"
        )

        df_gelir_selected = df_gelir_pivot[selected_gelir_years].copy()
        df_gelir_trend = df_gelir_selected.copy()

        for idx in df_gelir_trend.index:
            base_val = df_gelir_selected.loc[idx, base_year_gelir]
            if base_val != 0:
                df_gelir_trend.loc[idx] = (df_gelir_selected.loc[idx] / base_val) * 100
            else:
                df_gelir_trend.loc[idx] = 0

        st.dataframe(df_gelir_trend.style.format("{:.2f} %"))



def run_ratio_analysis_dashboard():
    

    st.markdown("## 📊 Rasyo Analizi Dashboard")

    # Sample data for now — replace with calculated values later
    data = {
        "Yıllar": [2020, 2021, 2022, 2023],
        "Cari Oran": [1.5, 2.1, 2.3, 2.0],
        "Borç / Özsermaye": [1.2, 1.5, 1.6, 1.4],
        "Net Kar Marjı": [10.0, 12.5, 14.0, 15.0]
    }

    df = pd.DataFrame(data)

    # --- KPI Metrics ---
    st.markdown("### 🔑 Temel Göstergeler")

    col1, col2, col3 = st.columns(3)
    col1.metric("Cari Oran", f"{df['Cari Oran'].iloc[-1]:.2f}", f"{df['Cari Oran'].iloc[-1] - df['Cari Oran'].iloc[-2]:+.2f}")
    col2.metric("Borç / Özsermaye", f"{df['Borç / Özsermaye'].iloc[-1]:.2f}", f"{df['Borç / Özsermaye'].iloc[-1] - df['Borç / Özsermaye'].iloc[-2]:+.2f}")
    col3.metric("Net Kar Marjı", f"{df['Net Kar Marjı'].iloc[-1]:.2f}%", f"{df['Net Kar Marjı'].iloc[-1] - df['Net Kar Marjı'].iloc[-2]:+.2f}%")

    # --- Ratio Charts Side-by-Side ---
    st.markdown("### 📈 Zaman İçindeki Değişim")

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.plotly_chart(px.line(df, x="Yıllar", y="Cari Oran", title="Cari Oran"), use_container_width=True)
    with chart_col2:
        st.plotly_chart(px.line(df, x="Yıllar", y="Borç / Özsermaye", title="Borç / Özsermaye"), use_container_width=True)

    # --- Data Table ---
    st.markdown("### 📊 Tüm Rasyo Verileri")
    st.dataframe(df.style.format({
        "Cari Oran": "{:.2f}",
        "Borç / Özsermaye": "{:.2f}",
        "Net Kar Marjı": "{:.2f}%"
    }))



# Sub-tab logic
sub_tab = None

if main_section == "📄 Tablolarım":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Bilanço", "Gelir Tablosu"])

    # st.markdown(f"#### {sub_tab}")

    # if sub_tab == "Bilanço":
    #     df = load_excel("file_example_XLS_10.xls")
    #     st.dataframe(df)
    #     chart_creator(df, key_prefix="bilanco")

    # elif sub_tab == "Gelir Tablosu":
    #     df = load_excel("file_example_XLS_102.xls")
    #     st.dataframe(df)
    #     chart_creator(df, key_prefix="gelir")

# elif main_section == "📄 Tablolarım":
    st.markdown(f"#### {sub_tab}")

    if sub_tab == "Bilanço":
        df = pd.read_excel("yapay_bilanco_2020_2024.xlsx")
        filtered_chart_section(df, key_prefix="bilanco")

    elif sub_tab == "Gelir Tablosu":
        df = pd.read_excel("yapay_gelir_tablosu_2020_2024.xlsx")
        filtered_chart_section(df, key_prefix="gelir")

    

elif main_section == "📈 Analizlerim":
    # sub_tab = st.sidebar.radio("Alt Sekmeler", ["Rasyo", "Trend", "Yüzde Analizi", "Karşılaştırmalı Analiz"])
    sub_tab = st.sidebar.radio("Alt Sekmeler", [ "Yüzde Analizi" ,  "Trend", "Rasyo"])

    if sub_tab == "Yüzde Analizi":
        run_common_size_analysis()

    elif sub_tab == "Trend":
        run_trend_analysis()

    elif sub_tab == "Rasyo":
        run_ratio_analysis_dashboard()




elif main_section == "🚗 Filo ve Değerleme":
    sub_tab = st.sidebar.radio("Alt Sekmeler", ["Filo", "Araç Değerleme"])

# In your main logic:
# elif main_section == "🚗 Filo ve Değerleme":
    # st.markdown(f"#### {sub_tab}")

    # if sub_tab == "Filo":
    #     display_fleet_data()

# elif main_section == "🚗 Filo ve Değerleme":
    st.markdown(f"#### {sub_tab}")

    if sub_tab == "Filo":
        display_fleet_data()

    elif sub_tab == "Araç Değerleme":
        run_car_valuation_form()

# Main content area
st.markdown(f"### {main_section}")

# if main_section == "📑 Raporum":
#     st.write("Burada rapor çıktılarınızı oluşturabilirsiniz.")
# elif sub_tab:
#     st.markdown(f"#### {sub_tab}")
#     st.write(f"`{sub_tab}` içeriği buraya gelecek...")

if main_section == "📑 Raporum":

    if "reports" not in st.session_state:
        st.session_state["reports"] = {}

    if "current_report" not in st.session_state:
        st.session_state["current_report"] = None

    # Create new report
    st.markdown("### 📄 Yeni Rapor Oluştur")
    new_report_name = st.text_input("Rapor Adı Girin", "")
    if st.button("Raporu Oluştur") and new_report_name:
        if new_report_name not in st.session_state["reports"]:
            st.session_state["reports"][new_report_name] = {
                "markdown": "",
                "charts": []
            }
            st.session_state["current_report"] = new_report_name

    report_names = list(st.session_state["reports"].keys())

    if report_names:
        selected = st.selectbox("Rapor Seç", report_names, index=report_names.index(st.session_state["current_report"]) if st.session_state["current_report"] in report_names else 0)
        st.session_state["current_report"] = selected
        report = st.session_state["reports"][selected]

        st.markdown("### ✍️ Rapor İçeriği")
        report["markdown"] = st.text_area("Markdown İçeriği", value=report["markdown"], height=200)

        st.markdown("### 📊 Eklenmiş Grafikler")
        for i, fig in enumerate(report["charts"]):
            st.plotly_chart(fig, use_container_width=True)

        # if st.button("PDF Olarak İndir"):
        #     pdf = FPDF()
        #     pdf.add_page()
        #     pdf.set_auto_page_break(auto=True, margin=15)
        #     pdf.set_font("Arial", size=12)
        #     for line in report["markdown"].split("\n"):
        #         pdf.multi_cell(0, 10, line)
        #     # buffer = BytesIO()
        #     # pdf.output(buffer)
        #     # buffer.seek(0)

        #     pdf_output = pdf.output(dest='S').encode('latin-1')
        #     buffer = BytesIO(pdf_output)

        #     b64 = base64.b64encode(buffer.read()).decode()
        #     href = f'<a href="data:application/octet-stream;base64,{b64}" download="{selected}.pdf">📥 PDF\'i İndir</a>'
        #     st.markdown(href, unsafe_allow_html=True)

        # if st.button("PDF Olarak İndir"):
        #     pdf = FPDF()
        #     pdf.add_page()
        #     pdf.set_auto_page_break(auto=True, margin=15)
        #     pdf.set_font("Arial", size=12)

        #     # Add Markdown text (without Turkish characters)
        #     for line in report["markdown"].split("\n"):
        #         safe_line = remove_accents(line)
        #         pdf.multi_cell(0, 10, safe_line)

        #     # Output PDF to memory
        #     pdf_output = pdf.output(dest='S').encode('latin-1')
        #     buffer = BytesIO(pdf_output)
        #     b64 = base64.b64encode(buffer.read()).decode()
        #     href = f'<a href="data:application/octet-stream;base64,{b64}" download="{selected}.pdf">📥 PDF\'i İndir</a>'
        #     st.markdown(href, unsafe_allow_html=True)

        if st.button("PDF Olarak İndir"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)

            # Convert markdown to simple formatted text (bold, headers, etc.)
            html = markdown(report["markdown"])
            soup = BeautifulSoup(html, "html.parser")

            for element in soup.find_all():
                if element.name == "h1":
                    pdf.set_font("Arial", "B", 16)
                    pdf.cell(0, 10, element.text, ln=True)
                elif element.name == "h2":
                    pdf.set_font("Arial", "B", 14)
                    pdf.cell(0, 10, element.text, ln=True)
                elif element.name == "li":
                    pdf.set_font("Arial", size=12)
                    pdf.cell(0, 10, f"- {element.text}", ln=True)
                elif element.name == "p":
                    pdf.set_font("Arial", size=12)
                    pdf.multi_cell(0, 10, element.text)
                pdf.ln(2)

            # Insert charts
            with tempfile.TemporaryDirectory() as tmpdir:
                for i, fig in enumerate(report["charts"]):
                    image_path = os.path.join(tmpdir, f"chart_{i}.png")
                    try:
                        fig.update_layout(
                            template="plotly",
                            paper_bgcolor="white",
                            plot_bgcolor="white"
                        )
                        # fig.write_image(image_path, format="png")
                        fig.write_image(image_path, format="png")
                        pdf.image(image_path, w=180)  # Fit width to page
                        pdf.ln(5)
                    except Exception as e:
                        st.warning(f"Grafik {i+1} PDF'e eklenemedi: {e}")

            # Export PDF to memory
            pdf_output = pdf.output(dest="S").encode("latin-1")
            buffer = BytesIO(pdf_output)
            b64 = base64.b64encode(buffer.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{selected}.pdf">📥 PDF\'i İndir</a>'
            st.markdown(href, unsafe_allow_html=True)

        

    else:
        st.info("Henüz oluşturulmuş bir rapor yok.")


    


