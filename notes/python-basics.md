# Getting started with Python

Python is a rich and fully featured language that can be used for almost any application you can imagine, from building websites to running robots. A thorough overview of the language would take months, so our class is going to concentrate on the absolute basics -- basic programming principles and syntax quirks that you're likely to encounter as you start learning how to program. This isn't intended to be a comprehensive Python tutorial. It's only meant to give you the basic skills you'll need to succeed in this course. That said, I would highly encourage you to explore the language further and will provide materials to do so at the end of this guide.

## How to run a Python program

Most Python code is run directly from the command line, which explains why it is so important that you master some command line basics. Recall from the [command line tutorial](https://github.com/ireapps/scraping-class/blob/master/notes/command-line-basics.md) that Python files have the file extension ".py". Any time you see a ".py" file, you can run it from the command line simply by typing ```python filename.py```, where filename is the name of whatever the file is. That's it. And it works for both OSX and Windows.

Python also comes with a very neat feature called an **interactive interpreter**, which allows you to execute Python code one line at a time, sort of like working from the command line. We'll be using this a lot in the beginning to demonstrate concepts, but in the real world it's often useful for testing and debugging. To open the interpreter, simply type ```python``` from your command line, and you should see a screen that looks like this:

![Python interactive interpreter](https://f.cloud.github.com/assets/947791/120133/9dc93b9e-6cc8-11e2-8232-4549e69c291b.png)

We'll get into more detail about that later.

## Variables and data types

No matter whether you're working in Python or another language, there are a handful of basic concepts you need to understand if you're going to be writing code. We'll walk through those here.

### Variables

Variables are like containers that hold different types of data so you can go back and refer to them later. They're fundamental to programming in any language, and you'll use them all the time. Here's an example

```
greeting = "Hello, world!"
print greeting
```

In this case, we've created a **variable** called ```greeting``` and assigned it the **string value** "Hello, world!". If we use the ```print``` command on the variable, Python will output "Hello, world!" to the terminal because that value is stored in the variable.

In Python, variable assignment is done with the = sign. On the left is the name of the variable you want to create (it can be anything) and on the right is the value that you want to assign to that variable. Variables can also contain many different kinds of data types, which we'll go over next:

### Data types

You may remember from earlier data journalism classes that data comes in different types and flavors. There are integers, strings, floating point numbers (decimals), and other types of data that languages like SQL like to deal with in different ways. Python is no different. In particular, there are six different data types you will be dealing with on a regular basis: strings, integers, floats, lists, tuples and dictionaries. Here's a little detail on each.

**Strings**: Strings contain text values like the "Hello, world!" example above. There's not much to say about them other than that **they are declared within single or double quotes** like so:

```
greeting = "Hello, world!"
goodbye = "Seeya later, dude."
favorite_animal = 'Donkey'
```
Note that either single or double quotes are allowed.

**Integers**: Integers are whole numbers like 1, 2, 1000 and 1000000. They do not have decimal points. Unlike many other variable types, **integers are not declared with any special type of syntax**. You can simply assign them to a variable straight away, like this:

```
a = 1
b = 2
c = 1000
```

**Floats**: Floats are a fancy name for numbers with decimal points in them. **They are declared the same way as integers** but have some idiosyncracies we'll discover later:

```
a = 1.1
b = 0.99332
c = 100.123
```

**Lists**: Lists are collections of values or variables. **They are declared with brackets like these [], and items inside are separated by commas**. They can hold collections of any type of data, including other lists. Here are several examples:

```
list_of_numbers = [1, 2, 3, 4, 5]
list_of_strings = ['a', 'b', 'c', 'd']
list_of_both = [1, 'a', 2, 'b']
list of lists = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]
```

Lists also have another neat feature: The ability to retrieve individual items. In order to get a specific item out of a list, you first need to know its position in that list. All lists in Python are **zero-indexed**, which means the first item in them sits at position 0. For example, in the list ```['a', 'b', 'c', 'd']```, the letter "a" is at position 0, "b" is at position 1, etc.

The syntax for extracting a single item from the list using those indexes also uses brackets and looks like this:

```
list_of_strings = ['a', 'b', 'c', 'd']
the_letter_a = list_of_strings[0]
the_letter_c = list_of_strings[2]
```

You can also extract a range of values by specifiying the first and last positions you want to retrieve with a colon in between them, like this:

```
list_of_strings = ['a', 'b', 'c', 'd']
the_letters_a_b_c = list_of_strings[0:2]
```

**Tuples**: Tuples are a special type of list that cannot be changed once they are created. That's not especially important right now. All you need to know is that **they are declared with parentheses ()**. For now, just think of them as lists.

```
tuple_of_numbers = (1, 2, 3, 4, 5)
tuple_of_strings = ('a', 'b', 'c', 'd')
```

**Dictionaries**: Dictionaries are probably the most difficult data type to explain, but also among the most useful. In technical terms, they are storehouses of key/value pairs. You can think of them like a phonebook. An example will make this a little more clear, but know for now that **they are declared with curly braces**.

```
my_phonebook = {'Chase Davis': '713-555-5555', 'Mark Horvit': '573-555-5555'}
```
In this example, the keys are the names "Chase Davis" and "Mark Horvit", which are declared as strings (Python dictionary keys usually are). The values are the phone numbers, which are also strings, although dictionary values in practice can be any data type. If I wanted to get Chase Davis' phone number from the dictionary, here's how I'd do it:

```
my_phonebook['Chase Davis']
```

Which would return the string '713-555-5555'. There's a lot more to dictionaries, but that's all you need to know for now.

## Control structures

If you, think of a Python script as a series of commands that execute one after another you might imagine it would be helpful to be able to control the order and conditions under which those commands will run. That's where control structures come in -- simple logical operators that allow you to execute parts of your code when the right conditions call for it.

For our purposes, there are two control structures you will use most often: **if/else statements** and **loops**.

### If/else statements

If/else statements are pretty much exactly what they sounds like. *If* a certain condition is met, your program should do one thing; or *else* it should do something else.

The syntax is pretty intuitive -- except for one **extremely important thing**: In Python, whitespace matters. A lot. It's easiest to demonstrate this with an example:

```
number = 10
if number > 5:
    print "Wow, that's a big number!"
```

There's a lot to unpack here, but first take note of the indentation. It helps sometimes to think of your program as taking place on different levels. In this case, the main level of our program (the one that isn't indented) has us declaring the variable ```number = 10``` and setting up our if condition (```if number > 5:```). The second level of our program executes only on the condition that our if statement is true. Therefore, because it depends on that if statement, it is indented **four spaces** underneath that statement.

If you look closely, there's a small detail that can help you remember when a program moves from one level to another: namely, the presence of a colon. When we declare an if statement, we **always end that line with a colon**. The colon is our way of telling Python that it should start another level in the program, and everything on that level must be indented accordingly.

If we wanted to continue our program, we could do something like this:

```
number = 10
if number > 5:
    print "Wow, that's a big number!"

print "I execute no matter what your number is!"
```

The last statement doesn't depend on the if statement, so it's back on the main level again.

Notice that I said indents must be **four spaces**. Four spaces means four spaces -- **NOT A TAB. TABS AND SPACES ARE DIFFERENT. YOU MUST PRESS THE SPACE BAR FOUR TIMES WHENVER YOU INDENT PYTHON CODE.** There are some text editors that automatically convert tabs to spaces, and once you feel more comfortable, you might want to use one. But for now, get in the habit of making all your indents **FOUR SPACES**.

Now with that being said, let's unpack the rest of our if statement:

```
number = 10
if number > 5:
    print "Wow, that's a big number!"
```

Our little program in this case starts with a variable, which we've called ```number```, being set to 10. That's pretty simple, and a concept you should be familiar with by this point. The next line, ```if number > 5:``` declares our if statement. In this case, we want something to happen if the ```number``` variable is greater than 5.

Most of the if statements we build are going to rely on equality operators like the kind we learned in elementary school: greater than (>), less than (<), greater than or equal to (>=), less than or equal to (<=) and plain old "equals". The equals operator is a little tricky, in that **it is declared with two equals signs (==), not one (=).** Why is that? Because you'll remember from above that a single equals sign is the notation we use to assign a value to a variable! **Single equals signs are for assignment (```number = 5```); double equals signs are for equality (```if number == 5:```)**. File that one away somewhere. It's important.

Now let's talk about the next part of the if statement -- the else clause. You'll notice from the program above that the else clause isn't required. You don't *need* to have an else condition for your if statements, but sometimes it helps. Consider this example:

```
number = 10
if number > 5:
    print "Wow, that's a big number!"
else:
    print "Gee, that number's kind of small, don't you think?"
```

In this case, we're telling our program to print one thing if ```number``` is greater than 5, and something else if it's not. Notice that the else statement also ends with a colon, and as such its contents are also indented four spaces.

### For loops

Remember earlier we discussed the concept of a list -- the type of variable that can hold multiple items in it all at once. Many times during your programming career, you'll find it helps to run through an entire list of items and do something with all of them, one at a time. That's where for loops come in.

Let's start by having Python say the ABC's:

```
list_of_letters = ['a', 'b', 'c']
for letter in list_of_letters:
    print letter
```

The output of this statement, as you might guess, would be "a b c". But there are still a few things to unpack here -- some familiar and some not.

First you'll notice from looking at the print statement that our indentation rules still apply. Everything that happens within the for loop must still be indented four spaces from the main level of the program. You'll also see that the line declaring the loop ends in a colon, just like the if/else statement. That's an indication that indentation will be necessary.

Second, turn your attention to the syntax of declaring the loop itself: ```for letter in list_of_letters:```

All of our for loops start, unsurprisingly, with the word ```for``` and follow the pattern ```for variable_name in list:```. The variable_name can be anything you want -- it's essentially just a new variable you're creating to refer to each item within your list as the for loop iterates over it. You can call this whatever you want. In this case it's ```letter```, but you could just as easily call it ```donkey```, like so:

```
list_of_letters = ['a', 'b', 'c']
for donkey in list_of_letters:
    print donkey
```

The next thing you have to specify is the list you want to loop over, in this case ```list_of_letters```. The line ends with a colon, and the next line starts with an indent. And that's the basics of building a loop!

## Functions

Often it's helpful to encapsulate a sequence of programming instructions into little tools that can be used over and over again. That's where functions come in.

Think of functions like little black boxes. They take input (known as **arguments**), perform some operations on those arguments, and then return an **output**. In Python, a simple function might take an integer and divide it by two, like this:

```
def divide_by_two(input_integer):
    return input_integer / 2
```

In order to call that function later in the program, I would simply have to invoke its name and feed it an integer -- any integer at all -- like so:

```
print divide_by_two(10)
```

In which case it would return the number 5.

The black box analogy is the key thing to understand about functions. Once you write one (assuming you do so correctly), you don't need to know how it works. You can just feed it an input and expect an output in return.

As for how functions are declared, you'll notice a couple new details as well as some similarities to loops. First, every function must be declared by the word ```def```, which stands for "define". That is followed by the name of the function (you can call it anything you want, but as always, it should ideally make some kind of logical sense), and then a set of parentheses in which you can define the arguments a function should expect.

In our example above, our ```divide_by_two``` function expects one argument, which we've called ```input_integer``` -- basically the number that we want to divide by two. When we feed it the number 10, like this ```print divide_by_two(10)```, a variable by the name of our argument is created so that we can process it within the function. In that way, the name you give the argument works almost like the variable you create in a for loop: it's a reference to whatever argument you pass in that applies only within the body of the function.

After you finish declaring arguments, you'll see something familiar -- namely a colon, just like the ones in our if statements and for loops. And that means the next line **must be indented four spaces** because any code within the function is nested one level deeper than the base level of the program.

The final thing you'll need to know about function notation in Python is that most functions return some kind of output. Arguments go in, some processing happens, and something comes out. As you probably guessed, it's the ```return``` statement that tells the function to return it output.

It's worth pointing out that functions don't necessarily need arguments, nor do they always need to return a value using the ```return``` command. You could also do something like this:

```
def say_hello():
    print "Hello!"
```

But the idea of arguments and return values are still fundamental in understanding functions, and they will come up more often than not.

## Object-oriented programming

The next and final concept we'll introduce is the idea of object-oriented programming. OOP, as it's known for short, is a complex subject that can easily take up a semester in an introductory computer science program. We're only going to scratch the surface here, but it should be enough to get you started.

### Python as a toolbox

The first thing you should know is that Python is basically a collection of tools. In fact, Python has tools for pretty much everything you'd ever want to do with a programming language: everything from navigating the web to scraping and analyzing data to performing mathematical operations to building web sites. Some of these are built into a toolbox that comes with the language, known as the **standard library**. Others have been built by members of the developer community and can be downloaded and installed from the web. There are two ways to import these tools into your scripts, which we'll demonstrate here:

To pull in an entire toolkit, use the ```import``` command. In this case, we'll get the ```urllib2``` package, which allows us to visit websites with Python:

```
import urllib2
```

You can also import specific tools from a toolkit using similar syntax:

```
from urllib2 import urlopen
```

In practice, you'll use both of these methods. It's worth noting that most of the time, any import statements you execute will be **at the top** of your program.

### Objects as tools

It's one thing to pull a hammer from the toolbox, but it's quite another to use it for actually hammering nails.

Pretty much everything you every work with in Python -- external libraries, variables, you name it -- is considered an **object**. Objects, in the OOP world, have a couple of properties: they have characteristics that describe them, known as **attributes*, and actions they can perform, known as **methods**. In our hammer example, our hammer might have an attribute of "color" or "weight" and a method called "pound". Let's see how this applies to one of the first things we learned: Python strings.

Say you've created a string variable ```my_string = 'Hello!'```. Just like the hammer, the string has certain attributes that can describe it and certain methods it can perform. For example, calling ```print string.upper()``` will return ```HELLO!```. That is because all Python strings come with a method called upper(), which returns an all-uppercase representation of that string.

You can see how this might be useful. Tools like this allow us to perform various tasks in Python without having to hard-code the operations ourselves. Lists, for example, can sort themselves with the ```sort()``` method. In general, there are a couple rules you should remember when it comes to invoking these attributes and methods:

1. Python uses what's known as dot notation to call attributes and methods. That means you will insert a period between the object you're working with and whatever method you want it to perform. For example ```my_string.upper()``` says "perform the upper() method on the object my_string". **The dot between the two is very important.**

2. As a general rule in Python, **methods are called with parentheses and attributes aren't**. The ```upper()``` method of ```mystring.upper()``` is a method, so it requires a set of open and closed parentheses -- not unlike a function. Methods are actually close cousins of functions (they can also accept arguments). A string attribute, such as

Also, one final Pro Tip. Python has a built-in function, known as ```dir()```, which will reveal to you a menu of all the attributes and methods a given object has. Try doing this and you'll see what I mean ```dir(my_string)```.
