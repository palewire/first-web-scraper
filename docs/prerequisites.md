```{include} _templates/nav.html
```

# Prerequisites

Before you can begin, your computer needs the following tools installed
and working to participate.

1. A [command-line
   interface](https://en.wikipedia.org/wiki/Command-line_interface)
   to interact with your computer
2. A [text editor](https://en.wikipedia.org/wiki/Text_editor) to work
   with plain text files
3. Version 3.10 of the
   [Python](https://www.python.org/downloads/release/python-3108/) programming
   language. The current version as of July 2023 is Python 3.10.8.
4. The [pip](https://pip.pypa.io/en/latest/installing.html)
   package manager for Python

Depending on your experience and operating system, you might already be ready to go with everything above. If so, move on to the next chapter. If not, don't worry. And don't give up! It will be a bit of a slog but the instructions below will point you in the right direction.

```{note}
One potential shortcut is using [GitHub codespaces](https://github.com/features/codespaces) instead of setting up your own computer. It's free and will let you use the command line and run Python without having to download a thing.
```

(command-line-prereq)=

### Command-line interface

Unless something is wrong with your computer, there should be a way to
open a window that lets you type in commands. Different operating
systems give this tool slightly different names, but they all have some
form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the
"command prompt." Here are instructions for [Windows
8](http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8)
and [earlier
versions](http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window). On Apple computers, you open the ["Terminal"
application](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line). Ubuntu Linux comes with a program of the [same
name](http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it).

### Text editor

A program like Microsoft Word, which can do all sorts of text formatting
like change the size and color of words, is not what you need. Do not
try to use it below.

You need a program that works with simple ["plain text"
files](https://en.wikipedia.org/wiki/Text_file), and is therefore
capable of editing documents containing Python code, HTML markup and
other languages without dressing them up by adding anything extra. Such
programs are easy to find and some of the best ones are free, including
those below.

For Windows, I recommend installing
[Notepad++](http://notepad-plus-plus.org/). For Apple computers, try
[TextWrangler](http://www.barebones.com/products/textwrangler/download.html).
In Ubuntu Linux you can stick with the pre-installed
[gedit](https://help.ubuntu.com/community/gedit) text editor.

### Python

If you are using Mac OSX or a common flavor of Linux, Python is probably
already installed and you can test to see what version, if any, is there
waiting for you by typing the following into your terminal.

```bash
python -V
```

If you don't have Python installed (a more likely fate for Windows
users) try downloading and installing it from
[here](https://www.python.org/downloads/release/python-3108/).

In Windows, it's also crucial to make sure that the Python program is
available on your system's `PATH` so it can be called from anywhere on
the command line. [This
screencast](http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96)
can guide you through that process.

Python 3.10 is preferred but you can probably find a way to make most of
this tutorial work with other versions if you futz a little.

(command-line-pip)=

### pip

The [pip package
manager](https://pip.pypa.io/en/latest/) makes it
easy to install open-source libraries that expand what you're able to do
with Python. Later, we will use it to install everything needed to
create a working web application.

If you don't have it already, you can get pip by following [these
instructions](https://pip.pypa.io/en/latest/installing.html).
In Windows, it's necessary to make sure that the Python `Scripts`
directory is available on your system's `PATH` so it can be called
from anywhere on the command line. [This
screencast](http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96)
can help.

Verify pip is installed with the following.

```bash
pip -V
```
