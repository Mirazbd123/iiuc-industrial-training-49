# Headers for request
HEADERS = ({'', 'Accept-Language': 'en-US, en;q=0.5'}) #add your user agent
# HTTP Request
webpage = requests.get(URL, headers=HEADERS)