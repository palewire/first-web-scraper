import urllib2
import csv
import re
from BeautifulSoup import BeautifulSoup

########## SETTINGS ##########

START_DATE = '10/1/2012'
END_DATE = '10/31/2012'

URL = 'http://www.gocolumbiamo.com/PSJC/Services/911/911dispatch/police.php?type=&keyword=&Start_Date=%s&End_Date=%s&Submit=Go' % (START_DATE, END_DATE)


########## HELPER FUNCTIONS ##########

def extract_coordinates(str):
    '''
    A simple function to extract lat/lon coordinates from the URL
    string in the dispatch table using regular expressions.
    '''
    coords = re.findall(r'q=(\d+.*)&', str)
    return coords[0].split(',')


########## MAIN BODY ##########

# Open the HTML file and turn it into a BeautifulSoup object for parsing
html = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html)

# Now create the output file for our scrape
handle = open('out.csv', 'a')
outfile = csv.writer(handle)

# The scrape actually starts here. In this case, there's only one table in the
# HTML document, so let's get that first.
only_table = soup.find('table')

# Now let's loop through every row in that table
for tr in only_table.findAll('tr'):

    # We need to set up a list to gather our processed data for the output csv. By default contains
    # column headers.
    output_row = []

    # Let's find all the TDs within our table row
    tds = tr.findAll('td')

    # We only care about the rows that have at least 5 cells. Those are the ones
    # that contain the data we need.
    if len(tds) == 5:

        # Loop through each cell in the rows we care about
        for td in tds:

            # Add the cell data to our output row
            output_row.append(td.text)

        # Now process lat and lon
        lat, lng = '', ''

        # tds[2] corresponds to the "Location" field of the table we're scraping. This
        # says "if the location field contains a link" ...
        if tds[2].find('a'):

            # Retrieve the lat and lng using the helper function above
            lat, lng = extract_coordinates(tds[2].find('a')['href'])
        
        # And append them to our output row
        output_row.append(lat)
        output_row.append(lng)

    # Finally, write our output row to the CSV (but not if the row is empty)
    if len(output_row) > 0: outfile.writerow(output_row)
