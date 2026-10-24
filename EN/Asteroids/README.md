# Near-Earth Object ETL Pipeline & Hazard Predictor
## Project Overview
This project bridges **Data Engineering** and **Data Science**:
1. **ETL Pipeline (Data Engineering):** Connects to NASA's NeoWs (Near Earth Object Web Service) API, extracts raw JSON data, parses key metrics, and loads it into a persistent SQLite database (`database.py` & `main.py`).
2. **Exploratory Data Analysis & ML (Data Science):** Utilizes Pandas to query the database and trains a **Random Forest Classifier** using Scikit-Learn to predict whether an incoming asteroid is potentially hazardous (`analysis.py`).
3. **Data Visualization:** Generates a professional scatter plot using Seaborn and Matplotlib illustrating the relationship between asteroid size, velocity, and hazard status (`visualize.py`).

---

## Tech Stack
* **Language:** Python 3.x
* **Data Engineering & ETL:** `requests`, `sqlite3`
* **Data Analysis & ML:** `pandas`, `scikit-learn`
* **Data Visualization:** `matplotlib`, `seaborn`
* **API:** NASA Near Earth Object Web Service 

---

## Project Structure
```text
Asteroids/
│
├── main.py          # Orchestrates the ETL pipeline and fetches data from NASA API
├── database.py      # Handles SQLite database creation and data insertion
├── analysis.py      # Loads data into Pandas, performs EDA, and trains ML model
├── visualize.py     # Creates data visualizations using Seaborn and Matplotlib
└── neo_database.db  # SQLite database (generated automatically upon running)