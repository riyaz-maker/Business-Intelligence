from etl.extract import load_raw_data
from etl.transform import transform
from etl.load import load_to_sqlite

if __name__ == "__main__":
    users, bookings, revenue, sessions, matches, market_trends = load_raw_data()
    users, bookings, revenue, sessions, matches, market_trends = transform(
        users, bookings, revenue, sessions, matches, market_trends
    )
    load_to_sqlite(users, bookings, revenue, sessions, matches, market_trends)
    print("ETL pipeline executed successfully.")
