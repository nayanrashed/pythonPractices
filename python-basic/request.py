import requests
#url= "http://subeen.com/allposts/"
response=requests.get("http://example.com/")
print(response.ok)
print(response.status_code)
print(response.text)
