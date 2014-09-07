# Intro to Github

[Git](http://git-scm.com/) and [Github](https://github.com/) (or the like, i.e. [Gitlab](https://www.gitlab.com/)) are tools to help you manage your code and collaborate.

[Git](http://git-scm.com/) is an open source tool that allows you to store code, track the changes that you made, and collaborate with others.

[Github](https://github.com/) (or the like, i.e. [Gitlab](https://www.gitlab.com/)) act as an external place that you can use get in a place that is accessible to others. As you may have noticed, this project is hosted on Github.

These tools are great tools that you should have in your tool belt. These notes, walk through the very basic usage of Git and communities like Github.

### Why are these tool important?

Git is easiest to understand through online communities such as Github. On Github, you can find the code for a lots of projects that you can use! Here are some interesting ones:

- [MIZZOU/IRE Scraping Class](https://github.com/ireapps/scraping-class)
  Here, you will find the code that we worked on during the class.
- [Requests library](https://github.com/kennethreitz/requests)
  Requests is the python library that we used in the class.
- [CSVkit](https://github.com/onyxfish/csvkit)
  CSVkit is another tool that you can use to interact with csvs.
- [United States](https://github.com/unitedstates/)
  This is a repo of data that is across the whole country.
- [Derek Willis](https://github.com/dwillis)
  A very active journalist on github.
- etc.

Essentially, this repositories of code are available for you to use and contribute to OR you can create your own and share it with others.

Lastly, you can use Github to store your own code for your own sanity and tracking. A lot of people use this space as a scratch pad, so don't worry about sharing you project while it is in development.

However, if you want to hide your projects, you can do one of the following:
- Free private repositories for eduction: [Github Education](https://education.github.com/)
- Pay monthly fee for github: [Github](https://www.github.com/)
- Free private repositories: Join [Gitlab](https://www.gitlab.com/)

## Setting up

So, how do I get started?
Tell me more!!
<p align="left">
  <img src="https://cloud.githubusercontent.com/assets/166734/4176539/537eac8e-3609-11e4-8652-35e410cb68f8.gif" alt="Tell me more"/>
</p>

To start using, there are two major things for our set up that we need to do.
- Install git on your machine
- Sign up for Github

Note: Gitlab is much the same, but a different layout. For this tutorial, we are using Github.

### Set up on your machine

You will only have to do the following once on your current machine.

#### Install Git

- Mac: Run this on your commandline: ```brew install git```
 - If you do not have homebrew, you will need to install homebrew, then rerun the command above.

   ```ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"```

- Windows: If you're already using Cygwin, [follow these instructions](http://www.celinio.net/techblog/?p=818) to install Git inside Cygwin. If you're not using Cygwin, download and install the following: http://msysgit.github.io

More info: http://git-scm.com/book/en/Getting-Started-Installing-Git

#### Copy the class repo to your computer

This is to make sure that your setup works.

```cd``` into the folder where you want the folder to be

```git clone https://github.com/ireapps/scraping-class.git```

Now, you should be able to ```cd``` into the folder and run some of the class scripts that are located in the git repository: https://github.com/ireapps/scraping-class

Try the following:

```
cd scraping-class/scrapers/crime/
python jailscrape.py
```

This should produce an output and create a csv in the crime folder.

```
ls
README.md              jailscrape.py          out-using-requests.csv
```

Let's sign up for Github and create our own repos!

### Sign up for Github

#### Visit Github.com and create your user name and password
<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/166734/4176375/85273d86-3600-11e4-936d-101b272cc62e.png" alt="Github homepage"/>
</p>

#### Select the free plan
<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/166734/4175590/32999e8e-35dc-11e4-960b-7880744d148c.png" alt=""/>
</p>

#### Your profile page (or in this case, [Ellie's](https://twitter.com/ellie_the_brave) profile page)
<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/166734/4175599/b38ed07c-35dc-11e4-98a3-3140d33ae426.png" alt="Github profile page"/>
</p>





#### Set your username and email up

```
git config --global user.name "elliethebrave"
git config --global user.email "elliesemail@somedomain.com"
```


## Let's set up our first repository

In the top right of the page, select create ```New Repository``` from the  ```+ ``` menu next to your name on the top right.

<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/166734/4176397/dfb79b96-3601-11e4-9267-ed543aac62b0.png" alt="Github create repository menu"/>
</p>

Then you will get a blank form to fill out.

<p align="center">
  <img src="https://cloud.githubusercontent.com/assets/166734/4176557/696e8e82-360a-11e4-995b-d87ec90d3c0e.png" alt="Github create repository form"/>
</p>

Things to consider on this form:
* Naming the repository -- choose something that means something. We named this repository 'scraping-class', because that is what it is.
* Description helps others who are visiting understand your code.
* Public/Private -- Public means everyone sees it. Private means only you see it.
* Initialize with README.md, means you start the repo with a README file -- this is important for your future self and others to understand the project.
* Add git ignore for Python repos.
* Licensing -- by default you own the copyright, but you should throw one on their of you choice just to be nice to others.

Submit the filled out form.

