```{include} _templates/nav.html
```

# Act 1: The command line

Working with Python (and pretty much any other programming language)
means becoming comfortable with your computer's command line
environment. If you haven't seen it before, it looks something like
this:

```{figure} _static/img/terminal.png
:width: 600 px
```

In this lesson we'll use it to give the computer direct commands to manage files, navigate through directories and execute Python scripts. If that sounds scary, don't worry, it'll only require only a few basic commands we'll cover now.

Open the command-line program for your operating system and let's get started.
If you need help finding it refer to the prequisite instructions for the {ref}`command-line-prereq`.

### Print the current directory

Once your terminal window is open the first thing we want to do if find out where you are. If you're using OSX or Linux, type this:

```bash
pwd
```

If you're on Windows try:

```bash
cd
```

The terminal should print out your current location relative to the root of your computer's filesystem. In this case, you're probably in the default directory for your user, also known as your **home** directory.

It's easy to lose track of which folder you're in when
you're working from the command line, so this is a helpful tool for
finding your way. You'll end up using it a lot more than you might think.

```{note}
In case you're curious, `pwd` standards "present working directory" and `cd`
stands for "change directory," a tool we'll use again soon to move between
folders on your file system.
```

### List files in a directory

In order to see all the files and folders in a directory, there's
another command you need to learn.  On OSX and Linux, type:

```bash
ls
```

On Windows:

```bash
dir
```

You should now see a list of files and folders appear, such as Downloads, Documents, Desktop, etc. These should look a little familiar. The command line is just another way of navigating the directory structure you're probably used to seeing when
clicking around your computer's folders in the user-interface provided
by your operating system.

### Change directories

Now let's move. In order to change directories from the command line, we'll
return to the `cd` command we saw earlier, which works for OSX, Linux and Windows.

The only thing you need to do is tell it which directory to move into. In this
case, the following will probably drop you on your desktop.

```bash
cd Desktop
```

Now run `ls` or `dir` to see what files we can find there. They should
mirror what you see as you look at your desktop in your operating system's
user interface.

To move back to our home folder, we'll use the `cd`
command again, but with a little twist.

```bash
cd ..
```

You'll notice that will move you back to the home directory where we began.
When you're working from the command line, it helps to think of your directory structure as a tree. Navigating through the directories is like going higher and lower on various branches. The convention for moving backwards is `..`

### Creating directories and files

You might also find it useful sometimes to create files and directories
from the command line. Let's create a folder called `Code` under our
home directory that we can use to store code from this class.

Using OSX or Linux, here's how:

```bash
mkdir Code
```

In Windows, try this:

```bash
md Code
```

Next let's jump into the directory. If you remember, that goes like this:

```bash
cd Code
```

If you type `ls` or `dir` you'll notice that nothing is there. That's because all we've done so far is create a directory, but we haven't put any files in it yet.

You won't have to do this very often, but the command for
creating a blank file in OSX and Linux is called `touch`. So here's how
you make a new file named `test.py`.

```bash
touch test.py
```

There's no similar command in Windows, but you can accomplish the same thing by saving
a file from a text editor or other program into our new directory.

### Deleting directories and files

If you wanted to remove the file you just made, here's how on OSX and Linux:

```bash
rm test.py
```

And here's how in Windows:

```bash
del test.py
```

```{warning}
**This must be done with caution**. Files you delete from the command line do not go into the recycle bin. They are gone. **Forever**.
```

And that's it! You've learned all the basic command-line tricks necessary to move on.
