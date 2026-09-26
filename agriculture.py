import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

crops = pd.read_csv("soil_measures.csv")

X = crops.drop("crop", axis=1)
y = crops["crop"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

best_predictive_feature = {}
best_score = 0
best_feature = 'placeholder'
max = -1
# Creating a model for each feture
for feature in X_train.columns:
    model = LogisticRegression()
    model.fit(X_train[[feature]], y_train)
    y_pred = model.predict(X_test[[feature]])
    score = metrics.f1_score(y_test, y_pred, average="weighted")
    if max < score:
        best_score = score
        best_feature = feature
        max = score
best_predictive_feature[best_feature] = best_score
print(f"F1-score for {best_feature}: {best_predictive_feature[best_feature]}")