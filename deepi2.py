import pandas as pd
import numpy as np

# 1. Create DataFrame and save to CSV
data = {
    "Name": ["Asha", "Bala", "Chitra", "Deepak", "Esha"],
    "Age": [23, np.nan, 25, np.nan, 22],
    "Dept": ["HR", "IT", np.nan, "IT", "HR"]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("Original DataFrame saved to students.csv")

# 2. Read CSV
df_read = pd.read_csv("students.csv")
print("\nRead DataFrame:\n", df_read)

# 3. Replace nulls safely (no warning)
df_read["Age"] = df_read["Age"].fillna(df_read["Age"].mean())       # mean for Age
df_read["Dept"] = df_read["Dept"].fillna(df_read["Dept"].mode()[0]) # mode for Dept

print("\nAfter filling nulls:\n", df_read)

# 4. Write updated DataFrame to new CSV
df_read.to_csv("students_updated.csv", index=False)
print("\nUpdated DataFrame saved to students_updated.csv")
