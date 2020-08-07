import json
import requests
from PIL import Image
import matplotlib.pyplot as plt
response = requests.get("http://starlord.hackerearth.com/recipe")
jsondata = response.json()
print (type(jsondata))
for i in range(len(jsondata)):
	print (jsondata[i]['name'])
	print (jsondata[i]['image'])

response = requests.get(jsondata[i]['image'], stream=True)
img = Image.open(response.raw)
plt.imshow(img)
plt.show()