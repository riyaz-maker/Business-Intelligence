import sqlite3
import pandas as pd

# Connect to SQLite and query monthly revenue
conn = sqlite3.connect("sports_bi.db")
monthly_revenue = pd.read_sql_query("""
    SELECT strftime('%Y-%m', revenue_date) AS month, SUM(total) AS net_revenue
    FROM revenue
    GROUP BY month
    ORDER BY month;
""", conn)
conn.close()

monthly_revenue['ds'] = pd.to_datetime(monthly_revenue['month'] + "-01")
monthly_revenue.rename(columns={'net_revenue': 'y'}, inplace=True)
monthly_revenue = monthly_revenue[['ds', 'y']]

print("Monthly Revenue Data for Forecasting:")
print(monthly_revenue.head())

from prophet import Prophet
import matplotlib.pyplot as plt

# Initialize the model
model = Prophet()
model.fit(monthly_revenue)

future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

# Plot forecast
fig1 = model.plot(forecast)
plt.title("Revenue Forecast using Prophet")
plt.xlabel("Date")
plt.ylabel("Net Revenue")
plt.show()
fig2 = model.plot_components(forecast)
plt.show()
