# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

from mongoDB_template import *

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	separator("START")

	# connecting to the cluster, database, collection

	user_credentials:json = get_credentials()
	driver_connection:str = f"mongodb+srv://{user_credentials['username']}:{user_credentials['password']}@cluster-01.f4zbhsn.mongodb.net/?retryWrites=true&w=majority&appName=cluster-01"
	
	# shows the heirarchy of the database
	cluster : MongoClient = MongoClient(host = driver_connection)
	db : database.Database = cluster["sample_analytics"]
	coll : collection.Collection = db["accounts"]
	result : cursor.Cursor = coll.find()

	for x in result :
		print(x)

	separator("TYPES")

	print(type(cluster))
	print(type(db))
	print(type(coll))
	print(type(result))

	separator("END")