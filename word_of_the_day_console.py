
# coding: utf-8

# # Word of the Day
# 
# This notebook fetches the word every day from the site http://www.dictionary.com/wordoftheday/ 
# 
# What it results into:
# 
# 1. Name of the word
# 2. Category of the word
# 3. Meanings of the word
# 4. Origin of the Word
# 5. Usage Examples from the Web
# 
# 

# In[43]:

# Import the necessary libraries

import requests
from bs4 import BeautifulSoup
import os
import datetime
import warnings

warnings.filterwarnings('ignore')
url = "http://www.dictionary.com/wordoftheday/"


# Get the date of previous day.

date = datetime.datetime.now() - datetime.timedelta(days=1)
date_format = str(date.year) + '/' + str(date.month) + '/' + str(date.day)

newurl = url + date_format

response = requests.get(newurl)

status_code = response.status_code 
if(~status_code == 200):
    print("The page you are trying to view is giving the error {}".format(status_code))
    quit()

# Using BeautifulSoup
soup = BeautifulSoup(response.content)

word = soup.find('div', class_ = 'tile-image')
word.a['href']

#Get the URL of each word. Each word has a separate page on the site.

word_url = word.a['href']


# Make a request to the word URL

response = requests.get(word_url)
soup = BeautifulSoup(response.content)

status_code = response.status_code 
if(~status_code == 200):
    print("The page you are trying to view is giving the error {}".format(status_code))
    quit()


# In[44]:

# Get the name of the word

soup = BeautifulSoup(response.content)

word = soup.find('h1', class_= 'head-entry')
name_of_word = word.contents[0].contents[0]
name_of_word


# In[45]:

# Get the category of the word

def_list = soup.find('div', class_ = 'def-list')
print(type(def_list))
category = def_list.contents[1].span.contents[0]
#category


# In[46]:

# Get the indices of the meanings of the word

numbers = def_list.contents[1].find_all('span', class_ = 'def-number')
print(type(numbers))
numbers_list = [x.contents[0] for x in numbers]
#numbers_list


# In[47]:

# Get the meanings of the words

meanings = def_list.contents[1].find_all('div', class_ = 'def-content')
meaning_list = [x.contents[0].strip() for x in meanings]
meaning_list


# In[48]:

# Append the indices and meanings of the word
new_meanings_list = []
for a,b in zip(numbers_list, meaning_list):
    new_meanings_list.append('{}{}'.format(a,b))
new_meanings_list


# In[49]:

# Get the origin of the words

origin_languages = soup.find_all('div', class_ = 'map-origin-language')
origin = []
for o in origin_languages:
    origin.append(o.find('a').contents[0])
origin


# In[50]:

# Get the Examples from the Web
import re
examples = soup.find_all('p', class_= 'partner-example-text')

web_usage = []
for text in examples:
    web = [] 
    for t in text:
        web.append(str(t))
    final_word = "".join(web).strip()
    final_word = re.sub(r'<em>', '', final_word)
    final_word = re.sub(r'</em>', '', final_word)
   
    web_usage.append(final_word)
web_usage


# # Here are the results

# In[51]:

f = open('results.txt', 'a+')
print("\n\nDate: {} \n".format(date.strftime('%Y-%m-%d')))
print("\nWord: {} \n".format(name_of_word))
print("\nCategory: {} \n".format(category))
print("\nMeanings: \n\n")
for x in new_meanings_list:
    print(x)
    print('\n')
i = 1
print("\nExample Usages from the Web: \n \n")
for x in web_usage:
    print('{}.{}'.format(i,x))
    print('\n')
    i+=1


# In[52]:

input("Press Enter to quit")


# In[ ]:




# In[ ]:



