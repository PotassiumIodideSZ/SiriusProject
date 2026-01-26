import sqlite3
import os

# Get the database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check which tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]
print(f"Existing tables: {tables}")

# Delete all migration records for the recommendations app
cursor.execute("DELETE FROM django_migrations WHERE app='recommendations';")

# Check if the recommendations tables exist
recommendation_table_exists = 'recommendations_recommendation' in tables
investment_profile_table_exists = 'recommendations_investmentprofile' in tables

print(f"recommendations_recommendation exists: {recommendation_table_exists}")
print(f"recommendations_investmentprofile exists: {investment_profile_table_exists}")

if not investment_profile_table_exists:
    print("Creating recommendations_investmentprofile table...")
    cursor.execute("""
    CREATE TABLE recommendations_investmentprofile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        risk_score INTEGER NOT NULL,
        risk_category VARCHAR(20) NOT NULL,
        asset_allocation TEXT NOT NULL,
        recommendations TEXT NOT NULL,
        key_traits TEXT NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        user_id INTEGER NOT NULL UNIQUE REFERENCES authentication_user(id) ON DELETE CASCADE
    );
    """)
    print("Created recommendations_investmentprofile table")

if not recommendation_table_exists:
    print("Creating recommendations_recommendation table...")
    cursor.execute("""
    CREATE TABLE recommendations_recommendation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recommendation_text TEXT NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        user_id INTEGER NOT NULL REFERENCES authentication_user(id) ON DELETE CASCADE
    );
    """)
    print("Created recommendations_recommendation table")

# Insert the initial migration as already applied
cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES ('recommendations', '0001_initial', datetime('now'));")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Successfully reset migration records for 'recommendations' app.")
print("The migration '0001_initial' has been marked as applied.")
