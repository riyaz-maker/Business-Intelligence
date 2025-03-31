import sqlite3

def load_to_sqlite(users, bookings, revenue, sessions, matches, market_trends, db_path="sports_bi.db"):
    conn = sqlite3.connect(db_path)
    
    users.to_sql("users", conn, if_exists="replace", index=False)
    bookings.to_sql("bookings", conn, if_exists="replace", index=False)
    revenue.to_sql("revenue", conn, if_exists="replace", index=False)
    sessions.to_sql("sessions", conn, if_exists="replace", index=False)
    matches.to_sql("matches", conn, if_exists="replace", index=False)
    market_trends.to_sql("market_trends", conn, if_exists="replace", index=False)
    
    conn.close()
