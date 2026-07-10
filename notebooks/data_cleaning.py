import pandas as pd

# Load datasets
products = pd.read_csv("data/raw/products_large.csv")
bom = pd.read_csv("data/raw/bom_large.csv")
warranty = pd.read_csv("data/raw/warranty_claims_large.csv")
ebay = pd.read_csv("data/raw/ebay_listings_large.csv")

print("========== BEFORE CLEANING ==========\n")

print("Products:", products.shape)
print("BOM:", bom.shape)
print("Warranty:", warranty.shape)
print("eBay:", ebay.shape)

# Remove duplicates
products = products.drop_duplicates()
bom = bom.drop_duplicates()
warranty = warranty.drop_duplicates()
ebay = ebay.drop_duplicates()

# Remove leading/trailing spaces from text columns
for df in [products, bom, warranty, ebay]:
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

print("\n========== AFTER CLEANING ==========\n")

print("Products:", products.shape)
print("BOM:", bom.shape)
print("Warranty:", warranty.shape)
print("eBay:", ebay.shape)

# Save cleaned data
products.to_csv("data/cleaned/products_cleaned.csv", index=False)
bom.to_csv("data/cleaned/bom_cleaned.csv", index=False)
warranty.to_csv("data/cleaned/warranty_cleaned.csv", index=False)
ebay.to_csv("data/cleaned/ebay_cleaned.csv", index=False)

print("\n✅ Cleaned files saved successfully!")