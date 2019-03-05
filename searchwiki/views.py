from configparser import ConfigParser
from django.shortcuts import render
import urllib
import wikipedia as wikipedia
import pdfkit
from django.http import HttpResponse
from .models import Pdfbyte

def home(request):
    return render(request, "base.html")

def search_list(request):
    query = str(request.POST.get('search_text', ''))
    if query != '':
        try:
            search_result = wikipedia.search(query, results=100)
        except:
            search_result = []
        frontend = {
            "search_result": search_result,
            "has_result": (search_result != [])
        }
    else:
        frontend = {
            "search_result": [],
            "has_result": False
        }
    return render(request, "ajax_search.html", frontend)

def download(request, string):
    titles=[]
    flag = 1
    try:
        page = wikipedia.page(urllib.request.unquote(string))
        titles.append(page.title)
    except wikipedia.exceptions.DisambiguationError as e:
        flag=0
        titles = e.options
    if 'search' in request.get_full_path():
        return render(request, "details.html", {"titles":titles, "error":None})
    if flag and 'search' not in request.get_full_path():
        try:
            filename=page.title.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).replace(" ", "_")+".pdf"
            try:
                pdf_object = Pdfbyte.objects.get(name=filename)
                print("its taking the pdf byte from database")
                pdf = pdf_object.bytedata
            except Pdfbyte.DoesNotExist:
                pdf = pdfkit.from_url(page.url, False)
                obj = Pdfbyte(name=filename, bytedata=pdf)
                obj.save()
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            return response
        except:
            return render(request, "details.html", {"titles":titles, "error":"Unable download the wikipedia page"})
    return render(request, "details.html", {"titles":titles, "error":"Unable download the wikipedia page"})