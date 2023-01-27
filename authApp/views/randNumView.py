from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def random_number_retrieve_view(request):
    url = "https://www.random.org/integers/?num=1&min=1&max=6&col=1&base=10&format=plain&rnd=new"
    response = requests.get(url)
    stringResponse = {'Random Number':response.json()}
    return Response(stringResponse, status=status.HTTP_200_OK)

          
