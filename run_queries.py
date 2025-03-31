import sqlite3
import os

def run_all_sql_files(directory, db_path="sports_bi.db"):
    """Run all .sql files in the specified directory against the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # List all .sql files in the given directory in sorted order
    sql_files = sorted([f for f in os.listdir(directory) if f.endswith(".sql")])
    
    for filename in sql_files:
        file_path = os.path.join(directory, filename)
        print(f"\n--- Running queries from file: {filename} ---")
        with open(file_path, "r") as file:
            sql = file.read()
        
        # Split the file content by semicolon to separate individual queries
        queries = sql.strip().split(";")
        
        for query in queries:
            if query.strip():  # Skip empty queries
                print(f"\nRunning Query:\n{query.strip()}")
                try:
                    cursor.execute(query.strip())
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                except Exception as e:
                    print(f"Error executing query: {e}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    queries_directory = "queries"
    run_all_sql_files(queries_directory)
