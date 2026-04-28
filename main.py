import requests
import pandas as pd
from datetime import datetime
import os

# Súradnice pre Trnavu
URL = "https://archive-api.open-meteo.com/v1/era5?latitude=48.3774&longitude=17.5833&start_date=2026-04-27&end_date=2026-04-27&hourly=temperature_2m,precipitation"

def fetch_data():
    response = requests.get(URL).json()
    # Berieme posledný záznam z dát
    return {
        'Cas': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Teplota_C': response['hourly']['temperature_2m'][-1],
        'Zrazky_mm': response['hourly']['precipitation'][-1]
    }

# Čítanie existujúceho CSV a pridanie nového riadku
new_data = fetch_data()
df = pd.read_csv('data.csv')
df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
df.to_csv('data.csv', index=False)
