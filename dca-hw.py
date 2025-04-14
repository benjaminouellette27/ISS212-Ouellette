'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - dca-hw.py
NOTE: Use files: dca-log.csv & dca-db.db .
'''

#import modules.
import csv
import sqlite3

#opening the log file that the user provided.
def retrieve_log_data(log_file):
    with open(log_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# connects the file provided by the user
# converts each row into a dictionary with different field names.
# Returns the dictionary.
def retrieve_database_data(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    return [{'id': row[0], 'username': row[1], 'role': row[2], 'email': row[3], 'website': row[4]} for row in rows]

#displays all user names found in the log
# ask user to select a username
# returns the user name.
def prompt_for_username(log_data):
    print("Available usernames:")
    for i, entry in enumerate(log_data):
        print(f"{i + 1}. {entry.get('username')}")

    selection = int(input("Select a username by entering its number: ")) - 1
    return log_data[selection].get('username').strip()

# Filters the log data for the selected username
# prints any data found that corresponds to the username.
# prints error message if no data is found
def correlate_data_based_on_user_input(database, log_data, selected_username):
    correlated_data = [entry for entry in log_data if entry.get('username').strip() == selected_username]

    if correlated_data:
        print(f"\nCorrelated data for '{selected_username}':")
        for entry in correlated_data:
            print(entry)
    else:
        print(f"No data found for the entered username '{selected_username}'.")

# main program execution
# prompts user to enter file and data base name
# displays output.
log_file = input("Enter the log file name (e.g., logfile.csv): ")
db_file = input("Enter the database file name (e.g., local_db_file.db): ")

log_data = retrieve_log_data(log_file)
database = retrieve_database_data(db_file)

selected_username = prompt_for_username(log_data)
correlate_data_based_on_user_input(database, log_data, selected_username)
