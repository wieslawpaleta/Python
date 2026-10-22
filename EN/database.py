import sqlite3

# Function to create table and save
def save_asteroids_to_db(data):
    # Connecting to SQLite database (Łączenie z bazą danych SQLite)
    conn = sqlite3.connect("neo_database.db")
    cursor = conn.cursor()

    # Creating table if it doesn't exist (Tworzenie tabeli, jeśli nie istnieje)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asteroids (
            id TEXT PRIMARY KEY,
            name TEXT,
            absolute_magnitude REAL,
            estimated_diameter_min_km REAL,
            estimated_diameter_max_km REAL,
            is_hazardous INTEGER,
            close_approach_date TEXT,
            miss_distance_km REAL,
            relative_velocity_kps REAL
        )
    ''')
    
    inserted_count = 0
    neo_days = data.get('near_earth_objects', {})
    
    for date_str, asteroid_list in neo_days.items():
        for asteroid in asteroid_list:
            neo_id = asteroid.get('id')
            name = asteroid.get('name')
            abs_mag = asteroid.get('absolute_magnitude_h')
            
            diameter_data = asteroid.get('estimated_diameter', {}).get('kilometers', {})
            diam_min = diameter_data.get('estimated_diameter_min')
            diam_max = diameter_data.get('estimated_diameter_max')
            
            is_haz = 1 if asteroid.get('is_potentially_hazardous_asteroid') else 0
            
            approach_data = asteroid.get('close_approach_data', [{}])[0]
            approach_date = approach_data.get('close_approach_date')
            miss_distance = float(approach_data.get('miss_distance', {}).get('kilometers', 0))
            velocity = float(approach_data.get('relative_velocity', {}).get('kilometers_per_second', 0))
        # Inserting record into database, ignoring duplicates (Wstawianie rekordu do bazy danych, ignorując duplikaty)
        cursor.execute('''
            INSERT OR IGNORE INTO asteroids (
                    id, name, absolute_magnitude, estimated_diameter_min_km, 
                    estimated_diameter_max_km, is_hazardous, close_approach_date, 
                    miss_distance_km, relative_velocity_kps
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (neo_id, name, abs_mag, diam_min, diam_max, is_haz, approach_date, miss_distance, velocity))
            
        inserted_count += 1
            
    conn.commit()
    conn.close()
    print(f"Stored {inserted_count} records into SQLite database! (Zapisano {inserted_count} rekordów w bazie danych SQLite!)")
        