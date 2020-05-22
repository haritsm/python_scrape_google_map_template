import os, sys, inspect
# import pymongo
import datetime
import csv
# from pymongo import MongoClient
import time, logging
#from config.config_s3 import upload_to_s3
# from helpers.args_parser import args
import json
import requests
# import MySQLdb

#MongoDB Databases
# client = MongoClient()
# db = MongoClient(args.src, 27017, readPreference = "secondary" ).setipe
# db_history = MongoClient(args.src, 27017, readPreference = "secondary" ).setipe_history

#MySQL Database
#db_mysql = MySQLdb.connect(user="root", host="127.0.0.1", db="reskrim", port=3306)
#cur = db_mysql.cursor(MySQLdb.cursors.DictCursor)

# NOTIFICATION_BASE_URL = {
# 	"production" :"https://notification.setipe.com",
# 	"development" : "http://localhost:1993"
# }

def initialize_logger (log_name = 'worker_log'):
	#logger
	logger = logging.getLogger(log_name)
	hdlr = logging.FileHandler('./logs/'+log_name+'.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr)
	logger.setLevel(logging.INFO)
	global global_logger
	global_logger = logger
	return True

def start_logger ():
	start_time = time.time()
	global_logger.info("--- MULAI : %s seconds ---" % (start_time))
	return start_time

def end_logger(start_time):
	global_logger.info("--- SELESAI : %s seconds ---" % (time.time() - start_time))
	return True

def write_to_excel (extracted_data, file_name):
	now = datetime.datetime.now()
	destination_path = "extracted_data" + now.strftime("%Y") + "/"+now.strftime("%m. %B") + "/" + now.strftime("%d")
	if not os.path.exists(destination_path):
		os.makedirs(destination_path)

	with open(destination_path+"/"+file_name, 'w') as f:
		wr = csv.writer(f, delimiter=',', dialect='excel')
		wr.writerows(extracted_data)

	return "extracted"

def send_email (payload):

	# Define Base url

	BASE_URL 	= NOTIFICATION_BASE_URL[args.notif_url]
	default_tag = "system-email"
	
	# Append email-blast tag 

	try:
		payload["tags"].append(default_tag)
	except Exception as e:
		payload["tags"] = [default_tag]
		
	sent = requests.post( 
		BASE_URL+'/send' , 
		data = json.dumps(payload),
		headers = { "Content-Type": "application/json"}
	)
	
	return sent.json()