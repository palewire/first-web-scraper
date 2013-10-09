# Exercise 1: Boone County Jail scraper

For this exercise, we'll be scraping the roster of inmates at the [Boone County Jail](http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp). The scraper will use Python's [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) toolkit to parse the site's HTML and extract the data.

In addition to BeautifulSoup, we'll also use a few tools from Python's standard library -- namely the urllib2 and csv modules -- to open the URL, download the HTML and ultimately save the results to a CSV file.

This exercise will build on your understanding of Python data structures like lists and strings, as well as control structures like loops. If you need to brush up on those concepts, feel free to review the [Python Basics](https://github.com/ireapps/scraping-class/blob/master/python-basics/python-basics.md) guide included in this repository.