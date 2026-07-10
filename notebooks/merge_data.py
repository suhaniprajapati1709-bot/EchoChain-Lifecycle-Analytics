import pandas as pd

# Load cleaned datasets
products = pd.read_csv("data/cleaned/products_cleaned.csv")
bom = pd.read_csv("data/cleaned/bom_cleaned.csv")
warranty = pd.read_csv("data/cleaned/warranty_cleaned.csv")

# Total warranty claims per SKU
claims = (
    warranty.groupby("SKU")
    .size()
    .reset_index(name="Warranty Claims")
)

# Average repair cost per SKU
repair = (
    warranty.groupby("SKU")["Repair Cost"]
    .mean()
    .reset_index(name="Avg Repair Cost")
)

# Number of components per SKU
components = (
    bom.groupby("SKU")
    .size()
    .reset_index(name="Total Components")
)

# Merge everything
final = products.merge(claims, on="SKU", how="left")
final = final.merge(repair, on="SKU", how="left")
final = final.merge(components, on="SKU", how="left")

# Fill missing values
final = final.fillna(0)

# Save file
final.to_csv("data/cleaned/final_lifecycle_data.csv", index=False)

print("✅ Final lifecycle dataset created successfully!")
print(final.head())