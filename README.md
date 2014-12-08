# Scraping class

An Investigative Reporters and Editors course on building your first web scraper, initially developed by [Chase Davis](mailto:chase.davis@gmail.com), [Jackie Kazil](mailto:jackiekazil@gmail.com), [Sisi Wei](mailto:me@sisiwei.com) and Matt Wynn for bootcamps held at the University of Missouri in Columbia, Missouri in 2013 and 2014.

Although the goal of this course is to introduce the concepts of web scraping, we will also spend time covering programming fundamentals that can be applied to other problems, from data analysis to web development.

* Documentation and tutorials: [scraping-class.rtfd.org](http://scraping-class.readthedocs.org/en/latest/)

## Contributing to the documentation

After installing the repository, the Sphinx documentation can be edited in the
``docs`` directory and published to ReadTheDocs by pushing changes to the ``master`` branch.

First install the requirements.

```bash
$ pip install -r requirements-dev.txt
```

Fire up the test server, which will automatically update to show changes made
to the restructured text files in the ``docs`` directory.

```bash
$ make docs
```

Open ``http://localhost:8000`` in your browser and start making changes.