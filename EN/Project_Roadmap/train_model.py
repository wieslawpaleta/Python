import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Connecting to the SQLite database (Łączenie się z bazą danych SQLite)
conn = sqlite3.connect("bike_sharing.db")

# Loading procesessed data into a DataFrame (Ładowanie przetworzonych danych do DataFrame)
query = "SELECT * FROM processed_rides"
df = pd.read_sql(query, conn)
conn.close()

# Preparing features (X) and target variable (y) (Przygotowanie cechy (X) 
#                                                   i zmienną docelową (y))
# Using hour, temperature, and encoded categorical features (Użycie godziny, temperatury 
#                                                           i zakodowanych cech kategorycznych )
df_encoded = pd.get_dummies(df, columns=["day_of_week", "weather_condition"], drop_first=True)

X = df_encoded.drop(columns=["id", "timestamp", "station_id", "available_bikes"])
y = df_encoded["available_bikes"]

# Spliting data into training and testing sets (Dzielenie danych na zbiory treningowe i testowy)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the Machine Learning model (Inicjowanie i trenowanie modelu uczenia maszynowego)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Making predictions on the test set (Wykonywanie przewidywań na zbiorze testowym)
y_pred = model.predict(X_test)

# Evaluating model performance (Ocenianie wydajności modelu)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Training Completed Successfully! (Trenowanie modelu zakończone pomyślnie!)")
print(f"Mean Absolute Error (Średni błąd bezwzględny - MAE): {mae:.2f}")
print(f"R2 Score (Wynik R2): {r2:.2f}")