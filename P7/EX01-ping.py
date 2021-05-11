import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/documentation/info"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
print(response.status, response.reason)

answer_decoded = response.read().decode()
print(type(answer_decoded), response.reason)
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)

if dict_response["ping"] == 1:
    print("PING OK!!! The database is running.")
else:
    print("Database is down!!!")