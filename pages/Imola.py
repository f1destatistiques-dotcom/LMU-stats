
import streamlit as st

#st.set_page_config(layout="wide") # Permet un affichage en plein écran


# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd
url_record_data = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/records.csv"
df_record_data = pd.read_csv(url_record_data)

url_lap_by_circuit = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/laps_by_circuit.csv"
df_lap_by_circuit = pd.read_csv(url_lap_by_circuit, encoding="latin-1")


TRACK = "Imola"


with st.container(border=True):
    st.image('Track - Imola.png', width=600, use_container_width=True)

    # st.dataframe(filtered) # Affichage sous forme de tableau

    # CHOIX DES ICONES POUR LES TUILES
    icons = {
        "Nombre de courses en multi": "🏁",
        "Nombre de tours": "🕓",
        "Nombre de victoires": "🏆",
        "Nombre de podium": "🥉",
        "Nombre de TOP5": "5️⃣",
        "Nombre de TOP10": "🔟",
        "Nombre de poles": "🎯",
        "Position moyenne en course": "🚥",
        "Position moyenne en qualif.": "🛞",
        "Nombre de DNF" : "🏴"
    }

    #for _, row in filtered.iterrows():
        #st.metric(label=row["Data"], value=row["Value"]) # Affichage dans une tuile simple

    filtered = df_lap_by_circuit[df_lap_by_circuit["Track"] == TRACK]

    cols = st.columns(3)
    filtered = filtered.reset_index(drop=True)  # <<< Permet de forcer d'afficher la première tuile à gauche

    for i, row in filtered.iterrows():
        label = row["Data"]
        value = row["Value"]
        icon = icons.get(label, "❓")

        col = cols[i % 3]  # 0,1,2 puis 0,1,2...
        #col = st.columns(cols)

        with col:
            st.markdown(f"""
                <div style="
                    background-color:#EEE6D8;
                    padding:5px;
                    border-radius:12px;
                    text-align:center;
                    color:black;
                    width:100%;
                    margin-bottom:20px;">
                    <div style="font-size:40px; margin-bottom:10px;">{icon}</div>
                    <div style="font-size:14px; opacity:0.7;">{label}</div>
                    <div style="font-size:32px; font-weight:700; margin-top:1px;">{value}</div>
                </div>
            """, unsafe_allow_html=True)



# AFFICHAGE POUR LA SECTION GT3___________________________________________________________________________________________________________
colonnes_a_afficher = ["Voiture", "Record", "Version"]
CATEGORIE = "GT3"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - GT3.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)


# AFFICHAGE POUR LA SECTION GTE___________________________________________________________________________________________________________

CATEGORIE = "GTE"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - GTE.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)


# AFFICHAGE POUR LA SECTION LMP3___________________________________________________________________________________________________________

CATEGORIE = "LMP3"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - P3.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)


    # AFFICHAGE POUR LA SECTION LMP2___________________________________________________________________________________________________________

CATEGORIE = "LMP2"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - P2.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)


    # AFFICHAGE POUR LA SECTION LMP2 - ELMS___________________________________________________________________________________________________________

CATEGORIE = "LMP2_ELMS"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - P2 ELMS.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)


# AFFICHAGE POUR LA SECTION HY___________________________________________________________________________________________________________

CATEGORIE = "Hypercar"
CIRCUIT = TRACK


with st.container(border=True):
    st.image('CAT - HY.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT) & (df_record_data["Record"] != "0:00.000")].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)
