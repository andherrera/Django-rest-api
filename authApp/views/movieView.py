from rest_framework import status
from rest_framework.response import Response
from authApp.models.movies import Movie
from authApp.serializers.movieWriteSerializer import MovieWriteSerializer
from authApp.serializers.movieReadSerializer import MovieReadSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from authApp.pagination.pagination import SetPagination

import logging
import logging.handlers
import os
import gzip

class GZipRotator:
    def __call__(self, source, dest):
        os.rename(source, dest)
        f_in = open(dest, 'rb')
        f_out = gzip.open("%s.gz" % dest, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(dest)    

logformatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')
#log = logging.handlers.TimedRotatingFileHandler('./BI/systemLogs/stdilogs.log', 'M', 1,)
log = logging.handlers.TimedRotatingFileHandler('./logs/movies.log', 'W6')
log.setLevel(logging.INFO)
log.setFormatter(logformatter)
log.rotator = GZipRotator()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log)

class MovieListCreateView(generics.ListCreateAPIView):
    """
    Class MovieListCreateView in charge of create a movie and retrieve all movies    
    """
    permission_classes = (IsAuthenticated,)
    pagination_class = SetPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Movie.objects.filter(status='public').order_by('id') | Movie.objects.filter(user=user).order_by('id')        
        return queryset 

    def get_serializer_class(self):
        if self.request.method in ["POST"]:
            return MovieWriteSerializer
        return MovieReadSerializer

    def post(self, request, *args, **kwargs):
        title = request.data['title']
        userAuthenticated = request.user.id
        data=request.data
        data.update({"user": userAuthenticated})
        serializerMovie=MovieWriteSerializer(data=data)
        if serializerMovie.is_valid(raise_exception=True):
            serializerMovie.save()
            logger.info(f' User: {request.user} uploads movie: {title} ')                
            stringResponse = {'message':'Movie created succesfully'}
        return Response(stringResponse, status=status.HTTP_201_CREATED)

class MovieRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class MovieRetrieveUpdateView in charge of update and delete a single movie    
    """ 
    lookup_field = "id"             
    lookup_url_kwarg = 'pk'         
    permission_classes = (IsAuthenticated,) 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        stringResponse = {'message':'Movie deleted succesfully'}
        return Response(stringResponse, status=status.HTTP_202_ACCEPTED)

    def get_serializer_class(self):
        if self.request.method in ["PUT", "DELETE"]:
            return MovieWriteSerializer
        return MovieReadSerializer

    def get_queryset(self):
        user = self.request.user.id
        method = self.request.method
        if method == "GET":
            queryset = Movie.objects.filter(status='public').order_by('id') | Movie.objects.filter(user=user).order_by('id')
        else:
            queryset = Movie.objects.filter(user=user)
        return queryset   

    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            response = super().get(request, *args, **kwargs)
            logger.info(f' User: {request.user} request information about movie id: {pk} ')
            return response
        except:
            stringResponse = {'message':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            userAuthenticated = str(request.user.id)
            request.data.update({"user": userAuthenticated})
            response = super().put(request, *args, **kwargs)
            logger.info(f' User: {request.user} modifies movie id: {pk} ')
            return response
        except:
            stringResponse = {'message':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            response = super().delete(request, *args, **kwargs)
            logger.info(f' User: {request.user} deletes movie id: {pk} ')
            return response
        except:
            stringResponse = {'message':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

