# Smart City Bike-Sharing Demand Prediction System

## Overview / Przegląd
This project is an end-to-end Data Engineering and Machine Learning portfolio project. It simulates a smart city bike-sharing infrastructure, ingesting raw operational data, processing it through an SQLite database pipeline, and training a machine learning model to predict bike availability.

## Project Architecture / Architektura Projektu
1. **Ingestion (`ingest.py`):** Simulates a data stream and loads raw data into a relational database (`bike_sharing.db`).
2. **Transformation (`transform.py`):** Extracts raw records, performs data cleaning, extracts temporal features (hour, day of week), and stores processed data back into the database.
3. **Machine Learning (`train_model.py`):** Trains a `RandomForestRegressor` using `scikit-learn` to predict available bike counts based on environmental and temporal features.

## Tech Stack / Stos Technologiczny
* **Python**
* **Pandas & NumPy** (Data Manipulation / Manipulacja danymi)
* **SQLite** (Database / Baza danych)
* **Scikit-Learn** (Machine Learning)

## How to Run / Jak Uruchomić
Execute the scripts sequentially in your terminal:
```bash
python ingest.py
python transform.py
python train_model.py