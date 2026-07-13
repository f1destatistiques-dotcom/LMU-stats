import streamlit as st
import datetime
import base64
from streamlit_autorefresh import st_autorefresh


# Rafraîchit toutes les 5 secondes (5000 ms)
st_autorefresh(interval=5000, key="progress_refresh")

st.set_page_config(layout="wide")
now = datetime.datetime.now()

st.title("Progressbars multiples (version stable et fluide)")

# ____________ Chargement image en base 64

def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

avion_base64 = load_image_base64("rect19.png")

# ____________ Heure actuelle
heure_actuelle = now.strftime("%H:%M")

# ---------------------------------------------------------
# 1) BARRE JOURNALIÈRE
# ---------------------------------------------------------

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois  = ["janvier", "février", "mars", "avril", "mai", "juin",
         "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

jour_nom = jours[now.weekday()]
mois_nom = mois[now.month - 1]

date_affichee = f"{jour_nom} {now.day} {mois_nom} {now.year}"

start_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
end_day   = start_day + datetime.timedelta(days=1)

pct_day = ((now - start_day).total_seconds() / (end_day - start_day).total_seconds()) * 100

# __________ Convertion automatique des positions relatives

# 08h
heure_1 = 8
position_08h = heure_1/24 * 100

# 18h
heure_2 = 18
position_18h = heure_2/24 * 100

# 21h
heure_3 = 21
position_21h = heure_3/24 * 100


# __________ Code barre html

bar_day = f"""
<div style="position: relative; width: 100%; background-color: #ffdafcff; border-radius: 8px; height: 5px;">

  <div style="
    width: {pct_day}%;
    height: 100%;
    background: #8e17dcff;
    border-radius: 6px;
  "></div>
</div>


<!-- Avion -->
<img src="data:png;base64,{avion_base64}"
  style="
    position: absolute;
    top: 5%;
    left: {pct_day}%;
    transform: translate(-50%, -50%);
    height: 30px;
    pointer-events: none;
  ">


<!-- 8h -->
  <div style="
    position: absolute;
    top: 30%;
    left: {position_08h}%;
    transform: translate(-50%, -50%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 08h"}
  </div>

<!-- 18h -->
  <div style="
    position: absolute;
    top: 30%;
    left: {position_18h}%;
    transform: translate(-50%, -50%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 18h"}
  </div>

<!-- 21h -->
  <div style="
    position: absolute;
    top: 30%;
    left: {position_21h}%;
    transform: translate(-50%, -50%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 21h"}
  </div>

<p style="color:#b141ffff;">{pct_day:.3f}% du jour</p>
"""


# ____ Titre au format html
titre = f"{date_affichee} | {heure_actuelle}"
st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:4px;'>{titre}</h3>",
    unsafe_allow_html=True
)

# _____ Affiche le contenu de la barre (issu du code html plus haut)
st.markdown(bar_day, unsafe_allow_html=True)



# ---------------------------------------------------------
# 2) BARRE HEBDOMADAIRE (statique)
# ---------------------------------------------------------
start_week = now - datetime.timedelta(days=now.weekday())  # lundi
start_week = datetime.datetime(start_week.year, start_week.month, start_week.day)
end_week   = start_week + datetime.timedelta(days=7)

pct_week = ((now - start_week).total_seconds() / (end_week - start_week).total_seconds()) * 100

bar_week = f"""
<div style="position: relative; width: 100%; background-color: #eee; border-radius: 6px; height: 14px;">
  <div style="
    width: {pct_week}%;
    height: 100%;
    background: #5784BA;
    border-radius: 6px;
  "></div>
</div>
<p style="color:#5784BA;">{pct_week:.3f}% de la semaine</p>
"""

st.subheader("Progression de la semaine")
st.markdown(bar_week, unsafe_allow_html=True)



# ---------------------------------------------------------
# 3) BARRE MENSUELLE (fluide + avion + zones weekend)
# ---------------------------------------------------------
start_month = datetime.datetime(now.year, now.month, 1)
if now.month == 12:
    end_month = datetime.datetime(now.year + 1, 1, 1)
else:
    end_month = datetime.datetime(now.year, now.month + 1, 1)

pct_month = ((now - start_month).total_seconds() / (end_month - start_month).total_seconds()) * 100


# --- Zones weekend ---
weekend_html = ""
cursor = start_month
total_month_seconds = (end_month - start_month).total_seconds()

while cursor < end_month:
    if cursor.weekday() == 5:  # samedi
        saturday = cursor
        sunday = cursor + datetime.timedelta(days=1)

        start_pos = ((saturday - start_month).total_seconds() / total_month_seconds) * 100
        end_pos   = ((sunday   - start_month).total_seconds() / total_month_seconds) * 100
        width     = end_pos - start_pos

        weekend_html += f"""
        <div style="
            position: absolute;
            left: {start_pos}%;
            width: {width}%;
            top: 0;
            bottom: 0;
            background: rgba(0,0,0,0.12);
        "></div>
        """

    cursor += datetime.timedelta(days=1)


bar_html_month = f"""
<div style="position: relative; width: 100%; background-color: #eee; border-radius: 6px; height: 12px; overflow: hidden;">

  {weekend_html}

  <div style="
    width: {pct_month}%;
    height: 100%;
    background: #5784BA;
    border-radius: 6px;
    transition: width 0.1s ease-out;
  "></div>

  <img src="https://cdn-icons-png.flaticon.com/128/7118/7118033.png"
  style="
    position: absolute;
    top: 50%;
    left: {pct_month}%;
    transform: translate(-50%, -50%);
    height: 25px;
    pointer-events: none;
  ">

</div>

<p style="color: #5784BA; margin-top: 2px;">{pct_month:.1f}%</p>
"""


st.subheader("Progression du mois")
st.markdown(bar_html_month, unsafe_allow_html=True)


# ---------------------------------------------------------
# 4) RERUN UNIQUEMENT POUR LA BARRE MENSUELLE
# ---------------------------------------------------------0
  
#st.rerun()

