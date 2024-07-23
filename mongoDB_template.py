# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# Real Description	: template as to not repeat code for the tutorials
# HEADERS ================================================================

import json

from pymongo import MongoClient, database, collection, cursor

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def separator(x:str = "SECTION") -> None:
	section:str = f"\n {x} {'-' * (40 - len(x))}\n"
	print(section)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def get_credentials()->json:
	file_path:str = "REFERENCES/auth.json"
	return json.load(open(file_path))

# see how this works in tutorial 01
def get_collection(
		database_name:str, 
		collection_name:str, 
		driver_connection:str = "") -> collection.Collection:

	if driver_connection == "":
		user_credentials:json = get_credentials()
		driver_connection = f"mongodb+srv://{user_credentials['username']}:{user_credentials['password']}@cluster-01.f4zbhsn.mongodb.net/?retryWrites=true&w=majority&appName=cluster-01"

	cluster : MongoClient = MongoClient(host = driver_connection)
	db : database.Database = cluster[database_name]
	return db[collection_name]