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
    query = "SELECT * FROM asteroids"
    df = pd.read_sql(query, conn)
    
    conn.close()
    return df

# Main execution for Data Science part (Główna egzekucja dla części Data Science)
if __name__ == "__main__":
    df = load_data_from_db()

    # Print basic information about the dataset (Wypisz podstawowe informacje o zbiorze danych)
    print(f"Dataset shape: {df.shape} (Kształt zbioru danych)")
    print("\nFirst 3 rows of data (Pierwsze 3 wiersze danych):")
    print(df.head(3))

    # Defining features (X) and target variable (y) (Definiowanie cech (X) i zmienną docelową (y))
    features = ['absolute_magnitude', 'estimated_diameter_min_km', 'estimated_diameter_max_km', 'miss_distance_km', 'relative_velocity_kps']
    target = 'is_hazardous'
    
    X = df[features]
    y = df[target]

    # Checking class distribution (Sprawdzanie rozkładu klasy)
    print(f"\nHazardous class distribution:\n{y.value_counts()} (Rozkład klas zagrożenia)")

    # Since small datasets might have all 0s for hazardous, we handle split safely (Ponieważ małe zbiory mogą mieć same zera dla niebezpiecznych, obsługujemy podział bezpiecznie)
    if y.nunique() > 1:
        # Spliting data into training and testing sets (Dzielenie danych na zbiory treningowy i testowy)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initializing and train Random Forest model (Inicjowanie i trenowanie modelu Random Forest)
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Making predictions (Wykonywanie predykcji)
        predictions = model.predict(X_test)

        # Evaluating model (Ocenianie modelu)
        print(f"\nModel Accuracy: {accuracy_score(y_test, predictions):.2f} (Dokładność modelu)")
    else:
        print("\nNote: Current date range has only non-hazardous asteroids, so ML training is skipped for this batch. (Uwaga: Bieżący zakres dat ma tylko niezagrożone asteroidy, więc trening ML dla tej paczki jest pomijany.)")