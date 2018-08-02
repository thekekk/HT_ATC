import selenium
import pandas
from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver


def urlinit:
    base_url = Input("What site did you want to run? (Enter 'HOTTOPIC' for HOTTOPIC)")
    if base_url == 'HOTOPIC':
        hts()
    else:
        print("Sorry please select a valid responce, see README for the full list")
        return #return the function

def varsinit:
    # Initiate profile and KWs here
    # To view proper kW docs make sure to View README
    f_name = Input("Enter your First Name")
    l_name = Input("Enter your Last Name")
    ad_one = Input("Enter your Address One")
    ad_two = Input("Enter your Address Two")
    phone = Input("Enter your US Phone")
    city = Input("Enter your City")
    state = Input("Enter your State")
    zip = Input("Enter your zip")
    email = Input("Enter your email")
    card_num = Input("Enter your card number")
    month = Input("Enter your card exp month")
    year = Input("Enter your card exp year")
    card_cvv = Input("Enter your card CVV")
    card_name = Input("Enter your Namer as it appears on your card")
    keyword1 = Input("Enter your keywords")
