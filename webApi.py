import requests,json
response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=125634")
res=json.loads(response.text)
print(res["quoteText"])
