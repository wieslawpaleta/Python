import sqlite3
import pandas as pd
from datetime import datetime

# Initialize SQLite database connection (Inicjalizacja połączenia z bazą danych SQlite)
conn = sqlite3.connect("bike_sharing.db")
cursor = conn.cursor()

# Creating table for raw bike data (Tworzenie tabeli dla surowych danych o rowerach)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS raw_rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station_id TEXT,
        timestamp TEXT,
        available_bikes INTEGER,
        temperature REAL,
        weather_condition TEXT
    )
"""
)
conn.commit()

sample_date = [
    ("station_A", "2026-10-20 08:00:00", 5, 12.5, "Cloudy"),
    ("station_A", "2026-10-20 08:30:00", 2, 13.0, "Sunny"),
    ("station_B", "2026-10-20 08:00:00", 12, 12.5, "Cloudy"),
    ("station_B", "2026-10-20 08:30:00", 9, 13.0, "Sunny"),
]

# Inserting data into the raw table (Wstawianie danych do tabeli surowej)
cursor.executemany(
    """
    INSERT INTO raw_rides (station_id, timestamp, available_bikes, temperature, weather_condition)
    VALUES (?, ?, ?, ?, ?)
""",
    sample_date
)
conn.commit()

# Verification of insertion with pandas (Weryfikacja wstawiania za pomocą pandas)
df_check = pd.read_sql("SELECT * FROM raw_rides", conn)
print("Raw Data Loaded Successfully (Surowe dane zostały pomyślnie załadowane):")
print(df_check.head())

# Closing database connection (Zamykanie połączenia z bazą danych)
conn.close()