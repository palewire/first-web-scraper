import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

########## STEP 1: Open and read the URL ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931'

# Create a new browser object and open the URL
br = Browser()
br.open(url)

########## STEP 2: Select and fill out the appropriate form ##########

br.select_form("ctl01")

# Each control can be set. Dropdown lists are handled as lists, text fields take text
br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'

########## STEP 3: Grab and parse the HTML ##########

number_of_pages = 10

output_rows = []
for i in range(number_of_pages + 1):
    # Submit the form
    br.select_form("ctl01")
    br.form['MozillaPager1$ddlPageNumber'] = [str(i)]
    br.submit('MozillaPager1$btnPageNumber')

    soup = BeautifulSoup(br.response())
    emptable = soup.find('table', id="grdEmployees")
    rows = emptable.findAll('tr')[1:]

    for tr in rows:

        output_row = []
        for td in tr.findAll('td'):
            output_row.append(td.text)

        output_rows.append(output_row)

########## STEP 5: Write results to file ##########

print output_rows

# handle = open('out-mechanize.csv', 'a')
# outfile = csv.writer(handle)

# outfile.writerows(output_rows)