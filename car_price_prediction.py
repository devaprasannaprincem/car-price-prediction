import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
data = pd.read_csv("car_data.csv")

# Feature engineering - using available columns
# Using wheelbase, carlength, curbweight as features since no Year/Kms_Driven available
X = data[['wheelbase', 'carlength', 'curbweight']]
y = data['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Random Forest
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Model comparison
print("Linear Regression R2:", r2_score(y_test, y_pred_lr))
print("Random Forest R2:", r2_score(y_test, y_pred_rf))

# Create subplots for all visualizations
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Feature importance (Random Forest)
importances = rf.feature_importances_
axes[0].bar(X.columns, importances, color='green')
axes[0].set_title("Feature Importance (Random Forest)")
axes[0].set_ylabel("Importance")

# Residual analysis
residuals = y_test - y_pred_rf
axes[1].scatter(y_pred_rf, residuals, color='purple')
axes[1].axhline(0, color='red', linestyle='--')
axes[1].set_xlabel("Predicted Price")
axes[1].set_ylabel("Residuals")
axes[1].set_title("Residual Analysis (Random Forest)")

# Actual vs Predicted (Random Forest)
axes[2].scatter(y_test, y_pred_rf, color="blue")
axes[2].plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
axes[2].set_xlabel("Actual Price")
axes[2].set_ylabel("Predicted Price")
axes[2].set_title("Car Price Prediction - Actual vs Predicted (Random Forest)")

plt.tight_layout()
plt.show()
