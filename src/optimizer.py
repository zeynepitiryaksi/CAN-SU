import os
import pandas as pd

def optimize_pumping_schedule():
    processed_path = "data/processed/can_weather_processed.csv"
    output_path = "data/processed/pumping_schedule.csv"
    
    if not os.path.exists(processed_path):
        print(f"✗ İşlenmiş veri bulunamadı: {processed_path}")
        return None
        
    df = pd.read_csv(processed_path)
    
    # Optimizasyon Mantığı:
    # Pompa Verimlilik Skoru > 25 olan saatlerde pompaları tam kapasite (%100) çalıştır
    # 10 - 25 arası olan saatlerde yarım kapasite (%50) çalıştır
    # < 10 olan saatlerde şebeke elektriği harcamamak için pompaları KAPAT (%0)
    
    def calculate_action(score):
        if score >= 25:
            return "AÇIK (%100 - Maksimum Rüzgâr Enerjisi)"
        elif score >= 10:
            return "KISMİ (%50 - Orta Rüzgâr Enerjisi)"
        else:
            return "KAPALI (%0 - Şebeke Tasarrufu)"

    df['pump_status'] = df['pump_efficiency_score'].apply(calculate_action)
    
    # Sonuçları kaydet
    df.to_csv(output_path, index=False)
    
    print(f"✓ Optimizasyon tamamlandı ve çalışma takvimi '{output_path}' konumuna kaydedildi.")
    print("\nTavsiye Edilen Pompa Çalışma Takvimi (İlk 10 Saat):")
    print(df[['time', 'wind_speed_100m', 'pump_efficiency_score', 'pump_status']].head(10))
    
    return df

if __name__ == "__main__":
    optimize_pumping_schedule()