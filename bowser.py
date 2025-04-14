'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - bowser.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

#import modules
import os
import sqlite3
from datetime import datetime


#main function that analyzes the browser history.
def analyze_chrome_history(history_path, output_file):
    #check if file exists
    if not os.path.isfile(history_path):
        print("Invalid file path. Please make sure the file exists.")
        return

    #try-except blocks for sqlite operations.
    try:

        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()

        #query the URL records
        cursor.execute("SELECT * FROM urls")
        rows = cursor.fetchall()

        #output header
        print("[--- Browser History Analysis ---]\n")
        #loop through results.
        with open(output_file, 'w', encoding='utf-8') as file:
            for row in rows:
                #etracts URL and site visit timestamp.
                url = row[1]
                last_visit_time_microseconds = row[5]

                #converting the webpage time to a humanreadable format.
                if last_visit_time_microseconds and last_visit_time_microseconds < 2**63:
                    try:

                        visit_time = datetime.fromtimestamp(
                            (last_visit_time_microseconds - 11644473600000000) / 1000000
                        ).strftime('%Y-%m-%d %H:%M:%S')

                    #error handling for time conversion
                    except (ValueError, TypeError) as e:
                        print(f"Error converting visit time: {e}")
                        visit_time = "N/A"
                else:
                    visit_time = "N/A"

                #output to the specified file.
                output_line = f"[+] URL: {url}\n   Last Visit Time: {visit_time}\n"
                print(output_line)
                file.write(output_line)

        #completion message.
        print(f"\nBrowser history has been saved to {output_file}")

    #error handling for SQlite
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    #closing connection.
    finally:

        if connection:
            connection.close()

#execute the main block.
if __name__ == "__main__":

    #user prompt for file.
    chrome_history_path = input("Enter the path to the Chrome history database: ")


    output_file_path = input("Enter the path to save the output file (e.g., output.txt): ")

    analyze_chrome_history(chrome_history_path, output_file_path)
