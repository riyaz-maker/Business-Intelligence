import pandas as pd
import sqlite3
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sports_bi.db")

# Load sessions and users data
sessions = pd.read_sql_query("""
    SELECT user_id, AVG(duration_minutes) AS avg_duration, COUNT(*) AS session_count
    FROM sessions
    GROUP BY user_id
""", conn)

users = pd.read_sql_query("SELECT * FROM users", conn)
conn.close()

# Merge data on user_id to form a complete DataFrame for segmentation
data = pd.merge(users, sessions, on="user_id", how="left")
data.fillna({'avg_duration': 0, 'session_count': 0}, inplace=True)

# Use engagement features for clustering
X_cluster = data[['session_count', 'avg_duration']]

# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_cluster)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 10), wcss, marker='o')
plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Choose, for example, 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(X_cluster)

print("User segmentation (first 10 rows):")
print(data[['user_id', 'session_count', 'avg_duration', 'cluster']].head())
