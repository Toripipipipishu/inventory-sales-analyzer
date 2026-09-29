import pandas as pd

# CSVデータを読み込み
df = pd.read_csv("sample_sales.csv")

# 売上金額を計算
df["sales_value"] = df["monthly_sales"] * df["unit_price"]

# 在庫が何か月分あるかを計算
df["stock_months"] = df["stock"] / df["monthly_sales"]

# 売上金額が高い順に並び替え
df = df.sort_values("sales_value", ascending=False)

print("=== Sales & Inventory Analysis ===")

print(
    df[
        [
            "product_name",
            "stock",
            "monthly_sales",
            "unit_price",
            "sales_value",
            "stock_months",
        ]
    ]
)
