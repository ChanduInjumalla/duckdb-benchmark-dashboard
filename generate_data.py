import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1_000_000

data = {
    "user_id": np.arange(1, rows + 1),
    "age": np.random.randint(18, 65, size=rows),
    "country": np.random.choice(
        ["India", "USA", "UK", "Germany", "Canada"],
        size=rows
    ),
    "salary": np.random.randint(20000, 150000, size=rows),
    "purchase_amount": np.random.uniform(10, 5000, size=rows)
}

df = pd.DataFrame(data)
df.to_csv("benchmark_data.csv", index=False)

print("CSV file generated successfully!")
