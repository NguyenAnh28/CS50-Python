import request
import sys

if len(sys.argv) != 2:
    sys.exit()
else:
    print(sys.argv[1])  

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

print(r)