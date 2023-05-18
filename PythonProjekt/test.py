from bs4  import BeautifulSoup as BS
import urllib3
import re
# from django.db import connection
from pkd.models import Pkd


http = urllib3.PoolManager()
url = "http://127.0.0.1:5500/PythonProjekt/pkd.html"
response = http.request('GET', url)
soup = BS(response.data, features="html.parser")
wrappedTag = soup.find_all("a", {"class":'card-header'})
numberAndDescPkdTable = []
pkdDict = {}
for content in wrappedTag:
    contentWithoutTagA = re.sub("</?a[^>]*>","", str(content).strip())
    contentWithoutTagSpan = re.sub("</?span[^>]*>","", str(contentWithoutTagA)).strip()
    numberAndDescPkdTable.append(contentWithoutTagSpan)
for i in numberAndDescPkdTable:
    numberAndDesc = i.split("\n")
    pkdDict[numberAndDesc[0]] = numberAndDesc[1]

print(pkdDict)
for pkdNum, pkdDesc in pkdDict.items():
    Pkd.objects.create(pkdNumber=pkdNum, pkdDesc=pkdDesc)
