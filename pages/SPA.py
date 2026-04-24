import streamlit as st

#st.set_page_config(layout="wide") # Permet un affichage en plein écran


# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd
url_record_data = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/records.csv"
df_record_data = pd.read_csv(url_record_data)

colonnes_a_afficher = ["Voiture", "Record", "Version"]

#st.image('Bacelone foncé.png', width=600, use_container_width=True)


# AFFICHAGE POUR LA SECTION GT3___________________________________________________________________________________________________________

CATEGORIE = "GT3"
CIRCUIT = "Spa-Francorchamps"


with st.container(border=True):
    #st.image('GT3.png', width=60)


    # Filtre statique
    df_filtered_gt3 = df_record_data[(df_record_data["Category"] ==  CATEGORIE) & (df_record_data["Circuit"] == CIRCUIT)].sort_values("Record")
    # AFFICHER TOUT LE TABLEAU CSV
    st.dataframe(df_filtered_gt3[colonnes_a_afficher], use_container_width=True, hide_index=True)
