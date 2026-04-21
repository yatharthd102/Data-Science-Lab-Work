# Project Title
Titanic Survival Prediction - Classification Analysis
## Description
Predicts whether a Titanic passenger would survive based on
features like passenger class, gender, age, fare, and family size.
Includes full EDA, data cleaning, feature engineering, and model comparison.
## Dataset
- Source: Synthetically generated Titanic-like data (500 passengers)
- Features: Pclass, Sex, Age, SibSp, Parch, Fare
- Target: Survived (0 = No, 1 = Yes)
## Steps Performed
1. Data Cleaning - Handled missing Age values using median imputation
2. Feature Engineering - Created FamilySize and IsAlone columns
3. Exploratory Data Analysis - Survival rates by gender and class
4. Visualization - Analyzed distributions and correlations
5. Model Building - KNN and Logistic Regression comparison
## Results
- Female survival rate significantly higher than male (~41% vs ~9%)
- 1st class passengers had highest survival rate (~28%)
- Best model achieved ~85% accuracy
- Logistic Regression and KNN both evaluated and compared
## Tools Used
- Python, NumPy, Pandas, Scikit-learn (KNN, Logistic Regression)
## Conclusion
Gender and passenger class are the strongest predictors of survival.
Family size also plays a role, with solo travelers having different
survival patterns than families.
## Author
Manus
