import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Function to load data from SQLite into a Pandas DataFrame (Funckja do wczytywanie danych z SQLite do DataFrame w Pandas)
def load_data_from_db():
    # Connect to SQLite database (Połącz z bazą banych SQLite)
    conn = sqlite3.connect("neo_database.db")

    # Reading SQL query into a pandas DataFrame (Wczytywanie zapytania SQL do DataFrame w pandas)
    query = "SELECT * from asteroids"
    df = pd.read_sql(query, conn)

    conn.close()
    return df

# Main execution for Data Science part (Główna egzekucja dla części Data Science)
if __name__ == "__main__":
    df = load_data_from_db()

    # Print basic information about the dataset (Wypisz podstawowe informacje o zbiorze danych)
    features = ['absolute_magnitude', 'estimated_diameter_min_km', 'estimated_diameter_max_km', 'miss_distance_km', 'relative_velocity_kps']
    target = 'is_hazardous'

    X = df[features]
    y = df[target]

    # Checking class distribution (Sprawdzanie rozkładu klasy)
    print(f"\Hazardous class distribution:\n{y.value_counts()} (Rozkład klas zagrożenia)")

    #Since small datasets might have all 0s for hazardous, we handle split safely (Ponieważ małe zbiory mogą mieć same zera dla niebezpiecznych, obsługujemy podział bezpiecznie)
    