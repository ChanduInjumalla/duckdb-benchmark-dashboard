import streamlit as st
import pandas as pd
import duckdb
import time
import plotly.express as px

st.set_page_config(page_title="Pandas vs DuckDB Benchmark", layout="wide")

st.title("⚡ Pandas vs DuckDB Benchmark Dashboard")
st.write("This dashboard compares execution time for an analytical query.")

CSV_FILE = "benchmark_data.csv"

st.sidebar.title("Controls")
run = st.sidebar.button("🚀 Run Benchmark")

def pandas_benchmark():
    start = time.time()
    df = pd.read_csv(CSV_FILE)
    df.groupby("country")["salary"].mean()
    return round(time.time() - start, 4)

def duckdb_benchmark():
    con = duckdb.connect()
    start = time.time()
    con.execute("""
        SELECT country, AVG(salary)
        FROM read_csv_auto('benchmark_data.csv')
        GROUP BY country
    """).fetchdf()
    return round(time.time() - start, 4)

if run:
    st.info("Running benchmark, please wait...")

    p_time = pandas_benchmark()
    d_time = duckdb_benchmark()

    col1, col2, col3 = st.columns(3)
    col1.metric("Pandas Time (sec)", p_time)
    col2.metric("DuckDB Time (sec)", d_time)
    col3.metric("Speedup", f"{round(p_time/d_time, 2)}x")

    df_result = pd.DataFrame({
        "Tool": ["Pandas", "DuckDB"],
        "Time (seconds)": [p_time, d_time]
    })

    fig = px.bar(
        df_result,
        x="Tool",
        y="Time (seconds)",
        color="Tool",
        title="Execution Time Comparison",
        text="Time (seconds)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Insights")
    st.write(
        "DuckDB outperforms Pandas due to vectorized execution "
        "and columnar processing, making it ideal for analytical workloads."
    )
else:
    st.info("Click **Run Benchmark** from the sidebar to start.")

