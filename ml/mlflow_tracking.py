import sqlite3
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Connect and load engagement data
conn = sqlite3.connect("sports_bi.db")
sessions = pd.read_sql_query("""
    SELECT user_id, AVG(duration_minutes) AS avg_duration, COUNT(*) AS session_count
    FROM sessions
    GROUP BY user_id
""", conn)
users = pd.read_sql_query("SELECT * FROM users", conn)
conn.close()

# Merge the data on user_id
data = pd.merge(users, sessions, on='user_id', how='left')
data.fillna({'avg_duration': 0, 'session_count': 0}, inplace=True)

# Create synthetic churn label: churn = 1 if session_count < 5, else 0
data['churn'] = (data['session_count'] < 5).astype(int)

# Encode gender as a numeric value
data['gender_encoded'] = data['gender'].map({'M': 0, 'F': 1})

# Define features and target variable
features = ['age', 'session_count', 'avg_duration', 'gender_encoded']
X = data[features]
y = data['churn']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an XGBoost classifier
model_xgb = xgb.XGBClassifier(objective='binary:logistic', use_label_encoder=False, eval_metric='logloss')
model_xgb.fit(X_train, y_train)
preds = model_xgb.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print("Churn Prediction Accuracy:", accuracy)


import mlflow
import xgboost as xgb

# Set the experiment name
mlflow.set_experiment("Churn Prediction Experiment")


with mlflow.start_run():
    # Train the XGBoost model
    model_xgb = xgb.XGBClassifier(objective='binary:logistic', use_label_encoder=False, eval_metric='logloss')
    model_xgb.fit(X_train, y_train)
    preds = model_xgb.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    
    # Log parameters and metrics
    mlflow.log_param("model_type", "XGBoost")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.xgboost.log_model(model_xgb, "model")
    
    print("Logged XGBoost model with accuracy:", accuracy)
