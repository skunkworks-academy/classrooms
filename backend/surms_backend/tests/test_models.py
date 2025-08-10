from django.test import TestCase
from ..models import Student, Course

class StudentModelTest(TestCase):
    def test_string_representation(self):
        student = Student(github_username='testuser')
        self.assertEqual(str(student), student.github_username)


class CourseModelTest(TestCase):
    def test_string_representation(self):
        course = Course(title='Intro AWS', vendor='AWS', course_type='self-paced')
        self.assertEqual(str(course), course.title)
