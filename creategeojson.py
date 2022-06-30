import pymongo
import pandas as pd
import json


def make_geo():
#this function is what creates our geojson by opening and combining the JSON's scraped from the web

# outlines
    with open('json/outlines.json') as f:
        data = json.load(f)

#parks
    with open('json/all_parks.json') as g:
            parks = json.load(g)

#adding all parks to properties in the outlines json
    for x in range(len(data['features'])):
        if data['features'][x]['properties']['name']== parks[x]["State"]:
            data['features'][x]['properties'].update(parks[x])

#colleges
    with open('json/colleges.json') as h:
        college = json.load(h)

#add colleges
    for x in range(len(data['features'])):
        if data['features'][x]['properties']['name']== college[x]["State"]:
            data['features'][x]['properties'].update(college[x])
    for x in range(len(data['features'])):
        for y in range(len(college)):
            if data['features'][x]['properties']['name']== college[y]["State"]:
                data['features'][x]['properties'].update(college[y])

# happiness
    with open('json/happiness.json') as k:
        happy = json.load(k)


#add happiness
    for x in range(len(data['features'])):
        if data['features'][x]['properties']['name']== happy[x]["State"]:
            data['features'][x]['properties'].update(happy[x])

#pets
    with open('json/pet_data.json') as p:
        pets = json.load(p)

#add pets
    for x in range(len(data['features'])):
        for y in range(len(pets)):
            if data['features'][x]['properties']['name']== pets[y]["name"]:
                data['features'][x]['properties'].update(pets[y])

    for x in range(len(data['features'])):
            try:
                    data['features'][x]["properties"]["pet ownership"] = float(data['features'][x]["properties"]["pet ownership"])
            except:
                    print(data['features'][x]["properties"]["State"])
            try:
                    data['features'][x]["properties"]["dog ownership"] = float(data['features'][x]["properties"]["dog ownership"])
            except:
                    print(data['features'][x]["properties"]["State"])
            try:
                    data['features'][x]["properties"]["cat ownership"] = float(data['features'][x]["properties"]["cat ownership"])
            except:
                    print(data['features'][x]["properties"]["State"])

#income
    with open('json/income.json') as i:
        income = json.load(i)

#add income
    for x in range(len(data['features'])):
        for y in range(len(income)):
            if data['features'][x]['properties']['name']== income[y]["State"]:
                data['features'][x]['properties'].update(income[y])

#crime
    with open('json/crime.json') as c:
        crime = json.load(c)

#add crime
    for x in range(len(data['features'])):
        for y in range(len(crime)):
            if data['features'][x]['properties']['name']== crime[y]["State"]:
                data['features'][x]['properties'].update(crime[y])

#centers
    with open('json/centerstates.json') as cs:
        centers = json.load(cs)

#add centers
    for x in range(len(data['features'])):
        for y in range(len(centers)):
            if data['features'][x]['properties']['name']== centers[y]["state"]:
                data['features'][x]['properties'].update(centers[y])

#return results
    return data