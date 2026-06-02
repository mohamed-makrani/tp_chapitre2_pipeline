import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
db_path = BASE_DIR / "ventes.duckdb"

required_columns = {
    "date", "produit", "categorie",
    "quantite", "prix_unitaire", "ville"
}

con = duckdb.connect(str(db_path))

# vérifier tables
tables = con.execute("SHOW TABLES").fetchall()
table_names = {t[0] for t in tables}

if "ventes" not in table_names:
    raise ValueError("Table 'ventes' introuvable dans la base DuckDB")

# schéma
columns = con.execute("DESCRIBE ventes").fetchall()
existing_columns = {col[0] for col in columns}

missing = required_columns - existing_columns

if missing:
    raise ValueError(f"Colonnes manquantes : {missing}")

# NULL check
null_count = con.execute("""
SELECT COUNT(*) 
FROM ventes
WHERE produit IS NULL 
   OR quantite IS NULL 
   OR prix_unitaire IS NULL
""").fetchone()[0]

con.close()

if null_count > 0:
    raise ValueError(f"Données invalides : {null_count} lignes incomplètes")
else:
    print("Validation réussie : schéma et qualité OK")