import requests
import sys

if len(sys.argv) != :
    sys.exit()
else:
    print(sys.argv[1])  

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(r)