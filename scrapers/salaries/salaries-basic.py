import requests
import csv
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'
response = requests.get(url)
html = response.content

########## STEP 2: Parse HTML with BeautifulSoup ##########

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'id': 'grdEmployees'})

########## STEP 3: Iterate through the results and write to an output list ##########

output = []

for row in results_table.findAll('tr'):

    output_row = []

    for cell in row.findAll('td'):
        output_row.append(cell.text)

    output.append(output_row)

########## STEP 4: Write results to file ##########

print output

handle = open('out-basic.csv', 'a')
outfile = csv.writer(handle)
outfile.writerows(output)
