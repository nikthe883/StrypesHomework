from urllib.request import urlopen

webpage = urlopen('https://slashdot.org/slashdot.rss').readlines()
print(webpage)
