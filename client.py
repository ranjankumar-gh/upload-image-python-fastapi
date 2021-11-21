import requests

url = "http://127.0.0.1:8000/upload_file"
files = {'image': open('31_left.jpeg', 'rb')}
response = requests.post(url, files=files)
print(response.text)
