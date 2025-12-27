# Pandas vs DuckDB Benchmark Dashboard

This project benchmarks **Pandas** and **DuckDB** for an analytical aggregation
query on a large CSV dataset and presents the results through an
interactive **Streamlit dashboard**.

The objective is to compare real execution performance under identical
conditions instead of relying on theoretical claims.

---

## 🚀 Project Highlights

- Benchmark performed on a **1 million row CSV dataset**
- Same aggregation query executed using Pandas and DuckDB
- Execution time measured in real-time
- Interactive dashboard built with **Streamlit**
- Professional visualizations using **Plotly**
- Fully reproducible setup

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas
- DuckDB
- Streamlit
- Plotly

---

## 📊 Benchmark Query

The following aggregation query is used for comparison:

```sql
SELECT country, AVG(salary)
FROM data
GROUP BY country;
