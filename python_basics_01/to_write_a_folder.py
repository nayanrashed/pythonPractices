import requests
url = "http://dimikcomputing.com"
response = requests.get(url)
with open("dimik.html","w", encoding=response.encoding) as f:
    f.write(response.text)








#fp = open("test.txt", "w")
#fp.write("creating text file using python\nhello")
#fp.close()
