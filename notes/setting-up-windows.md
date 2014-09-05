
# Windows Install

Make sure that you have already installed [Chrome](https://www.google.com/chrome/browser/) and [Sublime Text](http://www.sublimetext.com/).

Next, we'll be installing Cygwin, but make sure to read these instructions before you begin. 

1. Go to [Cygwin](https://cygwin.com/install.html) and download either the 32-bit or 64-bit version of the software, based on your computer.
2. Once it's downloaded, click on the .exe to start the setup.
3. Keep clicking "Next" until you see "Choose A Download Site." Here, you can pick any of the sites listed to keep installing Cygwin. Click Next.
4. When you see "Select Packages", click into the search box and type "setuptools."
5. Click on the plus icon to open up the "Python" folder, and then click on the icon next to "python-setuptools", no need to select "python3-setuptools.
6. Click the box under column "S" so that both boxes should now be checked.
7. Click next until you finish the install.

When Cygwin is finished, type the commands below into Cygwin, one line at a time, and then hit enter. When each command is finished running, type the next one.

* easy_install pip
* pip install beautifulsoup
* pip install requests
* pip install mechanize
