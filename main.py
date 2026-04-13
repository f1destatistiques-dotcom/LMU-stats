import streamlit as st


import os
import xml.etree.ElementTree as ET
import csv
import glob


folder = "xmls"
for file in os.listdir(xml_folder):
    if file.endswith(".xml"):
        path = os.path.join(folder, file)
        with open(path) as f:
            contenu = f.read()

# -------------------------------------------------------------------
# 4) Lecture des fichiers XML
# -------------------------------------------------------------------

files = glob.glob(folder + "/*.xml") + glob.glob(folder + "/*.txt")

for path in files:

    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except ET.ParseError:
        print("⚠️ Fichier XML illisible, ignoré :", path)
        continue

    # Trouver TON pilote
    driver = root.find(".//Driver[Name='Ramco ESS']")
    if driver is None:
        continue

    track = root.findtext(".//TrackCourse")
    version = root.findtext(".//GameVersion")
    car = driver.findtext(".//CarType")
    best_lap = driver.findtext(".//BestLapTime")

    if not (track and car and version and best_lap):
        continue
    if best_lap == "--.----":
        continue

    lap_sec = float(best_lap)

    # initialisation
    if track not in records:
        records[track] = {}
    if car not in records[track]:
        records[track][car] = {}

    # mise à jour du record par version
    if version not in records[track][car] or lap_sec < records[track][car][version]["time"]:
        records[track][car][version] = {
            "time": lap_sec,
            "file": os.path.basename(path)
        }



print("Records mis à jour dans records.csv")

st.title("Hi everyone, i'm one the place")
st.header("Ici un header")
st.subheader("subheader")

for track, cars in records.items():
    for car, versions in cars.items():
        for version, data in versions.items():
            st.text(track + " - " + car + " - " + format_lap_time(data["time"]))

st.markdown("---")

st.text("Test d'un nouveau test ici en direct 2")
