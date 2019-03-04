from configparser import ConfigParser
from django.shortcuts import render
import urllib
# import tmdbsimple as tmdb
import wikipedia as wikipedia
import pdfkit
from django.http import HttpResponse

def home(request):
    return render(request, "base.html")

def search_list(request):
    query = str(request.POST.get('search_text', ''))
    if query != '':
        # search_result = tmdb.Search().movie(query=query)['results']
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
            pdf = pdfkit.from_url(page.url, False)
            filename=page.title.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).replace(" ", "_")+".pdf"
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            return response
        except:
            return render(request, "details.html", {"titles":titles, "error":"Unable download the wikipedia page"})
    return render(request, "details.html", {"titles":titles, "error":"Unable download the wikipedia page"})