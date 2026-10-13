import sys
import os

# src klasörünü Python yoluna ekle
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_fetcher import fetch_weather_data
from data_processor import process_weather_data
from predictor import train_wind_predictor
from optimizer import optimize_pumping_schedule

def run_pipeline():
    print("==================================================")
    print("   ÇAN-SU: Akıllı Su ve Enerji Yönetim Sistemi   ")
    print("==================================================\n")
    
    # 1. Adım: Veri Çekme
    print("[1/4] Hava Durumu ve Rüzgâr Verileri Çekiliyor...")
    weather_df = fetch_weather_data()
    if weather_df is None:
        print("✗ Veri çekme başarısız oldu!")
        return
    print()

    # 2. Adım: Veri İşleme
    print("[2/4] Rüzgâr Gücü ve Verimlilik Hesaplamaları Yapılıyor...")
    processed_df = process_weather_data()
    if processed_df is None:
        print("✗ Veri işleme başarısız oldu!")
        return
    print()

    # 3. Adım: Makine Öğrenmesi Tahmini
    print("[3/4] Rüzgâr Hızı Tahmin Modeli Eğitiliyor...")
    model = train_wind_predictor()
    print()

    # 4. Adım: Optimizasyon Takvimi
    print("[4/4] Pompa Çalışma Takvimi Oluşturuluyor...")
    schedule_df = optimize_pumping_schedule()
    print()

    print("==================================================")
    print("✓ Tüm süreç başarıyla tamamlandı!")
    print("  Çıktılar 'data/processed/' konumuna kaydedildi.")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()