# This piece of code can display a secret message by finding the data it needs from a website, sorting it into its coordinates and the character it should display at said coordinates, and then finally displaying it into the console using the information.
# Author: Jonathan Pabilic
# Date : 8/22/2024

from bs4 import BeautifulSoup # BeautifulSoup allows one to access website data, which is very important for this program.
from urllib.request import urlopen

def find_data(soup): # This function finds the data by searching for the first instance of a number given the text returned by BeautifulSoup.
  i = 0
  text = soup.get_text()
  while text[i].isnumeric() == False:
    i += 1
    if text[i].isnumeric():
      data = text[i+1:] # Everything before the data is discarded.
  return data

def display_message(url): #The main, important function that displays the message.
  page = urlopen(url)
  html = page.read().decode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  data = find_data(soup)
  i = 0
  x_coordinates = []
  y_coordinates = []
  characters = []
  grid = ['-'] * 100
  data_list = []
  segment = ""

  
  while len(data) > 2: # Sorts data by splitting it up into its x and y coordinates and the character it should display at said coordinates into elements in a list.
    if data[i].isnumeric() == False: # Runs until it finds a character and works around it.
      segment = data[0:i+2]
      data_list.append(segment)
      data = data[i+2:] # Progessively shortens the original data as necessary.
      i = 0
    else:
      i += 1

  
  for data in data_list: # Depending on the length of the element, the data is further organized into their own respective lists.
    if len(data) == 3:
      x_coordinates.append(data[0:1])
      y_coordinates.append(data[-1:])
      characters.append(data[1:2])
    elif len(data) == 4:
      x_coordinates.append(data[0:2])
      y_coordinates.append(data[-1:])
      characters.append(data[2:3])

  
  for n in range (6,-2,-1): # This loop displays the message.
    print(''.join(grid)) 
    grid = ['-'] * 100
    for b in range(len(y_coordinates)):
      if y_coordinates[b] == str(n):
        grid[int(x_coordinates[b])] = characters[b]


display_message("https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub")