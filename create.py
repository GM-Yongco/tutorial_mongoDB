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

	birthday:dict = {
		"name" : {
			"name_first":"Timothy",
			"name_middle":"Grant",
			"name_last":"Ylaya"
		},
		"birth_date":{
			"year": 2002,
			"month": 12,
			"day": 15
		}
	}

	coll : collection.Collection = get_collection(database_name = "friends", collection_name = "birthdays")
	result = coll.insert_one(birthday)
	
	separator("RESULTS")

	print(result)
	print(type(result))

	separator("END")