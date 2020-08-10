import json
import requests
from PIL import Image
import urllib.request
import matplotlib.pyplot as plt
import os

response = requests.get("http://starlord.hackerearth.com/recipe")
jsondata = response.json()
print (type(jsondata))
for i in range(len(jsondata)):
	print (jsondata[i]['name'])
	print (jsondata[i]['image'])
	full_path = os.path.join("image", jsondata[i]['name'])
	#urllib.request.urlretrieve(jsondata[i]['image'], full_path) #download image
response = requests.get(jsondata[i]['image'], stream=True)
img = Image.open(response.raw)
plt.imshow(img)
plt.show()


#make the json file
with open('recipe-pizza.json', 'w') as f:
  json.dump(jsondata, f, indent=2)
# open the json file
#with open('recipe-pizza') as f:
#  state_data= json.load(f)