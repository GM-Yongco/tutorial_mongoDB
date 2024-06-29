# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
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

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	separator("START")

	# connecting to the cluster, database, collection

	user_credentials:json = get_credentials()
	driver_connection:str = f"mongodb+srv://{user_credentials['username']}:{user_credentials['password']}@cluster-01.f4zbhsn.mongodb.net/?retryWrites=true&w=majority&appName=cluster-01"
	
	cluster:MongoClient = MongoClient(driver_connection)
	db: database.Database = cluster["sample_analytics"]
	coll: collection.Collection = db["accounts"]
	
	# how to query

	query:json = {"limit":9000}
	selection:json = { "limit": 1}
	result:cursor.Cursor = coll.find(query, selection)

	separator("RESULTS")

	for x in result:
		print(x)

	separator("END")