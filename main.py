import streamlit as st

import pandas as pd

url = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/records.csv?token=GHSAT0AAAAAAD2KFXB5PESA7H4D5Z7MAXE42O5AG5Q"
#df = pd.read_csv(url)
token = st.secrets["GITHUB_TOKEN"]

df = pd.read_csv(url, storage_options={"Authorization": f"token {token}"})

st.dataframe(df)

st.title("Hi everyone, i'm one the place")
st.header("Ici un header")
st.subheader("subheader")


st.markdown("---")

st.text("Test d'un nouveau test ici en direct 2")
