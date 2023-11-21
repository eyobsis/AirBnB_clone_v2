#!/usr/bin/python3
import mysql.connector

def test_add_state():
    # Connect to your MySQL database
    connection = mysql.connector.connect(
        host="HBNB_MYSQL_HOST",
        user="HBNB_MYSQL_USER",
        password="HBNB_MYSQL_PWD",
        database="HBNB_MYSQL_DB"
    )
    cursor = connection.cursor()

    # Get initial record count
    cursor.execute("SELECT COUNT(*) FROM states")
    initial_count = cursor.fetchone()[0]

    # Execute the command to add a new state (e.g., "INSERT INTO states (name) VALUES ('California')")
    # Replace 'INSERT INTO states...' with your SQL command
    # ...

    # Get record count after the action
    cursor.execute("SELECT COUNT(*) FROM states")
    final_count = cursor.fetchone()[0]

    # Verify the difference in counts
    if final_count - initial_count == 1:
        print("Test passed: New record added successfully")
    else:
        print("Test failed: Record count didn't increase by 1 after the action")

    # Close cursor and connection
    cursor.close()
    connection.close()

# Run the test
if __name__ == "__main__":
    test_add_state()

