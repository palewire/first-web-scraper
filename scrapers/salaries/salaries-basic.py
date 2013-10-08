import urllib2
import csv
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'
html = urllib2.urlopen(url).read()

########## STEP 2: Parse HTML with BeautifulSoup ##########

soup = BeautifulSoup(html)
emptable = soup.find('table', id="grdEmployees")
rows = emptable.findAll('tr')[1:]

########## STEP 3: Iterate through the results and write to an output list ##########

output_rows = []
for tr in rows:

    output_row = []
    for td in tr.findAll('td'):
        output_row.append(td.text)

    output_rows.append(output_row)

########## STEP 5: Write results to file ##########

handle = open('out-basic.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_rows)