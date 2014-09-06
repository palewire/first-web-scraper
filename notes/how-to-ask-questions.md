# How to Ask Questions

Inevitably, we'll all need to ask for some coding help. It doesn't matter if you're emailing an instructor, emailing a listserv, posting on Stack Overflow, or even just tweeting out a question, here are some guidelines that will help you get answers:

### 1. Do your own research first
Many times, someone else has had the same question as you, and asked that question on the Internet. [Google your problem](http://knightlab.northwestern.edu/2014/03/13/googling-for-code-solutions-can-be-tricky-heres-how-to-get-started/) or search listserv archives. Try any of the solutions you find to see if it works for you. If it does, then you're done!

If solutions aren't working, keep track of what you've tried, as well as what happened when you tried them. When you post your question, you'll want to explain what you've already done.

### 2. Be specific
When asking your question, be specific. This means your post should include:

* The tools you're using
* What you're trying to accomplish -- what should be happening if everything worked?
* The code you're using (or just the relevant parts)
* Any error messages you got
* What you've tried already, and what happened

<b>Let's look at an example:</b>

I'm trying to scrape the Boone County inmate roster using Python, and the requests and BeautifulSoup packages. So far, I'm only trying to get requests and BeautifulSoup working.

Here's my code:
<pre>import requests
import csv
from BeautifulSoup import BeautifulSoup
 
url = http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp
 
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
 
print soup</pre>

The error I'm getting says:
<pre>"File "test.py", line 5
    url = http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp
              ^
SyntaxError: invalid syntax"</pre>

I've tried Googling for "SyntaxError: invalid syntax" and I know that I'm writing something wrong, but I can't figure out which part of the code is causing the problem. Please help!

### 3. Repeat
When people start responding with solutions, if you try them and it doesn't work, do not respond simply with "That didn't work."

* Show what your updated code looks like
* Show the new error message

If it did work, them simply respond and thank the person for his/her help!

### 4. Other guides

* http://codingkilledthecat.wordpress.com/2012/06/26/how-to-ask-for-programming-help/
* https://codereview.stackexchange.com/help/how-to-ask
* http://mattgemmell.com/what-have-you-tried/
