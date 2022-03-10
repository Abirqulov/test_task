import json
import os

with open('https://gorest.co.in/public/v1/posts') as json_file:
    data = json.loads(json_file).read()
    print("type:", type(data))
