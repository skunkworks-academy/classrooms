from django.urls import path
from ..views import (
    StudentListCreate,
    StudentDetail,
    CourseListCreate,
    CourseDetail,
    UserProfileListCreate,
    UserProfileDetail,
)

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('users/', UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('users/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
]
