import urllib2
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'
html = urllib2.urlopen(url).read()

########## STEP 2: Parse URL with BeautifulSoup ##########

soup = BeautifulSoup(html)
emptable = soup.find('table', id="grdEmployees")
rows = emptable.findAll('tr')[1:]

########## STEP 3: Iterate through the results and write to file ##########

for row in rows:
    print [c.text for c in row.findAll('td')]
