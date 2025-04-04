import streamlit as st
import pandas as pd
import numpy as np

st.dataframe(pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE")))

