# importing the requests library
import requests

# api-endpoint
URL = "http://192.168.1.142:5000/main"


# TODO record video
# TODO check 25 fps


# send video recorded
files = {'file': open('client/video.h264', 'rb')}
response = requests.post(URL, files=files)

# extracting data in json format
data = response.json()

# printing the output
print(data)

# TODO delete 0-sc
