
# Main selenium
# Go from the list of title codes, find if a hit is found.If so, add link to it, otherwise add NA

import urllib.request as req,  json 
import pandas as pd
url="https://data.cityofnewyork.us/resource/nzjr-3966.json?$select=count(title),descr&$group=descr&$order=COUNT(title)%20DESC"

baseURL="https://www1.nyc.gov/assets/dcas/downloads/pdf/noes/titlespecs/"

def getPDFLink(baseURL:str(), data:dict()):
    url="https://data.cityofnewyork.us/resource/nzjr-3966.json?$select=count(title),descr,title%20&$group=title,descr&$order=COUNT(title)%20DESC"
    with req.urlopen(url) as url:
        data=json.loads(url.read().decode())
    for ind, title in enumerate(data):
        # On HTTP Error, return a 404 string into the index
        try:
            data[ind]["status"]=str(req.urlopen(baseURL+title['title']+".pdf").getcode())
        except:
            print("Fail at index: "+str(ind))
            data[ind]["status"]="404"

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def downloadData(baseURL:str()):
    with open("Results/data.json") as js:
        df= json.load(js)

    print(df)
    #df=[
    # {
    #     "count_title": "8",
    #     "descr": "SUPERVISOR OF NURSES",
    #     "title": "50960",
    #     "status": "404"
    # },
    # {
    #     "count_title": "8",
    #     "descr": "SENIOR STATIONARY ENGINEER (EL",
    #     "title": "91639",
    #     "status": "200"
    # }]
    print(df)
    for item in df:
        if item["status"]=="200":
            
            response = req.urlopen(baseURL+ item["title"]+".pdf")    
            file = open("Results/"+item["title"]+"_"+str(item["descr"]).replace('/','_') + ".pdf", 'wb')
            file.write(response.read())
            file.close()

downloadData(baseURL)