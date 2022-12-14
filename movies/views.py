from .permissions import IsEmployeeOrReadOnly
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from .pagination import CustomPageNumber

from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class MovieView(APIView, CustomPageNumber):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(page, many=True)
        
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        movie = MovieSerializer(data=request.data)
        movie.is_valid(raise_exception=True)
        movie.save(user=request.user)

        return Response(movie.data, status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]
    
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie,id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie,id=movie_id)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class MovieOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie_order= MovieOrderSerializer(data=request.data)
        movie_order.is_valid(raise_exception=True)
        movie_order.save(user_order=request.user, movie_order=movie)
        return Response(movie_order.data, status.HTTP_201_CREATED)