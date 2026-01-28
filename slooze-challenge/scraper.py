import requests
import pandas as pd

categories = ["smartphones", "laptops"]

all_data = []

for cat in categories:
    url = f"https://dummyjson.com/products/category/{cat}"
    r = requests.get(url)
    data = r.json()

    for p in data["products"]:
        all_data.append({
            "product_name": p["title"],
            "price": p["price"],
            "supplier": "Multiple Vendors",
            "location": "Global",
            "category": cat
        })

df = pd.DataFrame(all_data)
df.to_csv("data/products.csv", index=False)

print("✅ Data collected successfully!")
print(df.head())
