import wikipedia
import os
import warnings
import calendar
import random
import datetime
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os 
from PIL import Image
import subprocess
import pyautogui 
import bs4 as bs
import urllib.request
import Classification
import pandas

class Brain():
    def greet(self, formality):
        if formality == 0:
            return "Hi"
        elif formality == 1:
            return "Hello"
        else:
            return "Its a pleasure to meet you"



    # 2: name
    def meeting_convo(self, name):
        print("Hei {}, I am Echo, a artificial intelligence assistant created by Neri")
        with 




    # 4: time
    def tell_time(self):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        return time

    # 5: search google

    def google_search(self, search_term):
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        return "Here is what I found for" + search_term + "on google"

    # 6: search youtube
    def youtube_search(self, search_term):
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        return "Here is what I found for " + search_term + "on youtube"

     #7: get stock price
    def get_stocks(self, search_term):
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        return "Here is what I found for " + search_term + " on google"
    


     #8 time table
    
     #9 weather
    def get_weather(self, search_term):
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        return "Here is what I found for on google"
     

     #10 stone paper scisorrs
    def rps_game(self, move):
        moves=["rock", "paper", "scissor"]
        cmove=random.choice(moves)
        pmove= move
        outcome = list()
        # outcome list sample = ¹result ²computer move ³player move
        if pmove==cmove:
            outcome.append("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            outcome.append("Player wins")
        elif pmove== "rock" and cmove== "paper":
            outcome.append("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            outcome.append("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            outcome.append("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            outcome.append("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            outcome.append("Computer wins")
        outcome.append("The computer chose " +cmove)
        outcome.append("You chose " +pmove)
        return outcome

     #11 toss a coin
    def toss_coin(self):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        return "The computer chose " + cmove

     #12 calc
    def calculate(self, num1, opr, num2):
        if opr == 'add':
            result = num1 + num2
        elif opr == 'subtract':
            result = num1 - num2
        elif opr == 'multiply':
            result = num1 * num2
        elif opr == 'divide':
            result = num1 / num2
        elif opr == 'power':
            result = num1 ** num2
        else:
            result = "Error Occured, try speak more clearly"
        return result

     #14 to search wikipedia for definition
    def wikipedia_search(self, definition):
        url=urllib.request.urlopen("https://en.wikipedia.org/wiki/'+definition")
        soup=bs.BeautifulSoup(url,"lxml")
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                result = 'im sorry i could not find that definition, please try a web search'
            elif definitions[1]:
                result = 'here is what i found '+definitions[1]
            else:
                result = 'Here is what i found '+definitions[2]
        else:
                result = "im sorry i could not find the definition for "+definition
        return result

