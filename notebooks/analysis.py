import pandas as pd

# Read datasets
products = pd.read_csv("data/raw/products_large.csv")
bom = pd.read_csv("data/raw/bom_large.csv")
warranty = pd.read_csv("data/raw/warranty_claims_large.csv")
ebay = pd.read_csv("data/raw/ebay_listings_large.csv")

datasets = {
    "Products": products,
    "BOM": bom,
    "Warranty": warranty,
    "eBay": ebay
}

for name, df in datasets.items():
    print("=" * 60)
    print(f"{name} Dataset")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")