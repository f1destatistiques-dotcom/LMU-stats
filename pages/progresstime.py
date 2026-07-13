import streamlit as st
import datetime

st.set_page_config(layout="wide")
st.title("Progression temporelle (fluide)")

# Dates en dur
start = datetime.datetime(2026, 7, 13, 19, 0, 0)
end   = datetime.datetime(2026, 7, 13, 22, 0, 0)

# Calcul du pourcentage
now = datetime.datetime.now()
total = (end - start).total_seconds()
elapsed = (now - start).total_seconds()

pct = min(max(elapsed / total, 0), 1)

# Affichage fluide
st.progress(pct)
st.write(f"{pct*100:.3f}%")

# Rafraîchissement automatique
if pct < 1:
    st.rerun()
