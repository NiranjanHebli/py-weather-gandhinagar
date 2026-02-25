#!/usr/bin/env python3
"""
gandhi-weather-full.py - AQI + AccuWeather analyzer.
Temperature (°C highs) and humidity (%) for Gandhinagar last 10 days.
"""
import statistics

temps_full = [34, 33, 33, 34, 36, 35, 34, 35, 35, 34]  # Highs blended
humidities_full = [35, 36, 34, 33, 30, 28, 32, 30, 25, 22]  # % AQI-influenced

def stats(data, label):
    print(f"{label}: Avg={statistics.mean(data):.1f}, Median={statistics.median(data):.1f}")

if __name__ == "__main__":
    print("Gandhinagar Weather (AQI+AccuWeather, Feb 16-25)")
    stats(temps_full, "Temperature (°C)")
    stats(humidities_full, "Humidity (%)")
