import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Training data:
# area_sqft, bedrooms, bathrooms, parking
X = np.array([
    [600, 1, 1, 0],
    [800, 2, 1, 1],
    [1000, 2, 2, 1],
    [1200, 3, 2, 1],
    [1500, 3, 2, 2],
    [1800, 3, 3, 2],
    [2200, 4, 3, 2],
    [2500, 4, 3, 3],
    [3000, 5, 4, 3],
    [3500, 5, 4, 4],
])

# Price in lakh rupees
y = np.array([
    35,
    48,
    60,
    72,
    90,
    110,
    135,
    155,
    190,
    225,
])

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "model/house_price_model.pkl")

print("Model trained successfully.")
print("Model saved to model/house_price_model.pkl")
