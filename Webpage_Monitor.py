#!/usr/bin/python3
import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module

# Defining a function to get text from website
def get_text_from_link(url):
    r = requests.get(url)  # Sends HTTP GET Request
    soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
    # Getting all the text and storing it in the variable Original_text
    new_text = " " # Initializing the variable
    for link in soup.find_all('a'):  # iterate over every <a> tag
        new_text = new_text + link.get_text()
    return new_text

# Creating the original text file with which the text will be compared in every run
# This function should be deleted after the first run or not called in subsequent runs
def creating_orig_file(url,file_name):
    File_object1 = open(file_name, "w") # This will create the file if it doesn't exist
    orig_text = get_text_from_link (url)
    File_object1.write(orig_text)
    File_object1.close()

# Defining a function which will check if there has been an update
def update_check(url,file_name):
    recent_text = get_text_from_link(url)
    File_object2 = open(file_name, "r")
    original_text = File_object2.read()
    # Checking if the two text are same
    if original_text == recent_text:
        print("The text read from file and scrapped from web are same")
    else:
        print("The page has been updated")
    File_object2.close()


# Initiazing the URL which will be monitored
URL = "https://admitvidya.com/"
# Initializing the file name for storing the first state(text) of website
file_name = "original_text_file.txt"

creating_orig_file(URL,file_name) # Needs to be called only once in the first run
update_check(URL,file_name)

