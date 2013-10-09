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

########## STEP 3: Loop through each page in the result set ##########

# How many pages do you want to retrieve?
number_of_pages = 3

output_rows = []
for i in range(number_of_pages + 1):

    # We'll grab and parse the HTML to get the appropriate table rows, just like we did before.
    soup = BeautifulSoup(br.response())
    emptable = soup.find('table', id="grdEmployees")
    rows = emptable.findAll('tr')[1:]

    # This is the same as the equivalent chunk in salaries-mechanize, only we're doing
    # it for multiple pages, rather than just one.
    for tr in rows:
        output_row = []
        for td in tr.findAll('td'):
            output_row.append(td.text)
        output_rows.append(output_row)

    # Now that we've retrieved and saved the results, we need to advance the page.
    # First, we'll select the appropriate form, just like we did before.
    br.select_form("ctl01")

    # Now we just need to change the page and repeat the process
    br.form['MozillaPager1$ddlPageNumber'] = [str(i)]
    br.submit()

########## STEP 4: Write results to file ##########

print output_rows

# handle = open('out-mechanize.csv', 'a')
# outfile = csv.writer(handle)

# outfile.writerows(output_rows)