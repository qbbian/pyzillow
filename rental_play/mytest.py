from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

#address = '2114 Bigelow Ave N'
#zipcode = '98109'
MY_ZILLOW_API_KEY = 'X1-ZWz1ezldubt8uj_376md'

addressList = [('14825 NW Fawnlily Dr', '97229'),
	('606 NW Naito Parkway, Unit A8', '97209'),
	('11080 SW Oneida Street', '97062')]

zillow_data = ZillowWrapper(MY_ZILLOW_API_KEY)
for address in addressList:
	street = address[0]
	zipcode = address[1]
	deep_search_response = zillow_data.get_deep_search_results(street, zipcode, True)
	result = GetDeepSearchResults(deep_search_response)
	print "Estimated monthy rent for %s is $%s" % (address, result.rentzestimate_amount)


