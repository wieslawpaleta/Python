import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import numpy as np
import pandas as pd

# [EN] Initialize Spark Session for distributed data processing
# [PL] (Inicjalizacja sesji Spark do rozproszonego przetwarzania danych)
spark = SparkSession.builder \
    .appName("GeospatialMatrixEngine") \
    .master("local[*]") \
    .getOrCreate()

# [EN] Defining schema for the geospatial dataset
# [PL] (Definiowanie schematu dla zbioru danych geosprzestrzennych)
schema = StructType([
    StructField("station_id", StringType(), True),
    StructField("latitude", DoubleType(), True),
    StructField("longitude", DoubleType(), True),
    StructField("signal_strength", DoubleType(), True)
])

# [EN] Creating mock data representing spatial coordinates and signal metrics
# [PL] (Tworzenie przykładowych danych reprezentujących współrzędne przestrzenne i metryki sygnału)
raw_data = [
    ("Node_A", 50.0647, 19.9450, 85.5),
    ("Node_B", 50.0614, 19.9366, 90.2),
    ("Node_C", 50.0700, 19.9500, 78.1),
    ("Node_D", 50.0500, 19.9200, 65.4),
    ("Node_E", 50.0800, 19.9600, 88.9)
]

# [EN] Creating Spark DataFrame from raw data
# [PL] (Tworzenie DataFrame Sparka z surowych danych)
df = spark.createDataFrame(raw_data, schema=schema)

# [EN] Mathematical transformation: Calculating distance vector norm from origin
# [PL] (Transformacja matematyczna: Obliczanie normy wektora odległości od początku układu)
df_transformed = df.withColumn(
    "vector_norm", 
    F.sqrt(F.col("latitude")**2 + F.col("longitude")**2)
)

# [EN] Converting Spark DataFrame back to Pandas for local matrix distance calculation
# [PL] (Konwertowanie DataFrame Sparka z powrotem do Pandas w celu lokalnego obliczenia macierzy odległości)
pdf = df_transformed.toPandas()
coordinates = pdf[['latitude', 'longitude']].values

# [EN] Computing pairwise Euclidean distance matrix using NumPy broadcasting
# [PL] (Obliczanie macierzy odległości euklidesowych w parach przy użyciu broadcasting w NumPy)
diff = coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]
distance_matrix = np.sqrt(np.sum(diff**2, axis=-1))

# [EN] Creating output directory if it does not exist inside container
# [PL] (Tworzenie katalogu wyjściowego, jeśli nie istnieje wewnątrz kontenera)
output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)

# [EN] Saving distance matrix to a CSV file using Pandas
# [PL] (Zapisywanie macierzy odległości do pliku CSV za pomocą Pandas)
output_file = os.path.join(output_dir, "distance_matrix.csv")
np.savetxt(output_file, distance_matrix, delimiter=",", fmt="%.4f")
print(f"--- [EN] Success! Matrix saved to {output_file} (PL: Sukces! Macierz zapisana do pliku) ---")

# [EN] Stopping Spark session gracefully
# [PL] (Poprawne zatrzymywanie sesji Spark)
spark.stop()