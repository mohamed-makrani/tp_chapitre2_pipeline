import pandas as pd
import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

csv_path = BASE_DIR / "data" / "ventes.csv"
db_path = BASE_DIR / "ventes.duckdb"

# lire CSV
df = pd.read_csv(csv_path)

# connexion DuckDB
con = duckdb.connect(str(db_path))

# charger dataframe dans table
con.execute("CREATE OR REPLACE TABLE ventes AS SELECT * FROM df")

con.close()

print("ingestion terminée avec succès")