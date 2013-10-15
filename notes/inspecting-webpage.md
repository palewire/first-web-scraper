# Inspecting a Web Page

A webpage is made of three major components:

* HTML -- Hypertext Markup Language -- This is creates the structure of a webpage.
* CSS -- Cascading Style Sheets -- This creates the style on a webpage.
* Javascript -- This is used to create interactive effects on a webpage.

For our use cases, the most important part is the HTML.

### General HTML

In order to scrape a website, we need to understand what each of these pieces do. HTML is the frame work contains the content of a page. Without HTML, you do not have a webpage.

To view the HTML code, open up Chrome, load [your web page](http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp), and right click on 'View Source'.

![screen shot 2013-10-11 at 3 39 09 pm](https://f.cloud.github.com/assets/166734/1318115/455e7fec-32b5-11e3-93c8-d67247faad1c.png)

HTML has markers that denote the start and end of the HTML ```<html></html>```. Inside the html tag, there are two main sections that are the head and the body.

```
<html>
	<head>
	</head>
	<body>
	</body>
</html>
```

In the case of well formatted HTML, the page will be made of nested HTML elements. In all our examples, we have decently formatted html. There are cases in the real work where this is not the case. Then solving for this becomes an additional problem to solve for.

The part that we are interested in is the body tag. Some where in there lies our content. To acces this more easily, we will use Chome's inspector. Right click on the table of data that you are interested in and select 'inspect element'.

![Inspect the element](https://f.cloud.github.com/assets/166734/1320358/7f309dae-3355-11e3-88db-5249ae5678e7.png)

Your browser will open Chrome's inspector and display the HTMLs and highlights the code where the table is.

![Inspector with the highlighted element](https://f.cloud.github.com/assets/166734/1320348/f12d3206-3354-11e3-8ef9-b6a4540e526b.png)

There are many ways to grab content from HTML. In our case, we extract content by the 'id' or 'class'. These are called CSS selectors. An 'id' ids a specific item on a page. If used corrected, there should be only one 'id' on page, but it is always not used correctly. A 'class' ids a specific type of item on a page. So, there maybe may instances of a class on a page.

In our crime example, there is only table. The table is identified by a class.
```<table class="resultsTable" style="margin: 0 auto; width: 90%; font-size: small;">```
While this example only has one instance of the class, it should be noted that it is possible that there maybe multiple instances of ```class="resultsTable"``` on the page.

### Inspecting a form

In our [second example script](http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx), we are trying to scrape data that we get back from a form. In the simple script, we start with a default url, but in [salaries-full.py](https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-full.py) and [salaries-mechanize.py](https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-mechanize.py), we identify the form and set the search in python.

Looking at our example, search and find the form tag that is wrapped about the fields that are you interested in. Most of the time, this is tightly wrapped around the fields, however in this case, the ```<form></form>``` is wrapped around the whole page. This is not the best designed HTML page, but it still works, so that's all we care about.

```
<form name="ctl01" method="post" action="searchemployees.aspx" id="ctl01">
```

The form tag have a couple of pieces of information that we need to know.

* name -- identifies the form. This must be unique.
* method -- the action of the data that is being transfered. See requests section for more information on what 'post' means.
* id -- this is a CSS Selector, which was discussed earlier. In this case the id and name is the same.

We will use the name to identify the form in our code. The reason for using the name over the id is that while ids are supposed to be unique on a page, sometimes they are not. In our code, we would be

```
br.select_form("ctl01")
```

Now, we need to identify the fields in form. On [this page](http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx), we will want to start by right clicking and 'inspect element'. Do this on the form, until you identify the 'id' of the form value. To know that you have the right element to match to the code you are looking at, you will see it highlighted in your browser.

![Highlighted element](https://f.cloud.github.com/assets/166734/1320458/b5bae160-335d-11e3-9b06-f55cab13161f.png)

For the calendar element, we can see that the name of the select tag is "SearchEmployees1$CalendarYear1$ddlCalendarYear". If you look at [salaries-full.py](https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-full.py) and [salaries-mechanize.py](https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-mechanize.py), you will see the form fields that we define by using this technique. In our script, we set those fields to specific values.

```python
# Each control can be set. Dropdown lists are handled as lists, text fields take text
br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'
```
**SPECIAL NOTE:** *Notice the last name field is set to a ```%```. The ```%``` is a wildcard character. This tells the database that you want to grab everything. The other wildcard to try is ```*```. If a web form was going to accept a wildcard, it will be one of these two. Often websites, don't allow wildcards.*

In our program, then we use these and submit the values in the form. This brings us to the idea of requests. The next section is not required understanding, but it will help in understanding how a form works.

### Requests -- Methods and Statuses

##### Request methods
Understanding a little about requests is helpful when troubleshooting what is happening on website. A request is how you communicate with the server that hosts the website that you are interacting with. For example, when you type 'google.com' in your browser's address bar and press enter, you are sending a request to *GET* that content. There are two types of request methods that you should understand.

* GET
* POST

A GET request method is basically the retrival of the content of a web page. A POST request method is what happens when you submit information via a web form.

This is available in the *Header* information of a web page, which can be found in the Inspector also. When you have the Inspector open, try clicking on the 'Network' tab. (The default tab is Elements. The Network tab should be two over.)

![Network Tab](https://f.cloud.github.com/assets/166734/1330753/2b68b952-3537-11e3-90d7-aaee3bc00036.png)

Now refresh the page. You will see the Network activity populate as the page loads. A web page is made of many requests. We are looking for the main one, which is the first one in this case.

![Jail get method](https://f.cloud.github.com/assets/166734/1331278/afeaa778-354e-11e3-8d3b-e5ccf2f13a3b.png)

Look at the line that says:
```
JailResidents.asp
/sheriff/JailResidents
```

You will see that the method is "GET".

Now let's try this while submitting a form for Missouri [state employee salaries](http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx). Load the page. Open up the inspector. Click on the "Network" tab. Fill out the form on the web page and hit submit.

At the top of the Network tab, you will see a request that occurred when you submitted the form -- the method is "POST" instead of "GET".

![Salary posts](https://f.cloud.github.com/assets/166734/1331302/f6a41cb6-354f-11e3-87d6-7ddadc0fb10a.png)

#### Request statuses
The Network tab is full of useful information. Another bit to take notice of are the values under status. These are HTTP status codes. In both of our examples, we had a 200, which is okay. The 200 is a common return value. Other return values which you may see often are the 404, which means that the content was not found and another is 301 or 302, which means that the request was redirected. Understanding these codes can help you in the troubleshooting process if the site that you requesting doesn't seem to be behaving in the way that you expect. Wikipedia's [List of HTTP Statuses](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes) is a great reference to learn more about what these codes mean.

#### Header information
Lastly, you should take note of header information. This is also found in the Network tab. After you go through the process of loading a request, click on the name and path column on the left. You will load more detailed information for that name and path on the right. The default tab is the Headers tab.

![Headers sample info](https://f.cloud.github.com/assets/166734/1331412/6f3501c2-3555-11e3-91ff-32f65b8afead.png)

The Headers tab includes information like the request method and the status, but a lot more also.

	Request URL:http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchEmployees.aspx
	Request Method:POST
	Status Code:200 OK
	..... more

Notice near the bottom of the content we have our form variables that are being submitted as part of the request made.

	SearchEmployees1$CalendarYear1$ddlCalendarYear:2013
	SearchEmployees1$ddlAgencies:931
	SearchEmployees1$txtLastName:
	SearchEmployees1$txtFirstName:
	SearchEmployees1$btnSearch:GO
	..... more


*If you have any questions regarding this content, please submit it as an issue and someone will add more clafication or details.*





