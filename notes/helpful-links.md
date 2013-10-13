# Helpful links

This document has some helpful resources that were mentioned during class.

### General links

[Notes from class](https://docs.google.com/document/d/1VvwGSCXynKJuq0-ATOITo9doUPPoX5WARS3I71o6glE/edit) taken by [Sean Sposito](https://twitter.com/seansposito)

[Examples of scraping projects](https://docs.google.com/spreadsheet/ccc?key=0AnUC82F2CpjJdFJoOGh4VHpiVFZsbkdQbXkxa0VTVXc&usp=sharing) from NICAR community.
Feel freel to add or edit to this. This is a work in progress.

[PyPi](https://pypi.python.org/pypi) is a directory of open source Python libraries. When you pip install a package, this is where pip looks for package information.

### Setup & Commandline Review
* [Setting up python on Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)
* [Setting up python on Windows](http://docs.python-guide.org/en/latest/starting/install/win/)
* [Commandline crash course](http://cli.learncodethehardway.org/book/)

### Intro to Python -- Discussion about Math
* [Floating Point Arithmetic: Issues and Limitations](http://docs.python.org/2/tutorial/floatingpoint.html#tut-fp-issues)
* [How do I round to 2 decimals?](https://gist.github.com/jackiekazil/6201722)

### Writing our scraper
Libraries
* [Python Standard Libraries](http://docs.python.org/2/library/)
* [urllib2](http://docs.python.org/2/library/urllib2.html)
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

As we build out our scraper, we come across issues. The easiest way to troubleshoot the problem is to google for the error. Another place to go is to the python docs.
* [Python Docs: Errors and Exceptions](http://docs.python.org/2/tutorial/errors.html)

* [HTTP Status Codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [Cronjobs](http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/) are used to set up scheduling for your script. The link is a simple script to get you started. The one thing to note is that a cronjob should be set up on a computer that is constantly connected to the internet -- such as ones that serve websites, because if you computer is not, then it won't be able to run. You can set this up on a computer/server from Amazon's EC2. There can be an associated cost, but these are low, unless you are trying to process all the Twitters.

### Community groups to check out

* [NICAR listserv](http://www.ire.org/resource-center/listservs/subscribe-nicar-l/) -- of course
* [PythonJournos listserv](https://groups.google.com/forum/#!forum/pythonjournos)
* Your local Hacks/Hackers. Example: [Hacks/Hackers in Columbia](http://www.meetup.com/hackshackersIRE/)
* [PyLadies](http://www.pyladies.com/)
* Your local Python community group. Example: [PyComo](http://www.meetup.com/pyCOMO/)

### Examples, fun projects, and readings
* Just came across this neat little application of scraping to solve a real world dirty data problem. Not entirely relevant, but [neat](http://www.p-value.info/2013/09/matching-misspelled-brand-names-easy-way.html)

