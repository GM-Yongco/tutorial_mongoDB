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

	coll : collection.Collection = get_collection(database_name = "friends", collection_name = "birthdays")
	
	# ====================================================================

	query_filter:json = {"birth_date.year" : 2002}
	query_projection:json = {"_id" : 0, "name":{"name_first":1}}	
	query_sort:json = {"account_id" : -1}

	result:cursor.Cursor = coll.find(query_filter, projection = query_projection, sort = query_sort)
	# result:cursor.Cursor = coll.find(projection = query_projection, sort = query_sort)

	separator("RESULTS")

	# print(f"number of results: {len(result)}")
	for x in result:
		print(x)

	separator("END")