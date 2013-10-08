# Navigating the command line

Working with Python, Django and pretty much any other programming language means becoming comfortable with your computer's command line environment. If you haven't seen it before,
it looks something like this:

![OSX terminal window](https://f.cloud.github.com/assets/947791/119759/801b7d6a-6cb3-11e2-8eab-d3c9f2dcac15.png)

In basic terms, the command line allows you to communicate with your computer at a lower level that is more explicit than the user-friendly graphical environments that you typically
use. This has both advantages and disadvantages. The good thing about learning a little about the command line is that is enables you to configure your computer in new ways, and to
run software that simply doesn't work in a graphical environment. The downside is that it takes a little time to learn. Here we'll walk you through most of the basics you'll need to know to succeed in this class.

## Opening the command line

Both Windows and OSX have built-in tools for accessing the command line.

On OSX, click on the **Spotlight** icon at the upper-right hand corner of your screen and type **Terminal**. You should see a program with the same name appear. Click on it to open your command prompt. However, to take that one step further, I recommend using a piece of software called iTerm2, which can be downloaded and installed [here](http://www.iterm2.com/#/section/home).

On Windows, navigate to the **Start Menu** and find the box called **Run**. Click on it. In the box that appears, type the letters **cmd**. This should open up your command prompt.

## Basic commands (OSX)

Most of what you'll be doing from the command line at this point will be navigating through directories and running Python files. These actions require only a few basic commands, which I'll cover here. Windows and OSX have slightly different syntaxes for their terminal commands, so we'll go over OSX first.

### Listing and changing directories

Once your terminal window is open, type ```pwd``` and you should see a directory path returned. Something like ```/Users/whatever_your_username_is```. PWD stands for "present working directory." It's basically your current location relative to the root of your filesystem. It's easy to lose track of which folder you're in when you're working from the command line, so it can be a helpful tool for finding your way. In this case, you're in the default directory for your username on the computer, also known as your **home directory**.

In order to see all the files and folders in your home directory, type the ```ls``` command. Once you do that, you should see a list of files and folders appear, such as Downloads, Documents, Desktop, etc. These should look a little familiar. The command line is just another way of navigating the directory structure you're probably used to seeing when you're clicking around your Mac.

To take that point one step further, let's go into the Desktop folder. In order to change directories from the command line, use the ```cd``` command, along with the directory you want to change to. In this case ```cd Desktop``` will take you into the desktop. Type ```ls``` again to list the contents of the folder, and you should find that they mirror what you see when you look at your desktop.

Now let's move back to our home folder. Again we'll use the ```cd```  command, but with a little twist. If you type ```cd ..``` and hit enter, you'll notice that you move back to the home directory that you were just in. When you're working from the command line, it helps to think of your directory structure as a tree. Navigating through the directories is like going higher and lower on various branches. The convention for moving backwards is the ```..``` notation.

### Creating and deleting files

You might also find it useful sometimes to create files and directories from the command line. Let's create a folder called "apps" under our home directory that we can use to store code from this class. The command for doing that is simply ```mkdir apps``` with mkdir being short for "make directory." If you type ```ls``` again, you should see your new apps directory listed along with the files and folders from before.

The next step is to navigate into our apps directory and make a file. As before, use the ```cd apps``` command to enter your apps directory. If you type ```ls``` you'll notice that nothing is there. That's because all we've done so far is create a directory, but we haven't put any files in it yet. You won't have to do this very often, but the command for creating a blank file in OSX is called ```touch```. Let's create a test python file that we can use later: ```touch test.py```. Notice the .py file extension. It's extremely important when working from the command line to be mindful of file extensions. The .py notation tells our computer that this is a Python file, meaning it needs to be run by the Python interpreter. You'll see more about what that means later. For now, if you type ```ls``` again, you should see the file in your apps directory.

The final task you might want to perform from the command line in this class is deleting files. Note that **this must be done with caution**. Files you delete from the command line DO NOT go into the recycle bin. They are gone. **Forever**. So don't delete anything this way unless you're absolutely sure you know what you're doing. That said, the command is very simple. First, let's create a new file to delete with ```touch deleteme.py```. Now to delete it, simply type ```rm deleteme.py```

### Quick review

Really, that's most of what you should need to navigate the command line for this class. As a quick review:

<table>
    <tr>
        <th>Command</th>
        <th>Example</th>
        <th>What it does</th>
        <th>Notes</th>
    </tr>
    <tr>
        <td>pwd</td>
        <td>pwd</td>
        <td>Shows your present working directory</td>
        <td>Useful for keeping track of where you are</td>
    </tr>
    <tr>
        <td>ls</td>
        <td>ls</td>
        <td>Shows the contents of the current directory</td>
        <td>Can also use ls -a or ls -l to show more information about files</td>
    </tr>
    <tr>
        <td>cd</td>
        <td>cd Desktop</td>
        <td>Changes directories</td>
        <td>Use cd ..``` to move backwards</td>
    </tr>
    <tr>
        <td>mkdir</td>
        <td>mkdir new-directory</td>
        <td>Creates a new directory</td>
        <td></td>
    </tr>
    <tr>
        <td>touch</td>
        <td>touch test.py</td>
        <td>Creates a new file</td>
        <td></td>
    </tr>
    <tr>
        <td>mv</td>
        <td>mv test.py ./Desktop</td>
        <td>This isn't covered above, but mv moves or renames a file.</td>
        <td></td>
    </tr>
    <tr>
        <td>rm</td>
        <td>rm test.py</td>
        <td>Deletes a file</td>
        <td>Use with extreme caution. Once a file is deleted this way, you can't get it back.</td>
    </tr>
</table>


## Basic commands (Windows)

The principles of working from the command line are the same in Windows as they are on Macs. The only thing that's different is the syntax. Here's a rundown of the equivalent commands:

<table>
    <tr>
        <th>OSX command</th>
        <th>Windows equivalent</th>
    </tr>
    <tr>
        <td>pwd</td>
        <td>cd (with no arguments)</td>
    </tr>
    <tr>
        <td>ls</td>
        <td>dir or dir -p</td>
    </tr>
    <tr>
        <td>cd</td>
        <td>cd followed by the directory name (ex. cd Desktop)</td>
    </tr>
    <tr>
        <td>mkdir</td>
        <td>md</td>
    </tr>
    <tr>
        <td>touch</td>
        <td>None (sorry!)</td>
    </tr>
    <tr>
        <td>mv</td>
        <td>move</td>
    </tr>
    <tr>
        <td>rm</td>
        <td>del</td>
    </tr>
</table>

## Tips and tricks

Working from the command line can be difficult and tedious at first. Here are a few tips for making your command line lives a little easier:

**Tab completion**: It's very easy to typo commands, which can lead to errors and unintended consequences. One way of helping to avoid that problem is using tab completion, which allows the computer to finish typing a command that you have begun. Say you're in your home directory and want to go to the Desktop -- you'd type ```cd Desktop```, right? You could also type ```cd Des <tab>``` and the computer would fill out the remaining text to spell "Desktop". This is a huge time-saver, especially when you're typing long directory paths (think something like ```cd Desktop/projects/apps/django/test-app/test/apps/models.py```). [Here's a demo](http://www.youtube.com/watch?v=N8TaSgKJ-LM) of tab completion in action.

**Go straight home**: Your home directory is sort of like True North in command line world. It's a great way to orient yourself if you end up lost in the file system. In OSX, no matter where you are in the directory structure, you can immediately get back home by either typing ```cd``` or ```cd ~/```.

**Guides and cheat sheets**: [Here's](http://wiseheartdesign.com/articles/2010/11/12/the-designers-guide-to-the-osx-command-prompt/) a useful guide for simple command line syntax on OSX and Linux. And [here's](http://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/) another one for Windows.
