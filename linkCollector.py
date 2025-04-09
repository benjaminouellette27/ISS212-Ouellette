#Benjamin M Ouellette
#Citations
#----------
#Week 11 - Tool Development 7 Walkthrough

#importing modules.
import requests
from bs4 import BeautifulSoup

#Creating the URL variable with target URL.
url = "https://www.wikipedia.com"
#Creating the GET request.
response = requests.get(url)
#Parsing content from response.
soup = BeautifulSoup(response.text, 'html.parser')

#with loop that saves all links found in the response to a text
#file called "Links_found.txt
with open("domain3script1.txt", "w") as f:
    for link in soup.find_all('a', href=True):
        f.write(link['href'] + "\n")

#output displaying the text file name.
print("Links written to text file.")
