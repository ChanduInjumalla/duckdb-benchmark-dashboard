# 📊 Pandas vs DuckDB Benchmark Dashboard

This project benchmarks **Pandas** and **DuckDB** for an analytical aggregation query on a large CSV dataset and visualizes the results using an interactive **Streamlit dashboard**.

The goal is to compare **real execution performance under identical conditions**, rather than relying on theoretical performance claims.

---

## 🚀 Project Highlights

- Benchmark performed on a **1 million row CSV dataset**
- Identical aggregation query executed using **Pandas** and **DuckDB**
- Execution time measured in real time
- Interactive dashboard built with **Streamlit**
- Professional visualizations using **Plotly**
- Fully reproducible setup with scripts

---

## 🛠️ Tech Stack

- Python 3.11  
- Pandas  
- DuckDB  
- Streamlit  
- Plotly  
- Matplotlib  

---

## 📊 Benchmark Query

The following aggregation query is used for comparison:

```sql
SELECT country, AVG(salary)
FROM data
GROUP BY country;
```

This query represents a common analytical workload involving grouping and aggregation operations.

---

## 📁 Project Structure

```bash
duckdb-benchmark-dashboard/
│
├── app.py                        # Streamlit dashboard application
├── ARTICLE.md                    # Detailed technical explanation
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── generate_data.py              # Dataset generation script
└── benchmark_pandas_vs_duckdb.py # Benchmark execution logic
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Generate the Dataset

```bash
python generate_data.py
```

> ⚠️ Dataset is not committed to GitHub to keep the repository lightweight.

---

### 3️⃣ Run the Dashboard

```bash
streamlit run app.py
```

Open your browser and navigate to:

```
http://localhost:8501
```

Click **Run Benchmark** from the sidebar to execute the comparison.

---

## 📈 Key Insights

- DuckDB consistently executes aggregation queries faster than Pandas
- DuckDB benefits from vectorized execution and columnar processing
- Pandas introduces additional overhead due to in-memory DataFrame operations
- DuckDB complements Pandas well for analytical workloads

---

## 🖥️ Dashboard Preview

![Pandas vs DuckDB Benchmark Dashboard](dashboard_screenshot.png.png)


## 🔁 Reproducibility

All source code, dataset generation scripts, and execution instructions are included to fully reproduce the benchmark.

---

## 👤 Author

**Chandu**  
ML / AI Intern Applicant
