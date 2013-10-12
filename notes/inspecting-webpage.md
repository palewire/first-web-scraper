# Inspecting a Web Page

A webpage is made of three major components:

* HTML -- Hypertext Markup Language -- This is creates the structure of a webpage.
* CSS -- Cascading Style Sheets -- This creates the style on a webpage.
* Javascript -- This is used to create interactive effects on a webpage.

For our use cases, the most important part is the HTML.

### HTML

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

There are many ways to grab content from HTML. In our case, we extract content by the 'id' or 'class'. These are CSS selectors. An 'id' ids a specific item on a page. If used corrected, there should be only one 'id' on page, but it is always not used correctly. A 'class' ids a specific type of item on a page. So, there maybe may instances of a class on a page.

In our crime example, there is only table. That table is identified by a class.
```<table class="resultsTable" style="margin: 0 auto; width: 90%; font-size: small;">```
While this example only has one instance of the class, it should be noted that it is possible that there maybe multiple instances of ```class="resultsTable"``` on the page.








