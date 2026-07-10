import pandas as pd

# Load integrated dataset
df = pd.read_csv("data/cleaned/final_lifecycle_data.csv")

# Normalize values (0 to 1)
df["Warranty Score"] = df["Warranty Claims"] / df["Warranty Claims"].max()
df["Repair Score"] = df["Avg Repair Cost"] / df["Avg Repair Cost"].max()
df["MSRP Score"] = df["MSRP"] / df["MSRP"].max()

# Circularity Score (0-100)
df["Circularity Score"] = (
    (0.4 * df["Warranty Score"]) +
    (0.3 * df["Repair Score"]) +
    (0.3 * df["MSRP Score"])
) * 100

# Recommendation
def recommendation(score):
    if score >= 70:
        return "High Priority Buy-Back"
    elif score >= 50:
        return "Medium Priority"
    else:
        return "Low Priority"

df["Recommendation"] = df["Circularity Score"].apply(recommendation)

# Save output
df.to_csv("data/cleaned/final_circularity_data.csv", index=False)

# Display top products
print("\nTop 10 Products by Circularity Score:\n")
print(
    df[["SKU", "Product Name", "Brand", "Circularity Score", "Recommendation"]]
    .sort_values(by="Circularity Score", ascending=False)
    .head(10)
)

print("\n✅ Circularity Score calculated successfully!")