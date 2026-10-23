import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data from SQLite database (Funkcja do wczytywania danych z bazy danych SQLite)
def load_data():
    conn = sqlite3.connect("neo_database.db")
    query = "SELECT * FROM asteroids"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to plot asteroid velocity vs diameter (Funkcja do wykreślenia prędkości asteroidy w stosunku do średnicy)
def plot_asteroids(df):
    #Setting the aesthetic style of the plots (Ustawianie estetycznego stylu wykresów)
    sns.set_theme(style="darkgrid")

    #Creating a readable label column to ensure correct legend colours (Tworzenie czytelnej kolumny etykiet, aby zapewnić poprawny kolory legendy)
    df['hazard_label'] = df['is_hazardous'].map({0: 'No (Nie)', 1: 'Yes (Tak)'})

    plt.figure(figsize=(10, 6))

    # Creating a scatter plot: X = diameter, Y = velocity, color = hazardous (Tworzenie wykresu punktowego: X = średnica, Y = prędkość, kolor = niebezpieczna)
    sns.scatterplot(
        data=df,
        x='estimated_diameter_max_km',
        y='relative_velocity_kps',
        hue='hazard_label',
        palette={'No (Nie)': 'blue', 'Yes (Tak)': 'red'},
        s=100,
        alpha=0.7
    )

    # Adding titles and labels (Dodawanie tytułów i etykiet)
    plt.title('Asteroid Size vs Relative Velocity (Rozmiar asteroidy a prędkość względna)', fontsize=14)
    plt.xlabel('Max Estimated Diameter (km) (Maksymalna szacowana średnica (km))', fontsize=12)
    plt.ylabel('Relative Velocity (km/s) (Prędkość względna (km/s))', fontsize=12)

    # Customizing Legend (Dostosowywanie legendy)
    plt.legend(title='Hazardous (Niebezpieczna)')

    # Show the plot (Pokaż wykres)
    plt.show()

# Main execution for visualization (Główna egzekucja dla wizualizacji)
if __name__ == "__main__":
    df = load_data()
    if not df.empty:
        print(f"Loaded {len(df)} records for visualization. (Wczytano {len(df)} rekordów do wizualizacji.)")
        plot_asteroids(df)
    else:
        print("No data found in database. (Nie znaleziono danych w bazie danych.)")