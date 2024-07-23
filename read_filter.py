# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

from mongoDB_template import *

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
	
	# ====================================================================

	# documents with limits equal to 9000
	# show id:false, account_id:true, limit: true
	#s ort by account id in descending order

	query_filter:json = {"limit":9000}	
	query_projection:json = {"_id" : 0, "account_id": 1, "limit": 1}	
	query_sort:json = {"account_id" : -1}

	result:cursor.Cursor = coll.find(query_filter, projection = query_projection, sort = query_sort)

	separator("RESULTS")

	for x in result:
		print(x)

	separator("END")