import streamlit as st

import pandas as pd

url = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/records.csv"
df = pd.read_csv(url)

st.dataframe(df)

st.title("Hi everyone, i'm one the place")
st.header("Ici un header")
st.subheader("subheader")


st.markdown("---")

st.text("Test d'un nouveau test ici en direct 2")
