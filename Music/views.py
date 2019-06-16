from django.http import HttpResponse

from . models import Album

def index(request):
    all_album = Album.objects.all()
    html = " "
    for album in all_album:
        url = '/Music/' +str(album)+ '/'
        html += '<a href="'+ url + '">' +album.album_title + '</a><br>'
    return HttpResponse("html")


def detail(request, var):
    return HttpResponse("<h2> Detail for album id:" +str(var)+ "<h2>")