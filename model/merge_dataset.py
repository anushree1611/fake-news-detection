import pandas as pd

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = "FAKE"
true["label"] = "REAL"

# Keep only useful columns
fake = fake[["text", "label"]]
true = true[["text", "label"]]

# Combine both datasets
combined = pd.concat([fake, true])

# Shuffle data
combined = combined.sample(frac=1).reset_index(drop=True)

# Save to new file
combined.to_csv("fake_news.csv", index=False)

print("✅ fake_news.csv created successfully!")
