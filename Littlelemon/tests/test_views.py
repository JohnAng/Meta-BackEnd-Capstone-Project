from django.test import TestCase
from restaurant.views import MenuView
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class MenuViewTest(TestCase):

    def setup(self):
        
        Menu.objects.create(title="Dish1", price=10.99, inventory=50)
        Menu.objects.create(title="Dish2", price=15.99, inventory=30)
        Menu.objects.create(title="Dish3", price=8.99, inventory=20)


    def test_getall(self):

        # Create a test user 
        self.user = User.objects.create_user(username="testuser1", password="2wsx@WSX")
        
        # Create an instance of the APIClient to simulate HTTP requests
        client = APIClient()

        client.force_authenticate(user=self.user)

        # Make a GET request to the MenuView
        response = client.get(
            "http://127.0.0.1:8000/restaurant/menu/"
        )

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the test instances added in the setup method
        serialized_data = MenuItemSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data in the response equals the expected serialized data
        self.assertEqual(response.data, serialized_data)
