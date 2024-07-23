# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

from mongoDB_template import *
from typing import List

# ========================================================================
# TEST 
# ========================================================================

if __name__ == '__main__':
	separator("START")

	birthdays = [  # Use plural 'birthdays' for consistency
		{
			"name": {  # Single "name" for first, middle, last
				"name_first": "Giulio",
				"middle_name": "Memarion",  # Corrected typo (middle instead of middle_)
				"name_last": "Yongco"
			},
			"birth_date": {
				"year": 2002,
				"month": 12,
				"day": 5
			}
		},
		{
			"name": {
				"name_first": "Alexandra",
				"middle_name": "R.",
				"name_last": "Abainza"
			},
			"birth_date": {
				"year": 2001,
				"month": 12,
				"day": 10
			}
		}
	]


	coll : collection.Collection = get_collection(database_name = "friends", collection_name = "birthdays")
	result = coll.insert_many(birthdays)
	
	separator("RESULTS")

	print(result)
	print(type(result))

	separator("END")