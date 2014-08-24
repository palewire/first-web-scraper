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
only_table = soup.find('table', attrs={'class': 'resultsTable'})

output_trs = []  # The list that's going to store all of our output rows

# First we need to loop through all the rows in the table
for tr in only_table.findAll('tr'):

    # And next, we want to get all the cells within each of the rows
    tds = tr.findAll('td')

    # We'll store all of the values for each given row in a list
    output_tds = []
    for td in tds:
        # Delete annoying tab character
        output_tds.append(td.text.replace('&nbsp;', ''))

    # And we'll add that list to our broader list of results
    output_trs.append(output_tds)

# Finally, we'll write our results to a file

print output_trs

handle = open('out-using-requests.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_trs)
