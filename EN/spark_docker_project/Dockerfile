# [EN] Use official Python image with Debian base
# [PL] (Użyj oficjalnego obrazu Pythona z bazą Debian)
FROM python:3.10-slim

# [EN] Install Java required for Apache Spark execution
# [PL] (Zainstaluj Javę wymaganą do uruchomienia Apache Spark)
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean;

# [EN] Set working directory inside container
# [PL] (Ustaw katalog roboczy wewnątrz kontenera)
WORKDIR /app

# [EN] Install required Python packages for data processing and linear algebra
# [PL] (Zainstaluj wymagane pakiety Pythona do przetwarzania danych i algebry liniowej)
RUN pip install --no-cache-dir pyspark numpy pandas

# [EN] Copy project files into container
# [PL] (Skopiuj pliki projektu do kontenera)
COPY . /app

# [EN] Default command to run script inside container
# [PL] (Domyślne polecenie uruchamiające skrypt wewnątrz kontenera)
CMD ["python", "spark_matrix_engine.py"]