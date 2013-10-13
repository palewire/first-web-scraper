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
br.form['SearchEmployees1$ddlAgencies'] = ['200']
br.form['SearchEmployees1$txtLastName'] = '%'

# Submit the form
br.submit()

########## STEP 3: Loop through each page in the result set ##########

# How many pages do you want to retrieve?
number_of_pages = 4

output_trs = []
for i in range(number_of_pages):

    ########## GO TO THE PROPER PAGE ##########

    # First we need to be sure we're on the correct page, which corresponds to
    # the i in our for loop.

    # We'll select the appropriate form, just like we did before.
    br.select_form("ctl01")

    # Now we just need to nagivate to the page corresponding to i and repeat the process
    br.form['MozillaPager1$ddlPageNumber'] = [str(i)]
    br.submit()

    ########## GRAB AND PARSE THE HTML #########

    # We'll grab and parse the HTML to get the appropriate table rows, just like we did before.
    soup = BeautifulSoup(br.response())
    employees = soup.find('table', id="grdEmployees")
    rows = employees.findAll('tr')[1:]

    ########## LOOP OVER ROWS AND CELLS ##########

    # This is the same as the equivalent chunk in salaries-mechanize, only we're doing
    # it for multiple pages, rather than just one.
    for tr in rows:
        
        output_tds = []
        for td in tr.findAll('td'):
            output_tds.append(td.text)
        
        output_trs.append(output_tds)

########## STEP 4: Write results to file ##########

print output_trs

handle = open('out-mechanize.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_trs)