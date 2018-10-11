#downloading web pages 

import requests
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
response.status_code
response.text
response.request.headers

response.request

response.request.url

#Check web download status
#requests.get('http://www.columbia.edu/invalid')

