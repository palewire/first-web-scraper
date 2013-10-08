from mechanize import Browser
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'

# Create a new browser object and open the URL
br = Browser()
br.open(url)

########## STEP 2: Select and fill out the appropriate form ##########

# Select the appropriate form, which we'll find by looking in Chrome
br.select_form("ctl01")

# Each control can be set. Dropdown lists are handled as lists, text fields take text
br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'

# Submit the form
br.submit()

########## STEP 3: Grab and parse the HTML ##########

soup = BeautifulSoup(br.response())
emptable = soup.find('table', id="grdEmployees")
rows = emptable.findAll('tr')[1:]

########## STEP 4: Iterate through the results and write to file ##########

for row in rows:
    print [c.text for c in row.findAll('td')]