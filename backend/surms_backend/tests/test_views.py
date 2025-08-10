from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Student, Course

class StudentTests(APITestCase):
    def test_create_student(self):
        url = reverse('student-list-create')
        data = {'github_username': 'testuser', 'email': 'test@example.com', 'full_name': 'Test User'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CourseTests(APITestCase):
    def test_create_course(self):
        url = reverse('course-list-create')
        data = {
            'title': 'Intro AWS',
            'description': 'Basics of AWS',
            'vendor': 'AWS',
            'course_type': 'self-paced',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
