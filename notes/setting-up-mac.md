# Instructions for setting up on a Mac

Type the word 'Terminal' in the Mac Search.
![screen shot 2014-09-05 at 9 17 05 am](https://cloud.githubusercontent.com/assets/166734/4166023/736b4c6c-3507-11e4-87ca-1d625d7fac04.png)

When you select it, Terminal will launch and it will look something like this:
![screen shot 2014-09-04 at 6 52 47 pm](https://cloud.githubusercontent.com/assets/166734/4166081/24b86e8c-3508-11e4-9155-d833dada79d6.png)

After the "$" Type:
```
sudo easy_install pip
```

Install libraries:
```
sudo pip install BeautifulSoup
sudo pip install Mechanize
sudo pip install Requests
```

Make sure that it works. Type:
```
python
```

You should see something that looks like this:
![screen shot 2014-09-05 at 9 23 53 am](https://cloud.githubusercontent.com/assets/166734/4166096/49b2a63a-3508-11e4-8f0f-aefab7ae32ff.png)


Your prompt has changed from this:
```
$
```
To this:
```
>>>
```
This means that you are currently in Python interpretor.

Then type the following to make sure you have the installed libraries:
```
import requests
import mechanize
import beautifulsoup
```

If nothing happens after each of those, then you are successfully setup. If you get an 'ImportError', then something isn't working correctly for you. Please ask an instructor or a friend for help.





