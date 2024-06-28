# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================
import json

from pymongo import MongoClient, database, collection

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

	user_credentials:json = get_credentials()
	driver_connection:str = f"mongodb+srv://{user_credentials['username']}:{user_credentials['password']}@cluster-01.f4zbhsn.mongodb.net/?retryWrites=true&w=majority&appName=cluster-01"
	
	cluster:MongoClient = MongoClient(driver_connection)
	db: database.Database = cluster["sample_analytics"]
	col: collection.Collection = db["accounts"]
	
	for x in col.find() :
		print(x)

	separator("TYPES")

	print(type(db))
	print(type(col))

	print(driver_connection)

	separator("END")