
# Main selenium
# Go from the list of title codes, find if a hit is found.If so, add link to it, otherwise add NA

import urllib.request as req,  json 

url="https://data.cityofnewyork.us/resource/nzjr-3966.json?$select=count(title),descr&$group=descr&$order=COUNT(title)%20DESC"
url="https://data.cityofnewyork.us/resource/nzjr-3966.json?$select=count(title),descr,title%20&$group=title,descr&$order=COUNT(title)%20DESC"
with req.urlopen(url) as url:
    data=json.loads(url.read().decode())
baseURL="https://www1.nyc.gov/assets/dcas/downloads/pdf/noes/titlespecs/"
print(req.urlopen(baseURL+"10124.pdf").getcode())

for ind, title in enumerate(data):
    # if req.urlopen(baseURL+title['title']+".pdf").getcode()==404:
    try:
        data[ind]["status"]=str(req.urlopen(baseURL+title['title']+".pdf").getcode())
    except:
        print("Fail at index: "+str(ind))
        data[ind]["status"]="404"

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)