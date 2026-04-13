import streamlit as st

import os
import xml.etree.ElementTree as ET
import csv
import glob

records_file = "/home/zoubair/Documents/Projets Python/Premier programme/records.csv"
folder = "/home/zoubair/Documents/Projets Python/Premier programme/xmls"

# -------------------------------------------------------------------
# 1) Fonction pour convertir "M:SS.mmm" → secondes (pour relire le CSV)
# -------------------------------------------------------------------
def parse_lap_time(formatted):
    minutes, rest = formatted.split(":")
    return int(minutes) * 60 + float(rest)

# -------------------------------------------------------------------
# 2) Fonction pour convertir secondes → "M:SS.mmm" (pour écrire le CSV)
# -------------------------------------------------------------------
def format_lap_time(seconds):
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:06.3f}"

# -------------------------------------------------------------------
# 3) Lecture du CSV existant (robuste)
# -------------------------------------------------------------------
records = {}   # structure : records[track][car][version] = {time, file}

if os.path.exists(records_file):
    with open(records_file, newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header

        for row in reader:
            # ignorer lignes vides ou incomplètes
            if len(row) < 5:
                continue

            track = row[0]
            car = row[1]
            version = row[2]
            best = row[3]
            source = row[4]

            # initialisation
            if track not in records:
                records[track] = {}
            if car not in records[track]:
                records[track][car] = {}

            # convertir le temps formaté vers secondes
            lap_sec = parse_lap_time(best)

            records[track][car][version] = {
                "time": lap_sec,
                "file": source
            }

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

# -------------------------------------------------------------------
# 5) Écriture du CSV final
# -------------------------------------------------------------------

with open(records_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Circuit", "Voiture", "Version", "Record", "Fichier source"])

    for track, cars in records.items():
        for car, versions in cars.items():
            for version, data in versions.items():
                writer.writerow([
                    track,
                    car,
                    version,
                    format_lap_time(data["time"]),
                    data["file"]
                ])

print("Records mis à jour dans records.csv")



st.title("Hi everyone, i'm one the place")
st.header("Ici un header")
st.subheader("subheader")

for track, cars in records.items():
    for car, versions in cars.items():
        for version, data in versions.items():
            st.text(track + " - " + car + " - " + format_lap_time(data["time"]))




st.markdown("---")