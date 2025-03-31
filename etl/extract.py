import pandas as pd

def load_raw_data(data_dir="data"):
    users = pd.read_csv(f"{data_dir}/users.csv")
    bookings = pd.read_csv(f"{data_dir}/bookings.csv")
    revenue = pd.read_csv(f"{data_dir}/revenue.csv")
    sessions = pd.read_csv(f"{data_dir}/sessions.csv")
    matches = pd.read_csv(f"{data_dir}/matches.csv")
    market_trends = pd.read_csv(f"{data_dir}/market_trends.csv")
    
    return users, bookings, revenue, sessions, matches, market_trends
