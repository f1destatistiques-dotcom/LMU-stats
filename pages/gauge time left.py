import streamlit as st
from streamlit_echarts import st_echarts
from datetime import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Paris")

# ---------------------------------------------------------
# 1) Fonction : calcul du palier + couleur + label
# ---------------------------------------------------------
def compute_paliers(end):
    now = datetime.now(TZ)
    remaining_seconds = (end - now).total_seconds()

    remaining_days_total = remaining_seconds / 86400
    remaining_months = remaining_days_total / 30
    remaining_hours = remaining_seconds / 3600

    months_remaining_int = int(remaining_days_total // 30)
    days_remaining_int = int(remaining_days_total % 30)

    if remaining_months > 9:
        return {"min": 9, "max": 12, "value": remaining_months,
                "label": f"{months_remaining_int} mois {days_remaining_int} j",
                "color": "#E10600"}
    elif remaining_months > 6:
        return {"min": 6, "max": 9, "value": remaining_months,
                "label": f"{months_remaining_int} mois {days_remaining_int} j",
                "color": "#F27438"}
    elif remaining_months > 3:
        return {"min": 3, "max": 6, "value": remaining_months,
                "label": f"{months_remaining_int} mois {days_remaining_int} j",
                "color": "#F2C038"}
    elif remaining_months > 1:
        return {"min": 1, "max": 3, "value": remaining_months,
                "label": f"{months_remaining_int} mois {days_remaining_int} j",
                "color": "#4CAF50"}
    elif remaining_days_total > 1:
        return {"min": 1, "max": 30, "value": remaining_days_total,
                "label": f"{int(remaining_days_total)} jours",
                "color": "#2196F3"}
    else:
        return {"min": 0, "max": 24, "value": remaining_hours,
                "label": f"{int(remaining_hours)} h",
                "color": "#9C27B0"}


# ---------------------------------------------------------
# 2) Fonction : construction d'une jauge ECharts
# ---------------------------------------------------------
def build_gauge(end_date):
    cfg = compute_paliers(end_date)

    options = {
        "series": [
            {
                "type": "gauge",
                "min": cfg["min"],
                "max": cfg["max"],


                "progress": {
                    "show": True,
                    "width": 8,
                    "itemStyle": {
                        "color": cfg["color"],
                    },
                },

                "axisLine": {"lineStyle": {"width": 8}},
                "axisTick": {"show": True},
                "splitLine": {"length": 5, "lineStyle": {"width": 2, "color": cfg["color"]}},
                "axisLabel": {"distance": 15, "color": cfg["color"], "fontSize": 10},

                "anchor": {
                    "show": True,
                    "showAbove": True,
                    "size": 15,
                    "color": cfg["color"],
                    "itemStyle": {"borderWidth": 5},
                },

                "title": {"show": False},
                "detail": {
                    "valueAnimation": True,
                    "fontSize": 15,
                    "offsetCenter": [0, "30%"],
                    "formatter": cfg["label"],
                },

                "data": [{"value": cfg["value"]}],
            }
        ]
    }

    return options


# ---------------------------------------------------------
# 3) Définition des jauges : (nom, date)
# ---------------------------------------------------------

gauges = [
    ("Clés", datetime(2026, 8, 12, 11, 0, tzinfo=TZ)),
    ("Automne 🍁", datetime(2026, 9, 21, 0, 0, tzinfo=TZ)),
    ("Hiver ⛄", datetime(2026, 12, 21, 0, 0, tzinfo=TZ)),
    ("Ra", datetime(2027, 2, 8, 0, 0, tzinfo=TZ)),
]

# ---------------------------------------------------------
# 4) Affichage : 4 jauges par ligne
# ---------------------------------------------------------

st.markdown("""
<style>
.echarts-container {
    margin-bottom: -20px !important;  /* Réduit l'espace sous la jauge */
}
.gauge-title {
    text-align: center;
    font-size: 18px;
    margin-top: -100px;               /* Remonte le titre */
}
</style>
""", unsafe_allow_html=True)



for i in range(0, len(gauges), 4):
    row = gauges[i:i+4]
    cols = st.columns(len(row))

    for col, (name, end_date) in zip(cols, row):
        with col:
            options = build_gauge(end_date)
            st_echarts(options, height="350px")
            st.markdown(f"<div class='gauge-title'>{name}</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# 5) Légende unique
# ---------------------------------------------------------
st.markdown("""
### Légende des paliers
🟥 **> 9 mois**  
🟧 **> 6 mois**  
🟨 **> 3 mois**  
🟩 **> 1 mois**  
🟦 **30 derniers jours**  
🟪 **24 dernières heures**
""")
