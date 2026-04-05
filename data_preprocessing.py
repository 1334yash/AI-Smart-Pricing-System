import pandas as pd

# Load dataset
df = pd.read_csv("data/amazon.csv")

# Drop missing values (basic cleaning)
df = df.dropna()

# Save directly (already structured)
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Data already clean. Saved as cleaned_data.csv")