from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
class TestAPI(TestCase):

    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/user/', 
            {
                "email": "test2@test.com",
                "password": "Holaand5#]"               
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        client = APIClient()
        response = client.post(
            '/login/', 
            { 
                "email":"test@test.com", 
                "password":"Holaand5#]"
            }, 
            format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('refresh' in  response.data.keys(), True)
        self.assertEqual('access' in  response.data.keys(), True)

    def test_movies(self):
        client = APIClient()
        token_access =  client.post(
                            '/login/', 
                            {"email":"test@test.com", "password":"Holaand5#]"}, 
                            format='json'
                        ).data["access"]        
        url = '/movie/'
        auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token_access,}    
        response = client.get(url,  **auth_headers)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_rand_number(self):
        client = APIClient()
        token_access =  client.post(
                            '/login/', 
                            {"email":"test@test.com", "password":"Holaand5#]"}, 
                            format='json'
                        ).data["access"]        
        url = '/randNum/'
        auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token_access,}    
        response = client.get(url,  **auth_headers)        
        self.assertEqual(response.status_code, status.HTTP_200_OK)