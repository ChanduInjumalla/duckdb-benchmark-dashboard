import pandas as pd
import duckdb
import time

CSV_FILE = "benchmark_data.csv"

# -------------------- Pandas Benchmark --------------------
start_time = time.time()

df = pd.read_csv(CSV_FILE)
pandas_result = (
    df.groupby("country")["salary"]
    .mean()
)

pandas_time = time.time() - start_time

# -------------------- DuckDB Benchmark --------------------
con = duckdb.connect()

start_time = time.time()

duckdb_result = con.execute("""
    SELECT country, AVG(salary) AS avg_salary
    FROM read_csv_auto('benchmark_data.csv')
    GROUP BY country
""").fetchdf()

duckdb_time = time.time() - start_time

# -------------------- Results --------------------
print("Pandas Result:")
print(pandas_result)
print(f"Pandas Time: {pandas_time:.4f} seconds\n")

print("DuckDB Result:")
print(duckdb_result)
print(f"DuckDB Time: {duckdb_time:.4f} seconds")
