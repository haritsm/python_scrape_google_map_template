import json
import requests
import time
import datetime
import os, sys, inspect
import csv
from urllib.request import urlopen
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib3.exceptions import MaxRetryError
import logging
import pandas as pd
# from oauth2client.service_account import ServiceAccountCredentials
import pprint
from import_function import import_excel
from worker_template import write_to_excel

# Basic

# The Basic category includes the following fields:
# address_component, adr_address, business_status, formatted_address, geometry, icon, name, permanently_closed, photo, place_id, plus_code, type, url, utc_offset, vicinity

# Contact

# The Contact category includes the following fields:
# formatted_phone_number, international_phone_number, opening_hours, website

# Atmosphere

# The Atmosphere category includes the following fields: price_level, rating, review, user_ratings_total

# https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key=YOUR_API_KEY

def call_google_place(query):
	site = 'https://maps.googleapis.com/maps/api/'
	service = 'place/textsearch/json?'
	inputs = 'query='+ query + '&location=-5.9036076,106.5296896&radius=100000'
	api_key = '&key=AIzaSyCOuXK2TAe7zqmaLCo5PRsfWNP5601aNFk'
	url = site + service + inputs + api_key
	return url

if __name__ == '__main__':
    
    file_name = '{{cookiecutter.project_name}}'
    file_name = file_name+".csv"
    header = ["name","lat","long","region","formatted_address","types","rating","user_ratings_total"]
    result = list()
    result.append(header)
    counter = 1

    ### EDIT HERE ###
    file_path = ("../XXX.xlsx")
    sheet = 'XXX'
    data = import_excel(file_path, sheet)
    ### DONE EDIT ###

    # keyword list
    list_keyword = data['Verb'].tolist()

    # latlong list
    list_location = data['Location'].tolist()

    for item in list_keyword:
        for item_2 in list_location:
            string = "Current list: " + item + "+" + item_2
            print(counter + " \n" + string)

            url = call_google_place(item)
            time.sleep(45)
            response = requests.get(url=url).json()
            # response = request_data_from_url(url)
            print(counter)
            for obj in response["results"]:
                name = obj["name"]
                lat = obj["geometry"]["location"]["lat"]
                lng = obj["geometry"]["location"]["lng"]
                addr = obj["formatted_address"]
                types = obj["types"]
                rating = obj["rating"]
                user_ratings_total = obj["user_ratings_total"]
                # place_id = obj["place_id"]
                temp = [name, lat, lng, addr, types, rating, user_ratings_total]
                result.append(temp)
                print(temp)
                
            while 'next_page_token' in response:
                URL = url + '&pagetoken=' + response["next_page_token"]
                time.sleep(45)
                response = requests.get(url=URL).json()
                # response = request_data_from_url(URL)
                for obj in response["results"]:
                    name = obj["name"]
                    lat = obj["geometry"]["location"]["lat"]
                    lng = obj["geometry"]["location"]["lng"]
                    addr = obj["formatted_address"]
                    types = obj["types"]
                    rating = obj["rating"]
                    user_ratings_total = obj["user_ratings_total"]
                    # place_id = obj["place_id"]
                    temp = [name, lat, lng, addr, types, rating, user_ratings_total]
                    result.append(temp)
                    print(temp)
            counter += 1

write_to_excel(result, file_name)