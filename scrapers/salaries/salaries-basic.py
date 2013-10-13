import urllib2
import csv
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'
html = urllib2.urlopen(url).read()

########## STEP 2: Parse HTML with BeautifulSoup ##########

soup = BeautifulSoup(html)
employees = soup.find('table', id="grdEmployees")
rows = employees.findAll('tr')[1:]

########## STEP 3: Iterate through the results and write to an output list ##########

output_trs = []
for tr in rows:

    output_tds = []
    for td in tr.findAll('td'):
        output_tds.append(td.text)

    output_trs.append(output_tds)

########## STEP 4: Write results to file ##########

print output_trs

handle = open('out-basic.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_trs)