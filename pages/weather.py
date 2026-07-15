import streamlit as st
import requests
import pandas as pd
import datetime
import locale
import time
import datetime


# Permet de gérer la marge avec le top de la page
st.markdown("""
<style>
.block-container {
    padding-top: 2rem !important;
}
</style>
""", unsafe_allow_html=True)


# --- Coordonnées ---
lat = 48.839
lon = 2.702

# --- API Open-Meteo ---
url = (
    "https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={lon}"
    "&current_weather=true"
    "&daily=weathercode,temperature_2m_max,temperature_2m_min"
    "&timezone=Europe/Paris"
)

data = requests.get(url).json()






# --- Images météo ---
weather_images = {
    0: "https://cdn-icons-png.flaticon.com/128/3262/3262944.png", 
    1: "https://cdn-icons-png.flaticon.com/128/3262/3262948.png",
    2: "https://cdn-icons-png.flaticon.com/128/3262/3262930.png",
    3: "https://cdn-icons-png.flaticon.com/128/3262/3262932.png",
    45: "https://cdn-icons-png.flaticon.com/512/3262/3262971.png",
    48: "https://cdn-icons-png.flaticon.com/512/3262/3262971.png",
    51: "https://cdn-icons-png.flaticon.com/512/3262/3262939.png",
    61: "https://cdn-icons-png.flaticon.com/512/3262/3262918.png",
    71: "https://cdn-icons-png.flaticon.com/128/1163/1163661.png",
    80: "https://cdn-icons-png.flaticon.com/512/3262/3262939.png",
    95: "https://cdn-icons-png.flaticon.com/512/3262/3262937.png",
}

# --- Météo actuelle ---
current = data["current_weather"]
current_icon = weather_images.get(current["weathercode"])
current_temp = current["temperature"]

st.title("🌤️ Météo actuelle & prévisions 7 jours")

jours = data["daily"]["time"]
codes = data["daily"]["weathercode"]
tmax = data["daily"]["temperature_2m_max"]
tmin = data["daily"]["temperature_2m_min"]

cols = st.columns(7)

jours_fr = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for i in range(7):
    with cols[i]:
        img = weather_images.get(codes[i])

        date_obj = datetime.datetime.strptime(jours[i], "%Y-%m-%d")
        jour = jours_fr[date_obj.weekday()]

        st.markdown(...)

# --- Affichage météo actuelle ---
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="{current_icon}" style="width:120px; margin:0; padding:0;">
        <div style="font-size: 40px; font-weight: bold; margin-top:10px;">
            {current_temp}°C
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

# --- Prévisions 7 jours ---
jours = data["daily"]["time"]
codes = data["daily"]["weathercode"]
tmax = data["daily"]["temperature_2m_max"]
tmin = data["daily"]["temperature_2m_min"]

cols = st.columns(7)

for i in range(7):
    with cols[i]:
        img = weather_images.get(codes[i])

        # --- Convertir la date en jour de la semaine ---
        date_obj = datetime.datetime.strptime(jours[i], "%Y-%m-%d")
        jour = date_obj.strftime("%A").capitalize()  # Lundi, Mardi, ...

        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{img}" style="width:70px; margin:0; padding:0;">
                <div style="font-size:22px; margin-top:4px;">{jour}</div>
                <div style="font-size:22px; color:#ff4b4b; font-weight:bold;">
                    {tmax[i]}°C
                </div>
                <div style="font-size:19px; color:#4b9cff; font-weight:bold;">
                    {tmin[i]}°C
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) CHANGEMENT AUTOMATIQUE DE PAGES
# --------------------------------------------------------------------------------------------------------------------------------------------------------



time.sleep(15)  # délai en secondes

st.switch_page("pages/Progress st.py")


# __________________ Courbes
# import plotly.graph_objects as go

# --- Courbe des températures max/min ---
# fig = go.Figure()

# # Courbe max
# fig.add_trace(go.Scatter(
#     x=jours,
#     y=tmax,
#     mode="lines+markers",
#     name="Température max",
#     line=dict(color="#ff4b4b", width=2),
#     marker=dict(size=6)
# ))

# # Courbe min
# fig.add_trace(go.Scatter(
#     x=jours,
#     y=tmin,
#     mode="lines+markers",
#     name="Température min",
#     line=dict(color="#4b9cff", width=2),
#     marker=dict(size=6)
# ))

# fig.update_layout(
#     title="Évolution des températures sur 7 jours",
#     xaxis_title="Jour",
#     yaxis_title="Température (°C)",
#     template="plotly_white",
#     height=400,
#     legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
# )

# st.plotly_chart(fig, use_container_width=True)
