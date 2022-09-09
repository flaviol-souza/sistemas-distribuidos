#import requests
from http.client import HTTPSConnection
import json
from time import perf_counter

def getLegend():    
    #resp = requests.get('https://api.chucknorris.io/jokes/random')
    http = HTTPSConnection('api.chucknorris.io',443)
    http.request('GET', '/jokes/random')
    resp = http.getresponse()
    jsonB = resp.read()
    jsonStr = jsonB.decode('utf-8')
    respJson = json.loads(jsonStr)
    print(respJson["value"])
    return respJson["value"]

def createLegend(): 
    for n in range(1, 11):
        legend = getLegend()
        file = open("legend-norris"+str(n)+".txt", "w")
        file.write(legend)
        file.close()

if __name__ == "__main__":
    start_time = perf_counter()
    createLegend()
    end_time = perf_counter()
    print(f'\nIt took {end_time- start_time :0.2f} second(s) to complete.')