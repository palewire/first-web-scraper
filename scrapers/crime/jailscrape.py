import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'

# Open the HTML file and turn it into a BeautifulSoup object for parsing
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

# The scrape actually starts here.
# Let's get the table that contains the results.
results_table = soup.find('table', attrs={'class': 'resultsTable'})

output = []  # The list that's going to store all of our output rows

# First we need to loop through all the rows in the table
for row in results_table.findAll('tr'):

    # We'll store all of the values for each given row in a list
    output_rows = []

    for cell in tr.findAll('td'):
        # Delete annoying tab character
        output_rows.append(cell.text.replace('&nbsp;', ''))

    # And we'll add that list to our broader list of results
    output.append(output_rows)

# Finally, we'll write our results to a file

print output

handle = open('out-using-requests.csv', 'a')
outfile = csv.writer(handle)
outfile.writerows(output)