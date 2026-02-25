#!/usr/bin/env python3
"""
gandhi-weather-accu.py - AccuWeather-only analyzer (no AQI).
Temperature (°C highs) and humidity (%) for Gandhinagar last 10 days.
"""
import statistics

temps_accu = [34, 34, 35, 35, 36, 35, 34, 34, 35, 36]  # Highs
humidities_accu = [45, 48, 52, 50, 47, 44, 42, 40, 38, 35]  # % averages

def stats(data, label):
    print(f"{label}: Avg={statistics.mean(data):.1f}, Median={statistics.median(data):.1f}")

if __name__ == "__main__":
    print("Gandhinagar Weather (AccuWeather, Feb 16-25)")
    stats(temps_accu, "Temperature (°C)")
    stats(humidities_accu, "Humidity (%)")
