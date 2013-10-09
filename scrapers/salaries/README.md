# Exercises 2-4: Scraping MO government salaries

The next three exercises will use several different methods to scrape the [salaries](http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx) of Missouri state government employees. These exercises are designed to build upon one another, using progressively more sophisticated techniques to retrieve the data and save it to CSV files.

## Exercise 2: Scraping an individual page

We'll start with the salaries-basic.py file.

This scraper retrieves an [individual page](http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchResults.aspx?last=%25&first=%25&year=2013&agency=931) of salary information and uses BeautifulSoup to parse that data into a CSV file. In many ways, it's a repeat of the [first exercise](https://github.com/ireapps/scraping-class/tree/master/scrapers/crime) we did to scrape Boone County inmates.

You'll work through this in steps on your own, with some guidance from the coaches.

## Exercise 3: Filling out forms

Next we'll move on to the salaries-mechanize.py file, which introduces the concept of filling out forms.

Interacting with forms and other comple page elements can be among the most difficult and frustrating aspects of scraping a website. Luckily, Python's [mechanize](http://wwwsearch.sourceforge.net/mechanize/) module makes these tasks much simpler.

In this exercise, we'll once again scrape an individual page, but we'll navigate to that page by filling out a form.

## Exercise 4: Scraping multiple pages at once

Finally we'll work through salaries-full.py. This exercise will put together the concepts we've gone over so far and put them together in order to scrape multiple pages of salary data at once.