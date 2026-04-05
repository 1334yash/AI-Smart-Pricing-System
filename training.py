import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
import joblib

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# One-hot encode category
df = pd.get_dummies(df, columns=['category'])

# Features & target
X = df.drop("discounted_price", axis=1)
y = df["discounted_price"]

# Save column structure (IMPORTANT for API)
joblib.dump(X.columns.tolist(), "models/columns.pkl")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# XGBoost Model ⭐
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6
)

model.fit(X_train, y_train)

# Evaluation
pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))

# Save model
joblib.dump(model, "models/pricing_model.pkl")

print("✅ Model trained & saved successfully!")