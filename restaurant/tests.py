from datetime import timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Booking, MenuItem

User = get_user_model()


class MenuApiTests(APITestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            title="Lemon cake", price="8.50", inventory=10,
            description="Fresh lemon cake"
        )

    def test_menu_list_is_public(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_menu_item_detail(self):
        response = self.client.get(f"/restaurant/menu/{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Lemon cake")


class BookingApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="StrongPass123!")
        self.token = Token.objects.create(user=self.user)

    def test_booking_requires_authentication(self):
        response = self.client.get("/restaurant/booking/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_booking(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.post("/restaurant/booking/", {
            "name": "Alex",
            "no_of_guests": 2,
            "booking_date": (timezone.now() + timedelta(days=1)).isoformat(),
            "comments": "Window seat",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().user, self.user)


class RegistrationTests(APITestCase):
    def test_registration_returns_token(self):
        response = self.client.post("/auth/register/", {
            "username": "newuser",
            "email": "new@example.com",
            "password": "StrongPass123!",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)
