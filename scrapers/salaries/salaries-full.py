import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

# How many pages do you want to retrieve?
NUMBER_OF_PAGES = 4

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

output = []

for i in range(NUMBER_OF_PAGES):

    ########## GO TO THE PROPER PAGE ##########

    # First we need to be sure we're on the correct page, which corresponds to
    # the i in our for loop.

    # We'll select the appropriate form, just like we did before.
    br.select_form("ctl01")

    # Now we just need to nagivate to the page corresponding to i and repeat the process
    br.form['MozillaPager1$ddlPageNumber'] = [str(i)] # Typecast i to string
    br.submit('MozillaPager1$btnPageNumber') # Use the bottom submit button!

    ########## GRAB AND PARSE THE HTML #########

    # We'll grab and parse the HTML to get the appropriate table rows, just like we did before.
    soup = BeautifulSoup(br.response())
    results_table = soup.find('table', attrs={'id': 'grdEmployees'})

    ########## LOOP OVER ROWS AND CELLS ##########

    # This is the same as the equivalent chunk in salaries-mechanize, only we're doing
    # it for multiple pages, rather than just one.
    for row in results_table.findAll('tr'):
        
        output_row = []

        for cell in row.findAll('td'):
            output_row.append(cell.text)
        
        output.append(output_row)

########## STEP 4: Write results to file ##########

print output

handle = open('out-mechanize.csv', 'a')
outfile = csv.writer(handle)
outfile.writerows(output)