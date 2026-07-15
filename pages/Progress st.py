import streamlit as st
import datetime
import base64
from streamlit_autorefresh import st_autorefresh
import calendar
import time

# Permet de supprimer les marges supérieures (la valeur 0rem permet d'ajuster)
st.markdown("""
<style>
.block-container {
    padding-top: 0rem !important;
}
</style>
""", unsafe_allow_html=True)



# Rafraîchit toutes les 5 secondes (5000 ms)
#st_autorefresh(interval=30000, key="progress_refresh")

st.set_page_config(layout="wide")
#now = datetime.datetime.now()
from zoneinfo import ZoneInfo
TZ = ZoneInfo("Europe/Paris")
now = datetime.datetime.now(ZoneInfo("Europe/Paris"))


st.title("Progress Time")

# ____________ Chargement image en base 64

def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

avion_base64 = load_image_base64("rect19.png")

# ____________ Dates et heure actuelle

heure_actuelle = now.strftime("%H:%M")
anne_actuelle = now.strftime("%Y")

jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois  = ["janvier", "février", "mars", "avril", "mai", "juin",
         "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

jour_nom = jours[now.weekday()]
mois_nom = mois[now.month - 1]





# ________________ PLACEMENT DES REPÈRES AU CHOIX _______________________________________________________________________________________________________
#___________ REP1

date_str = "18/07/2026 21:30"
image_source_rep1 = "https://cdn-icons-png.flaticon.com/128/16565/16565936.png"
parametre_centrage_icon_repere = -50 #0 pour prendre à gauche, -50 pour prendre le centre de l'image

# Séparation date + heure
date_part, time_part = date_str.split(" ")

# Extraction date
jour, mois, annee = map(int, date_part.split("/"))

# Extraction heure
heure, minute = map(int, time_part.split(":"))

# Construction de la datetime complète
d = datetime.datetime(annee, mois, jour, heure, minute, tzinfo=TZ)

#Récupérer le n° du jour dans l'année
numero_jour_annee = d.timetuple().tm_yday

#____ ANNÉE _____________________________
rep1_annee = numero_jour_annee/365*100

#____ MOIS _____________________________
# Renvoie (jour_de_la_semaine_du_1er, nombre_de_jours_dans_le_mois)
_, nb_jours_mois = calendar.monthrange(now.year, now.month)

if d.month == now.month:
    #rep1_mois = (d.day/nb_jours_mois) * 100
    rep1_mois = (((d.day - 1)*86400 + d.hour*3600 + d.minute*60) / (nb_jours_mois*86400))*100
else:
    rep1_mois = 1000

#____ SEMAINE _____________________________
# Numéro du jour de la semaine (1 = lundi, 7 = dimanche)
numero_jour_semaine = d.weekday() + 1

if d.isocalendar().week == now.isocalendar().week:
    rep1_week = (((numero_jour_semaine - 1)*86400 + d.hour*3600 + d.minute*60) / (7*86400)) * 100 # divise le nombre de millis de la date/heure cible divisé par le nomnbre total de millis dans une semaine
else:
    rep1_week = 1000

#____ JOUR _____________________________
if d.day == now.day:
    rep1_day = ((d.hour*3600 + d.minute*60)/ 86400)*100
else:
    rep1_day = 1000



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# BARRE ANNUELLE AVEC REPÈRES POUR CHAQUE MOIS
# ---------------------------------------------------------

# Début et fin d'année
start_year = datetime.datetime(now.year, 1, 1, tzinfo=TZ)
end_year   = datetime.datetime(now.year + 1, 1, 1, tzinfo=TZ)

pct_year = ((now - start_year).total_seconds() / (end_year - start_year).total_seconds()) * 100

# Repères des mois
mois_labels = ["Jan.", "Fév.", "Mar.", "Avr.", "Mai", "Juin", "Juil.", "Août", "Sept.", "Oct.", "Nov.", "Déc."]

repere_html_an = ""
for i in range(12):
  mois_start = datetime.datetime(now.year, i+1, 1, tzinfo=TZ)
  pos_an = ((mois_start - start_year).total_seconds() / (end_year - start_year).total_seconds()) * 100

  repere_html_an += f"""
  <div style="
      position: absolute;
      top: 12%;
      left: {pos_an}%;
      transform: translate(0%, 0%);
      color: black;
      font-size: 14px;
      pointer-events: none;
  ">
      | {mois_labels[i]}
  </div>
  """

# Barre HTML
bar_year = f"""
<div style="position: relative; width: 100%; background-color: #ffdafcff; border-radius: 8px; height: 5px;">

  <div style="
    width: {pct_year}%;
    height: 100%;
    background: #8e17dcff;
    border-radius: 6px;
  "></div>

</div>

<!-- Avion -->
<img src="data:png;base64,{avion_base64}"
  style="
    position: absolute;
    top: 4.5%;
    left: {pct_year - 0.7}%;
    transform: translate(-50%, -50%);
    height: 30px;
    pointer-events: none;
  ">

<!-- Repère 1 -->
<img src="{image_source_rep1}"
style="
  position: absolute;
  top: -56%;
  left: {rep1_annee}%;
  transform: translate({parametre_centrage_icon_repere}%, 0%);
  height: 25px;
  pointer-events: none;
">

{repere_html_an}

<p style="color:#b141ffff;">.</p>
"""

# Titre

# ____ Titre au format html

st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:0px;'>{anne_actuelle}</h3>",
    unsafe_allow_html=True
)

st.markdown(bar_year, unsafe_allow_html=True)





# ---------------------------------------------------------
# BARRE MENSUELLE AVEC REPÈRES POUR CHAQUE LUNDI
# ---------------------------------------------------------

start_month = datetime.datetime(now.year, now.month, 1, tzinfo=TZ)

if now.month == 12:
    end_month = datetime.datetime(now.year + 1, 1, 1, tzinfo=TZ)
else:
    end_month = datetime.datetime(now.year, now.month + 1, 1, tzinfo=TZ)

pct_month = ((now - start_month).total_seconds() / (end_month - start_month).total_seconds()) * 100

# Repères des lundis
repere_html = ""
cursor = start_month
total_month_seconds = (end_month - start_month).total_seconds()

# Liste des lundis
lundis = []

cursor = start_month
while cursor < end_month:
    if cursor.weekday() == 0:  # 0 = lundi
        lundis.append(cursor.day)
    cursor += datetime.timedelta(days=1)

# Attribution dans des variables
premier_lundi  = lundis[0] if len(lundis) > 0 else None
deuxieme_lundi = lundis[1] if len(lundis) > 1 else None
troisieme_lundi = lundis[2] if len(lundis) > 2 else None
quatrieme_lundi = lundis[3] if len(lundis) > 3 else None
cinquieme_lundi = lundis[4] if len(lundis) > 4 else None

rep_premier_lundi = (((premier_lundi-1) * 86400) / total_month_seconds) * 100
rep_deuxieme_lundi = (((deuxieme_lundi-1) * 86400) / total_month_seconds) * 100
rep_troisieme_lundi = (((troisieme_lundi-1) * 86400) / total_month_seconds) * 100
rep_quatriem_lundi = (((quatrieme_lundi-1) * 86400) / total_month_seconds) * 100
if cinquieme_lundi == None:
  rep_cinquieme_lundi = 1000
else:
  rep_cinquieme_lundi = (((cinquieme_lundi-1) * 86400) / total_month_seconds) * 100


# Barre HTML — repères INSÉRÉS DANS le conteneur principal
bar_month = f"""
<div style="position: relative; width: 100%; background-color: #ffdafcff; border-radius: 8px; height: 5px;">

  <div style="
    width: {pct_month}%;
    height: 100%;
    background: #8e17dcff;
    border-radius: 6px;
  "></div>

</div>

<!-- Avion -->
<img src="data:png;base64,{avion_base64}"
  style="
    position: absolute;
    top: 4.5%;
    left: {pct_month - 0.7}%;
    transform: translate(-50%, -50%);
    height: 30px;
    pointer-events: none;
  ">

  <!-- Premier lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: {rep_premier_lundi}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    | {premier_lundi}
  </div>

  <!-- 2ème lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: {rep_deuxieme_lundi}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    | {deuxieme_lundi}
  </div>

  <!-- 3ème lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: {rep_troisieme_lundi}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    | {troisieme_lundi}
  </div>

  <!-- 4ème lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: {rep_quatriem_lundi}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    | {quatrieme_lundi}
  </div>

  <!-- 5ème lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: {rep_cinquieme_lundi}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    | {cinquieme_lundi}
  </div>

<!-- Repère 1 -->
<img src="{image_source_rep1}"
style="
  position: absolute;
  top: -56%;
  left: {rep1_mois}%;
  transform: translate({parametre_centrage_icon_repere}%, 0%);
  height: 25px;
  pointer-events: none;
">

<p style="color:#b141ffff;">.</p>
"""
# <p style="color:#b141ffff;">{pct_month:.3f}%</p>

# Titre
# ____ Titre au format html

st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:4px;'>{mois_nom} | {now.day}</h3>",
    unsafe_allow_html=True
)

st.markdown(bar_month, unsafe_allow_html=True)




# ---------------------------------------------------------
# 2) BARRE HEBDOMADAIRE (statique)
# ---------------------------------------------------------
start_week = now - datetime.timedelta(days=now.weekday())  # lundi
start_week = datetime.datetime(start_week.year, start_week.month, start_week.day, tzinfo=TZ)
end_week   = start_week + datetime.timedelta(days=7)

pct_week = ((now - start_week).total_seconds() / (end_week - start_week).total_seconds()) * 100

bar_week = f"""
<div style="position: relative; width: 100%; background-color: #ffdafcff; border-radius: 8px; height: 5px;">

  <div style="
    width: {pct_week}%;
    height: 100%;
    background: #8e17dcff;
    border-radius: 6px;
  "></div>
</div>

<!-- Repère 1 -->
<img src="{image_source_rep1}"
  style="
    position: absolute;
    top: -56%;
    left: {rep1_week}%;
    transform: translate({parametre_centrage_icon_repere}%, 0%);
    height: 25px;
    pointer-events: none;
  ">

<!-- Avion -->
<img src="data:png;base64,{avion_base64}"
  style="
    position: absolute;
    top: 4.5%;
    left: {pct_week - 0.7}%;
    transform: translate(-50%, -50%);
    height: 30px;
    pointer-events: none;
  ">

  <!-- Lundi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 0%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Lun."}
  </div>

  

<!-- Mardi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 14.3%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Mar."}
  </div>

<!-- Mercredi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 28.57%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Mer."}
  </div>

  <!-- Jeudi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 42.85%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Jeu."}
  </div>

  <!-- Vendredi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 57.14%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Ven."}
  </div>

  <!-- Samedi -->
  <div style="
    position: absolute;
    top: 10%;
    left: 71.42%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Sam."}
  </div>

  <!-- Dimanche -->
  <div style="
    position: absolute;
    top: 10%;
    left: 85.71%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| Dim."}
  </div>



<p style="color:#b141ffff;">.</p>
"""

# ____ Titre au format html
titre_semaine = f"Semaine n° {numero_jour_semaine}"
titre = f"{jour_nom} | {heure_actuelle}"
st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:4px;'>{titre_semaine}</h3>",
    unsafe_allow_html=True
)

# _____ Affiche le contenu de la barre (issu du code html plus haut)
st.markdown(bar_week, unsafe_allow_html=True)


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) BARRE JOURNALIÈRE
# --------------------------------------------------------------------------------------------------------------------------------------------------------

date_affichee = f"{jour_nom} {now.day} {mois_nom} {now.year}"

start_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=TZ)
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

# 23h
heure_3 = 23
position_23h = heure_3/24 * 100


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

<!-- Repère 1 -->
<img src="{image_source_rep1}"
  style="
    position: absolute;
    top: -56%;
    left: {rep1_day}%;
    transform: translate({parametre_centrage_icon_repere}%, 0%);
    height: 25px;
    pointer-events: none;
  ">

<!-- Avion -->
<img src="data:png;base64,{avion_base64}"
  style="
    position: absolute;
    top: 4.5%;
    left: {pct_day - 0.8}%;
    transform: translate(-50%, -50%);
    height: 30px;
    pointer-events: none;
  ">


<!-- 8h -->
  <div style="
    position: absolute;
    top: 10%;
    left: {position_08h}%;
    transform: translate(0%, 0%);
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
    top: 10%;
    left: {position_18h}%;
    transform: translate(0%, 0%);
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
    top: 10%;
    left: {position_21h}%;
    transform: translate(0%, 0%);
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 21h"}
  </div>

  <!-- 23h -->
  <div style="
    position: absolute;
    top: 10%;
    left: {position_23h}%;
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 23h"}
  </div>

<p style="color:#b141ffff;">.</p>
"""
#<p style="color:#b141ffff;">{pct_day:.3f}% du jour</p>

# ____ Titre au format html
titre = f"{jour_nom} | {heure_actuelle}"
st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:4px;'>{titre}</h3>",
    unsafe_allow_html=True
)

# _____ Affiche le contenu de la barre (issu du code html plus haut)
st.markdown(bar_day, unsafe_allow_html=True)

#st.text(" ----------")



# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) BARRE PERSONNALISÉE
# --------------------------------------------------------------------------------------------------------------------------------------------------------



start = datetime.datetime(2026, 6, 17, 4, 30, 0, tzinfo=TZ)
end   = datetime.datetime(2026, 7, 18, 21, 30, 0, tzinfo=TZ)

now = datetime.datetime.now(ZoneInfo("Europe/Paris"))
total = (end - start).total_seconds()
elapsed = (now - start).total_seconds()
pct_barre1 = min(max(elapsed / total, 0), 1) * 100  # 0–100 float


# __________ Code barre html

bar_1 = f"""
<div style="position: relative; width: 100%; background-color: #B6D8F2; border-radius: 8px; height: 5px;">

  <div style="
    width: {pct_barre1}%;
    height: 100%;
    background: #5784BA;
    border-radius: 6px;
  "></div>
</div>


<!-- flèche -->
<img src="https://cdn-icons-png.flaticon.com/128/4238/4238526.png"
  style="
    position: absolute;
    top: -155%;
    left: {pct_barre1}%;
    transform: translate(-90%, 0%);
    height: 20px;
    pointer-events: none;
  ">

<!-- 1/4 -->
<img src="https://cdn-icons-png.flaticon.com/128/5582/5582272.png"
  style="
    position: absolute;
    top: 180%;
    left: 25%;
    transform: translate(-50%, 0%);
    height: 20px;
    pointer-events: none;
  ">

<!-- 1/2 -->
<img src="https://cdn-icons-png.flaticon.com/128/5582/5582264.png"
  style="
    position: absolute;
    top: 180%;
    left: 50%;
    transform: translate(-50%, 0%);
    height: 20px;
    pointer-events: none;
  ">


<!-- 3/4 -->
<img src="https://cdn-icons-png.flaticon.com/128/5582/5582259.png"
  style="
    position: absolute;
    top: 180%;
    left: 75%;
    transform: translate(-50%, 0%);
    height: 20px;
    pointer-events: none;
  ">

  <!-- 90% -->
  <div style="
    position: absolute;
    top: 100%;
    left: 90%;
    color: black;
    font-weight: normal;
    font-size: 14px;
    pointer-events: none;
  ">
    {"| 90%"}
  </div>

"""


# ____ Titre au format html
titre = f"Barre personelle | {pct_barre1:.2f}%"
st.markdown(
    f"<h3 style='font-size:20px; font-weight:600; margin-bottom:4px;'>{titre}</h3>",
    unsafe_allow_html=True
)

# _____ Affiche le contenu de la barre (issu du code html plus haut)
st.markdown(bar_1, unsafe_allow_html=True)


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1) CHANGEMENT AUTOMATIQUE DE PAGES
# --------------------------------------------------------------------------------------------------------------------------------------------------------



time.sleep(15)  # délai en secondes

st.switch_page("pages/weather.py")




