"""
1. Make a program that goes to https://sentence.yourdictionary.com/the and gets all the sentences
2. Add the words into a list
3. Save the list onto a file
"""

from bs4 import BeautifulSoup
import requests
import re

MyURL = "https://sentence.yourdictionary.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def remove_double_spaces(text):
    if text[0] == " ":
        text = text[1:]
    return re.sub(' +', ' ', text)

def remove_space(string):
    if string[0] == " ":
        return string[1:]
    else:
        return string

myList = []

def tidySentence(sentence):
    sentence.lower()
    sentence.capitalize()
    return remove_double_spaces(remove_space(sentence))

def remove_every_other(my_list):
    return my_list[::2]

def GT(Soup):
    Text = Soup.get_text()
    return Text

def getText(url):
    MyRequest = requests.get(url, headers=headers)
    Soup = BeautifulSoup(MyRequest.text, "lxml")
    return GT(Soup)

def getFile():
    myList = []
    if isinstance(MyURL, str):
        txt = getText(MyURL)
    elif isinstance(MyURL, list):
        txt = []
        for url in MyURL:
            for x in getText(url):
                txt.append(x)

    txt = txt.split('   ')

    for x in txt:
        if x != '' and (len(x) > 10) and not (x == "  Advertisement\n"):
            myList.append(x)

    for x in range(88):
        try:
            myList.pop(0)
        except:
            print("Error")
            break

    url = MyURL[36:]

    myFile = open("%s.txt" %url, "w")

    for x in myList:
        myFile.write(tidySentence(x) + '\n')
    myFile.close()


while True:
    print("put in your input")
    word = input("")
    if word == "quit":
        break
    else:
        MyURL = "https://sentence.yourdictionary.com/%s" %word
        getFile()