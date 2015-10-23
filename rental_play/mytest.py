from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

address = '2114 Bigelow Ave N'
zipcode = '98109'
MY_ZILLOW_API_KEY = 'X1-ZWz1ezldubt8uj_376md'

zillow_data = ZillowWrapper(MY_ZILLOW_API_KEY)
deep_search_response = zillow_data.get_deep_search_results(address, zipcode, True)
result = GetDeepSearchResults(deep_search_response)


