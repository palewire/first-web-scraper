import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx'

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
employees = soup.find('table', id="grdEmployees")
rows = employees.findAll('tr')[1:]

########## STEP 4: Iterate through the results and write to an output list ##########

output_trs = []
for tr in rows:

    output_tds = []
    for td in tr.findAll('td'):
        output_tds.append(td.text)

    output_trs.append(output_tds)

########## STEP 5: Write results to file ##########

print output_trs

handle = open('out-mechanize.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_trs)