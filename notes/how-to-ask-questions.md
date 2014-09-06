# How to Ask Questions

Inevitably, we'll all need to ask for some coding help. It doesn't matter if you're emailing an instructor, emailing a listserv (i.e. [NICAR](http://www.ire.org/resource-center/listservs/subscribe-nicar-l/) or [PyJournos](https://groups.google.com/forum/#!forum/pythonjournos)), posting on [Stack Overflow](http://stackoverflow.com/), or even just tweeting out a question, here are some guidelines that will help you get answers:

### 1. Do your own research first
Many times, someone else has had the same question as you, and asked that question on the Internet. [Google your problem](http://knightlab.northwestern.edu/2014/03/13/googling-for-code-solutions-can-be-tricky-heres-how-to-get-started/) or search listserv archives. Try any of the solutions you find to see if it works for you. If it does, then you're done!

If solutions aren't working, **keep track of what you've tried**, as well as what happened when you tried them. When you post your question, you'll want to explain what you've already done.

### 2. Be specific
When asking your question, be specific. This means your post should include:

* The tools you're using
* What you're trying to accomplish -- what should be happening if everything worked?
* The code you're using (or just the relevant parts)
* Any error messages you got
* What you've tried already, and what happened

<b>Let's look at an example email or post, looking for programming help:</b>

I'm trying to scrape the Boone County inmate roster using Python, and the requests and BeautifulSoup packages. So far, I'm only trying to get requests and BeautifulSoup working.

Here's my code:
<pre>import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

print soup</pre>

The error I'm getting says:
<pre>Traceback (most recent call last):
  File "test.py", line 3, in <module>
    from BeautifulSoup import BeautifulSoup
ImportError: cannot import name BeautifulSoup</pre>

I first checked the spelling and it is correctly imported. So, I then tried Googling for "ImportError: cannot import name BeautifulSoup". All the help out there says that I need to install it, but I thought I did. I tried again to make sure and the following happened:

<pre>
pip install BeautifulSoup
Requirement already satisfied (use --upgrade to upgrade): BeautifulSoup in /Users/jacquelinekazil/Projects/envs/scraping-class/lib/python2.7/site-packages
Cleaning up..
</pre>

I can't figure out why this is happening. Please help!

*Note: This is an actual example. Bonus points for the individual that can identify what the issue is.*

### 3. Repeat
When people start responding with solutions, try them. If the proposed solution doesn't work, do not respond simply with "That didn't work." Instead:

* Post what your updated code looks like
* Post the new error message
* Post anything else you were inspired to try since you posted your question

If a proposed solution does work, them simply respond and thank the person for his/her help!

### 4. Document and share

When you have an issue that you worked through, document and share your problem, the things that you tried, and the final solution. By doing so, you are paying it forward. Others that have the issue will be able to resolve it more easily.

### 4. Other guides
If you want to read more on this topic:

* [How to ask for programming help](http://codingkilledthecat.wordpress.com/2012/06/26/how-to-ask-for-programming-help/)
* [Stack Exchange's 'How to ask'](https://codereview.stackexchange.com/help/how-to-ask)
* [Matt Gemmell's 'What have you tried?'](http://mattgemmell.com/what-have-you-tried/)
