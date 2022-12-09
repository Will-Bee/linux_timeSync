


# curl -X 'GET' \
#   'https://www.timeapi.io/api/Time/current/ip?ipAddress=<IP-Address>' \
#   -H 'accept: application/json'


# command:
# $ sudo hwclock --set --date="MM/DD/YY hh:mm:ss"


import json, requests, os

url = "https://www.timeapi.io/api/Time/current/ip?ipAddress="

ip = "77.75.79.5"

response = requests.get(url + ip)

print(response.text)

data = json.loads(response.text)

for key, value in data.items():

    print(key, ":", value)

os.system("sudo hwclock --set --date=\"" + data["date"] + " " + data["time"] + ":" + str(data["seconds"]) + '\"')


