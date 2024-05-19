from django.shortcuts import render
from django.core.paginator import Paginator
import requests
# Create your views here.

API_KEY = 'c45a857c193f6302f2b5061c3b85e743'
BASE_URL = 'https://api.themoviedb.org/3'

def home(request):
    response = requests.get(f'{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1')
    movies = response.json().get('results', [])
    return render(request, 'movies/home.html', {'movies': movies})

def top_rated(request):
    page = request.GET.get('page', 1)
    response = requests.get(f'{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=en-US&page={page}')
    movies_data = response.json()
    movies = movies_data.get('results', [])
    paginator = Paginator(movies, 20)  # Show 20 movies per page

    try:
        movies_page = paginator.page(page)
    except PageNotAnInteger:
        movies_page = paginator.page(1)
    except EmptyPage: 
        movies_page = paginator.page(paginator.num_pages)

    context = {
        'movies': movies_page,
        'page': page,
        'next': int(page) + 1 if movies_page.has_next() else None,
        'previous': int(page) - 1 if movies_page.has_previous() else None,
    }
    return render(request, 'movies/top_rated.html', context)

def upcoming(request):
    page = request.GET.get('page', 1)
    response = requests.get(f'{BASE_URL}/movie/upcoming?api_key={API_KEY}&language=en-US&page={page}')
    movies_data = response.json()
    movies = movies_data.get('results', [])
    paginator = Paginator(movies, 20)  # Show 20 movies per page

    try:
        movies_page = paginator.page(page)
    except PageNotAnInteger:
        movies_page = paginator.page(1)
    except EmptyPage:
        movies_page = paginator.page(paginator.num_pages)

    context = {
        'movies': movies_page,
        'page': page,
        'next': int(page) + 1 if movies_page.has_next() else None,
        'previous': int(page) - 1 if movies_page.has_previous() else None,
    }
    return render(request, 'movies/upcoming.html', context)

def movie_detail(request, movie_id):
    movie_response = requests.get(f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US')
    movie = movie_response.json()
    cast_response = requests.get(f'{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US')
    cast = cast_response.json().get('cast', [])
    
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'cast': cast})

def search(request):
    query = request.GET.get('query')
    response = requests.get(f'{BASE_URL}/search/movie?api_key={API_KEY}&language=en-US&query={query}&page=1')
    movies = response.json().get('results', [])
    return render(request, 'movies/home.html', {'movies': movies})