# Lab 5 - Regression Analysis
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')
# ── 1. Simple Linear Regression ──────────────────────────────────────────────
np.random.seed(42)
hours_studied = np.array([1,2,3,4,5,6,7,8,9,10,
1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])
exam_scores = 50 + 4.5 * hours_studied + np.random.normal(0, 3, len(hours_studied))
X = hours_studied.reshape(-1, 1)
y = exam_scores
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("=== Simple Linear Regression ===")
print(f"Slope (m): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"Prediction (7 hrs): {model.predict([[7]])[0]:.2f}")
# ── 2. Multiple Linear Regression ────────────────────────────────────────────
data = {
'size_sqft': [650,800,1000,1200,1500,1800,2000,2200,2500,3000,
700,900,1100,1350,1600,1900,2100,2300,2700,3200],
'bedrooms': [1,2,2,3,3,3,4,4,4,5, 1,2,2,3,3,3,4,4,5,5],
'age_years': [20,15,10,12,8,5,7,3,2,1, 18,14,11,9,6,4,8,2,1,0],
'price_lakh':[25,35,50,65,85,110,130,155,185,240,
28,40,55,72,90,118,138,160,195,255]
}
df = pd.DataFrame(data)
X = df[['size_sqft','bedrooms','age_years']]
y = df['price_lakh']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
random_state=42)
mlr = LinearRegression()
mlr.fit(X_train, y_train)
y_pred = mlr.predict(X_test)
print("\n=== Multiple Linear Regression ===")
for col, coef in zip(X.columns, mlr.coef_):
    print(f" {col}: {coef:.4f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
new_house = pd.DataFrame({'size_sqft':[1500],'bedrooms':[3],'age_years':[5]})
print(f"Predicted price (1500sqft,3bed,5yr): {mlr.predict(new_house)[0]:.2f} Lakh")
# ── 3. Polynomial Regression ─────────────────────────────────────────────────
X_p = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y_p = np.array([2,8,18,32,50,72,98,128,162,200]) + np.random.normal(0,3,10)
X_tr, X_te, y_tr, y_te = train_test_split(X_p, y_p, test_size=0.2, random_state=42)
poly_model = Pipeline([
('poly', PolynomialFeatures(degree=2)),
('linear', LinearRegression())
])
poly_model.fit(X_tr, y_tr)
print(f"\n=== Polynomial Regression (degree=2) ===")
print(f"R² Score: {r2_score(y_te, poly_model.predict(X_te)):.4f}")
