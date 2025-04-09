#Benjamin M Ouellette
#Citations
#-----------
#Week 11 - Tool Development 7 Walkthrough
#used chatgpt to help fix my syntax when using .writerow
#used chatgpt to debug the for loop on line 35.

#import modules
import requests
import csv

#creating the variable containing the term to query
query = "bash"
#creating the variable containing the URL with the query.
url = f"https://api.github.com/search/repositories?q={query}&per_page=10"

#Create the GET request
response = requests.get(url)
#checks for the 200 repsponse code to know connection is made.
if response.status_code == 200:
    print("\nRequest Successful...")
    #get response in json format.
    data = response.json()
    #if there are items within the data variable
    if "items" in data:
        print("\nCreating .csv file...")
        #creating the csv file.
        with open('query3script3.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            #Header row on CSV file.
            writer.writerow(["Repo Name", "Owner", "Description", "URL"])

            #loop through repos and write details to CSV
            for repo in data["items"]:
                writer.writerow([
                    repo["name"],
                    repo["owner"]["login"],
                    repo["description"],
                    repo["url"]
                ])

        #Output to display if the data has been written
        print("\nData has been wrtiten to .csv file")
    else:
        print("\nNo data found...")
#Output statement incase connection to the repos cannot be made.
else:
    print(f"Error: Status Code - {response.status_code}")





