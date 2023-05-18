from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bs4  import BeautifulSoup as BS
import urllib3
from rest_framework.views import APIView
import re
from pkd.serializers import PkdSerializer
from pkd.models import Pkd

def homepage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def putDataIntoDb(request):
  http = urllib3.PoolManager()
  # url = "http://127.0.0.1:5500/PythonProjekt/pkdMissing.html"
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
  for pkdNum, pkdDesc in pkdDict.items():
      Pkd.objects.create(pkdNumber=pkdNum, pkdDesc=pkdDesc)


    
class PkdViewSet(APIView):
  def get(self, request):
    pkd = Pkd.objects.filter(pkdNumber=request.query_params["pkd_number"].upper())
    serializer = PkdSerializer(pkd, many=True)
    data = {}
    for val in serializer.data:
       data["pkdDesc"] = re.sub("'/?[^>]*'","",val["pkdDesc"])
       data["pkdNum"] = request.query_params["pkd_number"].upper()
    return render(request, 'foundDesc.html', data)
