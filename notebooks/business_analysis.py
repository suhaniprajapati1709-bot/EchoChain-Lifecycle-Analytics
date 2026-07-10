import pandas as pd

# Load cleaned datasets
products = pd.read_csv("data/cleaned/products_cleaned.csv")
bom = pd.read_csv("data/cleaned/bom_cleaned.csv")
warranty = pd.read_csv("data/cleaned/warranty_cleaned.csv")
ebay = pd.read_csv("data/cleaned/ebay_cleaned.csv")

print("="*60)
print("BUSINESS ANALYSIS")
print("="*60)

# Total products
print(f"\nTotal Products : {products['SKU'].nunique()}")

# Total Brands
print(f"Total Brands : {products['Brand'].nunique()}")

# Average MSRP
print(f"Average MSRP : ${products['MSRP'].mean():.2f}")

# Top Failed Components
print("\nTop 10 Failed Components")
print(warranty['Component Failed'].value_counts().head(10))

# Average Repair Cost
print("\nAverage Repair Cost")
print(warranty['Repair Cost'].mean())

# Top Suppliers
print("\nTop Suppliers")
print(bom['Supplier'].value_counts().head())

# eBay Conditions
print("\neBay Product Conditions")
print(ebay['Condition'].value_counts())

# Average eBay Price
print("\nAverage eBay Price")
print(ebay['Price'].mean())