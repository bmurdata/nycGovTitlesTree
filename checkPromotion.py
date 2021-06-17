# Check promotion status and get title nums

import json, re
import urllib.request as req
with open("Data/data_promotion_Only.json") as js:
        df= json.load(js)
for ind,title in enumerate(df):
    df[ind]["numPromos"]=list(map(str,re.findall(r'\d+',title["promotionLine"])))
# 81805- success, pdf available and NOT downloaded.

with open('Data/data_Nums.json', 'w', encoding='utf-8') as f:
        json.dump(df, f, ensure_ascii=False, indent=4)

with open("Data/data_promotion_Only.json") as js:
        comp= json.load(js)
        
truth=list()
baseURL="https://www1.nyc.gov/assets/dcas/downloads/pdf/noes/titlespecs/"

for item in comp:
    truth.append(item["title"])
for item in df:
    if item["numPromos"] is not None:
        for num in item["numPromos"]:
            if num not in truth:
                try:

                        response = req.urlopen(baseURL+ num+".pdf")    
                        file = open("Results/"+num+"_Rename"+ ".pdf", 'wb')
                        file.write(response.read())
                        file.close()
                except:
                    continue

