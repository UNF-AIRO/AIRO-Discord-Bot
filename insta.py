
import json

# Connecting the profile 
user = Instagram("geeks_for_geeks") 

def parse(self, response):
        x = response.xpath("//script[starts-with(.,'window._sharedData')]/text()").extract_first()
        json_string = x.strip().split('= ')[1][:-1]
        data = json.loads(json_string)