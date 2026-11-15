import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train_wind_predictor():
    processed_path = "data/processed/can_weather_processed.csv"
    
    if not os.path.exists(processed_path):
        print(f"✗ İşlenmiş veri bulunamadı: {processed_path}")
        return None

    df = pd.read_csv(processed_path)
    df['time'] = pd.to_datetime(df['time'])

    df['hour'] = df['time'].dt.hour
    df['dayofweek'] = df['time'].dt.dayofweek

  
    df['wind_speed_lag1'] = df['wind_speed_100m'].shift(1)
    df['wind_speed_lag2'] = df['wind_speed_100m'].shift(2)

   
    df = df.dropna().reset_index(drop=True)

    
    features = ['hour', 'dayofweek', 'temperature_2m', 'wind_speed_lag1', 'wind_speed_lag2']
    X = df[features]
    y = df['wind_speed_100m']

  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print("✓ Makine Öğrenmesi Tahmin Modeli Başarıyla Eğitildi!")
    print(f"  - Model Performansı (RMSE): {rmse:.2f} m/s")
    print(f"  - Doğruluk Skoru (R²): {r2:.2f}")

    results = y_test.to_frame(name='Gercek_Ruzgar_Hizi')
    results['Tahmin_Ruzgar_Hizi'] = y_pred
    print("\nÖrnek Tahmin Sonuçları (İlk 5 Satır):")
    print(results.head())

    return model

if __name__ == "__main__":
    train_wind_predictor()
