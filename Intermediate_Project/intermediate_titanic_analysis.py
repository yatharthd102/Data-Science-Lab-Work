# Intermediate Project - Titanic Survival Analysis & Prediction
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')
print("=== Intermediate Project: Titanic Survival Analysis ===")
# ── Generate Titanic-like Dataset ─────────────────────────────────────────────
np.random.seed(42)
n = 500
pclass = np.random.choice([1, 2, 3], n, p=[0.25, 0.25, 0.50])
sex = np.random.choice(['male', 'female'], n, p=[0.65, 0.35])
age = np.random.normal(30, 14, n).clip(1, 80)
sibsp = np.random.choice([0,1,2,3], n, p=[0.6,0.25,0.1,0.05])
parch = np.random.choice([0,1,2], n, p=[0.75,0.15,0.10])
fare = np.where(pclass==1, np.random.normal(85,40,n).clip(25,500),
np.where(pclass==2, np.random.normal(25,12,n).clip(10,100),
np.random.normal(13,8,n).clip(4,50)))
survival_prob = (0.15
+ 0.35*(sex=='female')
- 0.12*(pclass==3)
+ 0.08*(pclass==1)
- 0.003*np.maximum(age-18,0)
+ 0.02*(fare>50))
survival_prob = np.clip(survival_prob, 0.05, 0.95)
survived = (np.random.random(n) < survival_prob).astype(int)
df = pd.DataFrame({
'Pclass': pclass, 'Sex': sex, 'Age': age.round(1),
'SibSp': sibsp, 'Parch': parch, 'Fare': fare.round(2),
'Survived': survived
})
# ── Step 1: EDA ───────────────────────────────────────────────────────────────
print("\n--- Step 1: Exploratory Data Analysis ---")
print(df.head())
print(f"Shape: {df.shape}")
print(f"Overall Survival Rate: {df['Survived'].mean():.2%}")
print(df.groupby('Sex')['Survived'].mean().apply(lambda x: f'{x:.2%}'))
print(df.groupby('Pclass')['Survived'].mean().apply(lambda x: f'{x:.2%}'))
# ── Step 2: Data Cleaning & Feature Engineering ───────────────────────────────
print("\n--- Step 2: Data Cleaning ---")
# Simulate missing values
missing_idx = np.random.choice(df.index, 40, replace=False)
df.loc[missing_idx, 'Age'] = np.nan
print(f"Missing Age values: {df['Age'].isnull().sum()}")
df['Age'] = df['Age'].fillna(df['Age'].median()) # median imputation
print(f"After imputation: {df['Age'].isnull().sum()}")
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
print(f"FamilySize sample:\n{df['FamilySize'].value_counts().head()}")
# ── Step 3: Encoding & Modelling ─────────────────────────────────────────────
print("\n--- Step 3: Model Building ---")
df['Sex_enc'] = LabelEncoder().fit_transform(df['Sex'])
features = ['Pclass','Sex_enc','Age','Fare','FamilySize','IsAlone']
X = df[features].copy().values # numpy array, zero NaN
y = df['Survived'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train_s, y_train)
y_knn = knn.predict(X_test_s)
lr = LogisticRegression(max_iter=500)
lr.fit(X_train_s, y_train)
y_lr = lr.predict(X_test_s)
print(f"KNN Accuracy: {accuracy_score(y_test, y_knn):.4f}")
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, y_lr):.4f}")
best_pred = y_lr if accuracy_score(y_test,y_lr) >= accuracy_score(y_test,y_knn) else y_knn
best_name = "Logistic Regression" if accuracy_score(y_test,y_lr) >= accuracy_score(y_test,y_knn) else "KNN"
print(f"\nBest Model: {best_name}")
print(classification_report(y_test, best_pred, target_names=['Not Survived','Survived']))
# ── Sample Predictions ────────────────────────────────────────────────────────
print("\n--- Sample Predictions ---")
samples = np.array([[1,1,30,100,1,1],[3,0,25,8,1,1]])
preds = lr.predict(scaler.transform(samples))
proba = lr.predict_proba(scaler.transform(samples))
descs = ['1st class male, 30yr, alone','3rd class female, 25yr, alone']
for d, p, pr in zip(descs, preds, proba):
    print(f" {d}: {'Survived' if p==1 else 'Not Survived'} (prob={pr[1]:.2f})")
