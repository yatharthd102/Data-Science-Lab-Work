# Lab 6 - KNN Classification
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')
# ── 1. KNN on Iris Dataset ────────────────────────────────────────────────────
iris = load_iris()
X, y = iris.data, iris.target
print("=== KNN on Iris Dataset ===")
print(f"Shape: {X.shape} | Classes: {iris.target_names}")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_s, y_train)
y_pred = knn.predict(X_test_s)
print(f"Train Accuracy: {knn.score(X_train_s, y_train):.4f}")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# ── 2. Find Best K ────────────────────────────────────────────────────────────
print("\n=== Finding Best K ===")
test_scores = []
for k in range(1, 21):
    knn_k = KNeighborsClassifier(n_neighbors=k)
    knn_k.fit(X_train_s, y_train)
    test_scores.append(knn_k.score(X_test_s, y_test))
best_k = range(1, 21)[np.argmax(test_scores)]
print(f"Best K: {best_k} | Accuracy: {max(test_scores):.4f}")
# ── 3. Cross-Validation ───────────────────────────────────────────────────────
knn_best = KNeighborsClassifier(n_neighbors=best_k)
cv_scores = cross_val_score(knn_best, X, y, cv=5)
print(f"\n5-Fold CV Scores: {[f'{s:.4f}' for s in cv_scores]}")
print(f"Mean CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
# ── 4. Custom Student Dataset ─────────────────────────────────────────────────
print("\n=== KNN on Student Dataset ===")
np.random.seed(42)
study_hours = np.random.uniform(1, 12, 100)
prev_score = np.random.uniform(40, 100, 100)
attendance = np.random.uniform(50, 100, 100)
result = ((study_hours*5 + prev_score*0.4 + attendance*0.3) > 90).astype(int)
df = pd.DataFrame({'Study_Hours': study_hours,
'Previous_Score': prev_score,
'Attendance': attendance, 'Pass': result})
X2 = df[['Study_Hours','Previous_Score','Attendance']]
y2 = df['Pass']
X2_tr, X2_te, y2_tr, y2_te = train_test_split(X2, y2, test_size=0.2,
random_state=42)
scaler2 = StandardScaler()
X2_tr_s = scaler2.fit_transform(X2_tr)
X2_te_s = scaler2.transform(X2_te)
knn2 = KNeighborsClassifier(n_neighbors=5)
knn2.fit(X2_tr_s, y2_tr)
y2_pred = knn2.predict(X2_te_s)
print(f"Student Dataset Accuracy: {accuracy_score(y2_te, y2_pred):.4f}")
print(classification_report(y2_te, y2_pred, target_names=['Fail','Pass']))
# Predict one new student
sample = scaler2.transform([[8, 75, 85]])
pred = knn2.predict(sample)
proba = knn2.predict_proba(sample)
print(f"\nStudent (8hrs,75prev,85attend): {'Pass' if pred[0]==1 else 'Fail'}")
print(f"Probability [Fail,Pass]: {proba[0].round(2)}")
