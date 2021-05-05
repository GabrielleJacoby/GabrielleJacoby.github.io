from pivottablejs import pivot_ui
import pandas as pd
df = pd.read_csv("PivotTableTest.csv")
pivot_ui(df)