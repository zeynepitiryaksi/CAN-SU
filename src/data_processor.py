import os
import pandas as pd
import numpy as np

def process_weather_data():
    raw_path = "data/raw/can_weather_raw.csv"
    processed_path = "data/processed/can_weather_processed.csv"
    
    if not os.path.exists(raw_path):
        print(f"✗ Ham veri bulunamadı: {raw_path}")
        return None
    
    df = pd.read_csv(raw_path)
    
 
    df['time'] = pd.to_datetime(df['time'])
    
    
    AIR_DENSITY = 1.225  
    df['wind_power_density_100m'] = 0.5 * AIR_DENSITY * (df['wind_speed_100m'] ** 3)
    

    max_power = df['wind_power_density_100m'].max()
    if max_power > 0:
        df['pump_efficiency_score'] = (df['wind_power_density_100m'] / max_power) * 100
    else:
        df['pump_efficiency_score'] = 0


    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(processed_path, index=False)
    
    print(f"✓ Veri işlendi ve '{processed_path}' konumuna kaydedildi.")
    print("\nİşlenmiş Veriden İlk 5 Satır:")
    print(df[['time', 'wind_speed_100m', 'wind_power_density_100m', 'pump_efficiency_score']].head())
    
    return df

if __name__ == "__main__":
    process_weather_data()
