import urllib2
import json
import pandas as pd
import requests

quakes = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=2016-10-01%2000:00:00&endtime=2016-10-02%2000:00:00&minmagnitude=0&maxmagnitude=8&orderby=time")

quakes.text[0:100]
data = json.loads(quakes.text)
data.keys()
data['features'][0]['properties'].keys()

results =[]
for quake in data['features']:
    mag = quake['properties']['mag']
    place = quake['properties']['place']
    lat = quake['geometry']['coordinates'][0]
    long = quake['geometry']['coordinates'][1]
    title = quake['properties']['title']
    results.append((mag,place,lat,long,title))
    
print(len(results))
print(results[0:2])

df = pd.DataFrame(results, columns = ['mag','place','lat','long','title'])
print df.head()
df.to_csv('earthquake.csv',index = False,encoding = 'utf-8')