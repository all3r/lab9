from django.test import TestCase
from django.urls import reverse
from .models import User # Замени на импорт своей кастомной модели

class AppTests(TestCase):
    def setUp(self):
        # Эта функция запускается перед каждым тестом
        self.user = User.objects.create(email="test@test.com", admin=False)

    def test_index_page_status_code(self):
        # Проверяем, что главная страница возвращает код 200 (ОК)
        response = self.client.get(reverse('lab6:index')) # Убедись, что имя 'index' совпадает с name= в urls.py
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        # Проверяем, что пользователь корректно создался в БД
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, "test@test.com")