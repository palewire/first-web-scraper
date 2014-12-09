:tocdepth: 2

Scraping class
==============

An step-by-step guide to building your first web scraper.

Although the goal of this course is to introduce the concepts of web
scraping, we will also spend time covering programming fundamentals that
can be applied to other problems, from data analysis to web development.

This guide was initially developed by `Chase
Davis <chase.davis@gmail.com>`__, `Jackie
Kazil <jackiekazil@gmail.com>`__, `Sisi Wei <me@sisiwei.com>`__ and Matt
Wynn for bootcamps held by Investigative Reporters and Editors at the
University of Missouri in Columbia, Missouri in 2013 and 2014.

It was later modified by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ in December 2014 for workshops at `The Centre for Cultura Contemporania de Barcelona <http://www.cccb.org/en/curs_o_conferencia-data_journalism_work_session_viii-46957>`_ and `Medialab-Prado <http://medialab-prado.es/article/iitallerdeperiodismodedatosconvocatoriadeproyectos>`_ in Madrid.

-  Code repository:
   `github.com/ireapps/scraping-class/ <https://github.com/ireapps/scraping-class/>`__
-  Documentation:
   `scraping-class.rtfd.org/ <http://scraping-class.rtfd.org/>`__
-  Issues:
   `github.com/ireapps/scraping-class/issues/ <https://github.com/ireapps/scraping-class/issues>`__

Prelude: Prerequisites
----------------------

Before you can begin, your computer needs the following tools installed
and working to participate.

1. A `command-line
   interface <https://en.wikipedia.org/wiki/Command-line_interface>`__
   to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`__ to work
   with plain text files
3. Version 2.7 of the
   `Python <http://python.org/download/releases/2.7.6/>`__ programming
   language
4. The `pip <http://www.pip-installer.org/en/latest/installing.html>`__
   package manager for Python

.. note::

  Depending on your experience and operating system, you might
  already be ready to go with everything above. If so, move on to the next
  chapter. If not, don't worry. And don't give up! It will be a bit of a
  slog but the instructions below will point you in the right direction.

.. _command-line-prereq:

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to
open a window that lets you type in commands. Different operating
systems give this tool slightly different names, but they all have some
form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the
"command prompt." Here are instructions for `Windows
8 <http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8>`__
and `earlier
versions <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`__. On Apple computers, you open the `"Terminal"
application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`__. Ubuntu Linux comes with a program of the `same
name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`__.

Text editor
~~~~~~~~~~~

A program like Microsoft Word, which can do all sorts of text formatting
like change the size and color of words, is not what you need. Do not
try to use it below.

You need a program that works with simple `"plain text"
files <https://en.wikipedia.org/wiki/Text_file>`__, and is therefore
capable of editing documents containing Python code, HTML markup and
other languages without dressing them up by adding anything extra. Such
programs are easy to find and some of the best ones are free, including
those below.

For Windows, I recommend installing
`Notepad++ <http://notepad-plus-plus.org/>`__. For Apple computers, try
`TextWrangler <http://www.barebones.com/products/textwrangler/download.html>`__.
In Ubuntu Linux you can stick with the pre-installed
`gedit <https://help.ubuntu.com/community/gedit>`__ text editor.

Python
~~~~~~

If you are using Mac OSX or a common flavor of Linux, Python is probably
already installed and you can test to see what version, if any, is there
waiting for you by typing the following into your terminal.

.. code:: bash

    $ python -V

.. note::

    You don't have to type the "$" It's just a generic symbol
    geeks use to show they're working on the command line.

If you don't have Python installed (a more likely fate for Windows
users) try downloading and installing it from
`here <http://www.python.org/download/releases/2.7.6/>`__.

In Windows, it's also crucial to make sure that the Python program is
available on your system's ``PATH`` so it can be called from anywhere on
the command line. `This
screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`__
can guide you through that process.

Python 2.7 is preferred but you can probably find a way to make most of
this tutorial work with other versions if you futz a little.

pip and virtualenv
~~~~~~~~~~~~~~~~~~

The `pip package
manager <http://www.pip-installer.org/en/latest/index.html>`__ makes it
easy to install open-source libraries that expand what you're able to do
with Python. Later, we will use it to install everything needed to
create a working web application.

If you don't have it already, you can get pip by following `these
instructions <http://www.pip-installer.org/en/latest/installing.html>`__.
In Windows, it's necessary to make sure that the Python ``Scripts``
directory is available on your system's ``PATH`` so it can be called
from anywhere on the command line. `This
screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`__
can help.

Verify pip is installed with the following.

.. code:: bash

    $ pip -V

Act 1: The command line
-----------------------

Working with Python (and pretty much any other programming language)
means becoming comfortable with your computer's command line
environment. If you haven't seen it before, it looks something like
this:

.. figure:: _static/img/terminal.png
  :width: 600 px

Most of what you'll be doing from the command line at this point will be
navigating through directories and running Python files. These actions
require only a few basic commands.

Open the command-line program for your operating system and let's get started.
If you need help finding it refer to the prequisite instructions for the :ref:`command-line-prereq`.

Print the current directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your terminal window is open, before we start moving around the first thing we want to do if find out where you are. If you're using OSX or Linux, type this:

.. code:: bash

    $ pwd

.. note::

    You don't have to type the "$" It's just a generic symbol
    geeks use to show they're working on the command line.

If you're on Windows try:

.. code:: bash

    $ cd

The terminal should print out your current location relative to the root of
your computer's filesystem. In this case, you're in the default directory for your
user, also known as your **home** directory.

It's easy to lose track of which folder you're in when
you're working from the command line, so this is a helpful tool for
finding your way you'll end up using a lot more than you might think.

.. note::

  In case you're curious ``pwd`` standards "present working directory" and ``cd``
  stands for "change directory," a tool we'll use again soon to move between
  folders on your file system.

List files in a directory
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to see all the files and folders in your home directory, there's
another command you need to learn.  On OSX and Linux, type:

.. code:: bash

    $ ls

On Windows:

.. code:: bash

    $ dir

You should now see a list of files and folders appear, such as Downloads, Documents, Desktop, etc. These should look a little familiar. The command line is just another way of navigating the directory structure you're probably used to seeing when
you're clicking around your computer's folders in the user-interface provided
by your operating system.

Change directories
~~~~~~~~~~~~~~~~~~

Now let's move. In order to change directories from the command line, we'll
return to the ``cd`` command we saw earlier, which works for OSX, Linux and Windows.

The only thing you need to do is tell it which directory to move into. In this
case, the following will probably drop you on your desktop.

.. code:: bash

    $ cd Desktop

Now run ``ls`` or ``dir`` to see what files we can find there. They should
mirror what you see on your look at your desktop in your operating system's
user interface.

To move back to our home folder, we'll use the ``cd``
command again, but with a little twist.

.. code:: bash

    $ cd ..

You'll notice that will move you back to the home directory where we began.
When you're working from the command line, it helps to think of your directory structure as a tree. Navigating through the directories is like going higher and lower on various branches. The convention for moving backwards is ``..``

Creating directories and files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might also find it useful sometimes to create files and directories
from the command line. Let's create a folder called ``Code`` under our
home directory that we can use to store code from this class.

Using OSX or Linux, here's how:

.. code:: bash

    $ mkdir Code

In Windows, try this:

.. code:: bash

    $ md Code

Next let's jump into the directory. If you remember, that goes like this:

.. code:: bash

    $ cd Code

If you type ``ls`` or ``dir`` you'll notice that nothing is there. That's because all we've done so far is create a directory, but we haven't put any files in it yet.

You won't have to do this very often, but the command for
creating a blank file in OSX and Linux is called ``touch``. So here's how
you make a new file named ``test.py``.

.. code:: bash

    $ touch test.py

There's no similar command in Windows, but you can accomplish the same thing by saving
a file from a text editor or other program into our new directory.

Deleting directories and files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wanted to remove the file you just made, here's how on OSX and Linux:

.. code:: bash

    $ rm test.py

And here's how in Windows:

.. code:: bash

    $ del test.py

.. warning::

    **This must be done with caution**. Files you delete from the command line DO NOT go into the recycle bin. They are gone. **Forever**.

Act 2: Python
-------------

Python can be used for almost any application you can imagine, from building websites to running robots.

A thorough overview of the language would take months, so our class is going to concentrate on the absolute basics -- the basic programming principles and syntax quirks that you're likely to encounter as complete this course.

How to run a Python program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Python file is nothing more than a text file that has the extension ".py" at the end of its name. Any time you see a ".py" file, you can run it from the command line by typing into the command line:

.. code:: bash

  $ python filename.py

That's it. And it works for both OSX and Windows.

Python also comes with a very neat feature called an **interactive
interpreter**, which allows you to execute Python code one line at a
time, sort of like working from the command line.

We'll be using this a lot in the beginning to demonstrate concepts, but in the real world it's often useful for testing and debugging.

To open the interpreter, simply type ``python`` from your command line, and you should see a screen that
looks like this:

.. figure:: https://f.cloud.github.com/assets/947791/120133/9dc93b9e-6cc8-11e2-8232-4549e69c291b.png
   :alt: Python interactive interpreter

Next we'll use the interpreter to walk through a handful of basic concepts
you need to understand if you're going to be writing code, Python or otherwise.

Variables
~~~~~~~~~

Variables are like containers that hold different types of data so you
can go back and refer to them later. They're fundamental to programming
in any language, and you'll use them all the time.

To try them out, open your Python interpreter.

.. code:: bash

    $ python

Now let's start writing Python!

.. code:: python

    >>> greeting = "Hello, world!"

In this case, we've created a **variable** called ``greeting`` and
assigned it the **string value** "Hello, world!".

In Python, variable assignment is done with the = sign. On the left is
the name of the variable you want to create (it can be anything) and on
the right is the value that you want to assign to that variable.

If we use the ``print`` command on the variable, Python will output "Hello, world!" to
the terminal because that value is stored in the variable.

.. code:: python

    >>> print greeting

Data types
~~~~~~~~~~

Variables can contain many different kinds of data types. There are integers, strings, floating point numbers (decimals), and other types of data that languages like SQL like
to deal with in different ways.

Python is no different. In particular, there are six different data types you will be dealing with on a regular basis: strings, integers, floats, lists, tuples and dictionaries. Here's a little detail on each.

Strings
^^^^^^^

Strings contain text values like the "Hello, world!"
example above. There's not much to say about them other than that they
are declared within single or double quotes like so:

.. code:: python

    >>> greeting = "Hello, world!"
    >>> goodbye = "Seeya later, dude."
    >>> favorite_animal = 'Donkey'


Integers
^^^^^^^^

Integers are whole numbers like 1, 2, 1000 and 1000000.
They do not have decimal points. Unlike many other variable types,
integers are not declared with any special type of syntax. You can
simply assign them to a variable straight away, like this:

.. code:: python

    >>> a = 1
    >>> b = 2
    >>> c = 1000

Floats
^^^^^^

Floats are a fancy name for numbers with decimal points in
them. They are declared the same way as integers but have some
idiosyncracies we'll discover later:

.. code:: python

    >>> a = 1.1
    >>> b = 0.99332
    >>> c = 100.123

Lists
^^^^^

Lists are collections of values or variables. They are
declared with brackets like these [], and items inside are separated by
commas. They can hold collections of any type of data, including other
lists. Here are several examples:

.. code:: python

    >>> list_of_numbers = [1, 2, 3, 4, 5]
    >>> list_of_strings = ['a', 'b', 'c', 'd']
    >>> list_of_both = [1, 'a', 2, 'b']
    >>> list of lists = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]

Lists also have another neat feature: The ability to retrieve individual
items. In order to get a specific item out of a list, you first need to
know its position in that list.

All lists in Python are **zero-indexed**, which means the first item in them sits at position 0.

.. code:: python

    >>> my_list = ['a', 'b', 'c', 'd']
    >>> my_list[0]
    'a'
    >>> my_list[2]
    'c'

You can also extract a range of values by specifiying the first and last
positions you want to retrieve with a colon in between them, like this:

.. code:: python

    >>> my_list[0:2]
    ['a', 'b', 'c']

Tuples
^^^^^^

Tuples are a special type of list that cannot be changed once they are created. That's not especially important right now. All you need to know is that they are declared with parentheses (). For now, just think of them as lists.

.. code:: python

    >>> tuple_of_numbers = (1, 2, 3, 4, 5)
    >>> tuple_of_strings = ('a', 'b', 'c', 'd')

Dictionaries
^^^^^^^^^^^^

Dictionaries are probably the most difficult data type to explain, but also among the most useful. In technical terms, they are storehouses for pairs of keys and values. You can think of them like a phonebook.

An example will make this a little more clear, but know for now that they are declared with curly braces.

.. code:: python

    >>> my_phonebook = {'Mom': '713-555-5555', 'Chinese Takeout': '573-555-5555'}

In this example, the keys are the names "Mom" and "Chinese takeout",
which are declared as strings (Python dictionary keys usually are).

The values are the phone numbers, which are also strings, although
dictionary values in practice can be any data type.

If you wanted to get Mom's phone number from the dictionary, here's how:

.. code:: python

    >>> my_phonebook['Mom']
    713-555-5555

There's a lot more to dictionaries, but that's all you need to know for now.

Control structures
~~~~~~~~~~~~~~~~~~

As a beginner your first Python scripts won't be much more complicated that a series of commands that execute one after another, working together to accomplish a task.

In those situations, it is helpful to be able to control the order and conditions under which those commands will run.

That's where control structures come in -- simple logical operators that
allow you to execute parts of your code when the right conditions call
for it.

Here are two you will end up using a lot.

The if clause
^^^^^^^^^^^^^

If statements are pretty much exactly what they sound like. **If** a
certain condition is met, your program should do something.

Let's start with a simple example.

.. code:: python

    >>> number = 10
    >>> if number > 5:
    >>>    print "Wow, that's a big number!"
    >>>
    Wow, that's a big number!

Our little program in this case starts with a variable, which we've called ``number``, being set to 10. That's pretty simple, and a concept you should be familiar with by this point.

.. code-block:: python
    :emphasize-lines: 1

    >>> number = 10
    >>> if number > 5:
    >>>    print "Wow, that's a big number!"

The next line, ``if number > 5:`` declares our if statement. In this case, we want something to happen if the ``number`` variable is greater than 5.

.. code-block:: python
    :emphasize-lines: 2

    >>> number = 10
    >>> if number > 5:
    >>>    print "Wow, that's a big number!"

Most of the if statements we build are going to rely on equality operators like the kind we learned in elementary school: greater than (>), less than (<), greater than or equal to (>=), less than or equal to (<=) and plain old "equals". The equals operator is a little tricky, in that it is declared with two equals signs (==), not one (=). Why is that? Because you'll remember from above that a single equals sign is the notation we use to assign a value to a variable!

Next, take note of the indentation. In Python, whitespace matters. A lot.  Notice that I said indents must be four spaces. Four spaces means four spaces -- not a tab.

.. code-block:: python
    :emphasize-lines: 3

    >>> number = 10
    >>> if number > 5:
    >>>    print "Wow, that's a big number!"

Tabs and spaces are different. To avoid problems, you should press the space bar four times whenever you indent Python code.

.. note::

  There are some text editors that will automatically convert tabs to spaces, and once you feel more comfortable you might want to use one. But for now, get in the habit of making all indents four spaces.

If you look closely, there's another small detail you need to remember: The colon! When we declare an ``if`` statement, we always end that line with a colon.

.. code-block:: python
    :emphasize-lines: 2

    >>> number = 10
    >>> if number > 5:
    >>>     print "Wow, that's a big number!"
    >>>
    >>> print "I execute no matter what your number is!"

It helps sometimes to think of your program as taking place on different levels.

In this case, the first level of our program (the one that isn't indented) has us declaring the variable ``number = 10`` and setting up our if condition, ``if number > 5:``.

The second level of our program executes only on the condition that our if statement is true. Therefore, because it depends on that if statement, it is indented four spaces.

If we wanted to continue our program back on the first level, we could do something like this:

.. code-block:: python
    :emphasize-lines: 5

    >>> number = 10
    >>> if number > 5:
    >>>     print "Wow, that's a big number!"
    >>>
    >>> print "I execute no matter what your number is!"
    >>>
    Wow, that's a big number!
    I execute no matter what your number is!

The last statement doesn't depend on the ``if`` statement, so it will always run.

The else clause
^^^^^^^^^^^^^^^

Now let's talk about a common companion for ``if`` statement -- the ``else`` clause. It can be combined with an ``if`` statement to have the script execute a block of code when it turns out not to be true.

You don't need to have an ``else`` condition for your ``if`` statements, but sometimes it helps. Consider this example:

.. code-block:: python
    :emphasize-lines: 4,5

    number = 10
    if number > 5:
        print "Wow, that's a big number!"
    else:
        print "Gee, that number's kind of small, don't you think?"

In this case, we're telling our program to print one thing if ``number`` is greater than five, and something else if it's not. Notice that the ``else`` statement also ends with a colon, and as such its contents are also indented four spaces.

For loops
^^^^^^^^^

Remember earlier we discussed the concept of a list -- the type of
variable that can hold multiple items in it all at once?

Many times during your programming career, you'll find it helps to run through an entire list of items and do something with all of them, one at a time.

That's where for loops come in. Let's start by having Python say the ABC's:

.. code:: python

    >>> list_of_letters = ['a', 'b', 'c']
    >>> for letter in list_of_letters:
    >>>     print letter
    >>>
    a
    b
    c

The output of this statement is what you might guess. But there are still a few things to unpack here -- some familiar and some not.

First, you'll notice from looking at the print statement that our
indentation rules still apply. Everything that happens within the for
loop must still be indented four spaces from the main level of the
program. You'll also see that the line declaring the loop ends in a
colon, just like the if and else statements.

Second, turn your attention to the syntax of declaring the loop itself.

.. code-block:: python
    :emphasize-lines: 2

    >>> list_of_letters = ['a', 'b', 'c']
    >>> for letter in list_of_letters:
    >>>     print letter

All of our for loops start, unsurprisingly, with the word ``for`` and
follow the pattern ``for variable_name in list:``. The ``variable\_name``
can be anything you want -- it's essentially just a new variable you're
creating to refer to each item within your list as the ``for`` loop iterates
over it.

In this case we chose``letter``, but you could just as easily call it ``donkey``, like so:

.. code-block:: python
    :emphasize-lines: 2

    >>> list_of_letters = ['a', 'b', 'c']
    >>> for donkey in list_of_letters:
    >>>     print donkey

The next thing you have to specify is the list you want to loop over, in
this case ``list_of_letters``. The line ends with a colon, and the next
line starts with an indent. And that's the basics of building a loop!

Functions
^^^^^^^^^

Often it's helpful to encapsulate a sequence of programming instructions into little tools that can be used over and over again. That's where functions come in.

Think of functions like little boxes. They take input (known as **arguments**), perform some operations on those arguments, and then return an **output**.

In Python, a simple function might take an integer and divide it by two, like this:

.. code-block:: python

    >>> def divide_by_two(input):
    >>>    return input / 2.0

In order to call that function later in the program, I would simply have
to invoke its name and feed it an integer -- any integer at all -- like
so:

.. code-block:: python
    :emphasize-lines: 3,4

    >>> def divide_by_two(input):
    >>>    return input / 2.0
    >>> divide_by_two(10)
    5

Once you write a function (assuming it works) you don't need to know what's inside. You can just feed it an input and expect an output in return.

Every function must be declared by the word ``def``, which stands for "define". That is followed by the name of the function (like a loop you can call it anything you want, but you should aim for it to make some sense), and then a set of parentheses in which you can define the arguments the function should expect.

.. code-block:: python
    :emphasize-lines: 1

    >>> def get_half(input):
    >>>    return input / 2.0

In our example above, our ``divide_by_two`` function expects one
argument, which we've called ``input`` -- basically the number
that we want to divide by two.

When we feed it the number, like the number 10, a variable by the name of our argument is created within the function. You can name that what you want too.

.. code-block:: python
    :emphasize-lines: 1,2

    >>> def get_half(num):
    >>>    return num / 2.0

After you finish declaring arguments, you'll see something familiar --the colon. Just like the ``if`` statements and ``for`` loops, the next line must be indented four spaces because any code within the function is nested one level deeper than the base level of the program.

The final thing you'll need to know about function notation in Python is that most functions return some kind of output. Arguments go in, some processing happens, and something comes out. That's what the ``return`` statement is for.

.. code-block:: python
    :emphasize-lines: 2

    >>> def get_half(num):
    >>>    return num / 2.0

Functions don't necessarily need arguments, nor do they always need to return a value using the ``return`` command. You could also do something like this:

.. code-block:: python

    def say_hello():
        print "Hello!"

But the idea of arguments and ``return`` values are still fundamental in
understanding functions, and they will come up more often than not.

Python as a toolbox
^^^^^^^^^^^^^^^^^^^

Lucky for us, Python already has tools to do pretty much anything you'd
ever want to do with a programming language: everything from navigating
the web to scraping and analyzing data to performing mathematical
operations to building websites.

Some of these are built into a toolbox that comes with the language, known as the **standard library**. Others have been built by members of the developer community and can be downloaded and installed from the web.

There are two ways to import these tools into your scripts, which we'll demonstrate here:

To pull in an entire toolkit, use the ``import`` command. In this case,
we'll get the ``urllib2`` package, which allows us to visit websites
with Python:

.. code-block:: python

    >>> import urllib2
    >>> urllib2.urlopen("http://www.python.org/")

You can also import specific tools from inside a toolkit using something like this:

.. code-block :: python

    >>> from urllib2 import urlopen
    >>> urlopen("http://www.python.org/")

In practice, you'll use both of these methods. It's worth noting that
most of the time, any import statements you execute should be at the
top of your program.

Act 3: Web scraping
-------------------

A webpage is made of three major components:

-  HTML -- Hypertext Markup Language -- This is creates the structure of
   a webpage.
-  CSS -- Cascading Style Sheets -- This creates the style on a webpage.
-  Javascript -- This is used to create interactive effects on a
   webpage.

For our use cases, the most important part is the HTML.

General HTML
~~~~~~~~~~~~

In order to scrape a website, we need to understand what each of these
pieces do. HTML is the frame work contains the content of a page.
Without HTML, you do not have a webpage.

To view the HTML code, open up Chrome, load `your web
page <http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp>`__,
and right click on 'View Source'.

.. figure:: https://f.cloud.github.com/assets/166734/1318115/455e7fec-32b5-11e3-93c8-d67247faad1c.png
   :alt: screen shot 2013-10-11 at 3 39 09 pm

   screen shot 2013-10-11 at 3 39 09 pm
HTML has markers that denote the start and end of the HTML
``<html></html>``. Inside the html tag, there are two main sections that
are the head and the body.

::

    <html>
        <head>
        </head>
        <body>
        </body>
    </html>

In the case of well formatted HTML, the page will be made of nested HTML
elements. In all our examples, we have decently formatted html. There
are cases in the real work where this is not the case. Then solving for
this becomes an additional problem to solve for.

The part that we are interested in is the body tag. Some where in there
lies our content. To acces this more easily, we will use Chome's
inspector. Right click on the table of data that you are interested in
and select 'inspect element'.

.. figure:: https://f.cloud.github.com/assets/166734/1320358/7f309dae-3355-11e3-88db-5249ae5678e7.png
   :alt: Inspect the element

   Inspect the element
Your browser will open Chrome's inspector and display the HTMLs and
highlights the code where the table is.

.. figure:: https://f.cloud.github.com/assets/166734/1320348/f12d3206-3354-11e3-8ef9-b6a4540e526b.png
   :alt: Inspector with the highlighted element

   Inspector with the highlighted element
There are many ways to grab content from HTML. In our case, we extract
content by the 'id' or 'class'. These are called CSS selectors. An 'id'
ids a specific item on a page. If used corrected, there should be only
one 'id' on page, but it is always not used correctly. A 'class' ids a
specific type of item on a page. So, there maybe may instances of a
class on a page.

In our crime example, there is only table. The table is identified by a
class.
``<table class="resultsTable" style="margin: 0 auto; width: 90%; font-size: small;">``
While this example only has one instance of the class, it should be
noted that it is possible that there maybe multiple instances of
``class="resultsTable"`` on the page.

Inspecting a form
~~~~~~~~~~~~~~~~~

In our `second example
script <http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx>`__,
we are trying to scrape data that we get back from a form. In the simple
script, we start with a default url, but in
`salaries-full.py <https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-full.py>`__
and
`salaries-mechanize.py <https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-mechanize.py>`__,
we identify the form and set the search in python.

Looking at our example, search and find the form tag that is wrapped
about the fields that are you interested in. Most of the time, this is
tightly wrapped around the fields, however in this case, the
``<form></form>`` is wrapped around the whole page. This is not the best
designed HTML page, but it still works, so that's all we care about.

::

    <form name="ctl01" method="post" action="searchemployees.aspx" id="ctl01">

The form tag have a couple of pieces of information that we need to
know.

-  name -- identifies the form. This must be unique.
-  method -- the action of the data that is being transfered. See
   requests section for more information on what 'post' means.
-  id -- this is a CSS Selector, which was discussed earlier. In this
   case the id and name is the same.

We will use the name to identify the form in our code. The reason for
using the name over the id is that while ids are supposed to be unique
on a page, sometimes they are not. In our code, we would be

::

    br.select_form("ctl01")

Now, we need to identify the fields in form. On `this
page <http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx>`__,
we will want to start by right clicking and 'inspect element'. Do this
on the form, until you identify the 'id' of the form value. To know that
you have the right element to match to the code you are looking at, you
will see it highlighted in your browser.

.. figure:: https://f.cloud.github.com/assets/166734/1320458/b5bae160-335d-11e3-9b06-f55cab13161f.png
   :alt: Highlighted element

   Highlighted element
For the calendar element, we can see that the name of the select tag is
"SearchEmployees1:math:`CalendarYear1`\ ddlCalendarYear". If you look at
`salaries-full.py <https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-full.py>`__
and
`salaries-mechanize.py <https://github.com/ireapps/scraping-class/blob/master/scrapers/salaries/salaries-mechanize.py>`__,
you will see the form fields that we define by using this technique. In
our script, we set those fields to specific values.

.. code:: python

    # Each control can be set. Dropdown lists are handled as lists, text fields take text
    br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
    br.form['SearchEmployees1$ddlAgencies'] = ['931']
    br.form['SearchEmployees1$txtLastName'] = '%'

**SPECIAL NOTE:** *Notice the last name field is set to a ``%``. The
``%`` is a wildcard character. This tells the database that you want to
grab everything. The other wildcard to try is ``*``. If a web form was
going to accept a wildcard, it will be one of these two. Often websites,
don't allow wildcards.*

In our program, then we use these and submit the values in the form.
This brings us to the idea of requests. The next section is not required
understanding, but it will help in understanding how a form works.

Requests -- Methods and Statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request methods
^^^^^^^^^^^^^^^

Understanding a little about requests is helpful when troubleshooting
what is happening on website. A request is how you communicate with the
server that hosts the website that you are interacting with. For
example, when you type 'google.com' in your browser's address bar and
press enter, you are sending a request to *GET* that content. There are
two types of request methods that you should understand.

-  GET
-  POST

A GET request method is basically the retrival of the content of a web
page. A POST request method is what happens when you submit information
via a web form.

This is available in the *Header* information of a web page, which can
be found in the Inspector also. When you have the Inspector open, try
clicking on the 'Network' tab. (The default tab is Elements. The Network
tab should be two over.)

.. figure:: https://f.cloud.github.com/assets/166734/1330753/2b68b952-3537-11e3-90d7-aaee3bc00036.png
   :alt: Network Tab

   Network Tab
Now refresh the page. You will see the Network activity populate as the
page loads. A web page is made of many requests. We are looking for the
main one, which is the first one in this case.

.. figure:: https://f.cloud.github.com/assets/166734/1331278/afeaa778-354e-11e3-8d3b-e5ccf2f13a3b.png
   :alt: Jail get method

   Jail get method
Look at the line that says:

::

    JailResidents.asp
    /sheriff/JailResidents

You will see that the method is "GET".

Now let's try this while submitting a form for Missouri `state employee
salaries <http://mapyourtaxes.mo.gov/MAP/Employees/Employee/searchemployees.aspx>`__.
Load the page. Open up the inspector. Click on the "Network" tab. Fill
out the form on the web page and hit submit.

At the top of the Network tab, you will see a request that occurred when
you submitted the form -- the method is "POST" instead of "GET".

.. figure:: https://f.cloud.github.com/assets/166734/1331302/f6a41cb6-354f-11e3-87d6-7ddadc0fb10a.png
   :alt: Salary posts

   Salary posts
Request statuses
^^^^^^^^^^^^^^^^

The Network tab is full of useful information. Another bit to take
notice of are the values under status. These are HTTP status codes. In
both of our examples, we had a 200, which is okay. The 200 is a common
return value. Other return values which you may see often are the 404,
which means that the content was not found and another is 301 or 302,
which means that the request was redirected. Understanding these codes
can help you in the troubleshooting process if the site that you
requesting doesn't seem to be behaving in the way that you expect.
Wikipedia's `List of HTTP
Statuses <http://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__ is
a great reference to learn more about what these codes mean.

Header information
^^^^^^^^^^^^^^^^^^

Lastly, you should take note of header information. This is also found
in the Network tab. After you go through the process of loading a
request, click on the name and path column on the left. You will load
more detailed information for that name and path on the right. The
default tab is the Headers tab.

.. figure:: https://f.cloud.github.com/assets/166734/1331412/6f3501c2-3555-11e3-91ff-32f65b8afead.png
   :alt: Headers sample info

   Headers sample info
The Headers tab includes information like the request method and the
status, but a lot more also.

::

    Request URL:http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchEmployees.aspx
    Request Method:POST
    Status Code:200 OK
    ..... more

Notice near the bottom of the content we have our form variables that
are being submitted as part of the request made.

::

    SearchEmployees1$CalendarYear1$ddlCalendarYear:2013
    SearchEmployees1$ddlAgencies:931
    SearchEmployees1$txtLastName:
    SearchEmployees1$txtFirstName:
    SearchEmployees1$btnSearch:GO
    ..... more

