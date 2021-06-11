# File to read PDFs from result and generate a full list of titles

# Title Object: has code, description, previous, and next. Will store next and previouse code
# 
import PyPDF2 as pp2
import json
folderPath='Results/'
myJson=[dict()]
def readPDF(codeTitle:str()):
    # codeTitle=code_Descr.pdf
    # codeTitle+"_"+str(item["descr"]).replace('/','_')
    ofile=folderPath+codeTitle
    promoLine=str()
    with open(ofile, 'rb') as pdfFileObj:
        # creating a pdf reader object
        pdfReader = pp2.PdfFileReader(pdfFileObj)
        
        # creating a page object
        pageObj = pdfReader.getPage(pdfReader.numPages-1)
        # extracting text from page
        # try:
        #     pageObj.extractText().split("CODE")[0]
        # except:
        #     print("Failed to extract working group: "+ofile)
        try:
            promoLine= pageObj.extractText().split(" Promotion")[1].replace('\n','') #replace(' ','|')

            # print(pageObj.extractText().split(" Promotion")[1].replace('\n ',''))#replace(' ','|'))
        except:
            promoLine="Failed"
            print(ofile)
        # closing the pdf file object
        pdfFileObj.close()
    return promoLine
# x="10212_REPORTER_STENOGRAPHER.pdf"

# y="91722_ELECTRICIANS HELPER.pdf"
# z="91717_ELECTRICIAN.pdf"
# readPDF(x)
# readPDF(y)
# readPDF(z)

with open("Data/data.json") as js:
        df= json.load(js)
fdf=list()
for item in df:
    if item["status"]== "404":
        continue
    else:
        fdf.append(item)

print(len(fdf))

df=fdf

for ind,item in enumerate(df):
        if item["status"]=="200":
            itemFile = item["title"]+"_"+str(item["descr"]).replace('/','_') + ".pdf"
            myStr=readPDF(itemFile)
            # print(myStr)
            df[ind]["promotionLine"]=myStr

with open('Data/data_promotion_Only.json', 'w', encoding='utf-8') as f:
        json.dump(df, f, ensure_ascii=False, indent=4)