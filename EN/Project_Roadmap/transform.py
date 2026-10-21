import sqlite3
import pandas as pd

# Connecting to the SQLite database (Łączenie się z bazą danych SQLite)
conn = sqlite3.connect("bike_sharing.db")

# Loading raw data into a Pandas DataFrame (Ładowanie surowych danych do DataFrame biblioteki Pandas)
query = "SELECT * FROM raw_rides"
df = pd.read_sql(query, conn)

print("Raw DataFrame loaded (Załadowano surowy DataFrame):")
print(df.head())

# Converting timestamp string to datetime object (Konwertowanie tekstowego znacznika czasowego na obiekt datetime)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Feature Engineering: Extraction hour and day of week (Inżynieria cech: Wyodrębnienie godziny i dnia tygodnia)
df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.day_name()

# Handling missing values if any (Obsługiwanie brakujących wartości, jeśli jakieś są)
df = df.dropna()

# Saving the processed data into a new table for Machine Learning (Zapisywanie przetworzonych danych 
#                                                                   do nowej tabeli dla Uczenia Maszynowego)
df.to_sql("processed_rides", conn, if_exists="replace", index=False)

print("\nFeature Engineering completed successfully (Inżynieria cech zakończona pomyślnie):")
print(df[["station_id", "timestamp", "hour", "day_of_week", "available_bikes", "temperature"]])

# Closing the database connection (Zamykanie połączenia z bazą danych)
conn.close()