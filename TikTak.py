import streamlit as st


# Start the Streamlit app
st.title("Financial Data Analysis")
st.subheader("Analyze your financial data with ease!")
st.write("Upload your financial data in CSV format to get started.")

# Add a sidebar for navigation

st.sidebar.title("Navigation")
st.sidebar.markdown("Select an option below:")
st.sidebar.markdown("- [Home](#home)")
st.sidebar.markdown("- [Upload Data](#upload-data)")
st.sidebar.markdown("- [Data Analysis](#data-analysis)")
st.sidebar.markdown("- [Visualization](#visualization)")
st.sidebar.markdown("- [Map](#map)")
st.sidebar.markdown("- [About](#about)")

st.sidebar.markdown("## About")
st.sidebar.markdown("This app allows you to upload and analyze financial data in CSV format. "
                    "You can visualize the data using various charts and maps.")
st.sidebar.markdown("#### Designed by Uğurcan Demir")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the DataFrame
    st.write("Data Preview:")
    st.dataframe(df.head())

    # Display basic statistics of the DataFrame
    st.write("Basic Statistics:")
    st.write(df.describe())

    # Display the correlation matrix as a heatmap
    st.write("Correlation Matrix:")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    st.pyplot(plt)

# # Run the app only if the script is run directly (not imported as a module)
# if __name__ == "__main__":
    
import numpy as np
import pandas as pd

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Add a map centered around the given coordinates (41.0082° N, 28.9784° E)
st.write("Map centered around Istanbul, Turkey:")
istanbul_coordinates = pd.DataFrame(
    [[41.0082, 28.9784]],
    columns=['lat', 'lon']
)
st.map(istanbul_coordinates)

x = st.slider('Slider')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

  '...and now we\'re done!'

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()