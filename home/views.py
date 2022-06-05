from django.shortcuts import redirect, render
import requests
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

TMDB_API_KEY = "b3b2cba3f60060d27295ae00e67c7f6e"

def search(request):

    query = request.GET.get('q')
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&page=1&include_adult=false&query={query}")
        print(data.json())
    else:
        return HttpResponse("Please enter a search query")
        
    return render(request, 'results.html', {"data": data.json(),"type": request.GET.get("type")})


class IndexHome(View):
    template_name = 'home.html'
    def get(self, request,*args, **kwargs):
        for_you = requests.get(f"https://api.themoviedb.org/4/list/1?page=1&api_key={TMDB_API_KEY}").json()
        week      = requests.get(f"https://api.themoviedb.org/3/trending/all/week?api_key={TMDB_API_KEY}&language=en-US").json()
        popular   = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1").json()
        now_playing   = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US&page=1").json()
        context={'for_you':for_you, 'week':week,'popular':popular,'now_playing':now_playing}
        
        return render(request, self.template_name, context)




def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={TMDB_API_KEY}&language=en-US").json()
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US").json()
    
    return render(request, "tv_detail.html", {"data": data,"recommendations": recommendations,"type": "tv", })



def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US&append_to_response=videos").json()
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US").json()
    actors = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US").json()
    

    Trailers =  data
    for Trailer in Trailers['videos']['results']:
        pass
        
    return render(request, "movie_detail.html", {"data": data,"recommendations": recommendations,"movie_id":movie_id, 'Trailer':Trailer,"type": "movie","actors":actors})


def test(request):
    return render(request,'test.html')
