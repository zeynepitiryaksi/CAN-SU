import os
import requests
import pandas as pd

# Çanakkale / Çan koordinatları
LATITUDE = 39.95
LONGITUDE = 26.97

def fetch_weather_data():
    """
    Open-Meteo API'sinden Çanakkale/Çan için rüzgâr ve iklim verilerini çeker.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m",
            "wind_speed_100m",
            "wind_direction_10m"
        ],
        "timezone": "Europe/Istanbul"
    }

    print("Veri çekiliyor: Open-Meteo API...")
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        hourly_data = data.get("hourly", {})
        
        df = pd.DataFrame(hourly_data)
        
        # Raw klasörüne kaydet
        os.makedirs("data/raw", exist_ok=True)
        output_path = "data/raw/can_weather_raw.csv"
        df.to_csv(output_path, index=False)
        
        print(f"✓ Veri başarıyla çekildi ve '{output_path}' konumuna kaydedildi.")
        print("\nÇekilen Veriden İlk 5 Satır:")
        print(df.head())
        return df
    else:
        print(f"✗ Veri çekme başarısız! Hata Kodu: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_weather_data()