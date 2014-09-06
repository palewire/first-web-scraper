import csv
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

NUMBER_OF_PAGES = 4

########## GET URL, FILL OUT FORM ##########

url = 'http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx'

br = Browser()
br.open(url)

br.select_form('ctl01')

br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'
br.form['SearchEmployees1$txtFirstName'] = '%'

br.submit()

output = []

for page in range(NUMBER_OF_PAGES):
    # THIS IS THE PART THAT CHANGES THE PAGE
    br.select_form('ctl01')
    br.form['MozillaPager1$ddlPageNumber'] = [str(page)]
    br.submit()

    # THIS IS THE PART THAT PARSES THE HTML
    html = br.response()
    soup = BeautifulSoup(html)

    results_table = soup.find('table', attrs={'id': 'grdEmployees'})

    for row in results_table.findAll('tr'):

        output_row = []

        for cell in row.findAll('td'):
            output_row.append(cell.text)

        output.append(output_row)

print output
