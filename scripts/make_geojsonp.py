from datetime import datetime
import json
import random

# Used to create data that can be easily mapped in https://github.com/skeate/Leaflet.timeline in the earthquakes.html example
def get_epoch_time_ms(this_time):
    return (this_time - datetime(1970,1,1,0,0,0)).total_seconds() * 1000.0

def random_text():
    text = ("Regarding money of exchange, the use of representative money historically pre-dates the invention of coinage as well."
    " In the ancient empires of Egypt, Babylon, India and China, the temples and palaces often had commodity warehouses"
    " which made use of clay tokens and other materials which served as evidence of a claim upon a portion of the goods"
    " stored in the warehouses. Because these tokens could be redeemed at the warehouse for the commodity they represented,"
    " they were able to be traded in the markets as if they were the commodity or given to workers as payment."
    )
    return random.sample(text.split(),6)

def create_feature(time, data_type, value):
    return {"type":"Feature",
            "properties":
             {
                  "mag": 60,
                  "place": "8km S of Salton City, CA",
                  "time": get_epoch_time_ms(time),
                  "type": "earthquake",
                  "title": ' '.join(random_text()) + ' ' + time.isoformat()
             },
             "geometry":{
                 "type":"Point","coordinates":[-115.9613333+random.randint(-50,50),33.226+random.randint(-50,50),1]
             },
        }

features = [create_feature(datetime(2017,1,1,hour),None,None) for hour in range(0,24)]
geojson = {
    "type":"FeatureCollection","metadata": {},
    "features": features
}

with open('data.geojsonp', 'w') as outfile:
    outfile.write('eqfeed_callback({})'.format(json.dumps(geojson)))

