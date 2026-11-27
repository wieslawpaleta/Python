# Volcano Activity & Proximity Analyzer Map <!-- Main title of your GitHub repository (Główny tytuł Twojego repozytorium na GitHubie) -->

A Python data-engineering and geospatial analysis tool that fetches live volcano activity data, computes statistical alert anomalies and nearest-neighbor distances, and renders an interactive HTML world map—packaged with Docker for reproducible execution. <!-- Short one-sentence pitch summarizing what the project does (Krótkie jednozdaniowe podsumowanie, co robi projekt) -->

## Features <!-- Section header listing key project features (Nagłówek sekcji z głównymi funkcjami projektu) -->

- **Live API Ingestion with Resilience:** Fetches volcano coordinates and alert levels from the USGS Volcano API (`requests`) with an automatic built-in fallback dataset for offline or degraded network conditions. <!-- Bullet explaining API fetching and fallback handling (Punkt wyjaśniający pobieranie danych z API i zabezpieczenie zapasowe) -->
- **Numerical & Statistical Analysis (`NumPy`):** Computes mean alert levels, standard deviation, and standardized alert `z-scores` to highlight elevated volcanic activity. <!-- Bullet explaining NumPy statistical calculations (Punkt wyjaśniający obliczenia statystyczne w NumPy) -->
- **Spatial Nearest-Neighbor Search (`SciPy`):** Uses `scipy.spatial.cKDTree` to efficiently query the closest neighboring volcano for every site. <!-- Bullet explaining SciPy spatial tree lookup (Punkt wyjaśniający wyszukiwanie sąsiadów przez SciPy) -->
- **Interactive GeoJSON Map (`Folium`):** Generates a self-contained `volcano_map.html` with country boundaries, color-coded alert markers, metric popups, and dashed nearest-neighbor vectors—without relying on blocked external tile servers. <!-- Bullet explaining Folium + GeoJSON map output (Punkt wyjaśniający generowanie mapy Folium + GeoJSON) -->
- **Containerized Workflow (`Docker`):** Runs identically on any machine via a lightweight `python:3.12-slim` image. <!-- Bullet explaining Docker portability (Punkt wyjaśniający przenośność dzięki Dockerowi) -->

## Tech Stack <!-- Section header for technologies used (Nagłówek sekcji z użytymi technologiami) -->

- **Language:** Python 3.12 <!-- Specify Python version (Określa wersję Pythona) -->
- **Scientific & Data Libraries:** NumPy, SciPy, Requests <!-- List math and HTTP libraries (Wymienia biblioteki matematyczne i HTTP) -->
- **Visualization:** Folium (Leaflet.js + GeoJSON) <!-- List mapping library (Wymienia bibliotekę do wizualizacji mapy) -->
- **Containerization:** Docker <!-- List container runtime (Wymienia narzędzie do konteneryzacji) -->

## Project Structure <!-- Section header showing files in the repository (Nagłówek sekcji pokazującej pliki w repozytorium) -->

```text <!-- Start a plain-text code block for the folder tree (Rozpoczyna blok tekstu dla drzewa folderów) -->
. <!-- Root directory of the project (Główny folder projektu) -->
├── app.py              # Main ETL, NumPy/SciPy analysis, and map generator script (Główny skrypt ETL, analizy NumPy/SciPy i generatora mapy)
├── requirements.txt    # Pinned Python dependencies (Zależności Pythona do zainstalowania)
├── Dockerfile          # Container build instructions (Instrukcje budowania kontenera)
├── README.md           # Project documentation (Dokumentacja projektu)
└── volcano_map.html    # Generated interactive map output (Wygenerowany plik wyjściowy z interaktywną mapą)
``` <!-- End the folder tree code block (Zamyka blok drzewa folderów) -->

## Quick Start with Docker (Recommended) <!-- Section header for running via Docker (Nagłówek sekcji uruchamiania przez Dockera) -->

1. **Build the Docker image:** <!-- Step 1 instruction (Instrukcja kroku 1) -->
   ```bash <!-- Start a bash